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
- [Diverse and Sparse Mixture-of-Experts for Causal Subgraph-Based Out-of-Distribution Graph Learning(2026)](#diverse-and-sparse-mixture-of-experts-for-causal-subgraph-based-out-of-distribution-graph-learning)

## GNN
- [GraphCast:Learning skillful medium-range global weather forecasting(2023)](#graphcastlearning-skillful-medium-range-global-weather-forecasting)
- [Graph Mixture of Experts: Learning on Large-Scale Graphs with Explicit Diversity Modeling(2023)](#graph-mixture-of-experts-learning-on-large-scale-graphs-with-explicit-diversity-modeling)
- [GraphMETRO: Mitigating Complex Distribution Shifts in GNNs via Mixture of Aligned Experts(2023)](#graphmetro-mitigating-complex-distribution-shifts-in-gnns-via-mixture-of-aligned-experts)
- [Node-wise Filtering in Graph Neural Networks: A Mixture of Experts Approach(2024)](#node-wise-filtering-in-graph-neural-networks-a-mixture-of-experts-approach)
- [Diverse and Sparse Mixture-of-Experts for Causal Subgraph-Based Out-of-Distribution Graph Learning(2026)](#diverse-and-sparse-mixture-of-experts-for-causal-subgraph-based-out-of-distribution-graph-learning)


---

## 論文メモ
### 1991
#### [Adaptive Mixtures of Local Experts](https://www.cs.toronto.edu/~fritz/absps/jjnh91.pdf)
[Robert A. Jacobs](../Authors/overseas/RobertAJacobs.md) [Michael I. Jordan](../Authors/overseas/MichaelIJordan.md) [Steven J. Nowlan](../Authors/overseas/StevenJNowlan.md) [Geoffrey E. Hinton](../Authors/overseas/GeoffreyEHinton.md)

#Unread

複数の専門家ネットワークとSoftmaxゲートを一緒に最尤学習するMoEの原型を提案．EMに似た勾配更新でゲートが入力依存の混合重みを学び，母音識別タスクで各専門家が入力空間の異なる領域を担当することを示した．

### 2013
#### [Learning Factored Representations in a Deep Mixture of Experts](https://arxiv.org/abs/1312.4314)
[David Eigen](../Authors/overseas/DavidEigen.md) [Marc'Aurelio Ranzato](../Authors/overseas/MarcAurelioRanzato.md) [Ilya Sutskever](../Authors/overseas/IlyaSutskever.md)

#Unread

階層的にゲートと専門家を重ねたDMoEを提案し，層ごとに異なる因子（1層目で位置，2層目でクラス）に分解して専門化させることで指数的に多い経路を持ちながらパラメータを抑制．jittered MNISTと音声単音節でバランシング制約により全経路が活用されることを確認．

### 2016
#### [Ensemble Learning for Multi-Source Neural Machine Translation](https://aclanthology.org/C16-1133/)
[Ekaterina Garmash](../Authors/overseas/EkaterinaGarmash.md) [Christof Monz](../Authors/overseas/ChristofMonz.md)

#Unread

複数ソース言語のエンコーダを並列に持つNMTを重み付きアンサンブルする手法を比較し，ゲート付き線形結合が単一ソースや単純平均より有効で，独独→英などで最大+2.2 BLEU向上．マルチソース設定でMoE的な入力選択が有効であることを示した．

### 2017
#### [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538)
[Noam Shazeer](../Authors/overseas/NoamShazeer.md) [Azalia Mirhoseini](../Authors/overseas/AzaliaMirhoseini.md) [Krzysztof Maziarz](../Authors/overseas/KrzysztofMaziarz.md) [Andy Davis](../Authors/overseas/AndyDavis.md) [Quoc Le](../Authors/overseas/QuocLe.md) [Geoffrey Hinton](../Authors/overseas/GeoffreyEHinton.md) [Jeff Dean](../Authors/overseas/JeffDean.md)

#Unread

条件付き計算でモデル容量を1000倍規模に拡張しつつ計算コストをほぼ据え置くためのSparsely-Gated MoE層を提案．routerは入力に線形変換を施したロジットに可調整ガウスノイズを足し，Top-k（論文ではk=2）だけ残してSoftmaxするNoisy Top-K Gatingで各トークンを少数のexpertに送る．選ばれたexpertの出力のみ重み付き和を取るので，非活性expertの計算を省ける．routerが特定のexpertに偏らないよう，重要度分散と割り当て偏りを罰するauxiliary lossを導入して負荷を均衡化する．




### 2020
#### [GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding](https://arxiv.org/abs/2006.16668)
[Dmitry Lepikhin](../Authors/overseas/DmitryLepikhin.md) [HyoukJoong Lee](../Authors/overseas/HyoukJoongLee.md) [Yuanzhong Xu](../Authors/overseas/YuanzhongXu.md) [Dehao Chen](../Authors/overseas/DehaoChen.md) [Orhan Firat](../Authors/overseas/OrhanFirat.md) [Yanping Huang](../Authors/overseas/YanpingHuang.md) [Maxim Krikun](../Authors/overseas/MaximKrikun.md) [Noam Shazeer](../Authors/overseas/NoamShazeer.md) [Zhifeng Chen](../Authors/overseas/ZhifengChen.md)

#Unread

XLA拡張と注釈APIで自動シャーディングを行うGShardを提案し，MoEを含む多言語Transformerを600B超にスケール．2048 TPU v3で4日学習し，100言語→英翻訳で従来を上回るBLEUを達成．条件付き計算とデータ／モデル並列を一貫した記述で両立させた．

### 2021
#### [BASE Layers: Simplifying Training of Large, Sparse Models](https://proceedings.mlr.press/v139/lewis21a.html)

#Unread

巨大疎モデルの訓練を安定化するため，入力依存の柔軟なrouterだけに頼らず，ほぼ均等な割当を保つ学習可能なマッチング機構（BASE Layers）を提案．翻訳や言語モデリングでSwitch系に近い性能を維持しつつ，学習初期の負荷偏りと発散を抑えることを示し，router学習信号とデータ割当規則をどこまで分離すべきかという論点を残した．

### 2022
#### [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961)
[William Fedus](../Authors/overseas/WilliamFedus.md) [Barret Zoph](../Authors/overseas/BarretZoph.md) [Noam Shazeer](../Authors/overseas/NoamShazeer.md)

#Unread

MoEのルータをTop-1に単純化したSwitch routingで通信と計算を削減し，安定化テクニックによりbfloat16でも学習可能に．T5系でFLOPs一定のまま専門家数を増やし，最大7倍の事前学習速度とトリリオン規模パラメータを実現．

#### [ST-MoE: Designing Stable and Transferable Sparse Expert Models](https://arxiv.org/abs/2202.08906)
[Barret Zoph](../Authors/overseas/BarretZoph.md) [Irwan Bello](../Authors/overseas/IrwanBello.md) [Sameer Kumar](../Authors/overseas/SameerKumar.md) [Nan Du](../Authors/overseas/NanDu.md) [Yanping Huang](../Authors/overseas/YanpingHuang.md) [Jeff Dean](../Authors/overseas/JeffDean.md) [Noam Shazeer](../Authors/overseas/NoamShazeer.md) [William Fedus](../Authors/overseas/WilliamFedus.md)

#Unread

Switch系で課題だった不安定さと転移性能を改善する設計指針を提示．正規化・初期化・負荷分散損失を調整し，269BパラメータのST-MoE-32Bが32B密モデルと同等の計算量で多様な下流タスク（SuperGLUE，XSum等）でSOTAを達成した．

#### [Mixture-of-Experts with Expert Choice Routing](https://arxiv.org/abs/2202.09368)

#Unread

tokenがexpertを選ぶ従来のTop-k routerと逆に，expert側が受け取るtokenを選ぶExpert Choice Routingを提案し，容量制約下でも負荷分散と計算効率を両立．大規模言語モデリングで同計算量あたりの品質向上を報告し，routerの学習データ割当を「確率的選択」ではなく「制約付き割当」として設計する方向性を示した．


### 2023
#### [GraphCast:Learning skillful medium-range global weather forecasting](https://arxiv.org/abs/2212.12794)
[Remi Lam](../Authors/overseas/RemiLam.md) [Alvaro Sanchez-Gonzalez](../Authors/overseas/AlvaroSanchezGonzalez.md) [Matthew Willson](../Authors/overseas/MatthewWillson.md) [Peter Wirnsberger](../Authors/overseas/PeterWirnsberger.md) [Meire Fortunato](../Authors/overseas/MeireFortunato.md) [Ferran Alet](../Authors/overseas/FerranAlet.md) [Suman Ravuri](../Authors/overseas/SumanRavuri.md) [Timo Ewalds](../Authors/overseas/TimoEwalds.md) [Zach Eaton-Rosen](../Authors/overseas/ZachEatonRosen.md) [Weihua Hu](../Authors/overseas/WeihuaHu.md) [Alexander Merose](../Authors/overseas/AlexanderMerose.md) [Stephan Hoyer](../Authors/overseas/StephanHoyer.md) [George Holland](../Authors/overseas/GeorgeHolland.md) [Oriol Vinyals](../Authors/overseas/OriolVinyals.md) [Jacklynn Stott](../Authors/overseas/JacklynnStott.md) [Alexander Pritzel](../Authors/overseas/AlexanderPritzel.md) [Shakir Mohamed](../Authors/overseas/ShakirMohamed.md) [Peter Battaglia](../Authors/overseas/PeterBattaglia.md)

#Unread

GNNで全球0.25度格子の大気状態を6時間刻みでオートレグレッシブ予測するGraphCastを提案．DeepMindの実装は10日先までの227変数を60秒未満で生成し，ECMWF HRESを約89％の指標で上回る精度を示した．

#### [Graph Mixture of Experts: Learning on Large-Scale Graphs with Explicit Diversity Modeling](https://arxiv.org/abs/2304.02806)

#Unread

大規模グラフで過平滑化と表現の同質化を避けるため，複数expertの出力をrouterで選択統合しつつ，expert間の多様性を明示的に促進するGraph MoEを提案．ノード分類設定で性能改善を示し，routing粒度をnode側に置いたときの多様性制約の効き方が主要論点となっている．

#### [GraphMETRO: Mitigating Complex Distribution Shifts in GNNs via Mixture of Aligned Experts](https://openreview.net/forum?id=ofIAlQ0FPy)

#Unread

OODグラフ学習で複数の分布シフト要因を分解的に扱うため，shift要因に整合したexpert群とゲートを組み合わせるGraphMETROを提案．複数ベンチマークで頑健性向上を示し，routerが何を条件にexpertを選ぶべきかを「ラベル予測」以外の目的（shift同定）で学習する設計が争点になる．

### 2024
#### [Node-wise Filtering in Graph Neural Networks: A Mixture of Experts Approach](https://arxiv.org/abs/2406.03464)

#Unread

ノードごとの局所構造差を吸収するため，複数のフィルタexpertからnode-wiseに選択するMoE型GNNを提案．ノード分類タスクで一様フィルタより高精度を報告し，routing単位をgraph全体でなくnode単位に細分化したときの計算コストと専門化のトレードオフを明確化している．

### 2026
#### [Diverse and Sparse Mixture-of-Experts for Causal Subgraph-Based Out-of-Distribution Graph Learning](https://openreview.net/forum?id=4XVczusV2K)

#Unread

因果サブグラフに基づくOODグラフ学習に対し，疎ルーティングとexpert多様化制約を併用するDiSCOを提案．ICLR 2026で複数OOD設定の改善を示し，インスタンス（graph/sample）単位でのexpert選択が因果パターン抽出に有利かどうかを中心に議論している．
