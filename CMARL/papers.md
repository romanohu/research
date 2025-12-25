# MARL　論文
## 参考資料一覧
- 読んだ方が良い論文
    - [Planning Problems for Sophisticated Agents with Present Bias(2016)](https://arxiv.org/abs/1603.08177)
    - [Multi-agent Reinforcement Learning in Sequential Social Dilemmas(2017)](https://arxiv.org/abs/1702.03037)
    - [Multiagent cooperation and competition with deep reinforcement learning(2017)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0172395)
    - [Maintaining cooperation in complex social dilemmas using deep reinforcement learning(2018)](https://arxiv.org/abs/1707.01068)
    - [Inequity aversion improves cooperation in intertemporal social dilemmas(2018)](https://arxiv.org/abs/1803.08884)
    - [Exploration by Random Network Distillation(2018)](#exploration-by-random-network-distillation)
    - [Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning(2018)](#social-influence-as-intrinsic-motivation-for-multi-agent-deep-reinforcement-learning)
    - [Learning through Probing: a decentralized reinforcement learning architecture for social dilemmas(2018)](#learning-through-probing-a-decentralized-reinforcement-learning-architecture-for-social-dilemmas)
    - [Evolving intrinsic motivations for altruistic behavior(2018)](#evolving-intrinsic-motivations-for-altruistic-behavior)
    - [Agent Modeling as Auxiliary Task for Deep Reinforcement Learning(2019)](https://arxiv.org/abs/1907.09597)
    - [Emergent Multi-Agent Communication in the Deep Learning
Era(2020)](https://arxiv.org/abs/2006.02419)
    - [Promoting Coordination through Policy Regularization in Multi-Agent Deep Reinforcement Learning(2020)](https://arxiv.org/abs/1908.02269)
    - [Sample Factory: Egocentric 3D Control from Pixels at 100000 FPS with Asynchronous Reinforcement Learning(2020)](https://arxiv.org/abs/2006.11751)
    - [The Surprising Effectiveness of PPO in Cooperative, Multi-Agent Games(2021)](https://arxiv.org/abs/2103.01955?utm_source=chatgpt.com)
    - [Multi-agent deep reinforcement learning: a survey(2021)](https://link.springer.com/article/10.1007/s10462-021-09996-w?utm_source=chatgpt.com)
    - [Trust Region Policy Optimisation in Multi-Agent Reinforcement Learning(2022)](https://arxiv.org/abs/2109.11251?utm_source=chatgpt.com)
    - [A Review of Cooperative Multi-Agent Deep Reinforcement Learning(2019)](#a-review-of-cooperative-multi-agent-deep-reinforcement-learning)
    - [RPM: Generalizable Behaviors for Multi-Agent Reinforcement Learning(2022)](https://arxiv.org/abs/2210.09646)
    - [Multi-Agent Reinforcement Learning is a Sequence Modeling Problem(2023)](https://arxiv.org/abs/2205.14953?utm_source=chatgpt.com)
    - [A Comprehensive Survey on Multi-Agent Cooperative Decision-Making: Scenarios, Approaches, Challenges and Perspectives(2025)](https://arxiv.org/abs/2503.13415)
    - [OVERCOOKEDV2: RETHINKING OVERCOOKED FOR ZERO-SHOT COORDINATION(2025)](#overcookedv2-rethinking-overcooked-for-zero-shot-coordination)
    - [SocialJax: An Evaluation Suite for Multi-agent Reinforcement Learning in Sequential Social Dilemmas](#socialjax-an-evaluation-suite-for-multi-agent-reinforcement-learning-in-sequential-social-dilemmas)

## 論文メモ
### 2017
#### Multi-agent Reinforcement Learning in Sequential Social Dilemmas
従来のMGSDは1回の行動において"協力"か"裏切り"かの選択を迫る設定をしていたが、本論文ではその選択というのは短期的な行動選択ではなく、長期的な行動選択の方針(policy)として現れると主張している．それを県境するための枠組みとしてSequentialSocialDilemma(SSD)を提言する．これはMGSDの特徴を維持しつつも、時間的に拡張されたMarkovゲームとして定式化した社会ジレンマモデルである．SSDの特徴として協力の「度合い」も表現できる点がある．
また、MGSDの利得行列上では同質に見えたとしても、SSDとして見ると本質的に異なるゲームがあることが判明した．
記述的(Descriptive)な立場で、どのような行動パターンが現れるのかを観察．
それぞれのゲームの差異の他に、学習の際のハイパーパラメータにも着目している．
#### Multiagent cooperation and competition with deep reinforcement learning
Pongゲーム環境において、報酬設定pを操作することで、協力的/競争的な行動が創発する．また、固定方策AIを相手に学習するsingle-playerDQNよりも、固定方策AIを用いないmultiplayerDQNのほうが、より一般的でロバストな戦略が育つ．
### 2018
#### Maintaining cooperation in complex social dilemmas using deep reinforcement learning
深層強化学習を用いてTFT(しっぺ返し戦略)みたいに協力できるエージェントを作るにはどうしたら良いかという問題に挑戦し、拡張版のamTFTを提起している．マルチエージェントではなく単一エージェントの設計を狙っている．
#### Inequity aversion improves cooperation in intertemporal social dilemmas
不公平嫌悪(inquity aversion)を報酬構造に組み込むことで、自己利益だけでなく社会的な協調を誘導できると主張．

#### [Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning](https://arxiv.org/abs/1810.08647?utm_source=chatgpt.com)


#### [Learning through Probing: a decentralized reinforcement learning architecture for social dilemmas](https://arxiv.org/abs/1809.10007?utm_source=chatgpt.com)


#### [Evolving intrinsic motivations for altruistic behavior](https://arxiv.org/abs/1811.05931?utm_source=chatgpt.com)


#### [Exploration by Random Network Distillation](https://arxiv.org/abs/1810.12894)
深層強化学習における探索問題において有効な内的報酬の設計手法であるRandomNetworkDistillation(RND)を提案している．構造はかなりシンプルでエージェントが受け取る報酬に環境からのものに加えて独自の機構から出力される内的報酬を含めている．その機構には次状態の観測$o_(t+1)$を受け取る2つのニューラルネットで構成されている．片方のニューラルネットはパラメータを固定してあり、もう片方のニューラルネットが、その出力を予測するようにパラメータを学習する．そして内的報酬は、その予測誤差である．これにより、未知の状態に対しては学習が進んでいないため、予測が上手くいかず、結果として報酬が大きくなり、既知の状態に対しては、報酬が小さくなる．さらにRNDは、予測対象を環境依存の遷移ではなく固定されたランダム関数にすることで、確率的遷移に起因する noisy-TV 問題を回避しており、内的報酬は状態訪問密度の proxy として振る舞う．また内的報酬は非定常であるため、論文では外的報酬と価値関数を分離して学習している．

### 2020
#### Promoting Coordination through Policy Regularization in Multi-Agent Deep Reinforcement Learning

### 2021
#### Multi-agent deep reinforcement learning: a survey
MARL及びMADRLに関する包括的なサーベイ．メルポは、ゲーム設定が混合設定(一般和ゲーム)で、エージェントは独立学習者で、環境はPOMGな実験ということか．p11の分散訓練分散実行(DTDE)の詳細がかなり分かりやすい．Leibo(2017)も出てきているので、他の登場した文献も読んでおきたい．

### 2022
#### [A Review of Cooperative Multi-Agent Deep Reinforcement Learning](https://arxiv.org/abs/1908.03963)
MARLが扱う課題の多くはNP困難問題に分類される．このサーベイでは協調的な目標を持つ分散型問題に焦点を当てている．IL(Independent Learners)の限界を緩和するために提案された手法として、1パラメータ共有、2学習率・更新頻度の工夫、3役割分担(エージェント行動の固定/探索空間を削減)などがある．


### 2025
#### A Comprehensive Survey on Multi-Agent Cooperative Decision-Making: Scenarios, Approaches, Challenges and Perspectives


#### [OVERCOOKEDV2: RETHINKING OVERCOOKED FOR ZERO-SHOT COORDINATION](https://arxiv.org/html/2503.17821v1)
- MARLにおいてZSC(Zero-Shot Coordination)を上手く達成するにはどうすればいいのかは重大な課題
    - SP-XP gap：selfplayとcrossplayでの性能の差．
        - ZSCにおける「協調の失敗」を示す指標
    - ZSC失敗の原因は訓練時のstateの多様性が不十分であったために、未知の状態に対応できていない可能性が高い
    - 状態拡張アルゴリズム(state-augmentation algorithm)を適応することである程度は縮小
- ベンチマーク：OverCookedV2を提唱
    - エージェントの観測範囲を制限、情報の非対称性、確率性、(意味のある？)通信チャネルの導入
    - 既存のZSC手法でもZSC性能を向上させることが確認できたが、テスト時に適応を要求されるシナリオでは苦戦している?ことが確認できた

#### [SocialJax: An Evaluation Suite for Multi-agent Reinforcement Learning in Sequential Social Dilemmas](https://arxiv.org/abs/2503.14576v2)