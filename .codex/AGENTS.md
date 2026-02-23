# fill Author 運用指示書

## 目的
ユーザーが `fill Author`（または同義の短い指示）を出したときに、`03_research/*` の論文メモへ著者情報を追記し、`03_research/Authors/*` に著者ページを追加・更新し、相互リンクを通す作業を一括で再現する。

## トリガー
- ユーザーが `fill Author` と指示したとき
- または「論文メモから著者を埋めて Authors へリンクして」の意図が明確なとき

## 対象範囲
- 論文メモ: `03_research/**/papers.md` と `03_research/MARL/*_papers.md`
- 著者ページ: `03_research/Authors/japanese/*.md`, `03_research/Authors/overseas/*.md`
- 著者一覧: `03_research/Authors/index.md`

## 実施手順
1. `papers.md` から論文エントリを収集する。優先対象は `####` 見出しの論文。
2. 各論文の公式ページ（arXiv / 出版社 / OpenReview / 学会ページ）をWeb検索し、著者名を確認する。
3. 取得できた著者データに複数著者が含まれる場合は、第一著者のみで止めず全員を追記する。
4. 各論文見出しの直下に著者行を追記する。
   - 形式: `[Name](../Authors/overseas/NameFile.md) [Name2](../Authors/overseas/Name2File.md) ...`
   - 日本語名: `[氏名](../Authors/japanese/氏名.md)`
   - `著者:` のプレフィックスは付けない。
5. 著者ページを作成/更新する。
   - テンプレート:
     - `# 著者名`
     - `## 論文`
     - `### 年`
     - `- [論文タイトル](../../<分野>/papers.md#アンカー)`
6. `03_research/Authors/index.md` に著者リンクを追加する。
   - Japanese / Overseas の区分を守る。
   - 既存エントリは消さず、重複のみ回避する。
7. 相互リンクを検証する。
   - `papers.md` 側の `../Authors/...` が実ファイルを指すこと
   - `Authors/*.md` 側の `../../.../papers.md#...` が実在する論文アンカーを指すこと

## 記法ルール
- 既存ファイルの書式（見出しレベル、全角/半角、リンク相対パス）を壊さない。
- 既存にある著者行を上書きしない。必要なら追記・修正のみ行う。
- 迷った場合は新規の表記ゆれを作らず、既存ファイル名に合わせる。

## 完了条件
- 追加された論文に著者行がある
- 対応する著者ページが存在する
- `Authors/index.md` から辿れる
- 主要なリンク切れがない
