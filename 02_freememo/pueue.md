# pueue

Rust製のめちゃ便利CLI
処理に時間がかかる作業を待ち行列に入れて、裏で順番に回してくれる
インストールはバイナリでもパッケージマネージャでも良い(Nixで入れられるからdevboxで管理できる!!!)

---
起動/終了
```sh
# 起動
pueued -d
# 終了
pueue shutdown
```

---
タスクの追加
```sh
pueue add -- uv run train.py
## ラベル付きで追加
pueue add --label <label> uv run train.py
```

---
状況確認
```sh
# 全タスクのステータス表示
pueue status
# ログの確認
pueue log <task-id>
# 出力をリアルタイムで追跡
pueue follow <task-id>
```

---
タスクの削除
```sh
# 強制終了
pueue kill <task-id>
# キューから削除
pueue remove <task-id>
## 全削除
pueue reset
```

---
キューの操作
```sh
# 順番入れ替え
pueue switch <task-id-1> <task-id-2>
# 完了したタスクをリストから消去
pueue clear
```

---
グループ管理
```sh
# グループを作成
pueue group add <group>
# グループを指定してタスクを追加
pueue add --group <group> uv run train.py
```

---
Tips
```sh
# 並列数の変更
pueue parallel 2
```