# 論文紹介スライドテンプレートの使い方

このディレクトリは、調べてきた論文を共有するための Marp スライド資料を作成するためのテンプレートです。

1つのディレクトリが、1つの論文紹介プレゼンに対応します。

## 想定ディレクトリ構成

```text
paper-review/
├── README.md
├── slides.md
├── references.bib
├── figures/
│   ├── paper-overview.png
│   ├── method-overview.png
│   └── result-table.png
└── code/
    └── example.py
```

## 各ファイルの役割

```text
slides.md
```

論文紹介スライドの本体です。

```text
references.bib
```

紹介する論文や関連研究の BibTeX 情報を置きます。

```text
figures/
```

論文中の図、自作の説明図、実験結果の表、スクリーンショットなどを置きます。

```text
code/
```

論文の手法を説明するためのコード例を置きます。

## 最初にやること

`slides.md` の冒頭にある front matter を自分の発表内容に合わせて変更します。

```markdown
---
marp: true
theme: tmu-cs
paginate: true
math: mathjax

title: "論文紹介タイトル"
subtitle: "Paper Reading / Literature Review"
author: "氏名"
affiliation: "所属"
date: "YYYY-MM-DD"

bibliography: references.bib

sectionPages: true
sectionPageLevel: 2
tocPageMaxLevel: 2
---
```

変更する主な項目は次です。

```text
title        : 発表タイトル
subtitle     : 副題
author       : 発表者名
affiliation  : 所属
date         : 発表日
bibliography : 参考文献ファイル
```

## スライドの基本ルール

Marp では、`---` が1枚のスライドの区切りです。

```markdown
# 1枚目のスライド

---

# 2枚目のスライド

---

# 3枚目のスライド
```

つまり、`slides.md` という1つのファイルの中に、発表資料全体を書きます。

## 論文紹介スライドの基本構成

このテンプレートでは、次の順番で発表することを想定しています。

```text
1. タイトル
2. 目次
3. 論文の基本情報
4. 一言でいうと
5. なぜこの論文を選んだか
6. 背景
7. 問題設定
8. 既存手法の限界
9. 論文の主張
10. 提案手法
11. 実験設定
12. 主結果
13. アブレーション実験
14. 追加分析
15. 考察
16. 自分の研究との関係
17. まとめ
18. Discussion
19. References
```

必要に応じて、不要なスライドは削除して構いません。

## まず埋めるべきスライド

最初に、以下のスライドだけを埋めると全体像を作りやすいです。

```text
- 論文の基本情報
- 一言でいうと
- 研究背景
- 問題設定
- 既存手法の限界
- 提案手法の概要
- 主結果
- 論文の貢献
- 弱み・限界
- 自分の研究との関係
- まとめ
```

## 論文の基本情報を書く

```markdown
### 紹介する論文

| 項目 | 内容 |
| :-- | :-- |
| タイトル | 論文タイトル |
| 著者 | 著者名 |
| 発表年 | YYYY |
| 掲載先 | Conference / Journal |
| URL / DOI | URLまたはDOI |
| 分野 | 例：自然言語処理、機械学習、HCI、セキュリティなど |
```

## 「一言でいうと」の書き方

次の型を使うと書きやすいです。

```markdown
> この論文は、**何の問題**に対して、**どのような方法**を提案し、**何を示した**研究である。
```

例：

```markdown
> この論文は、既存手法では困難だった長文文脈理解の問題に対して、検索拡張型の推論手法を提案し、複数のQAデータセットで有効性を示した研究である。
```

## 背景スライドの書き方

背景では、いきなり手法を説明せず、次の順番で書くと伝わりやすいです。

```text
1. 分野全体で何が重要なのか
2. これまで何が研究されてきたのか
3. まだ何が解けていないのか
4. この論文はどこに着目しているのか
```

例：

```markdown
### 研究背景

この分野では、〇〇という問題が重要である。

- 〇〇は実応用で頻繁に発生する
- 既存手法では△△の条件で性能が低下する
- そのため、□□を扱える手法が求められている

既存研究では、〇〇に対して複数のアプローチが提案されてきた [@example2024]。
```

## 問題設定の書き方

```markdown
### 問題設定

この論文が扱う問題は次の通りである。

```text
入力：ここに入力を書く
出力：ここに出力を書く
目的：ここに目的を書く
```
```

例：

```markdown
```text
入力：ユーザの発話履歴
出力：次に推薦すべきアイテム
目的：ユーザの意図を反映した推薦精度を向上させる
```
```

