# Sample Factory 論文 ↔ 現行コード対応表

対象:
- 論文: "Sample Factory: Egocentric 3D Control from Pixels at 100000 FPS with Asynchronous Reinforcement Learning"
- 実装: https://github.com/alex-petrenko/sample-factory/tree/master/sample_factory

注意:
- 論文は 2020 年版 Sample Factory / APPO の説明．
- 現行 GitHub master は Sample Factory v2 系なので、ファイル名・抽象化は一部変わっている．
- ただし、rollout worker / policy worker / learner / shared buffer / V-trace / PPO clipping / multi-policy という中核設計は対応している．

---

## 0. 全体対応の要約

| 論文の概念 | 現行コード上の主な対応箇所 | 役割 |
|---|---|---|
| APPO training entrypoint | `sample_factory/train.py` | 学習実行の入口．`run_rl()` → `make_runner()` → `ParallelRunner` / `SerialRunner` |
| High-level architecture | `algo/runners/runner_parallel.py` | learner process と sampler を構築 |
| Sampler | `algo/sampling/sampler.py` | rollout worker と inference worker を生成・接続 |
| Rollout worker | `algo/sampling/rollout_worker.py` | 環境 step、観測・報酬収集、trajectory buffer への書き込み |
| Policy worker | `algo/sampling/inference_worker.py` | 論文中の “policy worker”．現行コードでは `InferenceWorker` |
| Learner | `algo/learning/learner_worker.py`, `algo/learning/learner.py` | trajectory batch を受け取り、actor-critic を更新 |
| Shared memory trajectory buffers | `algo/utils/shared_buffers.py`, `rollout_worker.py`, `inference_worker.py` | 観測・RNN state・action・reward などを shared tensor に保持 |
| FIFO queue communication | `algo/sampling/sampler.py`, `rollout_worker.py`, `inference_worker.py` | queue では主に index / request metadata を渡す |
| Double-buffered sampling | `rollout_worker.py`, `batched_sampling.py`, `non_batched_sampling.py` | `worker_num_splits`, `split_idx`, `VectorEnvRunner` |
| Policy lag reduction | `algo/utils/model_sharing.py`, `inference_worker.py`, `learner.py` | parameter server/client, `ensure_weights_updated()`, `policy_version` |
| PPO objective | `algo/learning/learner.py` | clipped surrogate loss |
| V-trace | `algo/learning/learner.py` | `cfg.with_vtrace` が有効な場合の off-policy value target correction |
| Multi-policy / self-play / PBT | `train.py`, `runner_parallel.py`, `sampler.py`, `pbt/` | policy ごとの learner / inference worker / population 管理 |

---

# 1. 学習開始: APPO training entrypoint

## 論文側

論文では Sample Factory は APPO を中心とする非同期 RL システムとして説明される．

重要な説明:
- single-machine setting に最適化
- actor / sampler / learner を分離
- PBT や self-play に拡張可能

## コード側

### `sample_factory/train.py`

主要関数:

```python
def make_runner(cfg):
    if cfg.restart_behavior == "resume":
        cfg = maybe_load_from_checkpoint(cfg)

    if cfg.serial_mode:
        runner_cls = SerialRunner
    else:
        runner_cls = ParallelRunner

    runner = runner_cls(cfg)

    if cfg.with_pbt:
        runner.register_observer(PopulationBasedTraining(cfg, runner))

    return cfg, runner


def run_rl(cfg):
    cfg, runner = make_runner(cfg)
    status = runner.init()
    if status == ExperimentStatus.SUCCESS:
        status = runner.run()
    return status
```

対応:
- 論文の APPO system 全体の入口．
- `serial_mode=False` なら `ParallelRunner` を使う．
- `with_pbt=True` なら Population Based Training を observer として登録．
- 実際の rollout / inference / learning process 構築は `ParallelRunner.init()` へ移る．

---

# 2. High-level architecture: rollout worker / policy worker / learner

## 論文側

Figure 1 / Sec. 3.1 の対応:

- `N` 個の rollout workers が環境を進める．
- `M` 個の policy workers が GPU forward で action を計算する．
- learner が complete trajectories を受け取り、actor と critic を更新する．
- 更新後の parameter は policy worker に即座に反映され、policy lag を抑える．

## コード側

### `sample_factory/algo/runners/runner_parallel.py`

主要クラス:

```python
class ParallelRunner(Runner):
    def init(self):
        status = super().init()

        for policy_id in range(self.cfg.num_policies):
            batcher_event_loop = EventLoop("batcher_evt_loop")
            self.batchers[policy_id] = self._make_batcher(
                batcher_event_loop,
                policy_id,
            )

            learner_proc = EventLoopProcess(
                f"learner_proc{policy_id}",
                mp_ctx,
                init_func=init_learner_process,
            )

            self.learners[policy_id] = self._make_learner(
                learner_proc.event_loop,
                policy_id,
                self.batchers[policy_id],
            )

        self.sampler = self._make_sampler(ParallelSampler, self.event_loop)
        self.connect_components()
```

