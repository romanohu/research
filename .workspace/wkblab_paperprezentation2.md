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

この学習における到達点の指標として1つ挙げられるのが「ナッシュ均衡(NE)」である
- いかなるプレイヤーも単独で戦略を変更することで利益を得られないという状態
- 一般にあるゲームにおいて複数存在する
- 異なるNEは異なる利得をもたらす可能性がある
→ しかし、様々なゲームで成功を収めている分散型ポリシー勾配アルゴリズム(PG)では複数NEが存在する場合でも、常に特定のNEに収束してしまうという問題がある

---

### Introduction②