---
marp: true
theme: freud
paginate: true
math: mathjax
---

# 論文紹介
klis3年 鈴木史麿

---

## 紹介する論文
- DISCOVERING DIVERSE MULTI-AGENT STRATEGIC
BEHAVIOR VIA REWARD RANDOMIZATION

---

### [DISCOVERING DIVERSE MULTI-AGENT STRATEGIC BEHAVIOR VIA REWARD RANDOMIZATION(2021)](https://arxiv.org/abs/2103.04564)
Zhenggang Tang, Chao Yu, Boyuan Chen, Huazhe Xu, Xiaolong Wang, Fei Fang, Simon Du, Yu Wang, Yi Wu

---

### Introduction①
分散型マルチエージェント強化学習
→ エージェント同士が相互に競争しながら、それぞれの報酬を最適化することで徐々に戦略を向上させていく

この学習における到達点の指標として1つ挙げられるのが「ナッシュ均衡(NE:Nash equilibrium)」である
- いかなるプレイヤーも単独で戦略を変更することで利益を得られないという状態
- 一般にあるゲームにおいて複数存在する
- 異なるNEは異なる利得をもたらす可能性がある
→ しかし、様々なゲームで成功を収めている分散型ポリシー勾配アルゴリズム(PG)では複数NEが存在する場合でも、常に特定のNEに収束してしまうという問題がある

---

### Introduction②
一般にそれは探索強化によって緩和が図られる
> 例 : RND, DIAYN, PBT

しかし、それらでは報酬地形(収束先)が固定されているため、所謂「戦略」の多様性は増えない

PGは広いbasinによって低報酬均衡に収束しがち

→ 問題提起「どうすれば多エージェント環境で意味のある多様な均衡戦略を発見できるのか？」

---

#### 均衡探索の新しい方法が必要

---

#### 提案① RR (Reward Randomization)
固定された報酬関数のもとで最適化するのではなく，報酬関数そのものをランダムに変形する

直感的には……
- 報酬地形が変わる
- 均衡の basin 構造が変わる
- 異なる均衡に到達可能になる

---

##### 通常の目的関数

各エージェント $i$ の目的：

$$
J_i(\theta)
=
\mathbb{E}_{\pi_\theta}
\left[
\sum_{t=0}^{\infty}
\gamma^t r_i(s_t,\mathbf{a}_t)
\right]
$$


##### RRの操作
報酬関数をランダムパラメータ $\omega$ によって変形：

$$
r_i^\omega(s,\mathbf{a})
=
r_i(s,\mathbf{a})
+
\omega^\top \phi_i(s,\mathbf{a})
$$

##### RRの目的関数
$$
J_i^\omega(\theta)
=
\mathbb{E}_{\pi_\theta}
\left[
\sum_t
\gamma^t r_i^\omega(s_t,\mathbf{a}_t)
\right]
$$

---

#### 提案② RPG (Reward-Randomized Policy Gradient)
RRとPolicy Gradientを組み合わせたアルゴリズム

##### Step1 : 報酬をサンプリング

$$
\omega_k \sim p(\omega)
$$

##### Step2 : 各報酬でPolicy Gradient

政策勾配：

$$
\nabla_\theta J_i^\omega(\theta)
=
\mathbb{E}
\left[
\nabla_\theta \log \pi_\theta(a_i|s)
\, A_i^\omega(s,\mathbf{a})
\right]
$$

ここで

$$
A_i^\omega = Q_i^\omega - V_i^\omega
$$

---

##### Step3 : 多様な戦略集合を得る

$$
\{ \theta^{(1)}, \theta^{(2)}, \dots, \theta^{(K)} \}
$$

##### Step4 : 元の報酬で再評価

$$
J_i^{\text{orig}}(\theta^{(k)})
=
\mathbb{E}
\left[
\sum_t
\gamma^t r_i(s_t,\mathbf{a}_t)
\right]
$$