対応:
- 論文の learner は `LearnerWorker` / `Learner`．
- 論文の sampler は `ParallelSampler`．
- policy が複数ある場合、`policy_id` ごとに learner / batcher を持つ．
- rollout worker と policy worker の生成は `ParallelSampler` 側で行う．

---

# 3. Sampler: rollout worker と policy worker の生成・接続

## 論文側

Sampler は以下の2種類の worker から構成される．

1. Rollout worker
   - 環境 simulation のみ担当
   - policy のコピーを持たない
   - 観測、報酬、hidden state、action などを trajectory buffer に保存

2. Policy worker
   - rollout worker から観測と hidden state を受け取る
   - 複数 rollout worker 由来の request を batch 化
   - GPU forward で action distribution / action / next hidden state を計算
   - 結果を rollout worker に返す

## コード側

### `sample_factory/algo/sampling/sampler.py`

主要クラス:

```python
class Sampler(AbstractSampler):
    def __init__(...):
        self.inference_queues = {
            p: get_queue(cfg.serial_mode)
            for p in range(self.cfg.num_policies)
        }

        self.inference_workers = {}
        self.rollout_workers = []
```

対応:
- `inference_queues[policy_id]` が rollout worker → policy worker の FIFO queue．
- 論文中の “policy worker” は現行コードでは `InferenceWorker`．

### `ParallelSampler`

```python
class ParallelSampler(Sampler):
    def __init__(...):
        for policy_id in range(self.cfg.num_policies):
            for i in range(self.cfg.policy_workers_per_policy):
                inference_proc = EventLoopProcess(
                    f"inference_proc{policy_id}-{i}",
                    mp_ctx,
                    init_func=init_inference_process,
                )

                inference_worker = self._make_inference_worker(
                    inference_proc.event_loop,
                    policy_id,
                    i,
                    self.policy_param_server[policy_id],
                )

        for i in range(self.cfg.num_workers):
            rollout_proc = EventLoopProcess(
                f"rollout_proc{i}",
                mp_ctx,
                init_func=init_rollout_worker_process,
            )

            rollout_worker = self._make_rollout_worker(
                rollout_proc.event_loop,
                i,
            )
```

対応:
- `num_workers` → rollout worker 数．
- `policy_workers_per_policy` → policy worker 数．
- `num_policies` → multi-policy / PBT / self-play 用の policy 数．
- learner は `runner_parallel.py` 側で policy ごとに作られる．

### worker 間 signal 接続

```python
def _connect_internal_components(self):
    self._for_each_inference_worker(
        lambda w: w.initialized.connect(self._inference_worker_ready)
    )

    for rollout_worker_idx in range(self.cfg.num_workers):
        rollout_worker = self.rollout_workers[rollout_worker_idx]

        self._inference_workers_initialized.connect(rollout_worker.init)

        for policy_id in range(self.cfg.num_policies):
            for inference_worker_idx in range(self.cfg.policy_workers_per_policy):
                self.inference_workers[policy_id][inference_worker_idx].connect(
                    advance_rollouts_signal(rollout_worker_idx),
                    rollout_worker.advance_rollouts,
                )
```

対応:
- inference worker が action を計算した後、`advance_rollouts_signal` で rollout worker に返す．
- これは論文の「policy worker が action と next hidden state を rollout worker に返す」に対応．

---

# 4. Rollout worker: 環境 simulation と trajectory 収集

## 論文側

Sec. 3.1 の記述:

- Rollout workers are solely responsible for environment simulation.
- Each rollout worker hosts `k >= 1` environments.
- Rollout worker does not own a copy of the policy.
- Observations `x_t` and hidden states `h_t` are sent to policy workers.
- Returned actions `a_t` are used to advance the simulation.
- Every transition is saved to a trajectory buffer in shared memory.
- Once `T` steps are collected, a complete trajectory is sent to learner.

## コード側

### `sample_factory/algo/sampling/rollout_worker.py`

主要クラス:

```python
class RolloutWorker(...):
    def __init__(..., worker_idx, buffer_mgr, inference_queues, cfg, env_info):
        self.buffer_mgr = buffer_mgr
        self.inference_queues = inference_queues
        self.worker_idx = worker_idx

        self.vector_size = cfg.num_envs_per_worker
        self.num_splits = cfg.worker_num_splits
        self.env_runners = []
```

対応:
- `cfg.num_envs_per_worker` が論文の rollout worker あたり `k` environments．
- `buffer_mgr` が shared trajectory buffer 管理．
- `inference_queues` が policy worker への queue．
- `RolloutWorker` 自体は policy model を持たない．

### rollout worker 初期化