## 提案手法の説明順

提案手法は、次の順番で説明すると理解されやすいです。

```text
1. まず全体像を図で示す
2. 入力と出力を説明する
3. 重要なアイデアを3つ程度に分ける
4. 必要なら数式を説明する
5. 必要なら擬似コードや実装例を示す
```

## 図を入れる

`figures/method-overview.png` を表示する例です。

```markdown
![width:900](figures/method-overview.png)
```

画像の幅を小さくする場合：

```markdown
![width:600](figures/method-overview.png)
```

図の後には、必ず読み取り方を書きます。

```markdown
図の説明：

- 左側：入力
- 中央：提案モデル
- 右側：出力
- 下部：学習または評価の流れ
```

## 数式を入れる

```markdown
$$
\mathcal{L}
=
\mathcal{L}_{task}
+
\lambda \mathcal{L}_{reg}
$$
```

数式の後には、各記号の意味を書きます。

```markdown
ここで、

- $\mathcal{L}_{task}$：主タスクの損失
- $\mathcal{L}_{reg}$：正則化項
- $\lambda$：重み係数
```

## コードを入れる

スライド内に直接書く場合：

```markdown
```python
def proposed_method(x, model):
    features = preprocess(x)
    output = model(features)
    return output
```
```

外部ファイルを読み込む場合：

```markdown
``` path="code/example.py"
```
```

高さに合わせて表示する場合：

```markdown
``` path="code/example.py" fit-height="true"
```
```

## コード注釈を使う

```markdown
```python
def proposed_method(x, model):
    features = preprocess(x)
    # [!annotate label="前処理" note="入力をモデルに適した形式へ変換する"]

    output = model(features)
    # [!annotate label="推論" note="提案モデルによる予測"]

    return output
```
```

## 実験設定の書き方

```markdown
### 実験設定

| 項目 | 内容 |
| :-- | :-- |
| データセット | データセット名 |
| 比較手法 | Baseline A, Baseline B, Proposed |
| 評価指標 | Accuracy, F1, AUC, RMSEなど |
| 実装 | フレームワーク、GPU、学習条件など |
| ハイパーパラメータ | learning rate, batch size, epochなど |
```

## 主結果の書き方

```markdown
### 主結果

| 手法 | Metric 1 | Metric 2 | Metric 3 |
| :-- | --: | --: | --: |
| Baseline A | 0.00 | 0.00 | 0.00 |
| Baseline B | 0.00 | 0.00 | 0.00 |
| Proposed | **0.00** | **0.00** | **0.00** |

結論：

- 提案手法は〇〇で最良
- 特に△△の条件で改善幅が大きい
- 一方で□□では改善が限定的
```

表だけを出すのではなく、必ず下に「何が読み取れるか」を書きます。

## アブレーション実験の書き方

```markdown
### アブレーション実験

| 設定 | Metric 1 | Metric 2 |
| :-- | --: | --: |
| Full Model | **0.00** | **0.00** |
| w/o Component A | 0.00 | 0.00 |
| w/o Component B | 0.00 | 0.00 |
| w/o Component C | 0.00 | 0.00 |

読み取り：

- Component A は〇〇に効いている
- Component B は△△に寄与している
- Component C の効果は限定的
```

## 考察スライドで書くべきこと

考察では、論文の内容をただ要約するだけでなく、自分の評価を書くとよいです。

```text
- 何が新しいのか
- 何が強いのか
- どこに限界があるのか
- 実験は十分か
- 自分の研究にどう関係するか
- 自分ならどう拡張するか
```

## 弱み・限界の書き方

```markdown
### 弱み・限界

- データセットが限定的
- 実運用環境での検証が不足
- 計算コストが高い可能性
- 特定条件で性能が低下する
- 理論的な説明が十分ではない
```

## 自分の研究との関係を書く

```markdown
### 自分の研究との関係

| 観点 | 関係 |
| :-- | :-- |
| 問題設定 | 〇〇が共通している |
| 手法 | △△を応用できる可能性がある |
| 評価 | □□という評価方法が参考になる |
| 今後の課題 | ◇◇を発展させられる |
```

## 参考文献を書く

`references.bib` に BibTeX を書きます。

```bibtex
@inproceedings{example2024,
  author = {Author, Alice and Author, Bob},
  title = {Title of the Paper},
  booktitle = {Proceedings of the Example Conference},
  year = {2024},
  pages = {1--10},
  url = {https://example.com/paper}
}
```

本文中では次のように引用します。

```markdown
既存研究ではこの問題が指摘されている [@example2024]。
```

