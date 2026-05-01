# wkblab_paperprezentation7-2 Design

## Goal

7分程度の共有会向けに、「事前学習で潜在的にも獲得していない能力は、Fine-tuning だけでは新たに獲得しにくい」という経験則を、初心者にも追える数式と論文ベースの説明で紹介する。

## Audience

- 機械学習には触れている
- ただし NTK や表現学習理論は専門ではない
- 共有会なので、厳密証明よりも見通しの良さが重要

## Main Claim

Fine-tuning は「無から新しい能力を作る」よりも、

1. 事前学習で作られた表現や知識を選び直す
2. その使い方を再重み付けする
3. 場合によっては既存能力の上に薄い `wrapper` を載せる

操作として理解する方が自然である。

## Source Strategy

- 中核: `Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks`
  - `wrapper`
  - `wrapped capability`
  - `capability revival`
- 理論補助: `A Kernel-Based View of Language Model Fine-Tuning`
  - pretrained checkpoint 近傍での `small change`
  - 局所線形化の見方
- 現象補助: `Understanding Finetuning for Factual Knowledge Extraction`
  - `fact salience`
  - `attention imbalance`
  - 保存が弱い知識は FT でむしろ引き出しにくい
- 入口の補強: `On the Emergence of Cross-Task Linearity in Pretraining-Finetuning Paradigm`
  - 幾何の直感を現代的な paper で補う

## Slide Structure

1. 問い
2. 高次元幾何と特徴軸の直感
3. 3本の論文がどの部分を支えるか
4. mechanistic paper: wrapper / revival
5. kernel paper: small change と局所線形化
6. factuality paper: fact salience と attention imbalance
7. まとめ
8. references

## Authoring Constraints

- `tmu-cs` テーマの既存パターンに揃える
- 数式は1スライド1式程度に抑える
- 図ファイルは増やさず、テキストと式で完結させる
- JL/Madry の話は直感の入口としてのみ扱い、FT の直接理論と誤解させない

## Files To Create

- `prezentaion/wkblab_paperprezentation7-2/slides.md`
- `prezentaion/wkblab_paperprezentation7-2/references.bib`