```python
def init(self):
    for split_idx in range(self.num_splits):
        env_runner_cls = (
            BatchedVectorEnvRunner
            if self.cfg.batched_sampling
            else NonBatchedVectorEnvRunner
        )

        env_runner = env_runner_cls(
            self.cfg,
            self.env_info,
            self.vector_size // self.num_splits,
            self.worker_idx,
            split_idx,
            self.buffer_mgr,
            self.sampling_device,
            self.training_info,
        )

        env_runner.init(self.timing)
        self.env_runners.append(env_runner)

    for r in self.env_runners:
        self._maybe_send_policy_request(r)
```

対応:
- rollout worker 内部の環境群を `num_splits` 個に分割．
- double-buffered sampling の場合、典型的には `worker_num_splits=2`．
- 各 split は `VectorEnvRunner` として管理される．
- 初期化後、最初の観測に対して policy request を送る．

### policy request の生成

```python
def _maybe_send_policy_request(self, runner):
    if not runner.update_trajectory_buffers(self.timing):
        return

    policy_request = runner.generate_policy_request()
    runner.synchronize_devices()

    if policy_request is not None:
        self._enqueue_policy_request(runner.split_idx, policy_request)
```

対応:
- 現在の観測 `x_t` と RNN state `h_t` への参照を policy worker へ送る．
- 実データ全体を queue に流すのではなく、shared buffer 上の index / request metadata を送る．
- 論文 Sec. 3.3 の shared tensor + FIFO queue に対応．

### policy request の queue 投入

```python
def _enqueue_policy_request(self, split_idx, policy_inputs):
    for policy_id, requests in policy_inputs.items():
        policy_request = (
            self.worker_idx,
            split_idx,
            requests,
            self.sampling_device,
        )
        self.inference_queues[policy_id].put(policy_request)
```

対応:
- policy ごとに queue を分ける．
- multi-policy / self-play / PBT のとき、agent-policy mapping に応じて request が routing される．
- queue payload は `(worker_idx, split_idx, requests, device)`．

### action を受け取って環境を進める

```python
def advance_rollouts(self, split_idx: int, policy_id: PolicyID):
    runner = self.env_runners[split_idx]

    complete_rollouts, episodic_stats = runner.advance_rollouts(
        policy_id,
        self.timing,
    )

    if complete_rollouts:
        self._enqueue_complete_rollouts(complete_rollouts)

    self._maybe_send_policy_request(runner)
```

対応:
- policy worker が shared buffer に action / value / log-prob などを書き戻す．
- `advance_rollouts()` がそれを読んで環境を1 step進める．
- rollout が完了したら learner 側へ送る．
- その後、次 step の observation に対して再び policy request を送る．

### complete trajectory を learner へ送る

```python
def _enqueue_complete_rollouts(self, complete_rollouts):
    rollouts_per_policy = dict()

    for rollout in complete_rollouts:
        policy_id = rollout["policy_id"]
        rollouts_per_policy.setdefault(policy_id, []).append(rollout)

    for policy_id, rollouts in rollouts_per_policy.items():
        self.emit(
            new_trajectories_signal(policy_id),
            rollouts,
            self.sampling_device,
        )
```

対応:
- 論文の「Once T environment steps are simulated, the trajectory becomes available to the learner」．
- 実体は shared buffer 上にあり、learner へは trajectory buffer index を含む metadata が送られる．
- policy ごとに trajectory を分ける．

---

# 5. Policy worker = `InferenceWorker`

## 論文側

Sec. 3.1 の policy worker:

- rollout worker から `x_t`, `h_t` を受け取る．
- 複数 rollout worker からの request を batch 化．
- neural network policy `π_θ` を GPU forward．
- action distribution `μ(a_t | x_t, h_t)` を計算．
- action `a_t` と next hidden state `h_{t+1}` を rollout worker に返す．
- learner 更新後の新しい parameter をすぐ取得し、policy lag を抑える．

## コード側

### `sample_factory/algo/sampling/inference_worker.py`

主要クラス:

```python
class InferenceWorker(...):
    def __init__(..., policy_id, worker_idx, buffer_mgr, param_server, inference_queue, cfg, env_info):
        self.policy_id = policy_id
        self.worker_idx = worker_idx

        self.traj_tensors = copy.copy(buffer_mgr.traj_tensors_torch)
        self.policy_output_tensors = copy.copy(
            buffer_mgr.policy_output_tensors_torch
        )

        self.device = policy_device(cfg, policy_id)
        self.param_client = make_parameter_client(
            cfg.serial_mode,
            param_server,
            cfg,
            env_info,
            self.timing,
        )

        self.inference_queue = inference_queue
```

対応:
- `traj_tensors` が rollout worker によって書き込まれた observation / RNN state 等．
- `policy_output_tensors` が action / log-prob / value / policy_version 等の返却先．
- `param_client` が learner 側の parameter server から最新重みを取得する窓口．
- 現行コードでは “policy worker” という名前ではなく `InferenceWorker`．

### request の batch 化: batched sampling

