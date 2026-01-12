---
marp: true
theme: freud
paginate: true
math: mathjax
---

# ニューイヤーランチ会論文紹介
klis3年 鈴木史麿

---
## 紹介する論文
- Proximal Policy Optimization Algorithms
- Graph Attention-Guided Search for Dense Multi-Agent Pathfinding

---

### Proximal Policy Optimization Algorithms(2017)
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov

---

---
marp: true
theme: default
paginate: true
math: katex
---

# Proximal Policy Optimization (PPO)
### Proximal Policy Optimization Algorithms  
John Schulman et al., 2017

---

## 本発表の目的

- 強化学習（RL）の基礎を復習
- Policy Gradient と Actor-Critic の位置づけ
- TRPO の課題を理解
- PPO の目的関数と設計思想を数式で理解する

---

## 強化学習の基本設定

- **状態**: \( s_t \in \mathcal{S} \)
- **行動**: \( a_t \in \mathcal{A} \)
- **報酬**: \( r_t = r(s_t, a_t) \)
- **方策**:  
\[
\pi_\theta(a|s)
\]

- **目的**: 期待割引報酬の最大化
\[
J(\theta) = \mathbb{E}_\pi \left[\sum_{t=0}^\infty \gamma^t r_t \right]
\]

---

## Policy Gradient の基本

方策を直接最適化する：

\[
\nabla_\theta J(\theta)
= \mathbb{E}_{\pi_\theta} \left[
\nabla_\theta \log \pi_\theta(a_t|s_t) \, G_t
\right]
\]

- \(G_t\): 時刻 \(t\) からの累積報酬
- **REINFORCE** アルゴリズムの基礎

---

## 分散削減：Advantage 関数

- 状態価値関数
\[
V^\pi(s) = \mathbb{E}_\pi[G_t | s_t=s]
\]

- **Advantage**
\[
A^\pi(s_t,a_t) = Q^\pi(s_t,a_t) - V^\pi(s_t)
\]

- 勾配は次の形に：
\[
\nabla_\theta J(\theta)
= \mathbb{E}[\nabla_\theta \log \pi_\theta(a_t|s_t) A_t]
\]

---

## Actor-Critic 法

- **Actor**: 方策 \(\pi_\theta(a|s)\)
- **Critic**: 価値関数 \(V_\phi(s)\)

Advantage の近似：
\[
A_t \approx r_t + \gamma V_\phi(s_{t+1}) - V_\phi(s_t)
\]

➡️ 方策勾配を低分散で推定可能

---

## Policy Gradient の実践的問題

- 学習が不安定
- 一度のデータで **1回しか更新できない**
- 更新が大きすぎると性能が崩壊

➡️ **「方策をどれくらい変えてよいか」制御したい**

---

## Trust Region Policy Optimization (TRPO)

制約付き最適化問題：

\[
\max_\theta \;
\mathbb{E}\left[
\frac{\pi_\theta(a|s)}{\pi_{\theta_{\text{old}}}(a|s)}
A^{\pi_{\text{old}}}(s,a)
\right]
\]

subject to：
\[
D_{KL}(\pi_{\theta_{\text{old}}} \| \pi_\theta) \le \delta
\]

---

## TRPO の課題

- 二次近似・共役勾配法が必要
- 実装が複雑
- ミニバッチ SGD と相性が悪い

➡️ **もっとシンプルに trust region を実現したい**

---

## PPO の基本アイデア

- TRPO の「安全な更新」を
- **制約ではなく目的関数側で実現**
- 何度もミニバッチ更新できる

---

## PPO の確率比

\[
r_t(\theta)
= \frac{\pi_\theta(a_t|s_t)}
{\pi_{\theta_{\text{old}}}(a_t|s_t)}
\]

- 新旧方策の「変化量」を表す

---

## PPO の Clipped Surrogate Objective

\[
L^{\text{CLIP}}(\theta)
=
\mathbb{E}_t \Big[
\min(
r_t(\theta) A_t,\;
\text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) A_t
)
\Big]
\]

---

## Clip の意味

- \(r_t\) が
  - \(1+\epsilon\) を超える
  - \(1-\epsilon\) を下回る  
➡️ **それ以上の改善を無視**

- 方策更新を「近接（proximal）」に保つ

---

## PPO の直感的理解

- 良い行動（\(A_t > 0\)）  
  → ほどほどに強化
- 悪い行動（\(A_t < 0\)）  
  → ほどほどに抑制

➡️ 極端な更新を自動的に防ぐ

---

## Value Loss & Entropy Bonus

実際の最適化対象：

\[
L = L^{\text{CLIP}}
- c_1 (V_\phi(s_t) - V_t^{\text{target}})^2
+ c_2 \mathcal{H}(\pi_\theta)
\]

- Value loss：Critic 学習
- Entropy bonus：探索促進

---

## PPO アルゴリズムの流れ

1. 現在の方策で trajectory を収集
2. Advantage を計算
3. ミニバッチに分割
4. \(L^{\text{CLIP}}\) を **複数 epoch** 最適化
5. 方策更新

---

## PPO の特徴まとめ

- TRPO 並みの安定性
- 実装が非常に簡単
- SGD / Adam と相性良好
- 実用上のデファクトスタンダード

---

## 実験結果（論文より）

- MuJoCo（連続制御）
- Atari（離散制御）
- 多くのタスクで
  - A2C / TRPO より高性能
  - 学習が安定

---

## まとめ

- PPO = 「安全な Policy Gradient」
- Clipped Objective が核心
- Actor-Critic と自然に統合
- 現代 RL の基礎技術

---

### Graph Attention-Guided Search for Dense Multi-Agent Pathfinding(2025)
Rishabh Jain, Keisuke Okumura, Michael Amir, Amanda Prorok

---