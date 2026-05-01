---
marp: true
theme: tmu-cs
paginate: true
math: mathjax

title: "論文紹介"
subtitle: "Sample Factory: Egocentric 3D Control from Pixels at 100000 FPS with Asynchronous Reinforcement Learning"
author: "鈴木史麿"
affiliation: "wkblab"
date: "05-01"

bibliography: references.bib

sectionPages: true
sectionPageLevel: 2
tocPageMaxLevel: 2
---

# 目次

<!-- toc -->

---

## 背景

---

### 論文

| 項目 | 内容 |
| :-- | :-- |
| タイトル | Sample Factory: Egocentric 3D Control from Pixels at 100000 FPS with Asynchronous Reinforcement Learning |
| 著者 | Aleksei Petrenko, Zhehui Huang, Tushar Kumar, Gaurav S. Sukhatme, Vladlen Koltun |
| 発表 | ICML 2020 |
| 主張 | single machine でも $10^5$ FPS 級の RL 学習が可能 |
| 今回の焦点 | 論文の課題設定が現行実装でどう具体化されているか |

---

### 強化学習では何を繰り返しているか

> #### 1 step の流れ
>
> agent は観測 `s_t` を見て行動 `a_t` を選び、
> 環境は次の観測と報酬 `r_t` を返す。

- この反復を何千・何百万 step と続ける
- learner はその履歴から policy を更新する
- Sample Factory はこの反復を速く回す実行系である

---

<!-- _class: column-layout -->

### `sample` `rollout` `batch` の違い

<div class="column">

#### sample

- 1 回の `env.step()`
- 1 時刻ぶんの観測・行動・報酬

</div>

<div class="column">

#### rollout

- sample を数 step ためたもの
- worker が learner へ渡す単位

</div>

<div class="column">

#### batch

- rollout を集めて束ねたもの
- learner が SGD に使う単位

</div>

---

### 同期 RL はどこで待つのか

```text
env を進める
  -> policy で推論する
    -> learner が更新する
      -> 次の env を進める
```

- この順番だと CPU と GPU が交互に待ちやすい
- 全体の速度は最も遅い段階に引っ張られる
- 論文の出発点はこの待ち時間を減らすこと

---

<!-- _class: column-layout -->

### 非同期化すると速くなるが難しさも増える

<div class="column">

#### うれしいこと

- env 実行と GPU 推論を重ねられる
- learner 更新も並行しやすい
- throughput を大きく上げやすい

</div>

<div class="column">

#### 難しいこと

- worker 間通信が増える
- 古い policy のデータが混ざる
- 学習が不安定になることがある

</div>

---

### `policy lag` 

> #### 直感
>
> データを集めたときの policy と、
> learner が今更新している policy がずれること。

- 非同期化するとこのズレが大きくなりやすい
- ズレが大きすぎると update が不安定になる
- 後半では、このズレをどう抑えるかを実装と式の両方から見る

---

### Sample Factory の核は実行系の分業にある

> #### 何をした論文か
>
> Sample Factory は、
> **CPU の環境実行・GPU 推論・GPU 学習を同時並行で回す** ために、
> RL システムを部品分割した実行系である。 [@petrenko2020samplefactory]

- ただ速いだけでは不十分
- async 化で増える policy lag も抑えないと学習が崩れる
- 実装はこの 2 つを両立させる設計になっている

---

<!-- _class: column-layout -->

### 既存法で何が詰まるか

<div class="column">

#### 同期 PPO / A2C

- env step 中しか CPU が働かない
- forward/backward 中は env が止まる
- 高い GPU 利用率を作りにくい

</div>

<div class="column">

#### 単純な async 化

- worker 間通信が重い
- 古い policy で集めた軌跡が増える
- sample efficiency が落ちやすい

</div>

---

### この論文が解く 4 つの問題

| 問題 | 論文の方針 |
| :-- | :-- |
| 待ち時間 | workload を rollout / policy / learner に分割 |
| 通信量 | tensor は shared memory、queue は index だけ |
| policy lag | 重み即時反映 + 古い軌跡の制御 |
| off-policy 化 | PPO clipping と V-trace で補正 |

<small>論文: pp.2-5, Sec. 3.1-3.4</small>

---

## 設計

---

### `sample_factory/` は入口・学習本体・周辺機能に分かれる

```text path="code/project_layout.txt" fit-height="true"
```

---

### `algo/` に実行系の中核が集まっている

```text path="code/algo_layout.txt" fit-height="true"
```

---

### `sampling/` は env 実行と推論を分業している

```text path="code/sampling_layout.txt" fit-height="true"
```

---

### `learning/` と `algo/utils/` が更新処理を支える

```text path="code/learning_utils_layout.txt" fit-height="true"
```

---

### 学習開始から learner 更新までの本線

```text path="code/training_path.txt" fit-height="true"
```

---

### APPO - asynchronous PPO 