```python
def _batch_slices(self, timing):
    obs = dict()
    rnn_states = []

    for actor_idx, split_idx, traj_idx, device in self.requests:
        traj_tensors = self.traj_tensors[device]
        dict_of_lists_append_idx(obs, traj_tensors["obs"], traj_idx)
        rnn_states.append(traj_tensors["rnn_states"][traj_idx])

    dict_of_lists_cat(obs)
    rnn_states = cat_tensors(rnn_states)

    return obs, rnn_states
```

対応:
- 複数 rollout worker / split から observation と RNN state を集める．
- 論文の “collects batches of x_t, h_t from multiple rollout workers” に対応．
- shared buffer の index から tensor を集める．

### request の batch 化: non-batched sampling

```python
def _batch_individual_steps(self, timing):
    indices = []

    for request in self.requests:
        actor_idx, split_idx, request_data, device = request

        for env_idx, agent_idx, traj_buffer_idx, rollout_step in request_data:
            index = [traj_buffer_idx, rollout_step]
            indices.append(index)

    indices = tuple(np.array(indices).T)
    traj_tensors = self.traj_tensors[device]

    observations = traj_tensors["obs"][indices]
    rnn_states = traj_tensors["rnn_states"][indices]

    return observations, rnn_states
```

対応:
- batched env でない場合も、shared buffer index から observation / hidden state を取り出す．
- queue で実 tensor を送らず index を送る設計．

### GPU forward

```python
def _handle_policy_steps(self, timing):
    obs, rnn_states = self._batch_func(timing)
    num_samples = rnn_states.shape[0]

    actor_critic = self.param_client.actor_critic
    if actor_critic.training:
        actor_critic.eval()

    action_mask = (
        ensure_torch_tensor(obs.pop("action_mask")).to(self.device)
        if "action_mask" in obs
        else None
    )

    normalized_obs = prepare_and_normalize_obs(actor_critic, obs)
    rnn_states = ensure_torch_tensor(rnn_states).to(self.device).float()

    policy_outputs = actor_critic(
        normalized_obs,
        rnn_states,
        action_mask=action_mask,
    )

    policy_outputs["policy_version"] = torch.empty([num_samples]).fill_(
        self.param_client.policy_version
    )
```

対応:
- `actor_critic(...)` が policy network + value network の forward．
- action distribution / sampled actions / log-probs / values / next RNN states などが `policy_outputs` に入る．
- `policy_version` を trajectory に記録することで、learner 側で policy lag / off-policy 補正に使える．

### policy output を shared buffer に書き戻す

```python
def _prepare_policy_outputs_batched(...):
    for actor_idx, split_idx, _, device in requests:
        self.policy_output_tensors[device][actor_idx, split_idx] = (
            policy_outputs[ofs : ofs + samples_per_actor]
        )

    for actor_idx, split_idx, _, _ in requests:
        payload = (split_idx, self.policy_id)
        signals_to_send[actor_idx].append(payload)

    return signals_to_send
```

対応:
- action などの output 本体は `policy_output_tensors` に書く．
- rollout worker には signal だけ送る．
- 論文 Sec. 3.3 の “send only indices through FIFO queues” と同じ思想．

### policy worker のメインループ

```python
def _run(self):
    self._get_inference_requests_func()

    if not self.requests:
        return

    with self.timing.add_time("update_model"):
        self.param_client.ensure_weights_updated()

    with self.timing.timeit("one_step"):
        self._handle_policy_steps(self.timing)
```

対応:
- queue から request を集める．
- forward 前に `ensure_weights_updated()` で learner の最新重みを取得．
- これが論文の「parameter updates are sent to policy worker as soon as available; policy lag is minimized」に対応．

---

# 6. Double-buffered sampling

## 論文側

Sec. 3.2 / Figure 2:

- rollout worker は `k` 個の environment を持つ．
- `k` 個を2グループに分ける．
- group A の env step 中に group B の action を policy worker が計算する．
- group B の env step 中に group A の action を計算する．
- これにより CPU rollout worker の idle time を減らす．
- 条件の目安: `k / 2 > ceil(t_inf / t_env)`

## コード側

### `rollout_worker.py`

```python
self.vector_size = cfg.num_envs_per_worker
self.num_splits = cfg.worker_num_splits

assert self.vector_size >= self.num_splits
assert self.vector_size % self.num_splits == 0
```

対応:
- `num_envs_per_worker` が論文の `k`．
- `worker_num_splits` が分割数．
- double-buffered sampling では通常 `worker_num_splits = 2`．
- 各 split は `k / worker_num_splits` 個の env を持つ．

### split ごとの VectorEnvRunner

```python
for split_idx in range(self.num_splits):
    env_runner = env_runner_cls(
        self.cfg,
        self.env_info,
        self.vector_size // self.num_splits,
        self.worker_idx,
        split_idx,
        self.buffer_mgr,
        self.sampling_device,
        self.training_info,
    )

    self.env_runners.append(env_runner)
```

