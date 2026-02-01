# git

## 1. Setup & Config

| コマンド                                       | 説明                     |
| :----------------------------------------- | :--------------------- |
| ```git config --global user.name "名前"```   | ユーザー名の設定               |
| ```git config --global user.email "メール"``` | メールアドレスの設定             |
| ```git config --list```                    | 現在の設定内容を確認する           |
| ```git init```                             | カレントディレクトリをGitリポジトリ化する |
| ```git clone <url>```                      | 既存のリポジトリをローカルにコピーする    |

## 2. Basic Snapshotting

| コマンド | 説明 |
| :--- | :--- |
| ```git status``` | 変更されたファイルの状態を表示する |
| ```git add <file>``` | 特定のファイルをステージング(index)に追加 |
| ```git add .``` | 全ての変更（新規・修正・削除）をステージングに追加 |
| ```git add -p``` | ファイル内の変更箇所（ハンク）を確認しながら追加 |
| ```git commit -m "msg"``` | メッセージを付けてコミットする |
| ```git commit --amend``` | 直前のコミットを修正する（メッセージ変更など） |

## 3. Inspection & Comparison

| コマンド | 説明 |
| :--- | :--- |
| ```git log``` | コミット履歴を表示する |
| ```git log --oneline --graph --all``` | ブランチの分岐を視覚的に表示する |
| ```git diff``` | ワークツリーとステージングの差分を表示 |
| ```git diff --cached``` | ステージングと最新コミットの差分を表示 |
| ```git show <commit>``` | 特定のコミットの詳細内容を表示する |
| ```git blame <file>``` | ファイルの各行を誰がいつ編集したか表示する |

## 4. Branching & Merging

| コマンド | 説明 |
| :--- | :--- |
| ```git branch``` | ローカルブランチの一覧を表示 |
| ```git branch -a``` | リモートを含む全てのブランチを表示 |
| ```git switch <branch>``` | ブランチを切り替える |
| ```git switch -c <branch>``` | 新しいブランチを作成して切り替える |
| ```git merge <branch>``` | 現在のブランチに指定ブランチを統合する |
| ```git rebase <branch>``` | 現在のブランチの基点を指定ブランチの先端に移動する |
| ```git cherry-pick <hash>``` | 特定のコミットだけを現在のブランチに取り込む |

## 5. Sharing & Updating

| コマンド | 説明 |
| :--- | :--- |
| ```git remote -v``` | 登録されているリモートリポジトリを確認 |
| ```git fetch <remote>``` | リモートの最新情報を取得する（統合はしない） |
| ```git pull``` | リモートの変更を取得して現在のブランチにマージする |
| ```git push <remote> <branch>``` | ローカルの変更をリモートに送信する |
| ```git push -f``` | リモート履歴を強制的に上書きする（※注意が必要） |

## 6. Undoing & Stashing

| コマンド                          | 説明                         |
| :---------------------------- | :------------------------- |
| ```git restore <file>```          | ワークツリーの変更を元に戻す             |
| ```git restore --staged <file>``` | ステージングした内容を取り消す（Unstage）   |
| ```git reset --soft HEAD~1```     | コミットだけを取り消し、変更内容はステージングに残す |
| ```git reset --hard HEAD~1```     | コミットも変更内容も完全に破棄して1つ前に戻す    |
| ```git clean -fd```               | 追跡対象外のファイルやディレクトリを削除する     |
| ```git stash```                   | 未コミットの変更を一時的にスタックに退避する     |
| ```git stash list```              | 退避させている一覧を表示する             |
| ```git stash pop```               | 最新の退避内容を復元し、リストから削除する      |
