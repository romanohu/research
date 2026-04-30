---
marp: true
theme: tmu-cs
paginate: true
math: mathjax

title: "発表タイトル"
subtitle: "副題・研究テーマ"
author: "氏名"
affiliation: "所属"
date: "2026-04-30"

bibliography: references.bib

sectionPages: true
sectionPageLevel: 2
tocPageMaxLevel: 2
---

# 目次

<!-- toc -->

---

## 背景

---

### 研究背景

- 問題領域の概要
- 既存研究・既存手法の限界
- 本研究で扱う問い

関連研究として Internet Protocol の仕様 [@postel1981ip] と、C++ の体系的解説 [@stroustrup2022tour] を例示する。

---

### 定義カード

> #### 正規化
> 非負値の列を、その総和が1になるように変換する操作。
> 確率分布、重み付け、特徴量処理などで使われる。

---

<!-- _class: column-layout -->

### 2カラム構成

<div class="column">

#### 現状

- データの分布が不均衡
- 手法間の比較条件が不統一
- 評価指標の解釈が難しい

</div>

<div class="column">

#### 提案

- 前処理を明示化
- 同一条件で比較
- 指標を複数提示

</div>

---

## 提案手法

---

### 数式

正規化の基本形は次のように書ける。

$$
p_i % [!annotate label="確率" note="i番目の要素に割り当てる確率"]
= \frac{x_i}{\sum_j x_j} % [!annotate note="全要素の総和で割って正規化する"]
$$

---

### コード注釈

```python
def normalize(values):
    total = sum(values)
    # [!annotate label="total" note="正規化の分母。0の場合は別処理が必要。"]
    if total == 0:
        return values
    return [v / total for v in values]
```

---

### ステップ強調

```python
values = [1, 2, 3]                 # [!step 1 highlight]
total = sum(values)                # [!step 2 focus]
probs = [v / total for v in values] # [!step 3 info]
print(probs)                       # [!step 4 highlight]
```

---

### 外部コード読み込み

``` path="code/example.py" fit-height="true"
```

---

## 実験

---

### 実験設定

| 項目 | 内容 |
| :-- | :-- |
| データ | ここにデータセット名を書く |
| 比較手法 | Baseline, Proposed |
| 指標 | Accuracy, F1, Runtime |

---

### 結果

| 手法 | Accuracy | F1 | Runtime |
| :-- | --: | --: | --: |
| Baseline | 0.82 | 0.79 | 1.00x |
| Proposed | 0.87 | 0.84 | 1.12x |

---

## まとめ

---

### 結論

- 問題設定を整理した
- 提案手法の要点を示した
- 実験結果により有効性を確認した

今後の課題：

- より大規模なデータでの検証
- アブレーションスタディ
- 実運用条件での評価

---

# References

::: {#refs}
:::