対応:
- split 0 と split 1 が論文 Figure 2 の2グループ．
- 各 split が独立に policy request → action receive → env step を繰り返す．

### `BatchedVectorEnvRunner`

`sample_factory/algo/sampling/batched_sampling.py`

```python
class BatchedVectorEnvRunner(VectorEnvRunner):
    """
    A collection of environments simulated sequentially.
    With double buffering each actor worker holds two vector runners
    and switches between them.
    """
```

対応:
- コメント上でも double buffering が明示されている．
- `worker_idx` と `split_idx` で rollout worker 内の環境グループを識別．

### env runner 初期化

```python
def init(self, timing):
    for env_i in range(self.num_envs):
        vector_idx = self.split_idx * self.num_envs + env_i
        env_id = self.worker_idx * self.cfg.num_envs_per_worker + vector_idx

        env_config = AttrDict(
            worker_index=self.worker_idx,
            vector_index=vector_idx,
            env_id=env_id,
        )

        env = make_env_func_batched(self.cfg, env_config)
        env.seed(env_id)
        envs.append(env)
```

対応:
- `split_idx` により worker 内の env group を分ける．
- global な `env_id` は `worker_idx`, `split_idx`, `env_i` から決まる．
- 論文の `E_1, ..., E_k` の具体的な index 管理．

---

# 7. Shared memory + FIFO queue communication

## 論文側

Sec. 3.3:

- RL のデータ構造は固定 shape tensor として表現できる．
- trajectory, observation, hidden state などを shared tensor に事前確保する．
- component 間では tensor 本体ではなく index だけを FIFO queue で送る．
- serialization を避ける．
- parameter update は GPU memory sharing を使う．

## コード側

### shared buffers

主なファイル:

```text
sample_factory/algo/utils/shared_buffers.py
sample_factory/algo/sampling/rollout_worker.py
sample_factory/algo/sampling/inference_worker.py
```

主要オブジェクト:

```python
buffer_mgr.traj_tensors_torch
buffer_mgr.policy_output_tensors_torch
```

対応:
- `traj_tensors_torch`:
  - obs
  - rnn_states
  - actions
  - rewards
  - dones
  - values
  - log-probs
  - policy_id
  - policy_version
  などを保持する trajectory tensor 群．

- `policy_output_tensors_torch`:
  - inference worker が rollout worker へ返す action / value / log-prob / next rnn state など．

### rollout worker → inference worker

```python
policy_request = (
    self.worker_idx,
    split_idx,
    requests,
    self.sampling_device,
)

self.inference_queues[policy_id].put(policy_request)
```

対応:
- queue に入るのは worker index, split index, trajectory buffer index など．
- observation tensor 本体は shared buffer にある．

### inference worker 側で shared buffer 参照

```python
self.traj_tensors = copy.copy(buffer_mgr.traj_tensors_torch)
self.policy_output_tensors = copy.copy(
    buffer_mgr.policy_output_tensors_torch
)
```

対応:
- inference worker は shared buffer への参照を持つ．
- queue から受け取った index に基づいて observation / RNN state を読む．
- action / value / log-prob 等を shared output tensor に書き戻す．

### signal-slot

主な signal:

```python
advance_rollouts_signal(worker_idx)
new_trajectories_signal(policy_id)
```

対応:
- `advance_rollouts_signal`: policy output が準備できたので rollout worker を進める．
- `new_trajectories_signal`: complete trajectory が learner / batcher 側で利用可能になったことを通知．

---

# 8. Learner: trajectory batch による actor-critic 更新

## 論文側

Sec. 3.1:

- complete trajectories are sent from rollout workers to learner.
- learner continuously processes batches of trajectories.
- learner updates actor parameters `θ_π` and critic parameters `θ_V`.
- updated parameters are made available to policy workers.

## コード側

主なファイル:

```text
sample_factory/algo/learning/learner_worker.py
sample_factory/algo/learning/learner.py
```

### `Learner` 初期化

```python
class Learner(Configurable):
    def __init__(..., policy_versions_tensor, policy_id, param_server):
        self.policy_id = policy_id
        self.actor_critic = None
        self.optimizer = None
        self.train_step = 0
        self.env_steps = 0

        self.policy_versions_tensor = policy_versions_tensor
        self.param_server = param_server
```

対応:
- `actor_critic` が actor + critic．
- `optimizer` が learner の update 実体．
- `policy_versions_tensor` が policy lag 計測・共有用．
- `param_server` が policy worker への parameter 共有用．

### actor-critic model 作成

```python
self.actor_critic = create_actor_critic(
    self.cfg,
    self.env_info.obs_space,
    self.env_info.action_space,
)
```

対応:
- 論文の `π_θ` と `V_θ`．
- 実装上は `ActorCritic` に policy head と value head がまとまる．

### learner update

概念的対応:

