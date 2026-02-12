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

### [MeltingPot](https://github.com/google-deepmind/meltingpot)<sub> ([paper](https://arxiv.org/abs/2211.13746))</sub>



---
<!-- _header: MeltingPot → SocialJax -->

### [SocialJax](https://github.com/cooperativex/SocialJax)<sub> ([paper](https://arxiv.org/abs/2503.14576))</sub>


---

## 2. cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について

---

<!-- _header: cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について -->

### cleanup
報酬のためには、個人はリンゴの収穫を優先しなければならない一方で、汚染されるとリンゴが育たなくなる川を(報酬なしで)掃除する必要があるという社会ジレンマを模したゲーム．

![bg right]()

---

<!-- _header: cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について -->

### cleanupゲームに焦点を当てた理由
- 報酬が自然発生しない(最初の数十ステップを除いて)
  - common_harvest, mashroom :「どうすれば既存の報酬を枯らさずに維持し続けることができるのか」
  - cleanup : 「どうすれば継続的に報酬を生み出せるのか」
- 利得行列とエージェントのActionが(おそらく)一致しない
  - common_harvest : ビーム == 相手を排除することで自分の利益を重視
  - cleanup : ビーム == 相手に当てる → 自分重視 / 川に当てる → 

→ SSDにおける協調行動の獲得のためには、他ゲームよりも複雑な方策の獲得が必要

---
<!-- _header: cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について -->

### 検証動機

1. IPPO
   - defalt
2. MAPPO
   - cleanupゲームがあまりにも難しいため……
3. SVO
   - cleanupゲームがあまりにも難しいため……
   - DTDEにて(何かしらの文脈で説明可能な)報酬形状の変更を取り入れることで何かしら変化があるのかを確かめるため

---
<!-- _header: cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について -->

### IPPO(Independent PPO)
- 報酬はほとんど発生しない(0.000 ~ 0.005)
```
2026-02-12 22:43:11 | INFO | update=25 | env_step=819200 | reward_mean=0.0001
2026-02-12 22:43:15 | INFO | update=26 | env_step=851968 | reward_mean=0.0000
2026-02-12 22:43:18 | INFO | update=27 | env_step=884736 | reward_mean=0.0000
2026-02-12 22:43:20 | INFO | update=28 | env_step=917504 | reward_mean=0.0000
2026-02-12 22:43:22 | INFO | update=29 | env_step=950272 | reward_mean=0.0005
2026-02-12 22:43:25 | INFO | update=30 | env_step=983040 | reward_mean=0.0001
```
- ゲーム開始から川の汚染によりリンゴが育たなくなるまでの間に発生したリンゴのみが報酬となる
→ 報酬が共有されていない状態では「川を掃除するとリンゴが育つ(報酬が生まれる)」という関係を学習することが難しい．

---
<!-- _header: cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について -->

![IPPO demo]()

---
<!-- _header: cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について -->

### MAPPO(Multi-Agent PPO)
- IPPOよりは報酬が発生する(0.01 ~ 0.5)
```
2026-02-08 02:58:26 | INFO | update=6610 | env_step=27074560 | reward_mean=0.2605
2026-02-08 02:58:27 | INFO | update=6611 | env_step=27078656 | reward_mean=0.1917
2026-02-08 02:58:27 | INFO | update=6612 | env_step=27082752 | reward_mean=0.1763
2026-02-08 02:58:28 | INFO | update=6613 | env_step=27086848 | reward_mean=0.2192
2026-02-08 02:58:29 | INFO | update=6614 | env_step=27090944 | reward_mean=0.3245
2026-02-08 02:58:29 | INFO | update=6615 | env_step=27095040 | reward_mean=0.1199
```
- 川を掃除する個体とリンゴ畑で収穫を待つ個体、中間エリアで呆然とする個体、全てに同じ報酬が与えられる
→ フリーライダー問題(Free-rider)/怠慢なエージェント問題(Lazy Agent Problem)/負の影響回避(Negative Impact Avoidance)
- 社会ジレンマと言えるのだろうか？

---
<!-- _header: cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について -->

![MAPPO demo]()

---
<!-- _header: cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について -->

### SVO(Social Value Orientation)
SVOにおけるエージェントの報酬 : $r_i^{SVO} = \cos(\theta_i) r_i + \sin(\theta_i) r_{-i}$
→ $\theta$が大きいほどエージェント$i$が受け取る報酬における他者依存の割合が大きくなる
- 報酬角の設定によってはMAPPOよりも報酬が発生する(0.000 ~ 1.500)
```
(ログ取れていなかった……)
```
- 報酬角によって他者の報酬が流入するため、擬似報酬共有状態になる
- エージェントの振る舞いが報酬角によって分化する
- 社会ジレンマと言えるのだろうか？

---
<!-- _header: cleanupゲームにおけるippo, mappo, svoそれぞれの学習結果について -->

![SVO demo]()

---

## 3. cleanupゲームの難易度緩和について
### 検証動機
cleanupのdefault設定の難度が高いことがネックになっているのではないか？

1. dirtSpawnProbability(汚れの発生確率)
2. thresholdDepletion(リンゴが育たなくなる川の汚染度の閾値)
3. map_ASCII(マップ形状の変更)

---
> clean_up.yaml(一部省略)
```
env_kwargs:
  num_agents: 7
  shared_rewards: false
  maxAppleGrowthRate: 0.05
  thresholdDepletion: 0.4
  thresholdRestoration: 0.0
  dirtSpawnProbability: 0.5
  delayStartOfDirtSpawning: 0
  observe_others_rewards: false
  map_ASCII:
    - "HFFFHFFHFHFHFHFHFHFHHFHFFFHF"
    - "HFHFHFFHFHFHFHFHFHFHHFHFFFHF"
    - "HFFHFFHHFHFHFHFHFHFHHFHFFFHF"
    - "HFHFHFFHFHFHFHFHFHFHHFHFFFHF"
    - "HFFFFFFHFHFHFHFHFHFHHFHFFFHF"
    - "==============+~FHHHHHHf===="
    - "   P    P  P   ===+~SSf     "
    - "     P     P   P  <~Sf  P   "
    - "             P   P<~S>      "
    - "   P    P         <~S>   P  "
    - "               P  <~S>P     "
    - "     P           P<~S>      "
    - "           P      <~S> P    "
    - "  P   P   P     P <~S>      "
    - "^T^T^T^T^T^T^T^T^T;~S,^T^T^T"
    - "BBBBBBBBBBBBBBBBBBBssBBBBBBB"
    - "BBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    - "BBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    - "BBBBBBBBBBBBBBBBBBBBBBBBBBBB"
```

---


## 4.


---

## 5. 知的探求の世界まとめ & 反省