> #### 定義
>
> PPO の clipped update を土台にしつつ、
> サンプリングと learner 更新を非同期に重ねる方式。

- learner が更新している間も rollout worker は sample を集め続ける
- そのため sample は「少し古い policy」によるものを含む
- Sample Factory はこの前提で throughput を上げる [@petrenko2020samplefactory]

<small>論文: p.1, Introduction 後半; pp.4-5, Sec. 3.4</small>

---

### APPO を成立させる 3 つの要素

| 要素 | 役割 |
| :-- | :-- |
| async sampling | CPU の env 実行と learner 更新を止めない |
| PPO clipping | policy update を急に動かしすぎない |
| V-trace / lag control | 古い policy 由来の sample のズレを抑える |

この後の `shared memory`、`policy_version`、V-trace はこの表の具体化として読む。

---

### 論文の部品と現行コード

| 論文の語 | 現行実装 | 役割 |
| :-- | :-- | :-- |
| rollout worker | `algo/sampling/rollout_worker.py` | env を進める |
| policy worker | `algo/sampling/inference_worker.py` | GPU forward |
| learner | `algo/learning/learner.py` | SGD と重み更新 |
| sampler / runner | `sampler.py`, `runner_parallel.py` | 接続と起動管理 |

注: 論文の `policy worker` は、現行 master では `InferenceWorker` という名前になっている。
対応コードの参照: [@samplefactoryrepo2026]
<small>論文: p.3, Figure 1 / Sec. 3.1</small>

---

### 実行時データフロー

```text
RolloutWorker
  -> policy request を queue へ送る
InferenceWorker
  -> request を batch 化して GPU forward
  -> action / logprob / value を shared buffer に書く
RolloutWorker
  -> env.step() して rollout を完成させる
Batcher / Learner
  -> 学習バッチ化し、重みと policy_version を更新する
```

- 重要なのは「大きな tensor を送らない」こと
- 重要なのは「推論と学習の更新をなるべく止めない」こと

<small>論文: p.3, Figure 1 caption; Sec. 3.1 の rollout/policy/learner 説明</small>

---

## 問題と解決

---

### 1. 待ち時間: env と推論が交互に止まる

- 論文の解決策は double-buffered sampling
- 1 worker が持つ env 群を split し、片方の推論待ち中にもう片方を進める
- 現行実装では `worker_num_splits` がそのまま対応する

対応箇所:
- `RolloutWorker.num_splits`
- `RolloutWorker.env_runners`
- `BatchedVectorEnvRunner` / `NonBatchedVectorEnvRunner`

<small>論文: p.4, Figure 2(b) と Sec. 3.2 冒頭</small>

---

### 実装での double buffering

```python path="code/double_buffering.py" fit-height="true"
```

---

### 2. 通信量: actor と learner 間で巨大 tensor を送りたくない

- 論文は「queue では metadata だけ送る」と整理する
- 実データは shared tensor 上に置き、受け手は index から参照する

対応箇所:
- `shared_buffers.py::BufferMgr`
- `rollout_worker.py::_enqueue_policy_request()`
- `inference_worker.py::_batch_*()`

<small>論文: p.4, Sec. 3.3 前半</small>


---

### 3. policy lag: async 化すると古い policy の軌跡が混ざる

- 論文では lag の原因を 2 つに分ける
- 1つ目: 推論側が古い重みを持つ
- 2つ目: learner が処理し切れない軌跡が溜まる

現行実装の対策:
- `ensure_weights_updated()` で推論側へ即時反映
- `policy_version` を軌跡ごとに保存
- `max_policy_lag` を超えたデータは learner 側で無効化

<small>論文: pp.4-5, Sec. 3.4 前半</small>

---

### 実装での policy lag 制御

```python path="code/policy_lag_controls.py" fit-height="true"
```

---

### 4. off-policy のズレは learner 側で吸収する

$$
r_t % [!annotate label="ratio" note="target policy と behavior policy のズレを測る"]
= \exp(
\log \pi_\theta(a_t|s_t) % [!annotate label="target" note="learner が今最適化している policy"]
- \log \mu(a_t|s_t) % [!annotate label="behavior" note="実際にサンプルを生成した古い側の policy"]
)
$$

- policy loss は PPO の clipped surrogate を使う
- value / advantage 側では `with_vtrace=True` で V-trace を有効化できる
- つまり「高速化で生じるズレ」を learner 側で吸収する設計になっている

対応箇所:
- `learner.py`
- `cfg.py::with_vtrace`, `vtrace_rho`, `vtrace_c`

<small>論文: p.5, Sec. 3.4 後半の V-trace / PPO clipping 段落</small>

---

## まとめ

---

### まとめ


- Sample Factory の凄い点は「アルゴリズム」だけでなく「実行系の設計」にある
- 論文の問題設定は、現行実装でもかなり直接的に追跡できそう

---

# References

::: {#refs}
:::