```python
LearnerWorker.on_new_training_batch(...)
    -> Learner.train(...)
        -> minibatch construction
        -> forward pass
        -> loss calculation
        -> optimizer.step()
        -> policy version update
        -> parameter server update
```

対応:
- rollout worker が complete trajectory を送る．
- batcher が trajectory を training batch 化．
- learner が PPO / V-trace / value loss / entropy loss 等を計算．
- optimizer step 後、policy worker が新 weight を取得できる状態にする．

---

# 9. PPO clipping

## 論文側

Sec. 3.4:

- asynchronous sampling により off-policy data が混ざる．
- trust-region 的な制約として PPO clipping を使う．
- behavior policy と target policy が大きく離れすぎないようにする．

## コード側

### `sample_factory/algo/learning/learner.py`

対応する主要処理:

```python
ratio = exp(new_log_prob - old_log_prob)

surr1 = ratio * advantage
surr2 = clamp(ratio, 1 - clip_ratio, 1 + clip_ratio) * advantage

policy_loss = -min(surr1, surr2)
```

実際のコード上では `_policy_loss()` 付近に相当．

対応:
- `old_log_prob`: rollout 時に policy worker が記録した behavior policy の log-prob．
- `new_log_prob`: learner の現在 policy で再計算した log-prob．
- `ratio`: importance ratio．
- `clip_ratio`: PPO clipping range．
- `policy_loss`: clipped PPO surrogate objective．

---

# 10. V-trace

## 論文側

Sec. 3.4:

- PPO clipping と V-trace は独立に使える．
- V-trace は truncated importance sampling により value target を補正する．
- Sample Factory では PPO clipping と V-trace の組み合わせを採用．

## コード側

### `sample_factory/algo/learning/learner.py`

概念的対応:

```python
if self.cfg.with_vtrace:
    # behavior policy と current policy の log-prob から importance weights を作る
    # rho, c を clip
    # V-trace target vs を計算
    # advantage adv を計算
else:
    # GAE を使用
    adv = mb.advantages
    returns = mb.returns
```

対応:
- `cfg.with_vtrace=True` のとき V-trace target を使う．
- `cfg.with_vtrace=False` のとき通常の GAE advantage / return を使う．
- 非同期 APPO で policy lag があるため、V-trace が off-policy correction として働く．

---

# 11. Policy lag

## 論文側

Sec. 3.1 / 3.4:

- learner が更新した parameter を policy worker がすぐ取得する．
- 古い policy で集められる experience を減らす．
- ただし非同期なので完全 on-policy ではない．
- policy lag は V-trace / PPO clipping で補正・制御する．

## コード側

### inference worker

```python
def _run(self):
    self._get_inference_requests_func()

    if not self.requests:
        return

    self.param_client.ensure_weights_updated()
    self._handle_policy_steps(self.timing)
```

対応:
- action 計算直前に最新 weight を取得．
- これにより stale policy の使用を抑える．

### policy version の記録

```python
policy_outputs["policy_version"] = torch.empty([num_samples]).fill_(
    self.param_client.policy_version
)
```

対応:
- rollout に「どの policy version で生成された action か」を記録．
- learner / stats 側で policy lag を把握できる．
- off-policy 補正の文脈で重要．

### learner 側

```python
self.policy_versions_tensor = policy_versions_tensor
self.train_step = 0
```

対応:
- learner の SGD step / policy update count が policy version として扱われる．
- shared tensor を通じて他 process と共有される．

---

# 12. Multi-agent / multi-policy / self-play / PBT

## 論文側

Sec. 3.5:

- multi-agent learning と self-play をサポート．
- 複数 policy を同時に持つ．
- agent-policy mapping に基づいて、各 agent の observation を対応する policy worker に送る．
- policy ごとに learner を持てる．
- PBT では policy population の hyperparameter / weight を更新する．

## コード側

### policy ごとの learner

`runner_parallel.py`

```python
for policy_id in range(self.cfg.num_policies):
    self.batchers[policy_id] = self._make_batcher(...)
    self.learners[policy_id] = self._make_learner(...)
```

対応:
- policy ごとに learner / batcher を作る．
- self-play / PBT / multi-policy training に対応．

### policy ごとの inference queue

`sampler.py`

```python
self.inference_queues = {
    p: get_queue(cfg.serial_mode)
    for p in range(self.cfg.num_policies)
}
```

対応:
- policy ごとに action request queue を分離．
- rollout worker は `policy_id` に応じて request を投げ分ける．

### rollout worker の routing

`rollout_worker.py`

```python
def _enqueue_policy_request(self, split_idx, policy_inputs):
    for policy_id, requests in policy_inputs.items():
        policy_request = (
            self.worker_idx,
            split_idx,
            requests,
            self.sampling_device,
        )
        self.inference_queues[policy_id].put(policy_request)
```

