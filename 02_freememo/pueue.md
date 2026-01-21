Rust製のめちゃ便利CLI
処理に時間がかかる作業を待ち行列に入れて、裏で順番に回してくれる
インストールはバイナリでもパッケージマネージャでも良い(Nixで入れられるからdevboxで管理できる!!!)

## コマンド
タスクの追加(Add)
```sh
pueue add -- uv run train.py
```

ステータス確認
```
pueue status
```

ログの確認
```
pueue log <task-id>
# 出力をリアルタイムで追跡
pueue follow <task-id>
```