---
marp: true
theme: freud
paginate: true
math: mathjax
---

# 知的探求の世界 2025 最終発表
klis3年 鈴木史麿

---

## 内容
1. MeltingPot → SocialJax
2. cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について
3. cleanupゲームの難易度緩和について
4. ( )
5. 知的探求の世界まとめ & 反省

---

## 1. MeltingPot → SocialJax

---
<!-- _header: MeltingPot → SocialJax -->

### [MeltingPot](https://github.com/google-deepmind/meltingpot)



---
<!-- _header: MeltingPot → SocialJax -->

### [SocialJax](https://github.com/cooperativex/SocialJax)


---

## 2. cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について

---
<!-- _header: cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について -->

### cleanup
報酬のためには、個人はリンゴの収穫を優先しなければならない一方で、汚染されるとリンゴが育たなくなる川を(報酬なしで)掃除する必要があるという社会ジレンマを模したゲーム．

---
<!-- _header: cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について -->

### IPPO(Independent PPO)
- 報酬はほとんど発生しない
```
2026-02-12 22:43:11 | INFO | update=25 | env_step=819200 | reward_mean=0.0001
2026-02-12 22:43:15 | INFO | update=26 | env_step=851968 | reward_mean=0.0000
2026-02-12 22:43:18 | INFO | update=27 | env_step=884736 | reward_mean=0.0000
2026-02-12 22:43:20 | INFO | update=28 | env_step=917504 | reward_mean=0.0000
2026-02-12 22:43:22 | INFO | update=29 | env_step=950272 | reward_mean=0.0005
2026-02-12 22:43:25 | INFO | update=30 | env_step=983040 | reward_mean=0.0001
```
- ゲーム開始から川の汚染によりリンゴが育たなくなるまでの間に発生したリンゴのみが報酬となる
→ 報酬が共有されていない状態では「川を掃除するとリンゴが育つ(報酬が生まれる)」という因果

---
<!-- _header: cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について -->

### MAPPO(Multi-Agent PPO)
-


---
<!-- _header: cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について -->

### SVO(Social Value Orientation)


---

## 3. cleanupゲームの難易度緩和について


---


## 4.


---

## 5. 知的探求の世界まとめ & 反省

