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

#### Introduction

- 近年のMARLの手法
→ 如何に非定常性を和らげるか
  - CTDE手法を使うことが多い

しかしCTDEには学習時にグローバル情報が必要であるために、実運用上では現実的な制約により学習を上手くできない可能性がある

→ 問題提起：「グローバル情報に依存しない学習枠組みが必要である」

---

#### 「局所観測 + 近傍のpeer-to-peer通信だけ」で協調を学ぶ分散型MARL手法が必要

---

