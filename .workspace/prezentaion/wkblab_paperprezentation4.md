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
- Birds of a Feather Flock Together: A Close Look at
Cooperation Emergence via Multi-Agent RL

---

## [Birds of a Feather Flock Together: A Close Look at Cooperation Emergence via Multi-Agent RL](https://arxiv.org/abs/2104.11455?utm_source=chatgpt.com)
Heng Dong, Tonghan Wang, Jiayuan Liu, Chi Han, Chongjie Zhang


---

### Introduction①

協力行動の創発は進化生物学・経済学・AIなど多くの分野で研究されている重要な問題

特に 社会的ジレンマ(Social Dilemma) では

- 個人の合理的行動
- 集団全体の利益

が衝突する

例：

- Public Goods
- Tragedy of the Commons

---

### Introduction②

従来研究により以下のような利他的インセンティブを与えることで協力が生まれることが知られている(環境行動ではない)

- reward
- punishment

---

### 既存研究の問題

最近のMARL研究ではエージェントが

- 環境行動
- 他エージェントへのインセンティブ

を同時に学習することで協力を促すが、それでは協力レベルが安定しないという問題がある

---

### 観察された現象

学習中の協力率

協力 → 裏切り → 協力 → 裏切り


のように行動方針が周期的に振動してしまい安定した協力に収束しない

---

### 原因：Second-order Social Dilemma

協力を維持するためには

- 罰
- 報酬

などの利他的インセンティブが必要であるが、しかし、そのインセンティブ自体にもコストがある

---

### Second-order Free Rider

例：
Agent A : punish
Agent B : punish
Agent C : punishしない

しかしCは他エージェントのインセンティブ行動によって生まれた恩恵だけ受ける
→ フリーライダー化

---

### 結果
punisher 減少
↓
インセンティブ崩壊
↓
協力崩壊


---

### 論文のアイデア

人間社会では

**Homophily(同類性)**

と呼ばれる性質が知られている

> 似た者同士は集まる
> *Birds of a Feather Flock Together*

この論文ではその性質を マルチエージェント強化学習に応用する

---

### Homophily

環境で似た行動をとるエージェントは似たインセンティブ行動をとるように学習させる

これにより

- 協力するエージェント同士が互いに支援する
- フリーライダーが利益を得にくくなる

という構造を作る

---

### 提案手法 : Homophily-based Incentive Learning

各エージェントは次の2つの方策を学習する

① 環境行動policy
(環境内でどの行動をとるか)

② インセンティブpolicy
(他エージェントに reward / punish / none を与えるか)

この2つを同時に学習することで協力関係の形成を目指す

---

### 学習構造

エージェントの学習の流れ

観測
↓
環境行動 Q-function(環境内での行動を決定)
↓
環境行動
↓
インセンティブ Q-function(他エージェントへのインセンティブを決定)
↓
他エージェントへreward / punish を与える

---

### Homophily Loss

同類性を実現するためにHomophily Lossを導入する

$$
L_{homo,i}(\phi_i)
=
\mathbb{E}_D
\left[
-
\sum_{j \ne i}
S_{env}(i,j)\,S_{inc}(i,j;\phi_i)
\right]
$$

環境行動が似ているエージェント同士のインセンティブ行動も似るように学習する

最終的な目的関数

$$
L_i =
L_{env}
+
\lambda_{inc}L_{inc}
+
\lambda_{homo}L_{homo}
$$

---

### 直感

Homophily が無い場合

協力エージェントがフリーライダーに利用されてしまう

A 協力 → reward
B 協力 → reward
C 非協力 → rewardしない

しかしCはrewardの恩恵だけ受ける
↓
Second-order free rider

---

### Homophilyあり

Homophilyにより似た行動のエージェント同士が結びつく
協力グループ
AとBはreward を与え合う

非協力
C

↓

協力者同士が互いに支援する構造が生まれる

---

### 実験環境

Sequential Social Dilemmas を用いて評価

代表的な2種類の社会的ジレンマ

- Cleanup(Public Goods)
- Harvest(Tragedy of the Commons)

---

### Cleanup

Public Goods 型のジレンマ

環境には

- ゴミ
- りんご

が存在する

ゴミを掃除するとりんごが生えるようになる

しかし掃除自体には個人の直接報酬がないため誰かが掃除する必要がある

---

### Harvest
Tragedy of the Commons 型のジレンマ

エージェントはりんごを収穫して報酬を得る

しかし取りすぎるとりんごが再生しなくなる
↓
短期利益
→ すぐ収穫

長期利益
→ 資源を残す

---

### 結果

Homophilyなし

- 協力率が振動
- 安定した協力が形成されない

Homophilyあり

- 協力が安定して維持される
- チーム報酬も高くなる
- 協力エージェントに対して他のエージェントがrewardを放出(cleanup)

---

### まとめ

この論文の主な貢献

1. 協力が崩壊する原因として
   Second-order Social Dilemmaを分析

2. Homophily を利用した新しいインセンティブ学習手法を提案

3. MARL環境において安定した協力の形成を実証

---

### 所感

- second-order dilemma の分析が興味深い
- 社会学の概念(homophily)をMARLに導入している点が特徴的
- 社会的ジレンマ研究への応用が期待できる
- ただ環境とは別軸で報酬rewardをエージェントに与える都合上、エージェント毎に役割が固定化されることが多そう


---