最良の戦略を選択：

$$
k^* =
\arg\max_k
\sum_i
J_i^{\text{orig}}(\theta^{(k)})
$$

---

##### 通常のPGとの比較

通常PG：

$$
\Pr(\theta \to \theta^*)
\propto
\text{Vol}(\mathcal{B}(\theta^*))
$$

RPG：

$$
\Pr(\text{good equilibrium})
=
\mathbb{E}_\omega
\left[
\Pr_\omega(\theta \to \theta^*)
\right]
$$

→ 狭い高報酬均衡に到達する確率を増やせる

---

### 実験設定：Temporal Trust Dilemmas

#### 目的
- 「リスクの高い協調均衡（高報酬）」と
- 「安全だが低報酬な非協調均衡」

が共存するゲームで  
RPGが多様な戦略を発見できるか検証

---

#### Gridworld①：Monster-Hunt
最適解：同時に正確に協調して捕獲

しかし
- 単独リンゴ狩りは安全
- 協調は高報酬だが難しい

#### Gridworld②：Escalation
協調を続けるほどリスク増大
NEは複数存在： Lステップ協調して離脱

---

#### Agar.io
戦略のジレンマ
- 協調：囲んで効率よく狩る
- 裏切り：相手を食べる（即時大報酬）

→ 高報酬協調は極めて不安定

---

### 結果

#### Monster-Hunt

- 通常PG → 低報酬戦略に収束
- RPG → 協調均衡を安定的に発見
- fine-tuning後は常に最適戦略へ

特徴：
- RR段階だけでは不安定
- RPG（評価＋微調整）で最適解に到達

---

#### Escalation
- RRだけで複数の異なるNEを発見
- 一部のwで既に最適均衡に到達
- fine-tuning不要なケースもあり
---

#### Agar.io

通常PG：
- 一時的協調 → 攻撃発生 → 最終的に非協調へ

RPG：
- 協調均衡を安定的に発見
- fine-tuningでさらに報酬向上

#### Agar.io（攻撃的設定）

より難しい環境：

- 通常PG・PBT・RND → 協調失敗
- RPG → 高報酬協調を安定発見

---

読んでみた所感としては



---

### 報酬系の論文①

- [Exploration by Random Network Distillation(2018)](https://arxiv.org/abs/1810.12894)
- [Evolving intrinsic motivations for altruistic behavior(2018)](https://arxiv.org/abs/1811.05931?utm_source=chatgpt.com)
- [Inequity aversion improves cooperation in intertemporal social dilemmas(2018)](https://arxiv.org/abs/1803.08884)
- [Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning(2018)](https://arxiv.org/abs/1810.08647?utm_source=chatgpt.com)
- [Coordinated Exploration via Intrinsic Rewards for Multi-Agent Reinforcement Learning(2019)](https://arxiv.org/abs/1905.12127)
- [Influence-Based Multi-Agent Exploration(2019)](https://arxiv.org/abs/1910.05512)

---
### 報酬系の論文②
- [Social diversity and social preferences in mixed-motive reinforcement learning(2020)](https://arxiv.org/abs/2002.02325)
- [LJIR: Learning Joint-Action Intrinsic Reward in cooperative multi-agent reinforcement learning(2023)](https://www.sciencedirect.com/science/article/abs/pii/S0893608023004355)
- [Two Heads are Better Than One: A Simple Exploration Framework for Efficient Multi-Agent Reinforcement Learning(2023)](https://openreview.net/forum?id=AYLlZMmUbo&noteId=sIoIRG6uqi)
- [Situation-Dependent Causal Influence-Based Cooperative Multi-agent Reinforcement Learning(2023)](https://arxiv.org/abs/2312.09539)
- [MESA: Cooperative Meta-Exploration in Multi-Agent Learning through Exploiting State-Action Space Structure](https://arxiv.org/abs/2405.00902)