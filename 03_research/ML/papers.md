# ML論文
## MoE
- [Adaptive Mixtures of Local Experts(1991)](#adaptive-mixtures-of-local-experts)
- [Learning Factored Representations in a Deep Mixture of Experts(2013)](#learning-factored-representations-in-a-deep-mixture-of-experts)
- [Ensemble Learning for Multi-Source Neural Machine Translation(2016)](#ensemble-learning-for-multi-source-neural-machine-translation)
- [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer(2017)](#outrageously-large-neural-networks-the-sparsely-gated-mixture-of-experts-layer)
- [GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding(2020)](#gshard-scaling-giant-models-with-conditional-computation-and-automatic-sharding)
- [BASE Layers: Simplifying Training of Large, Sparse Models(2021)](#base-layers-simplifying-training-of-large-sparse-models)
- [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity(2022)](#switch-transformers-scaling-to-trillion-parameter-models-with-simple-and-efficient-sparsity)
- [ST-MoE: Designing Stable and Transferable Sparse Expert Models(2022)](#st-moe-designing-stable-and-transferable-sparse-expert-models)
- [Mixture-of-Experts with Expert Choice Routing(2022)](#mixture-of-experts-with-expert-choice-routing)
- [Graph Mixture of Experts: Learning on Large-Scale Graphs with Explicit Diversity Modeling(2023)](#graph-mixture-of-experts-learning-on-large-scale-graphs-with-explicit-diversity-modeling)
- [GraphMETRO: Mitigating Complex Distribution Shifts in GNNs via Mixture of Aligned Experts(2023)](#graphmetro-mitigating-complex-distribution-shifts-in-gnns-via-mixture-of-aligned-experts)
- [Node-wise Filtering in Graph Neural Networks: A Mixture of Experts Approach(2024)](#node-wise-filtering-in-graph-neural-networks-a-mixture-of-experts-approach)
- [Mixture of Weak and Strong Experts on Graphs(2024)](#mixture-of-weak-and-strong-experts-on-graphs)
- [Mixture of Decoupled Message Passing Experts with Entropy Constraint for General Node Classification(2025)](#mixture-of-decoupled-message-passing-experts-with-entropy-constraint-for-general-node-classification)
- [MoLE-GNN: Parameter-Efficient Fine-Tuning of Graph Neural Networks with Mixture-of-Experts(2025)](#mole-gnn-parameter-efficient-fine-tuning-of-graph-neural-networks-with-mixture-of-experts)
- [Diverse and Sparse Mixture-of-Experts for Causal Subgraph-Based Out-of-Distribution Graph Learning(2026)](#diverse-and-sparse-mixture-of-experts-for-causal-subgraph-based-out-of-distribution-graph-learning)

## GNN
- [Neural Message Passing for Quantum Chemistry(2017)](#neural-message-passing-for-quantum-chemistry)
- [Principal Neighbourhood Aggregation for Graph Nets(2020)](#principal-neighbourhood-aggregation-for-graph-nets)
- [Learning How to Propagate Messages in Graph Neural Networks(2021)](#learning-how-to-propagate-messages-in-graph-neural-networks)
- [GraphCast:Learning skillful medium-range global weather forecasting(2023)](#graphcastlearning-skillful-medium-range-global-weather-forecasting)
- [Hierarchical message-passing graph neural networks(2023)](#hierarchical-message-passing-graph-neural-networks)
- [Graph Mixture of Experts: Learning on Large-Scale Graphs with Explicit Diversity Modeling(2023)](#graph-mixture-of-experts-learning-on-large-scale-graphs-with-explicit-diversity-modeling)
- [GraphMETRO: Mitigating Complex Distribution Shifts in GNNs via Mixture of Aligned Experts(2023)](#graphmetro-mitigating-complex-distribution-shifts-in-gnns-via-mixture-of-aligned-experts)
- [Node-wise Filtering in Graph Neural Networks: A Mixture of Experts Approach(2024)](#node-wise-filtering-in-graph-neural-networks-a-mixture-of-experts-approach)
- [Mixture of Weak and Strong Experts on Graphs(2024)](#mixture-of-weak-and-strong-experts-on-graphs)
- [Mixture of Decoupled Message Passing Experts with Entropy Constraint for General Node Classification(2025)](#mixture-of-decoupled-message-passing-experts-with-entropy-constraint-for-general-node-classification)
- [MoLE-GNN: Parameter-Efficient Fine-Tuning of Graph Neural Networks with Mixture-of-Experts(2025)](#mole-gnn-parameter-efficient-fine-tuning-of-graph-neural-networks-with-mixture-of-experts)
- [Diverse and Sparse Mixture-of-Experts for Causal Subgraph-Based Out-of-Distribution Graph Learning(2026)](#diverse-and-sparse-mixture-of-experts-for-causal-subgraph-based-out-of-distribution-graph-learning)


---

## 論文メモ
### 1991
#### [Adaptive Mixtures of Local Experts](https://www.cs.toronto.edu/~fritz/absps/jjnh91.pdf)
[Robert A. Jacobs](../Authors/overseas/RobertAJacobs.html) [Michael I. Jordan](../Authors/overseas/MichaelIJordan.html) [Steven J. Nowlan](../Authors/overseas/StevenJNowlan.html) [Geoffrey E. Hinton](../Authors/overseas/GeoffreyEHinton.html)

#Unread

複数の専門家ネットワークとSoftmaxゲートを一緒に最尤学習するMoEの原型を提案．EMに似た勾配更新でゲートが入力依存の混合重みを学び，母音識別タスクで各専門家が入力空間の異なる領域を担当することを示した．

### 2013
#### [Learning Factored Representations in a Deep Mixture of Experts](https://arxiv.org/abs/1312.4314)
[David Eigen](../Authors/overseas/DavidEigen.html) [Marc'Aurelio Ranzato](../Authors/overseas/MarcAurelioRanzato.html) [Ilya Sutskever](../Authors/overseas/IlyaSutskever.html)

#Unread

階層的にゲートと専門家を重ねたDMoEを提案し，層ごとに異なる因子（1層目で位置，2層目でクラス）に分解して専門化させることで指数的に多い経路を持ちながらパラメータを抑制．jittered MNISTと音声単音節でバランシング制約により全経路が活用されることを確認．

### 2016
#### [Ensemble Learning for Multi-Source Neural Machine Translation](https://aclanthology.org/C16-1133/)
[Ekaterina Garmash](../Authors/overseas/EkaterinaGarmash.html) [Christof Monz](../Authors/overseas/ChristofMonz.html)

#Unread

複数ソース言語のエンコーダを並列に持つNMTを重み付きアンサンブルする手法を比較し，ゲート付き線形結合が単一ソースや単純平均より有効で，独独→英などで最大+2.2 BLEU向上．マルチソース設定でMoE的な入力選択が有効であることを示した．

### 2017
#### [Neural Message Passing for Quantum Chemistry](https://arxiv.org/abs/1704.01212)
Justin Gilmer, Samuel S. Schoenholz, Patrick F. Riley, Oriol Vinyals, George E. Dahl

#Unread

メッセージ関数と更新関数を分離したMPNN枠組みを提示し，既存の分子グラフ向け手法を統一的に記述可能にした．量子化学ベンチマークで高精度を示し，核心は「エッジ特徴付きメッセージ設計」を一般化した点にある．開放論点は，タスク依存でmessage/update/readoutのどこが性能ボトルネックになるかをどう切り分けるかである．

#### [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538)
[Noam Shazeer](../Authors/overseas/NoamShazeer.html) [Azalia Mirhoseini](../Authors/overseas/AzaliaMirhoseini.html) [Krzysztof Maziarz](../Authors/overseas/KrzysztofMaziarz.html) [Andy Davis](../Authors/overseas/AndyDavis.html) [Quoc Le](../Authors/overseas/QuocLe.html) [Geoffrey Hinton](../Authors/overseas/GeoffreyEHinton.html) [Jeff Dean](../Authors/overseas/JeffDean.html)

#Unread

条件付き計算でモデル容量を1000倍規模に拡張しつつ計算コストをほぼ据え置くためのSparsely-Gated MoE層を提案．routerは入力に線形変換を施したロジットに可調整ガウスノイズを足し，Top-k（論文ではk=2）だけ残してSoftmaxするNoisy Top-K Gatingで各トークンを少数のexpertに送る．選ばれたexpertの出力のみ重み付き和を取るので，非活性expertの計算を省ける．routerが特定のexpertに偏らないよう，重要度分散と割り当て偏りを罰するauxiliary lossを導入して負荷を均衡化する．




### 2020
#### [Principal Neighbourhood Aggregation for Graph Nets](https://arxiv.org/abs/2004.05718)
Gabriele Corso, Luca Cavalleri, Dominique Beaini, Pietro Lio, Petar Velickovic

#Unread

PNAは平均や最大など複数の集約器と次数スケーラを組み合わせ，連続特徴空間での識別力低下を補うmessage passing設計を提案する．分子回帰を中心とした評価でGIN系を上回る性能を報告し，noveltyは「次数統計を明示的に取り込む汎用集約ブロック」にある．今後の論点は，計算コスト増と表現力向上のトレードオフをどの程度許容するかである．

#### [GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding](https://arxiv.org/abs/2006.16668)
[Dmitry Lepikhin](../Authors/overseas/DmitryLepikhin.html) [HyoukJoong Lee](../Authors/overseas/HyoukJoongLee.html) [Yuanzhong Xu](../Authors/overseas/YuanzhongXu.html) [Dehao Chen](../Authors/overseas/DehaoChen.html) [Orhan Firat](../Authors/overseas/OrhanFirat.html) [Yanping Huang](../Authors/overseas/YanpingHuang.html) [Maxim Krikun](../Authors/overseas/MaximKrikun.html) [Noam Shazeer](../Authors/overseas/NoamShazeer.html) [Zhifeng Chen](../Authors/overseas/ZhifengChen.html)

#Unread

XLA拡張と注釈APIで自動シャーディングを行うGShardを提案し，MoEを含む多言語Transformerを600B超にスケール．2048 TPU v3で4日学習し，100言語→英翻訳で従来を上回るBLEUを達成．条件付き計算とデータ／モデル並列を一貫した記述で両立させた．

### 2021
#### [Learning How to Propagate Messages in Graph Neural Networks](https://doi.org/10.1145/3447548.3467451)
Teng Xiao, Zhengyu Chen, Donglin Wang, Suhang Wang

#Unread

ノードごとに最適な伝播ステップを潜在変数として学習するLTPフレームワークを提案し，固定層数・固定k-hopの制約を緩和した．変分EMで伝播戦略と予測器を同時最適化し，複数ノード分類ベンチマークで精度向上を示す．主な論点は，推論時の計算コストと学習された伝播戦略の解釈可能性をどう両立するかである．

#### [BASE Layers: Simplifying Training of Large, Sparse Models](https://proceedings.mlr.press/v139/lewis21a.html)
[Mike Lewis](../Authors/overseas/MikeLewis.html) [Shruti Bhosale](../Authors/overseas/ShrutiBhosale.html) [Tim Dettmers](../Authors/overseas/TimDettmers.html) [Naman Goyal](../Authors/overseas/NamanGoyal.html) [Luke Zettlemoyer](../Authors/overseas/LukeZettlemoyer.html)

#Unread

巨大疎モデルの訓練を安定化するため，入力依存の柔軟なrouterだけに頼らず，ほぼ均等な割当を保つ学習可能なマッチング機構（BASE Layers）を提案．翻訳や言語モデリングでSwitch系に近い性能を維持しつつ，学習初期の負荷偏りと発散を抑えることを示し，router学習信号とデータ割当規則をどこまで分離すべきかという論点を残した．

### 2022
#### [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961)
[William Fedus](../Authors/overseas/WilliamFedus.html) [Barret Zoph](../Authors/overseas/BarretZoph.html) [Noam Shazeer](../Authors/overseas/NoamShazeer.html)

#Unread

MoEのルータをTop-1に単純化したSwitch routingで通信と計算を削減し，安定化テクニックによりbfloat16でも学習可能に．T5系でFLOPs一定のまま専門家数を増やし，最大7倍の事前学習速度とトリリオン規模パラメータを実現．

#### [ST-MoE: Designing Stable and Transferable Sparse Expert Models](https://arxiv.org/abs/2202.08906)
[Barret Zoph](../Authors/overseas/BarretZoph.html) [Irwan Bello](../Authors/overseas/IrwanBello.html) [Sameer Kumar](../Authors/overseas/SameerKumar.html) [Nan Du](../Authors/overseas/NanDu.html) [Yanping Huang](../Authors/overseas/YanpingHuang.html) [Jeff Dean](../Authors/overseas/JeffDean.html) [Noam Shazeer](../Authors/overseas/NoamShazeer.html) [William Fedus](../Authors/overseas/WilliamFedus.html)

#Unread

Switch系で課題だった不安定さと転移性能を改善する設計指針を提示．正規化・初期化・負荷分散損失を調整し，269BパラメータのST-MoE-32Bが32B密モデルと同等の計算量で多様な下流タスク（SuperGLUE，XSum等）でSOTAを達成した．

#### [Mixture-of-Experts with Expert Choice Routing](https://arxiv.org/abs/2202.09368)
[Yanqi Zhou](../Authors/overseas/YanqiZhou.html) [Tao Lei](../Authors/overseas/TaoLei.html) [Hanxiao Liu](../Authors/overseas/HanxiaoLiu.html) [Nan Du](../Authors/overseas/NanDu.html) [Yanping Huang](../Authors/overseas/YanpingHuang.html) [Vincent Zhao](../Authors/overseas/VincentZhao.html) [Andrew Dai](../Authors/overseas/AndrewDai.html) [Zhifeng Chen](../Authors/overseas/ZhifengChen.html) [Quoc Le](../Authors/overseas/QuocLe.html) [James Laudon](../Authors/overseas/JamesLaudon.html)

#Unread

tokenがexpertを選ぶ従来のTop-k routerと逆に，expert側が受け取るtokenを選ぶExpert Choice Routingを提案し，容量制約下でも負荷分散と計算効率を両立．大規模言語モデリングで同計算量あたりの品質向上を報告し，routerの学習データ割当を「確率的選択」ではなく「制約付き割当」として設計する方向性を示した．


### 2023
#### [GraphCast:Learning skillful medium-range global weather forecasting](https://arxiv.org/abs/2212.12794)
[Remi Lam](../Authors/overseas/RemiLam.html) [Alvaro Sanchez-Gonzalez](../Authors/overseas/AlvaroSanchezGonzalez.html) [Matthew Willson](../Authors/overseas/MatthewWillson.html) [Peter Wirnsberger](../Authors/overseas/PeterWirnsberger.html) [Meire Fortunato](../Authors/overseas/MeireFortunato.html) [Ferran Alet](../Authors/overseas/FerranAlet.html) [Suman Ravuri](../Authors/overseas/SumanRavuri.html) [Timo Ewalds](../Authors/overseas/TimoEwalds.html) [Zach Eaton-Rosen](../Authors/overseas/ZachEatonRosen.html) [Weihua Hu](../Authors/overseas/WeihuaHu.html) [Alexander Merose](../Authors/overseas/AlexanderMerose.html) [Stephan Hoyer](../Authors/overseas/StephanHoyer.html) [George Holland](../Authors/overseas/GeorgeHolland.html) [Oriol Vinyals](../Authors/overseas/OriolVinyals.html) [Jacklynn Stott](../Authors/overseas/JacklynnStott.html) [Alexander Pritzel](../Authors/overseas/AlexanderPritzel.html) [Shakir Mohamed](../Authors/overseas/ShakirMohamed.html) [Peter Battaglia](../Authors/overseas/PeterBattaglia.html)

#Unread

GNNで全球0.25度格子の大気状態を6時間刻みでオートレグレッシブ予測するGraphCastを提案．DeepMindの実装は10日先までの227変数を60秒未満で生成し，ECMWF HRESを約89％の指標で上回る精度を示した．

#### [Hierarchical message-passing graph neural networks](https://link.springer.com/article/10.1007/s10618-022-00890-9)
Zhiqiang Zhong, Cheng-Te Li, Jun Pang

#Unread

階層的に構成したsuper graph間でbottom-up / within-level / top-downの3種類の伝播を行うHMGNNを提案し，長距離依存と高次近傍情報を同時に扱う．リンク予測・ノード分類・コミュニティ検出で既存flat message passingより高い性能を報告した．未解決点は，階層生成品質への依存が強く，構造化前処理の設計が性能を大きく左右する点である．

#### [Graph Mixture of Experts: Learning on Large-Scale Graphs with Explicit Diversity Modeling](https://arxiv.org/abs/2304.02806)
[Haotao Wang](../Authors/overseas/HaotaoWang.html) [Ziyu Jiang](../Authors/overseas/ZiyuJiang.html) [Yuning You](../Authors/overseas/YuningYou.html) [Yan Han](../Authors/overseas/YanHan.html) [Gaowen Liu](../Authors/overseas/GaowenLiu.html) [Jayanth Srinivasa](../Authors/overseas/JayanthSrinivasa.html) [Ramana Rao Kompella](../Authors/overseas/RamanaRaoKompella.html) [Zhangyang Wang](../Authors/overseas/ZhangyangWang.html)

#Unread

大規模グラフで過平滑化と表現の同質化を避けるため，複数expertの出力をrouterで選択統合しつつ，expert間の多様性を明示的に促進するGraph MoEを提案．ノード分類設定で性能改善を示し，routing粒度をnode側に置いたときの多様性制約の効き方が主要論点となっている．

#### [GraphMETRO: Mitigating Complex Distribution Shifts in GNNs via Mixture of Aligned Experts](https://openreview.net/forum?id=ofIAlQ0FPy)
[Shirley Wu](../Authors/overseas/ShirleyWu.html) [Kaidi Cao](../Authors/overseas/KaidiCao.html) [Bruno Ribeiro](../Authors/overseas/BrunoRibeiro.html) [James Zou](../Authors/overseas/JamesZou.html) [Jure Leskovec](../Authors/overseas/JureLeskovec.html)

#Unread

OODグラフ学習で複数の分布シフト要因を分解的に扱うため，shift要因に整合したexpert群とゲートを組み合わせるGraphMETROを提案．複数ベンチマークで頑健性向上を示し，routerが何を条件にexpertを選ぶべきかを「ラベル予測」以外の目的（shift同定）で学習する設計が争点になる．

### 2024
#### [Mixture of Weak and Strong Experts on Graphs](https://openreview.net/forum?id=wYvuY60SdD)
Hanqing Zeng, Hanjia Lyu, Diyi Hu, Yinglong Xia, Jiebo Luo

#Unread

Mowstは弱いMLP expertと強いGNN expertをゲートで混合し，ノードごとに「自己特徴中心か隣接構造中心か」を切り替えるMoE設計を示す．homophilyとheterophilyが混在するデータで精度改善を示し，core methodは信頼度に基づくnode-wise routingである．議論点は，ゲートがデータ分布変化時に安定に機能するかと，expert間の役割分担が再現可能かである．

#### [Node-wise Filtering in Graph Neural Networks: A Mixture of Experts Approach](https://arxiv.org/abs/2406.03464)
[Haoyu Han](../Authors/overseas/HaoyuHan.html) [Juanhui Li](../Authors/overseas/JuanhuiLi.html) [Wei Huang](../Authors/overseas/WeiHuang.html) [Xianfeng Tang](../Authors/overseas/XianfengTang.html) [Hanqing Lu](../Authors/overseas/HanqingLu.html) [Chen Luo](../Authors/overseas/ChenLuo.html) [Hui Liu](../Authors/overseas/HuiLiu.html) [Jiliang Tang](../Authors/overseas/JiliangTang.html)

#Unread

ノードごとの局所構造差を吸収するため，複数のフィルタexpertからnode-wiseに選択するMoE型GNNを提案．ノード分類タスクで一様フィルタより高精度を報告し，routing単位をgraph全体でなくnode単位に細分化したときの計算コストと専門化のトレードオフを明確化している．

### 2025
#### [Mixture of Decoupled Message Passing Experts with Entropy Constraint for General Node Classification](https://openreview.net/forum?id=yVuxtcI8XO)
Xuanze Chen, Jiajun Zhou, Jinsong Chen, Shanqing Yu, Qi Xuan

#Unread

異なるmessage passing演算を独立expertとして持ち，soft/hard gatingとエントロピー制約でノード単位の割当を学習するDecoupled MP-Expertsを提案する．複数のノード分類ベンチマークでhomophily/heterophily双方への汎化を検証し，noveltyはroutingの偏りを制御しつつexpert specializationを促す点にある．論点は，制約強度のチューニングがデータごとに必要で，実運用での頑健設定が難しいことである．

#### [MoLE-GNN: Parameter-Efficient Fine-Tuning of Graph Neural Networks with Mixture-of-Experts](https://openreview.net/forum?id=MynAEqF9Nc)
Shrimon Mukherjee, Madhusudan Ghosh, Partha Basuchowdhuri

#Unread

MoLE-GNNはadapterベースのPEFTとMoE routingを統合し，GNN全体を再学習せずに深さ感度に応じたexpert選択を可能にする．報告では総パラメータの約5.1%のみ更新して複数設定で既存PEFT法を上回る結果を示した．開放論点は，graphサイズ分布が大きく変わるタスクでrouting規則がどこまで転移可能かである．

### 2026
#### [Diverse and Sparse Mixture-of-Experts for Causal Subgraph-Based Out-of-Distribution Graph Learning](https://openreview.net/forum?id=4XVczusV2K)
[Jerry Sun](../Authors/overseas/JerrySun.html) [Mohamed Abubakr Hassan](../Authors/overseas/MohamedAbubakrHassan.html) [Yaoyu Zhang](../Authors/overseas/YaoyuZhang.html) [Wanying Zhang](../Authors/overseas/WanyingZhang.html) [Chi-Guhn Lee](../Authors/overseas/ChiGuhnLee.html)

#Unread

因果サブグラフに基づくOODグラフ学習に対し，疎ルーティングとexpert多様化制約を併用するDiSCOを提案．ICLR 2026で複数OOD設定の改善を示し，インスタンス（graph/sample）単位でのexpert選択が因果パターン抽出に有利かどうかを中心に議論している．
