traj_tensors = alloc_trajectory_tensors(..., share=True)
# [!annotate label="trajectory buffer" note="obs, rewards, logprob, values を共有テンソルに置く。"]
policy_output_tensors = alloc_policy_output_tensors(..., share=True)
# [!annotate label="policy output buffer" note="action と next rnn state も共有テンソルに置く。"]
policy_request = (worker_idx, split_idx, requests, sampling_device)
inference_queues[policy_id].put(policy_request)
# [!annotate label="tiny message" note="queue に載せるのは index と metadata だけ。"]
observations = traj_tensors["obs"][indices]
rnn_states = traj_tensors["rnn_states"][indices]
# [!annotate label="lookup by index" note="受信側は shared buffer から必要な行だけ参照する。"]
