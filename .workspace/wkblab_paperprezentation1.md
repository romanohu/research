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
- MULTI-AGENT DEEP REINFORCEMENT LEARNING UNDER CONSTRAINED COMMUNICATIONS

---

### [MULTI-AGENT DEEP REINFORCEMENT LEARNING UNDER CONSTRAINED COMMUNICATIONS(2026)](https://www.arxiv.org/pdf/2601.17069)
Shahil Shaik, Jonathon M. Smereka, Yue Wang

---

### Introduction

- 近年のMARLの手法
→ 如何に非定常性を和らげるか
  - CTDE手法を使うことが多い

しかしCTDEには学習時にグローバル情報が必要であるために、実運用上では現実的な制約により学習を上手くできない可能性がある
- スケーラビリティの低さ
- 一般化性能の低さ
- ロバストでない

→ 問題提起：「グローバル情報に依存しない学習枠組みが必要である」

---

#### 「局所観測 + 近傍のpeer-to-peer通信だけ」で協調を学ぶ分散型MARL手法が必要

---

#### 提案① D-GATs(Distributed Graph Attention Networks)
GATv2(Brody et al., 2023) + D-SGD(Lian et al., 2017; Assran et al., 2019)
- 局所的なメッセージパッシングのみを用いてグローバル状態表現を構築

---

#### 提案② DG-MAPPO(Distributed Graph-attention MAPPO)
中央集権的な学習やグローバルな観測可能性を必要としない原理的な分散型MARLフレームワーク
- エージェントの局所観測情報
- D-GATによるグローバル状態推論
- 共有/平均化されたチーム報酬

(Decentralizedではない)

---

#### D-GATsが推定していること
各エージェントiはD-GATsを通して$\hat o_t^i$を得る．
$\hat o_t^i$が含意するのは以下の情報
- 各エージェントiの局所観測
- 近傍から伝播してきた情報
- multi-hopによる拡散された情報

→ グローバル情報から得られる情報を近似

---

#### DG-MAPPOの情報の流れ
- 局所観測 $o_t^i$ を取得

- D-GAT通信により $\hat{o}_t^i$ を推定

- 結合入力を作成  
  $\tilde{o}_t^i = [\, o_t^i,\ \hat{o}_t^i \,]$

- ローカル方策 $\pi_{\theta_i}^i(\cdot \mid \tilde{o}_t^i)$ により行動を選択

- 共有（平均）報酬 $R(o_t, a_t)$ を受け取る

- ローカル critic $V_{\phi_i}^i(\tilde{o}_t^i)$ により価値関数および advantage を推定

- PPO により各エージェントが独立に方策・価値関数を更新

---

### 実験&結果
1. SMAC(StarCraft II Multi-Agent Challenge)
2. Google Research Football
3. Multi-Agent MuJoCo

これらの環境に対してMAPPOやHAPPOなどのCTDE手法と比較して実験を行い、同等もしくは上回る性能を示した．

---

読んでみた所感としては
- 報酬が共有(同じ最適化目的を持っている)しているので完全なDTDEと言えるのだろうかと思った．
  - 共有報酬はグローバル情報ではないのか?
- 通信対象は環境依存であるため学習対象ではなさそう
  - 必要な情報を誰が持っていそうかを学習するのではなく、あくまでも与えられた情報の処理
