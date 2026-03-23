# Auto Summary Generator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 自動生成スクリプトで`.md`のみを昇順列挙した`SUMMARY.md`を再構築し、mdBookで全メモをブラウザ表示できるようにする。

**Architecture:** Python標準ライブラリ（`pathlib`, `re`, `argparse`など）だけで、リポジトリ直下を走査し、除外ディレクトリをスキップしつつツリーを組み立てる。各Markdownの先頭見出しをタイトルにし、`index.md`は親ディレクトリ名を優先する。結果を`SUMMARY.md`に上書き保存し、作成件数を標準出力へ表示する。

**Tech Stack:** Python 3 (標準ライブラリ), mdBook 0.5.2

---

### Task 1: スクリプトの骨組みを用意

**Files:**
- Create: `scripts/gen_summary.py`

- [ ] **Step 1:** `scripts/gen_summary.py`を作成し、`if __name__ == "__main__": main()`のエントリーポイントを置く。
- [ ] **Step 2:** `argparse`でオプションを定義（`--root` デフォルト`.`、`--output` デフォルト`SUMMARY.md`）。後で柔軟に使えるようにする。
- [ ] **Step 3:** 除外リストを定数で定義（`book`, `config/templates`, `.git`, `target`, `node_modules`, `__pycache__`）。`Path(root).resolve()`で基準パスを決め、除外判定は「候補の絶対パスが除外ディレクトリの配下かどうか」を`Path.is_relative_to`で判定する。

### Task 2: タイトル抽出とツリー構築

**Files:**
- Modify: `scripts/gen_summary.py`

- [ ] **Step 0:** ノード構造を決める（辞書 or dataclass）。`{ \"title\": str, \"path\": Path|None, \"children\": list, \"is_dir\": bool }` で統一し、`path`はMarkdownファイルにのみセットする。
- [ ] **Step 1:** `read_title(path: Path)`関数を実装。先頭の`# `見出しを正規表現で抽出し、無ければファイル名 stem を返す。UTF-8で読み、巨大ファイル対策で最初の数行だけ読む。
- [ ] **Step 2:** `node_title(path, parent_name=None)`を実装し、`index.md`の場合は親ディレクトリ名をデフォルトにしつつ見出しを優先する。
- [ ] **Step 3:** ディレクトリを再帰走査する`build_tree(path)`を作成。除外パスと`.md`拡張子フィルタを適用し、ディレクトリ→ファイルの順で昇順ソートしてノードを返す。`SUMMARY.md`自身と`root/index.md`（後で手動先頭挿入するため）を明示的にスキップする。

### Task 3: SUMMARY出力ロジック

**Files:**
- Modify: `scripts/gen_summary.py`
- Modify: `SUMMARY.md` (生成結果)

- [ ] **Step 1:** `render_tree(node, depth=0)`でMarkdownリストを組み立て、`- [Title](relative/path)`形式で出力。ノードがディレクトリの場合はリンク無しでタイトルだけ出し、その子をインデントしてレンダリングする。
- [ ] **Step 2:** `write_summary(root, output)`関数で`# Summary`ヘッダを付け、`root/index.md`を最初に置いたあとツリーを連結する。`render_tree`側で`root/index.md`が含まれないことを再確認（防御的に除外）。
- [ ] **Step 3:** `main()`で`write_text`し、生成件数（ノード数）を`print(f\"Wrote ...\")`で表示。上書き前のバックアップは不要（git管理で十分）。

### Task 4: 簡易セルフテスト

**Files:**
- Modify: `scripts/gen_summary.py`

- [ ] **Step 1:** `python - <<'PY'` のワンショットで `tempfile.TemporaryDirectory()` を使い、`a/index.md`, `a/b.md`, `a/c.md`, `book/skip.md`, `SUMMARY.md` を作成。`build_tree`と`write_summary`を呼んで「`book/`配下が除外される」「`index.md`が一度だけ出現する」「`b.md`と`c.md`が昇順で並ぶ」ことを`assert`する短い検証を書く。
- [ ] **Step 2:** 追加で`config/templates/foo.md`が除外されるケースも同じスクリプト内で検証し、すべての`assert`が通ることを確認する。

### Task 5: 動作確認とビルド

**Files:**
- Modify: `SUMMARY.md`

- [ ] **Step 1:** 実行: ``python scripts/gen_summary.py``。期待: コンソールに生成件数と出力パスが出る。`SUMMARY.md`が更新される。
- [ ] **Step 2:** `mdbook build`を実行し、ビルドが成功することを確認。期待: `book/` が更新され、エラーなし。
- [ ] **Step 3:** 必要なら`mdbook serve`でブラウザ確認（手動）。

### Task 6: 仕上げ

**Files:**
- Modify: `SUMMARY.md`
- Create/Modify: `scripts/gen_summary.py`

- [ ] **Step 1:** `git status`で変更確認。必要なら`git diff`で内容をざっと確認。
- [ ] **Step 2:** (任意) `git add scripts/gen_summary.py SUMMARY.md` でステージングし、`git commit -m "chore: auto-generate SUMMARY"`。
