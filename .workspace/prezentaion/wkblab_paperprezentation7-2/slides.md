---
marp: true
theme: tmu-cs
paginate: true
math: mathjax

title: "論文紹介"
subtitle: "Fine-tuning によって新しい能力を獲得できるのか"
author: "鈴木史麿"
affiliation: "wkblab"
date: "2026-05-01"

sectionPages: true
sectionPageLevel: 2
tocPageMaxLevel: 2
style: |
  section.refs-compact {
    font-size: 0.8em;
  }
---

# 目次

<!-- toc -->

---

## 問い

### 今日の問い

> 事前学習でまだ作られていない能力は、
> Fine-tuning だけで新たに獲得できるのか？

- 実務では `難しい` とよく言われる
- ただし、これは 1 本の完全な定理ではない
- 今日は `なぜそう考えられるのか` を 3 本の論文でつなぐ

> 今日の問い自体は一般の事前学習モデルを念頭に置く  
> ただし、紹介する論文は主に LM / Transformer 周辺の結果である

---

<!-- _class: all-text-center align-center -->

### 先に結論

> Fine-tuning は  
> **新能力の創造** というより  
> **事前学習でできた表現の使い方の変更**  
> とみると理解しやすい

---

## 直感

---

### 高次元ベクトル空間とは何か

$$
h(x) \in \mathbb{R}^d \qquad (d \text{ がとても大きい})
$$

- 多くの事前学習済みモデルでは、内部表現を巨大な次元のベクトルとして見られる
- この空間では、多くの方向を同時に持てる
- 直感的には `意味1 の方向`、`意味2 の方向`、`構文の方向` のように、特徴が別方向に分かれて入ると考える

> ここで言う `方向` は、特徴や回路の比喩である

---

### なぜ「高次元」が効くのか

$$
\cos \angle(u,v)=\frac{u^\top v}{\lVert u\rVert \lVert v\rVert}\approx 0
$$

- 高次元では、無関係な 2 方向は `ほぼ直交` とみなしやすい
- すると、ある特徴を強めても別の特徴を壊しにくい
- このため pretraining では、多数の特徴を `別の方向` に持ちやすい

> これは JL 補題そのものではない  
> より近いのは `高次元での内積の集中` や `concentration of measure` の直感である

---

### 「別方向に保持される」とはどういうことか

$$
h \approx a\,u + b\,v, \qquad u^\top v \approx 0
$$

- `u` を特徴 A の方向、`v` を特徴 B の方向とみる
- `a` を変えると A の強さが変わり、`b` を変えると B の強さが変わる
- `u^\top v \approx 0` なら、A を読む量と B を読む量があまり混ざらない

$$
u^\top h \approx a \lVert u\rVert^2, \qquad v^\top h \approx b \lVert v\rVert^2
$$

> つまり `特徴ごとに別のつまみがある` イメージになる

---

### なぜこれが FT の性質につながるのか

$$
f_{\mathrm{FT}}(x)
\approx
\sum_i (w_i+\Delta w_i)\phi_i(x)
$$

- すでに `\phi_i` があるなら、FT はまず `\Delta w_i` を動かして目的タスクに合わせればよい
- これは `既存のつまみを回す` だけなので、比較的小さい更新で済む

> まず `今ある特徴で解けるか` を試すのが自然になる

---

### 新しい特徴を作る方がなぜ重いのか

$$
f_{\mathrm{new}}(x)
\approx
\sum_i (w_i+\Delta w_i)\phi_i(x) + \alpha \psi(x)
$$

- 本当に新しい能力 `\psi(x)` を作るには、内部表現そのものを作り変える必要がある
- これは `既存のつまみを回す` より大きな更新を要しやすい

> だから最適化はまず `再重み付けで済む解` に寄りやすい

---

### そこから FT をどう見るか

$$
f(x)\approx \sum_{i=1}^{m} w_i \phi_i(x)
$$