対応:
- agent-policy mapping に従って `policy_inputs` が policy ごとに分かれる．
- 各 policy の inference worker が該当 agent の action を計算する．

### PBT

`train.py`

```python
if cfg.with_pbt:
    runner.register_observer(PopulationBasedTraining(cfg, runner))
```

主な対応ディレクトリ:

```text
sample_factory/pbt/
```

対応:
- 論文の Population Based Training．
- runner observer として training stats / reward / policy state を監視し、population の更新を行う．

---

# 13. Batched sampling と environment vectorization

## 論文側

Figure 2a:

- GPU-accelerated batched sampling．
- policy forward を batch 化することで GPU を効率利用．
- ただし単純 batched sampling では rollout worker が action 待ちで idle になる．

## コード側

### `sample_factory/algo/sampling/batched_sampling.py`

```python
class BatchedVectorEnvRunner(VectorEnvRunner):
    """
    A collection of environments simulated sequentially.
    With double buffering each actor worker holds two vector runners
    and switches between them.
    """
```

対応:
- 1つの `VectorEnvRunner` が複数 env をまとめて扱う．
- `cfg.batched_sampling=True` なら `BatchedVectorEnvRunner`．
- `cfg.batched_sampling=False` なら `NonBatchedVectorEnvRunner`．

### action preprocessing

```python
def preprocess_actions(env_info, actions, to_numpy=True):
    if env_info.all_discrete or isinstance(env_info.action_space, gym.spaces.Discrete):
        return process_action_space(actions, env_info.gpu_actions, is_discrete=True)
    elif isinstance(env_info.action_space, gym.spaces.Box):
        return process_action_space(actions, env_info.gpu_actions, is_discrete=False)
    elif isinstance(env_info.action_space, gym.spaces.Tuple):
        ...
```

対応:
- policy worker が出した tensor action を environment API に合う形へ変換．
- discrete / continuous / tuple action space を処理．

---

# 14. 実行時のデータフロー

## 論文上の流れ

```text
rollout worker:
    env observation x_t, hidden state h_t
        ↓
policy worker:
    batch(x_t, h_t)
    GPU forward πθ
    action a_t, next hidden state h_{t+1}
        ↓
rollout worker:
    env.step(a_t)
    save transition to shared trajectory buffer
        ↓
if T steps collected:
    learner receives trajectory index
        ↓
learner:
    PPO / V-trace loss
    update θπ, θV
        ↓
policy worker:
    fetch latest weights
```

## 現行コード上の流れ

```text
train.py
    run_rl(cfg)
        ↓
runner_parallel.py
    ParallelRunner.init()
        - make batcher
        - make learner process
        - make ParallelSampler
        ↓
sampler.py
    ParallelSampler
        - create inference_proc{policy_id}-{i}
        - create rollout_proc{i}
        - connect signals
        ↓
rollout_worker.py
    RolloutWorker.init()
        - create BatchedVectorEnvRunner / NonBatchedVectorEnvRunner
        - reset envs
        - _maybe_send_policy_request()
        ↓
rollout_worker.py
    _enqueue_policy_request()
        - inference_queues[policy_id].put(...)
        ↓
inference_worker.py
    _run()
        - read requests from queue
        - param_client.ensure_weights_updated()
        - _batch_slices() / _batch_individual_steps()
        - actor_critic(...)
        - write policy_outputs to shared buffer
        - emit advance_rollouts_signal
        ↓
rollout_worker.py
    advance_rollouts()
        - env_runner.advance_rollouts()
        - env.step(action)
        - save transition
        - if rollout complete: emit new_trajectories_signal
        - send next policy request
        ↓
learner_worker.py / learner.py
    on_new_training_batch()
        - learner.train()
        - compute PPO / V-trace losses
        - optimizer.step()
        - update policy version / shared weights
```

---

# 15. 論文 Figure 1 の各矢印とコード対応

| Figure 1 の矢印 | 意味 | コード対応 |
|---|---|---|
| rollout worker → policy worker: observations | observation / hidden state を送る | `RolloutWorker._maybe_send_policy_request()` → `_enqueue_policy_request()` |
| policy worker → rollout worker: actions | action / next hidden state を返す | `InferenceWorker._prepare_policy_outputs_*()` → `advance_rollouts_signal` |
| rollout worker → learner: full trajectories | complete rollout を learner へ通知 | `RolloutWorker._enqueue_complete_rollouts()` → `new_trajectories_signal(policy_id)` |
| learner → policy worker: policy updates | 最新 parameter を policy worker が取得 | `ParameterServer`, `make_parameter_client`, `ensure_weights_updated()` |
| shared memory observations/actions | tensor 本体を shared buffer に置く | `BufferMgr`, `traj_tensors_torch`, `policy_output_tensors_torch` |
| GPU memory | policy forward / parameter sharing | `policy_device()`, `actor_critic(...)`, `ParameterServer` |

---

# 16. 論文 Sec. 3.2 Double-buffered sampling のコード対応

