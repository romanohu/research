# TMU CS Marp Slides Project

このプロジェクトは、`marp-theme-tmu-cs` を使って複数の発表資料を管理・ビルドするためのテンプレートです。

各発表資料は、それぞれ独立したディレクトリに置きます。

## ディレクトリ構成

```text
my-slides/
├── package.json
├── scripts/
│   └── build.mjs
├── seminar/
│   ├── slides.md
│   ├── references.bib
│   ├── figures/
│   └── code/
├── conference/
│   ├── slides.md
│   ├── references.bib
│   ├── figures/
│   └── code/
└── dist/
```

## 各ファイルの役割

```text
package.json
```

ビルドコマンドと依存パッケージを管理します。

```text
scripts/build.mjs
```

指定したMarkdownファイルをHTML、PDF、PPTXなどに変換するためのビルドスクリプトです。

```text
seminar/slides.md
conference/slides.md
```

各発表資料の本体です。1つの `slides.md` が1つの発表資料に対応します。

```text
references.bib
```

各発表資料で使う参考文献ファイルです。資料ごとに分けて管理します。

```text
figures/
```

図、スクリーンショット、グラフなどを置きます。

```text
code/
```

スライド中で表示するソースコードを置きます。

```text
dist/
```

ビルド後のHTML、PDF、PPTXが出力されます。

## セットアップ

最初に依存パッケージをインストールします。

```sh
npm install
```

## PDFとしてビルドする

```sh
npm run pdf -- seminar/slides.md
```

出力例：

```text
dist/seminar-slides.pdf
```

## HTMLとしてビルドする

```sh
npm run html -- seminar/slides.md
```

出力例：

```text
dist/seminar-slides.html
```

## 単一HTMLとしてビルドする

画像などを埋め込んだ単一HTMLを作る場合は、次を使います。

```sh
npm run standalone -- seminar/slides.md
```

出力例：

```text
dist/seminar-slides.html
```

## PPTXとしてビルドする

```sh
npm run pptx -- seminar/slides.md
```

出力例：

```text
dist/seminar-slides.pptx
```

## 新しい発表資料を追加する

例えば、`paper-review` という発表資料を追加する場合は、次のようにディレクトリを作ります。

```text
my-slides/
└── paper-review/
    ├── slides.md
    ├── references.bib
    ├── figures/
    └── code/
```

その後、次のようにビルドします。

```sh
npm run pdf -- paper-review/slides.md
```

## Markdown内で画像を使う

`figures/result.png` を表示する場合：

```markdown
![width:800](figures/result.png)
```

## Markdown内で参考文献を使う

`references.bib` を同じディレクトリに置き、`slides.md` のfront matterで指定します。

```markdown
---
marp: true
theme: tmu-cs
paginate: true
bibliography: references.bib
---
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

## Markdown内で外部コードを読み込む

`code/example.py` を表示する場合：

```markdown
``` path="code/example.py"
```
```

高さに合わせて表示したい場合：

```markdown
``` path="code/example.py" fit-height="true"
```
```

## スライドの区切り

Marpでは、`---` が1枚のスライドの区切りです。

```markdown
# 1枚目

---

# 2枚目

---

# 3枚目
```

## 基本的なslides.mdの例

```markdown
---
marp: true
theme: tmu-cs
paginate: true
bibliography: references.bib
---

# 発表タイトル

氏名  
所属

---

## 背景

- 背景1
- 背景2
- 背景3

---

## 提案手法

- 手法1
- 手法2
- 手法3

---

## 結果

![width:800](figures/result.png)

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