- `\phi_i(x)` を `すでに獲得済みの特徴` とみる
- pretraining は `どんな特徴 \phi_i があるか` を作る段階
- FT はまず `重み w_i を変えて、どの特徴を前に出すか` を調整する段階

> だから `軸が最初から無い能力` は FT だけでは作りにくい

---

## 論文

---

### 1. Mechanistic 論文の主張

> Fine-tuning は capability を丸ごと作り直すより、
> その上に薄い `wrapper` を載せることが多い

```text
pretraining capability C
  -> fine-tuning
wrapped capability g ∘ C
```

- つまり `中身` より `見え方・使い方` が変わる
- 論文: Jain et al. (2024)
- 著者らは synthetic task でこれを mechanistic に追っている

---

### `wrapper` があるなら何が起きるか

```text
wrapped capability
  -> prune する
  or reverse fine-tuning する
  -> 元の capability が戻る
```

- 実際に著者らは `capability revival` を観測した
- これは `能力が完全に消えた` のでなく、`表面から使われなくなっただけ` と読む方が自然
- `FT は能力の配線を覆う` という見方を強く支持する

---

### 2. Kernel 論文の主張

$$
f_{\theta_0+\Delta\theta}(x)
\approx
f_{\theta_0}(x)+\nabla_{\theta}f_{\theta_0}(x)^\top\Delta\theta
$$

- `\theta_0` は pretrained checkpoint
- `\Delta\theta` は fine-tuning での更新
- この式は `pretrained 点の近くなら、FT は一次近似でかなり説明できる` という見方を与える
- 論文: Malladi et al. (ICML 2023)

> つまり `大改造` より `小さな再調整` とみる方が合う

---

### 3. Factuality 論文の主張

$$
\mathrm{salience}(s,r,a)=e(a)^\top V e(s)
$$

- `fact salience` は、その fact が pretrained model にどれだけ強く保存されているかの尺度
- 保存が弱い fact で FT すると、知識そのものを使うより `もっともらしい近道` が強化されやすい
- 著者らはこれを `attention imbalance` で説明する
- 論文: Ghosal et al. (ICML 2024)

---

### この論文が示すこと

> `知識がまったく無い` だけでなく、
> `弱くしか保存されていない` 場合も FT は危うい

- つまり FT は `知識注入装置` ではない
- 先に内部に十分強く保存されている知識ほど、FT で引き出しやすい
- 逆に保存が弱いと、FT は新知識の獲得より shortcut 強化に流れうる

---

## まとめ

---

### 3 本をつなぐと

1. 高次元表現では、特徴は別方向に分かれて保持されやすい
   つまり `特徴ごとに別のつまみを持てる`
2. Mechanistic 論文では、FT 後も元の capability が `revival` する
3. Kernel 論文では、FT は pretrained 点近傍の `small change` とみなせる
4. Factuality 論文では、弱い知識は FT で素直に出ず、shortcut 側が強まる

---

### Takeaway

> Fine-tuning は  
> **pretraining で作られた特徴・知識・回路を**  
> **選び直し、抑えたり前に出したりする操作**  
> とみるのが基本

- したがって `pretraining に無い能力を FT で作る` ことは難しい
- 少なくとも `小さい更新の regime` では、その見方がかなり強い
- 逆に言うと、本体は FT より pretraining にある

---

### ただし言いすぎには注意

- `絶対に不可能` を示す万能定理ではない
- 大きな更新、長い学習、構造変更では話が変わりうる
- 今日の結論は  
  `通常の FT では、新能力の創造より既存能力の再利用が主である`

---

<!-- _class: refs-compact -->

# 参考文献

- Zhou et al., *On the Emergence of Cross-Task Linearity in Pretraining-Finetuning Paradigm*, ICML 2024
- Jain et al., *Mechanistically Analyzing the Effects of Fine-Tuning on Procedurally Defined Tasks*, arXiv 2024
- Malladi et al., *A Kernel-Based View of Language Model Fine-Tuning*, ICML 2023
- Ghosal et al., *Understanding Finetuning for Factual Knowledge Extraction*, ICML 2024
