num_splits = cfg.worker_num_splits
# [!annotate label="split count" note="1 worker が持つ env 群を 2 つ以上に分割する。"]
for split_idx in range(num_splits):
    env_runner = make_env_runner(split_idx)
    env_runners.append(env_runner)
def advance_rollouts(split_idx, policy_id):
    complete_rollouts, _ = env_runners[split_idx].advance_rollouts(policy_id, timing)
    # [!annotate label="step one split" note="action が返った split だけを進める。"]
    maybe_send_policy_request(env_runners[split_idx])
    # [!annotate label="overlap" note="片方の split が推論待ちの間に、もう片方の env 実行を続けやすい。"]
