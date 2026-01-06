# CMARL　論文
## 参考資料一覧
- 読んだ方が良い論文
    - [Planning Problems for Sophisticated Agents with Present Bias(2016)](https://arxiv.org/abs/1603.08177)
    - **[Multi-agent Reinforcement Learning in Sequential Social Dilemmas(2017)](#multi-agent-reinforcement-learning-in-sequential-social-dilemmas)**
    - [Multiagent cooperation and competition with deep reinforcement learning(2017)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0172395)
    - [Maintaining cooperation in complex social dilemmas using deep reinforcement learning(2018)](https://arxiv.org/abs/1707.01068)
    - [Inequity aversion improves cooperation in intertemporal social dilemmas(2018)](#inequity-aversion-improves-cooperation-in-intertemporal-social-dilemmas)
    - **[Exploration by Random Network Distillation(2018)](#exploration-by-random-network-distillation)**
    - **[Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning(2018)](#social-influence-as-intrinsic-motivation-for-multi-agent-deep-reinforcement-learning)**
    - [Learning through Probing: a decentralized reinforcement learning architecture for social dilemmas(2018)](#learning-through-probing-a-decentralized-reinforcement-learning-architecture-for-social-dilemmas)
    - [Evolving intrinsic motivations for altruistic behavior(2018)](#evolving-intrinsic-motivations-for-altruistic-behavior)
    - [Agent Modeling as Auxiliary Task for Deep Reinforcement Learning(2019)](https://arxiv.org/abs/1907.09597)
    - [Learning Reciprocity in Complex Sequential Social Dilemmas(2019)](#learning-reciprocity-in-complex-sequential-social-dilemmas)
    - [Emergent Multi-Agent Communication in the Deep Learning Era(2020)](https://arxiv.org/abs/2006.02419)
    - [Promoting Coordination through Policy Regularization in Multi-Agent Deep Reinforcement Learning(2020)](https://arxiv.org/abs/1908.02269)
    - [Sample Factory: Egocentric 3D Control from Pixels at 100000 FPS with Asynchronous Reinforcement Learning(2020)](https://arxiv.org/abs/2006.11751)
    - [The Surprising Effectiveness of PPO in Cooperative, Multi-Agent Games(2021)](https://arxiv.org/abs/2103.01955?utm_source=chatgpt.com)
    - [Birds of a Feather Flock Together: A Close Look at Cooperation Emergence via Multi-Agent RL](#birds-of-a-feather-flock-together-a-close-look-at-cooperation-emergence-via-multi-agent-rl)
    - [Multi-agent deep reinforcement learning: a survey(2021)](https://link.springer.com/article/10.1007/s10462-021-09996-w?utm_source=chatgpt.com)
    - [Trust Region Policy Optimisation in Multi-Agent Reinforcement Learning(2022)](https://arxiv.org/abs/2109.11251?utm_source=chatgpt.com)
    - [A Review of Cooperative Multi-Agent Deep Reinforcement Learning(2019)](#a-review-of-cooperative-multi-agent-deep-reinforcement-learning)
    - [RPM: Generalizable Behaviors for Multi-Agent Reinforcement Learning(2022)](https://arxiv.org/abs/2210.09646)
    - [Multi-Agent Reinforcement Learning is a Sequence Modeling Problem(2023)](https://arxiv.org/abs/2205.14953?utm_source=chatgpt.com)
    - [A Review of Cooperation in Multi-agent Learning(2023)](#a-review-of-cooperation-in-multi-agent-learning)
    - [A Comprehensive Survey on Multi-Agent Cooperative Decision-Making: Scenarios, Approaches, Challenges and Perspectives(2025)](https://arxiv.org/abs/2503.13415)
    - [OVERCOOKEDV2: RETHINKING OVERCOOKED FOR ZERO-SHOT COORDINATION(2025)](#overcookedv2-rethinking-overcooked-for-zero-shot-coordination)
    - **[SocialJax: An Evaluation Suite for Multi-agent Reinforcement Learning in Sequential Social Dilemmas(2025)](#socialjax-an-evaluation-suite-for-multi-agent-reinforcement-learning-in-sequential-social-dilemmas)**

## 論文メモ
### 2017
#### [Multi-agent Reinforcement Learning in Sequential Social Dilemmas](https://arxiv.org/abs/1702.03037)
[Joel Z. Leibo](../Authors/overseas/JoelZ.Leibo.md)
従来のMGSDは1回の行動において"協力"か"裏切り"かの選択を迫る設定をしていたが、本論文ではその選択というのは短期的な行動選択ではなく、長期的な行動選択の方針(policy)として現れると主張している．それを県境するための枠組みとしてSequentialSocialDilemma(SSD)を提言する．これはMGSDの特徴を維持しつつも、時間的に拡張されたMarkovゲームとして定式化した社会ジレンマモデルである．SSDの特徴として協力の「度合い」も表現できる点がある．
また、MGSDの利得行列上では同質に見えたとしても、SSDとして見ると本質的に異なるゲームがあることが判明した．
記述的(Descriptive)な立場で、どのような行動パターンが現れるのかを観察．
それぞれのゲームの差異の他に、学習の際のハイパーパラメータにも着目している．


#### Multiagent cooperation and competition with deep reinforcement learning
Pongゲーム環境において、報酬設定pを操作することで、協力的/競争的な行動が創発する．また、固定方策AIを相手に学習するsingle-playerDQNよりも、固定方策AIを用いないmultiplayerDQNのほうが、より一般的でロバストな戦略が育つ．
### 2018
#### Maintaining cooperation in complex social dilemmas using deep reinforcement learning
深層強化学習を用いてTFT(しっぺ返し戦略)みたいに協力できるエージェントを作るにはどうしたら良いかという問題に挑戦し、拡張版のamTFTを提起している．マルチエージェントではなく単一エージェントの設計を狙っている．
#### [Inequity aversion improves cooperation in intertemporal social dilemmas](https://arxiv.org/abs/1803.08884)
[Joel Z. Leibo](../Authors/overseas/JoelZ.Leibo.md)
SSD環境において、不公平嫌悪(inquity aversion)を報酬構造に組み込むことで、自己利益だけでなく社会的な協調を誘導できると主張．

#### [Learning through Probing: a decentralized reinforcement learning architecture for social dilemmas](https://arxiv.org/abs/1809.10007?utm_source=chatgpt.com)
> [Leibo(2017)](#multi-agent-reinforcement-learning-in-sequential-social-dilemmas)のSSDに沿っているものではない

本論文は、社会的ジレンマ環境におけるマルチエージェント強化学習に対して、「相手の行動が将来どのように変化するか」を学習過程に明示的に取り込む、新しい分散型学習アーキテクチャ Learning through Probing(LTP)を提案した研究である．従来の多くの MARL 手法では、各エージェントは自分が得た即時的・割引累積的な報酬に基づいて方策を更新するが、LTP ではそれに加えて「ある行動を取った結果、相手の学習・行動方針がどう変わったか」という相互作用の二次的効果を評価対象に含める点が特徴である．特に本研究は、社会的相互作用を「解くべきゲーム」ではなく、「学習主体同士が適応し続ける社会的プロセス」として捉え直す立場を明確にしている．

先行研究と比べた際の顕著な新規性は、相手の内部モデルを推定したり、勾配を明示的に考慮したりすることなく、純粋に分散的かつモデルフリーな枠組みの中で、相手の将来行動変化を学習に反映させている点にある．例えば LOLA(Learning with Opponent-Learning Awareness)のような手法では、相手の学習更新を勾配レベルで見積もる必要があり、計算的・実装的に重い．一方 LTP は、あくまで経験軌跡に基づく Q-learning を基礎としながら、報酬の再解釈という比較的単純な仕組みによって、相手への影響を考慮できる点で実用性が高い．また、単に協調を誘導する設計報酬を与えるのではなく、相互学習の結果として協調が出現する点を重視している点も、規範的・設計主導のアプローチとは一線を画している．

技術的・手法的な「キモ」は、プロービングフェーズと学習フェーズを分離し、経験の「評価方法」を後から変更するという点にある．エージェントはまずプロービングフェーズで相互作用を行い、その中で得られた経験列を保存する．その後の学習フェーズでは、単なる即時報酬ではなく、「その行動が相手の将来行動をどの程度好ましい方向に変えたか」を反映した調整報酬を用いて Q 値を更新する．このとき導入されるパラメータ η は、将来の相手行動変化をどれだけ重視するかを制御する役割を果たし、短期的自己利益と長期的協調誘導とのトレードオフを一つのスカラーで表現している点が重要である．この「報酬の事後的再重み付け」によって、エージェントは自分の行動を、相手の適応を含んだ長期的文脈の中で評価できるようになる．

本手法の有効性は、主に Iterated Prisoner’s Dilemma(IPD)を用いた実験によって検証されている．LTP エージェント同士を対戦させた場合、通常の独立 Q-learning では裏切りに収束しやすい設定においても、協調が安定的に成立し、平均累積報酬が有意に高くなることが示されている．また、学習済み LTP エージェントを Axelrod トーナメント型の静的戦略エージェント(Tit-for-Tat など)と対戦させた場合にも、極端に搾取されることなく良好な性能を維持できる点が示されており、「協調的だがナイーブではない」振る舞いを獲得できていることが確認されている．さらに、ランダムに相手が入れ替わる擬似的な社会環境においても、協調的傾向が集団レベルで維持されることが報告されている．

一方で、議論の余地や限界も明確に存在する．第一に、本手法は相手が学習する存在であることを暗黙に前提としており、完全に非適応的、あるいは非常に高速に変化する相手に対してどの程度有効かは十分に検証されていない．第二に、η の設定は結果に大きく影響するが、その理論的な決定指針は与えられておらず、現状では経験的調整に依存している．さらに、評価環境は基本的に IPD に限定されており、より高次元・部分観測・多人数の社会的ジレンマ環境にどこまでスケールするかは未解決である．ただし、これらの点は同時に、本研究が「協調の出現を説明・分析するための概念的枠組み」を提示した論文であることを示しており、社会的相互作用を扱う MARL 研究への重要な問題提起として位置づけられる．

#### [Evolving intrinsic motivations for altruistic behavior](https://arxiv.org/abs/1811.05931?utm_source=chatgpt.com)
内初的報酬に関する研究の1つ．
本論文は，利他的・協力的行動がどのようにして自己利益を追求するエージェント集団から自然に生じうるのかという，進化理論とマルチエージェント強化学習(MARL)の両分野に共通する根源的な問いに取り組んだ研究である．特に，短期的な個人利益と長期的な集団利益が鋭く対立する intertemporal social dilemma(ISD) を対象に，協力行動が「外から設計された報酬」ではなく，エージェント自身の内発的動機として学習・進化されうることを示す点に特徴がある．

従来のMARLにおける協力研究では，協力を促すために報酬設計を工夫したり(共有報酬・ shaping・centralized critic など)，あるいは不平等嫌悪や他者報酬を人為的に固定した形で組み込むアプローチが主流であった．一方，本論文の新規性は，「どのような内発的報酬を持つべきか」自体を進化の対象にした点にある．すなわち，利他的な価値観や協力志向を「前提」とせず，自然選択に類似したプロセスを通じて，協力的な帰納バイアスそのものが獲得されることを示した点が，先行研究と比べて本質的に新しい．

この目的を実現するために導入された技術的中核は，強化学習と進化的選択を分離・接続する多階層(multi-level selection)学習アーキテクチャである．各エージェントは通常のモデルフリー強化学習によって行動方策を学習するが，その際に用いる報酬は，環境から与えられる外的報酬だけでなく，「内発的動機モジュール」が生成する内的報酬を含む．この内発的報酬のパラメータは，個々のエピソード内では更新されず，集団全体の成果に基づいて世代単位で進化的に選択・更新される．つまり，短時間スケールでは「自己利益を最大化する合理的エージェント」として振る舞いながら，長時間スケールでは「どのような価値観を持つ個体が集団として成功するか」が選択される構造になっている．この分離こそが，本研究の“キモ”であり，文化進化や群選択の計算論的アナロジーと解釈できる．

有効性の検証は，2つの代表的な intertemporal social dilemma 環境 を用いたシミュレーション実験によって行われている．これらの環境では，短期的には資源を独占・過剰利用する行動が個体に有利である一方，集団としては資源枯渇や低スコアにつながる構造が組み込まれている．実験の結果，内発的動機を進化可能な形で導入したエージェント集団は，標準的な強化学習エージェントや固定的な社会的報酬を持つエージェントと比べて，より高い集団パフォーマンスと安定した協力行動を示した．重要なのは，協力が直接報酬化されていないにもかかわらず，進化の結果として「他者や将来への配慮」を反映した行動が現れた点である．

もっとも，本論文にはいくつかの議論すべき点も存在する．第一に，進化的選択は環境設計や集団評価指標に依存するため，どの程度まで一般的な協力原理を獲得しているのかは慎重に解釈する必要がある．第二に，計算コストやスケールの問題から，現実的な大規模MARLへの直接適用には課題が残る．また，進化された内発的動機の「解釈可能性」は限定的であり，それが人間的な倫理や社会規範とどこまで対応しているかは未解決である．ただし，これらの制約を踏まえても，本研究は協力・利他性を“設計する”のではなく，“進化させる”という発想を，深層強化学習の枠組みで具体化した点で，理論的にも方法論的にも大きな意義を持つ．



#### [Exploration by Random Network Distillation](https://arxiv.org/abs/1810.12894)
深層強化学習における探索問題において有効な内的報酬の設計手法であるRandomNetworkDistillation(RND)を提案している．構造はかなりシンプルでエージェントが受け取る報酬に環境からのものに加えて独自の機構から出力される内的報酬を含めている．その機構には次状態の観測$o_(t+1)$を受け取る2つのニューラルネットで構成されている．片方のニューラルネットはパラメータを固定してあり、もう片方のニューラルネットが、その出力を予測するようにパラメータを学習する．そして内的報酬は、その予測誤差である．これにより、未知の状態に対しては学習が進んでいないため、予測が上手くいかず、結果として報酬が大きくなり、既知の状態に対しては、報酬が小さくなる．さらにRNDは、予測対象を環境依存の遷移ではなく固定されたランダム関数にすることで、確率的遷移に起因する noisy-TV 問題を回避しており、内的報酬は状態訪問密度の proxy として振る舞う．また内的報酬は非定常であるため、論文では外的報酬と価値関数を分離して学習している．
#### [Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning](https://arxiv.org/abs/1810.08647?utm_source=chatgpt.com)
[Joel Z. Leibo](../Authors/overseas/JoelZ.Leibo.md)
[Leibo(2017)](#multi-agent-reinforcement-learning-in-sequential-social-dilemmas)のSSDに対応した上で、報酬項に変更を加えた．各エージェントiの報酬を以下のように定義．
$$r_i(t)=r^{ext}_i(t)+Br^{inf}_i(t)$$
$$r^{inf}_t(t)=\sum_{j≠i} D(\pi_j(・|o_t,a^i_t)||\pi_j(・|o_t,a^{i,cf}_t))$$
第２項の部分はinfluence reward(内初的報酬)であり、この論文の文脈では、「自分の行動が他者の将来行動分布をどれだけ変えたか」を測る指標である．この部部では自分の観測と行動が入力信号として入り、しゅつりょくに相手の次行動の分布を出す行動予測モデルを学習している．そこで教師信号として相手の行動を(環境情報ではなく学習中のログを)使っている．この内初的報酬は「自分の行動が相手の行動分布を変えたと推定されたとき」である．これは暴力的・支配的な行動(例えばビームを打つなど)を助長しないかという疑問があるが、短期的なrewardが上がるが長期的には相手の行動分布の差分が小さくなりinfluence rewardがむしろ下がるために、そういった行動は安定にはならないとしている．

### 2019
#### [Learning Reciprocity in Complex Sequential Social Dilemmas](https://arxiv.org/abs/1903.08082)
> [Joel Z. Leibo](../Authors/overseas/JoelZ.Leibo.md)

[この論文](#inequity-aversion-improves-cooperation-in-intertemporal-social-dilemmas)と似ているが、あちらがエージェントの行動に対する因果的影響度を報酬として用いて学習するのに対し、これは互恵性(相手の行動パターンに応じて戦略を調整すること、自分の行動が相手の"報酬"にどれだけ影響を与えたか)を学習することを意図した論文．この論文の手法ではエージェントは環境報酬に加えて、互恵性に基づく内在報酬を得る．
(読み途中)


### 2020
#### Promoting Coordination through Policy Regularization in Multi-Agent Deep Reinforcement Learning

### 2021
#### Multi-agent deep reinforcement learning: a survey
MARL及びMADRLに関する包括的なサーベイ．メルポは、ゲーム設定が混合設定(一般和ゲーム)で、エージェントは独立学習者で、環境はPOMGな実験ということか．p11の分散訓練分散実行(DTDE)の詳細がかなり分かりやすい．Leibo(2017)も出てきているので、他の登場した文献も読んでおきたい．

#### [Birds of a Feather Flock Together: A Close Look at Cooperation Emergence via Multi-Agent RL](https://arxiv.org/abs/2104.11455?utm_source=chatgpt.com)
協調分散MARLに関してのこれの先行研究では、エージェントの行動に影響するインセンティブ(他のエージェントに報酬/罰を与える)を学習させることで協調を促進してきたが、それでは安定せず、協力と裏切りの間で周期的に変動する脆弱(ロバストでない)挙動が観察されたとしている．それを解決するための方法として同類志向(homophily)を導入した学習枠組みを提案している．
本研究は、この不安定性がインセンティブ行動自体が利己的になり得る「第二次社会的ジレンマ」に起因することを理論的に分析した点が大きな貢献である．さらに、人間社会で広く観察される同類志向(homophily)に着目し、エージェント同士が似たインセンティブを与えるよう学習を誘導する homophilic incentives を提案した．これにより学習ダイナミクスが安定化し、協調行動が持続的に維持される．提案手法は、Public Goods や Tragedy of the Commons といった代表的な逐次的社会的ジレンマ環境で検証され、従来手法と比べて高く安定した協調水準を達成することが示された．一方で、同質性を促す設計が異質性を必要とするタスクに与える影響や、大規模・複雑な環境への一般化可能性については今後の課題として議論の余地がある．
- 第1次的社会的ジレンマ
  - 各エージェントが協力すれば全体報酬は最大化される
  - しかし個々には裏切り（フリーライド）した方が得
- 第2次的社会的ジレンマ
  - インセンティブを与えるにはコストがかかる
  - 他者がインセンティブを出してくれるなら、自分は出さない方が得


### 2022
#### [A Review of Cooperative Multi-Agent Deep Reinforcement Learning](https://arxiv.org/abs/1908.03963)
MARLが扱う課題の多くはNP困難問題に分類される．このサーベイでは協調的な目標を持つ分散型問題に焦点を当てている．IL(Independent Learners)の限界を緩和するために提案された手法として、1パラメータ共有、2学習率・更新頻度の工夫、3役割分担(エージェント行動の固定/探索空間を削減)などがある．

### 2023
#### [A Review of Cooperation in Multi-agent Learning](https://arxiv.org/abs/2312.05162)
> [Joel Z. Leibo](../Authors/overseas/JoelZ.Leibo.md), [Usman Islam](../Authors/overseas/UsmanIslam.md), [Richard Willis](../Authors/overseas/RichardWillis.md), [Peter Sunehag](../Authors/overseas/PeterSunehag.md)

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
SSDに対するMARLの評価基盤として、SocialJaxという実装スイートを提案している．エージェントは観測として、MeltingPotのように2D画像を受け取るのではなく、環境設計として数理的に利害構造が埋め込まれる、つまりかなり抽象的な表現を受け取る．
より具体的にはMeltingPotが持っているRGBピクセル観測は存在せず、11×11のグリッドで環境が構成されており、CNN等で「何が見えているか」を学習する必要は無い．
> [サイト？](https://sites.google.com/view/socialjax/home)、[github](https://github.com/cooperativex/SocialJax)