| 論文の記述 | コード対応 |
|---|---|
| rollout worker stores vector of environments `E_1, ..., E_k` | `cfg.num_envs_per_worker` |
| split into two groups | `cfg.worker_num_splits`, usually `2` |
| first group stepped while second group inference runs | split ごとの `VectorEnvRunner` と async signal |
| policy worker computes actions for other group | `InferenceWorker._run()` |
| rollout worker resumes when actions ready | `advance_rollouts_signal` → `RolloutWorker.advance_rollouts()` |
| mask communication overhead | shared buffer + queue + split alternation |

---

# 17. 論文 Sec. 3.3 Communication のコード対応

| 論文の記述 | コード対応 |
|---|---|
| preallocate tensors in system RAM | `BufferMgr`, `traj_tensors_torch` |
| communicate by indices | `policy_request = (worker_idx, split_idx, requests, device)` |
| FIFO queues | `self.inference_queues[policy_id]` |
| no serialization of large data | observation/action tensor 本体は shared buffer |
| parameter updates via GPU memory sharing | `ParameterServer`, `ParameterClient` |
| policy worker copies latest weights | `param_client.ensure_weights_updated()` |

---

# 18. 論文 Sec. 3.4 APPO / off-policy correction のコード対応

| 論文の概念 | コード対応 |
|---|---|
| asynchronous PPO | `cfg.async_rl`, `ParallelRunner`, `ParallelSampler` |
| policy lag | `policy_version`, `policy_versions_tensor` |
| behavior policy log-probs | trajectory buffer に保存される rollout-time log-probs |
| target policy log-probs | learner forward で再計算 |
| PPO clipping | `Learner._policy_loss()` |
| V-trace | `cfg.with_vtrace` branch in `Learner` |
| GAE fallback | `gae_advantages` / minibatch advantages |

---

# 19. 実装を読む順番

1. `sample_factory/train.py`
   - 学習の入口．
   - `run_rl()` と `make_runner()` を確認．

2. `sample_factory/algo/runners/runner_parallel.py`
   - learner process / sampler の構築を確認．

3. `sample_factory/algo/sampling/sampler.py`
   - rollout worker / inference worker の process 生成と signal 接続を確認．

4. `sample_factory/algo/sampling/rollout_worker.py`
   - environment step、policy request、complete rollout 通知を確認．

5. `sample_factory/algo/sampling/inference_worker.py`
   - request batch 化、GPU forward、policy output 書き戻し、weight update を確認．

6. `sample_factory/algo/sampling/batched_sampling.py`
   - vectorized env と double-buffered split の具体処理を確認．

7. `sample_factory/algo/utils/shared_buffers.py`
   - trajectory tensor / policy output tensor の shared memory 構造を確認．

8. `sample_factory/algo/utils/model_sharing.py`
   - learner と inference worker 間の parameter sharing を確認．

9. `sample_factory/algo/learning/learner_worker.py`
   - trajectory batch を learner に渡す箇所を確認．

10. `sample_factory/algo/learning/learner.py`
    - PPO loss、V-trace、optimizer step、policy version update を確認．

11. `sample_factory/pbt/`
    - PBT / self-play を見る場合に確認．

---

# 20. 研究メモとしての最短対応表

```text
Paper Figure 1
    rollout workers
        -> rollout_worker.py::RolloutWorker
        -> batched_sampling.py::BatchedVectorEnvRunner
        -> non_batched_sampling.py::NonBatchedVectorEnvRunner

    policy workers
        -> inference_worker.py::InferenceWorker

    learner
        -> learner_worker.py::LearnerWorker
        -> learner.py::Learner

    shared memory
        -> shared_buffers.py::BufferMgr
        -> buffer_mgr.traj_tensors_torch
        -> buffer_mgr.policy_output_tensors_torch

    FIFO queues
        -> sampler.py::self.inference_queues
        -> rollout_worker.py::_enqueue_policy_request()
        -> inference_worker.py::_get_inference_requests_async()

    policy updates
        -> model_sharing.py::ParameterServer
        -> inference_worker.py::param_client.ensure_weights_updated()

Paper Section 3.2
    double-buffered sampling
        -> cfg.worker_num_splits
        -> cfg.num_envs_per_worker
        -> RolloutWorker.env_runners[split_idx]
        -> BatchedVectorEnvRunner(..., split_idx, ...)

Paper Section 3.3
    tiny messages / no serialization
        -> queue payload is indices / request metadata
        -> tensor payload stays in shared buffers

Paper Section 3.4
    APPO, PPO clipping, V-trace
        -> learner.py::_policy_loss()
        -> learner.py::_calculate_losses()
        -> cfg.with_vtrace

Paper Section 3.5
    multi-agent / self-play / PBT
        -> cfg.num_policies
        -> policy_id routing
        -> train.py::PopulationBasedTraining
        -> sample_factory/pbt/
```