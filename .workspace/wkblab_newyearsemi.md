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

#### 流れ

- 強化学習（RL）の基礎を復習
- Policy Gradient と Actor-Critic の位置づけ
- TRPO の課題を理解
- PPO の目的関数を数式で理解する

---

#### 強化学習の基本設定

- 状態: $s_t \in \mathcal{S}$
- 行動: $a_t \in \mathcal{A}$
- 報酬: $r_t = r(s_t, a_t)$
- 方策:
$$
\pi_\theta(a|s)
$$

- 目的関数:
$$
J(\theta)
= \mathbb{E}_\pi \left[\sum_{t=0}^\infty \gamma^t r_t \right]
$$

---

#### Policy Gradient の基本

方策を直接最適化する：

$$
\nabla_\theta J(\theta)
=
\mathbb{E}_{\pi_\theta}
\left[
\nabla_\theta \log \pi_\theta(a_t|s_t) \, G_t
\right]
$$

- $G_t$: 時刻 $t$ からの累積報酬
- REINFORCE の基本式

---

#### 分散削減：Advantage 関数

- 状態価値関数:
$$
V^\pi(s)
=
\mathbb{E}_\pi[G_t | s_t=s]
$$

- Advantage:
$$
A^\pi(s_t,a_t)
=
Q^\pi(s_t,a_t) - V^\pi(s_t)
$$

- 勾配は次の形に書ける：
$$
\nabla_\theta J(\theta)
=
\mathbb{E}
\left[
\nabla_\theta \log \pi_\theta(a_t|s_t) A_t
\right]
$$

---

#### Actor-Critic 法

- Actor: 方策 $\pi_\theta(a|s)$
- Critic: 価値関数 $V_\phi(s)$

TD 誤差による Advantage 近似：
$$
A_t
\approx
r_t + \gamma V_\phi(s_{t+1}) - V_\phi(s_t)
$$

➡️ 分散が小さく、安定した学習が可能

---

#### Policy Gradient の課題

- 学習が不安定
- 一度集めたデータで **1回しか更新できない**
- 更新が大きすぎると性能崩壊

➡️ 方策の更新量を制御したい

---

#### Trust Region Policy Optimization (TRPO)

制約付き最適化問題：

$$
\max_\theta
\;
\mathbb{E}
\left[
\frac{\pi_\theta(a|s)}
{\pi_{\theta_{\text{old}}}(a|s)}
A^{\pi_{\text{old}}}(s,a)
\right]
$$

subject to:
$$
D_{KL}
\left(
\pi_{\theta_{\text{old}}}
\;\|\;
\pi_\theta
\right)
\le \delta
$$

---

#### TRPO の問題点

- KL 制約の二次近似が必要
- 共役勾配法など実装が複雑
- ミニバッチ SGD が使いにくい

➡️ より簡単な trust region が必要

---

#### PPO の基本アイデア

- TRPO の「安全な更新」を
- **制約ではなく目的関数で実現**
- ミニバッチで複数 epoch 更新可能

---

#### 確率比 $r_t(\theta)$

$$
r_t(\theta)
=
\frac{\pi_\theta(a_t|s_t)}
{\pi_{\theta_{\text{old}}}(a_t|s_t)}
$$

- 新旧方策の変化量を表す

---

#### PPO の Clipped Objective

$$
L^{\text{CLIP}}(\theta)
=
\mathbb{E}_t
\Big[
\min(
r_t(\theta) A_t,\;
\text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) A_t
)
\Big]
$$

---

#### Clip の役割

- $r_t(\theta) > 1+\epsilon$
- $r_t(\theta) < 1-\epsilon$

➡️ それ以上の改善・悪化を **打ち切る**

➡️ 方策を「近接（proximal）」に保つ

---

#### PPO の直感

- $A_t > 0$  
  → 行動確率を適度に増やす
- $A_t < 0$  
  → 行動確率を適度に減らす

➡️ 極端な更新を防ぐ仕組み

---

#### Value Loss & Entropy Bonus

実際に最適化する目的関数：

$$
L(\theta)
=
L^{\text{CLIP}}
- c_1 (V_\phi(s_t) - V_t^{\text{target}})^2
+ c_2 \mathcal{H}(\pi_\theta)
$$

- Value loss: Critic 学習
- Entropy bonus: 探索の促進

---

#### PPO アルゴリズム

1. 方策 $\pi_{\theta_{\text{old}}}$ で軌道収集
2. Advantage を計算
3. データをミニバッチ化
4. $L^{\text{CLIP}}$ を複数 epoch 最適化
5. 方策更新

---

#### PPO の特徴

- TRPO 並みの安定性
- 実装が非常に簡単
- Adam / SGD と相性良好
- 実用 RL のデファクト

---

#### 実験結果（論文）

- MuJoCo（連続制御）
- Atari（離散制御）
- A2C / TRPO を多くのタスクで上回る

---

#### まとめ

- PPO = 安定な Policy Gradient
- 核心は Clipped Objective
- Actor-Critic と自然に統合
- 現代 RL の基盤技術

---

### Graph Attention-Guided Search for Dense Multi-Agent Pathfinding(2025)
Rishabh Jain, Keisuke Okumura, Michael Amir, Amanda Prorok

---