最後に参考文献スライドを置きます。

```markdown
# References

::: {#refs}
:::
```

## ビルド方法

プロジェクトルートにいる状態で実行します。

```sh
npm install
```

PDFを作る場合：

```sh
npm run pdf -- paper-review/slides.md
```

HTMLを作る場合：

```sh
npm run html -- paper-review/slides.md
```

PPTXを作る場合：

```sh
npm run pptx -- paper-review/slides.md
```

単一HTMLを作る場合：

```sh
npm run standalone -- paper-review/slides.md
```

## 出力先

ビルド結果は `dist/` に出力されます。

例：

```text
dist/paper-review-slides.pdf
dist/paper-review-slides.html
dist/paper-review-slides.pptx
```

## 発表前チェックリスト

発表前に、次を確認します。

```text
[ ] 論文タイトル・著者・発表年が正しい
[ ] 論文の主張を一言で説明できる
[ ] 背景と問題設定が分かる
[ ] 提案手法の全体像を図で説明できる
[ ] 実験設定が明確
[ ] 主結果の表に読み取りコメントがある
[ ] アブレーション実験の意味を説明できる
[ ] 弱み・限界を書いている
[ ] 自分の研究との関係を書いている
[ ] Discussion 用の問いを用意している
[ ] 参考文献が正しく出力される
[ ] PDFでレイアウト崩れがない
```

## 推奨する作成手順

```text
1. 論文を読む
2. 論文の基本情報を slides.md に書く
3. references.bib に BibTeX を追加する
4. 「一言でいうと」を書く
5. 背景・問題設定・既存手法の限界を書く
6. 提案手法の図を figures/ に置く
7. 実験設定と主結果を書く
8. 強み・弱み・自分の研究との関係を書く
9. Discussion スライドを作る
10. PDFにビルドして確認する
```

## よくある修正ポイント

### スライドに情報を詰め込みすぎる

1枚のスライドには、基本的に1つの主張だけを書く。

悪い例：

```text
背景、問題設定、既存研究、提案手法を1枚にまとめる
```

良い例：

```text
背景で1枚
問題設定で1枚
既存手法の限界で1枚
提案手法で1枚
```

### 表だけで説明がない

表の下には、必ず読み取りを書く。

```markdown
読み取り：

- 提案手法は Metric 1 で最良
- Baseline B との差は 〇〇
- ただし Metric 3 では改善が小さい
```

### 図の意味が分からない

図を貼るだけではなく、どこを見るべきかを書く。

```markdown
この図では、中央の〇〇モジュールが提案手法の主要部分である。
```

## 発表時間ごとの目安

### 5分発表

```text
1. タイトル
2. 一言でいうと
3. 背景
4. 提案手法
5. 主結果
6. まとめ
```

### 10分発表

```text
1. タイトル
2. 論文の基本情報
3. 背景
4. 問題設定
5. 既存手法の限界
6. 提案手法
7. 実験設定
8. 主結果
9. 考察
10. まとめ
```

### 15分以上の発表

```text
1. タイトル
2. 目次
3. 論文の基本情報
4. 背景
5. 問題設定
6. 既存手法の限界
7. 提案手法の全体像
8. 手法の詳細
9. 数式またはアルゴリズム
10. 実験設定
11. 主結果
12. アブレーション実験
13. 追加分析
14. 強み・弱み
15. 自分の研究との関係
16. Discussion
17. References
```

## 最小構成の slides.md

時間がない場合は、次の最小構成から作るとよいです。

```markdown
---
marp: true
theme: tmu-cs
paginate: true
math: mathjax
title: "論文紹介"
author: "氏名"
affiliation: "所属"
date: "YYYY-MM-DD"
bibliography: references.bib
---

# 論文紹介

## 論文タイトル

著者名  
会議・ジャーナル名, 年

---

## 一言でいうと

> この論文は、**何の問題**に対して、**どのような方法**を提案し、**何を示した**研究である。

---

## 背景

- 背景1
- 背景2
- 背景3

---

## 問題設定


入力：
出力：
目的：


---

## 提案手法

![width:900](figures/method-overview.png)

---

## 実験結果

| 手法 | Metric 1 | Metric 2 |
| :-- | --: | --: |
| Baseline | 0.00 | 0.00 |
| Proposed | **0.00** | **0.00** |

---

## 考察

- 強み：
- 弱み：
- 自分の研究との関係：

---

## まとめ

- 要点1
- 要点2
- 要点3

---

# References

::: {#refs}
:::
```