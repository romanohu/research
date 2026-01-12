---
marp: true
theme: default
paginate: true
---

# Proximal Policy Optimization (PPO)
### Proximal Policy Optimization Algorithms
#### Schulman et al., 2017

---

## この発表のゴール
- PPOとは何かを**直観と数式の両方**で理解する
- なぜTRPOの代替として有効なのかを説明できる
- PPOが「なぜ安定して学習できるのか」を説明できる

---

## 背景：強化学習の基本設定
- エージェントが環境と相互作用
- 状態 \(s_t\)、行動 \(a_t\)、報酬 \(r_t\)
- 方策 \(\pi_\theta(a|s)\) を最適化

目的：
\[
\max_\theta \mathbb{E}\left[\sum_t \gamma^t r_t\right]
\]

---

## 方策勾配法（Policy Gradient）
- 方策を直接パラメータ \(\theta\) で最適化
- 勾配：
\[
\nabla_\theta J(\theta)
= \mathbb{E}[\nabla_\theta \log \pi_\theta(a_t|s_t) A_t]
\]

- **Advantage \(A_t\)**：
  - 「その行動は平均よりどれだけ良かったか」

---

## 既存手法の問題点
### Vanilla Policy Gradient
- 1サンプル → 1更新
- サンプル効率が悪い
- 学習が不安定

### 大きな更新の危険性
- 方策が一気に変わると性能が崩壊する

---

## TRPO（Trust Region Policy Optimization）
- 方策の更新幅を制限
- KL距離で制約：
\[
D_{KL}(\pi_{\theta_{\text{old}}} || \pi_\theta) \le \delta
\]

### 問題点
- 実装が複雑
- 二次最適化が必要
- 計算コストが高い

---

## 問題設定の整理
理想：
- 方策更新は**小さく**
- でも
- **同じデータで何度も学習**したい

→ 「安全で、簡単で、効率の良い」方法は？

---

## PPOの基本アイデア
- TRPOの「信頼領域」を
- **制約最適化ではなく**
- **目的関数に埋め込む**

キーワード：
- Surrogate Objective
- Importance Sampling
- Clipping

---

## Importance Sampling Ratio
\[
r_t(\theta)
= \frac{\pi_\theta(a_t|s_t)}
       {\pi_{\theta_{\text{old}}}(a_t|s_t)}
\]

意味：
- 「新しい方策が、過去の行動をどれだけ支持するか」

---

## PPOのClipped Objective
\[
L^{CLIP}(\theta)
= \mathbb{E}\left[
\min(
r_t(\theta) A_t,\;
\text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) A_t
)
\right]
\]

---

## Clippingの直観
- \(r_t\) が大きくなりすぎると
  - 学習を「打ち切る」
- → 急激な方策更新を防止

結果：
- TRPOと似た安定性
- しかし実装は非常に簡単

---

## PPOの学習ループ
1. 現在の方策でロールアウト
2. Advantage推定（GAEなど）
3. 同じデータで
   - ミニバッチ
   - 複数エポック
4. Clipped Objectiveで更新

---

## なぜPPOはうまくいくのか
- 更新幅を**暗黙的に制御**
- KL制約を解かない
- ノイズに強い
- 実装が簡単

---

## 実験設定
- MuJoCo（ロボット制御）
- Atariゲーム
- 比較手法：
  - Vanilla PG
  - TRPO
  - A2C など

---

## 実験結果
- PPOは
  - 高いサンプル効率
  - 安定した学習
  - 実装容易性
を同時に達成

→ 現在の標準アルゴリズムに

---

## PPOの限界
- 理論保証はTRPOより弱い
- クリップ幅 \(\epsilon\) に依存
- オフポリシーには不向き

---

## まとめ
- PPOは「実用最優先」の方策勾配法
- TRPOの思想をシンプルに実装
- 現代RLのデファクトスタンダード

---

## Take Home Message
**PPO = 安定性 × 実装容易性 × サンプル効率**
