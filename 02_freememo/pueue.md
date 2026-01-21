Rust製のめちゃ便利CLI
処理に時間がかかる作業を待ち行列に入れて、裏で順番に回してくれる
インストールはバイナリでもパッケージマネージャでも良い(Nixで入れられるからdevboxで管理できる!!!)

タスクの追加(Add)
```sh
pueue add -- uv run train.py
## ラベル付きで追加
pueue add --label <label> uv run train.py
```

状況確認
```sh
# 全タスクのステータス表示
pueue status
# ログの確認
pueue log <task-id>
# 出力をリアルタイムで追跡
pueue follow <task-id>
```

タスクの削除
```sh
# 強制終了
pueue kill <task-id>
# キューから削除
pueue remove <task-id>
```