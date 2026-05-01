self.param_client.ensure_weights_updated()
# [!annotate label="fast sync" note="learner 側の新しい重みを inference worker がすぐに反映する。"]
policy_outputs["policy_version"] = fill(current_policy_version)
# [!annotate label="stamp" note="各サンプルがどの policy で収集されたかを記録する。"]
self.policy_versions_tensor[self.policy_id] = self.train_step
# [!annotate label="publish" note="learner 更新後に最新 version を共有メモリへ公開する。"]
lag_ok = curr_policy_version - buff["policy_version"] < cfg.max_policy_lag
valids = valids & lag_ok
# [!annotate label="drop stale data" note="古すぎる軌跡は learner 側で無効化する。"]
