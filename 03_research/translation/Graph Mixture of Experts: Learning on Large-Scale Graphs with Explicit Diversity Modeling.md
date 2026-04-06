# Graph Mixture of Experts: Learning on Large-Scale Graphs with Explicit Diversity Modeling

Graph Mixture of Experts: Learning on Large-Scale Graphs with Explicit Diversity Modeling
グラフ混合エキスパート：明示的多様性モデリングによる大規模グラフ上の学習

Haotao Wang1∗, Ziyu Jiang2∗, Yuning You2, Yan Han1, Gaowen Liu3, Jayanth Srinivasa3, Ramana Rao Kompella3, Zhangyang Wang1
Haotao Wang1∗, Ziyu Jiang2∗, Yuning You2, Yan Han1, Gaowen Liu3, Jayanth Srinivasa3, Ramana Rao Kompella3, Zhangyang Wang1

1University of Texas at Austin, Texas A&M University2, Cisco Systems3
1テキサス大学オースティン校、テキサスA&M大学2、シスコシステムズ3

## Abstract

Graph neural networks (GNNs) have found extensive applications in learning from graph data.
グラフニューラルネットワーク（GNN）は、グラフデータからの学習において広範な応用が見出されている。

However, real-world graphs often possess diverse structures and comprise nodes and edges of varying types.
しかし、現実世界のグラフはしばしば多様な構造を持ち、様々な種類のノードとエッジから構成されている。

To bolster the generalization capacity of GNNs, it has become customary to augment training graph structures through techniques like graph augmentations and large-scale pre-training on a wider array of graphs.
GNNの汎化能力を強化するために、グラフ拡張や、より広範なグラフ群に対する大規模事前学習といった手法を通じて、訓練グラフ構造を拡充することが慣例となっている。

Balancing this diversity while avoiding increased computational costs and the notorious trainability issues of GNNs is crucial.
計算コストの増大やGNNにおける悪名高い訓練可能性の問題を回避しながら、この多様性のバランスを保つことは極めて重要である。

This study introduces the concept of Mixture-of-Experts (MoE) to GNNs, with the aim of augmenting their capacity to adapt to a diverse range of training graph structures, without incurring explosive computational overhead.
本研究は、爆発的な計算オーバーヘッドを生じさせることなく、多様な訓練グラフ構造への適応能力を高めることを目的として、混合エキスパート（MoE）の概念をGNNに導入する。

The proposed Graph Mixture of Experts (GMoE) model empowers individual nodes in the graph to dynamically and adaptively select more general information aggregation experts.
提案するグラフ混合エキスパート（GMoE）モデルは、グラフ内の個々のノードが、より汎用的な情報集約エキスパートを動的かつ適応的に選択することを可能にする。

These experts are trained to capture distinct subgroups of graph structures and to incorporate information with varying hop sizes, where those with larger hop sizes specialize in gathering information over longer distances.
これらのエキスパートは、グラフ構造の異なるサブグループを捉え、様々なホップサイズで情報を組み込むよう訓練されており、より大きいホップサイズを持つエキスパートは、より長距離にわたる情報収集を専門とする。

The effectiveness of GMoE is validated through a series of experiments on a diverse set of tasks, including graph, node, and link prediction, using the OGB benchmark.
GMoEの有効性は、OGBベンチマークを用いたグラフ、ノード、リンク予測を含む多様なタスクセットに対する一連の実験を通じて検証される。

Notably, it enhances ROC-AUC by 1.81% in ogbg-molhiv and by 1.40% in ogbg-molbbbp, when compared to the non-MoE baselines.
特筆すべきことに、非MoEベースラインと比較して、ogbg-molhivでROC-AUCを1.81%、ogbg-molbbbpで1.40%向上させる。

Our code is publicly available at https://github.com/VITA-Group/Graph-Mixture-of-Experts.
コードはhttps://github.com/VITA-Group/Graph-Mixture-of-Expertsにて公開されている。

## 1 Introduction

Graph learning has found extensive use in various real-world applications, including recommendation systems [1], traffic prediction [2], and molecular property prediction [3].
グラフ学習は、推薦システム[1]、交通予測[2]、分子特性予測[3]など、様々な現実世界の応用において広く利用されている。

Real-world graph data typically exhibit diverse graph structures and heterogeneous nodes and edges.
現実世界のグラフデータは、一般に多様なグラフ構造と異種のノード及びエッジを示す。

In graph-based recommendation systems, for instance, a node can represent a product or a customer, while an edge can indicate different interactions such as view, like, or purchase.
例えば、グラフベースの推薦システムでは、ノードは商品や顧客を表すことができ、エッジは閲覧、いいね、購入などの様々なインタラクションを示すことができる。

Similarly in biochemistry tasks, datasets can comprise molecules with various biochemistry properties and therefore various graph structures.
同様に、生化学タスクにおいても、データセットは様々な生化学的特性を持つ分子、したがって様々なグラフ構造を含み得る。

Moreover, purposefully increasing the diversity of graph data structures in training sets has become a crucial aspect of GNN training.
さらに、訓練セットにおけるグラフデータ構造の多様性を意図的に増大させることは、GNN訓練における重要な側面となっている。

Techniques such as graph data augmentations [4, 5] and large-scale pre-training on diverse graphs [6, 7, 8, 9, 10] have been widely adopted to allow GNNs for extracting more robust and generalizable features.
グラフデータ拡張[4, 5]や多様なグラフに対する大規模事前学習[6, 7, 8, 9, 10]といった手法は、GNNがより頑健で汎化可能な特徴を抽出できるよう広く採用されている。

Meanwhile, many real-world GNN applications, such as recommendation systems and molecule virtual screening, usually involve processing a vast number of candidate samples and therefore demand computational efficiency.
一方、推薦システムや分子バーチャルスクリーニングなどの多くの現実世界のGNN応用は、通常、膨大な数の候補サンプルを処理することを伴い、したがって計算効率を要求する。

That invites the key question: Can one effectively scale a GNN model's capacity to leverage larger-scale, more diverse graph data, without compromising its inference efficiency?
これは重要な問いを提起する：GNNモデルの推論効率を損なうことなく、より大規模で多様なグラフデータを活用するモデルの能力を効果的にスケールさせることは可能か？

A common limitation of many GNN architectures is that they are essentially "homogeneous" across the whole graph, i.e., forcing all nodes to share the same aggregation mechanism, regardless of the differences in their node features or neighborhood information.
多くのGNNアーキテクチャの一般的な制限は、それらがグラフ全体にわたって本質的に「均質」であること、すなわち、ノード特徴や近傍情報の違いにかかわらず、全ノードに同一の集約メカニズムを強制することである。

That might be suboptimal when training on diverse graph structures, e.g, when some nodes may require information aggregated over longer ranges while others prefer shorter-range local information.
これは、例えばあるノードはより長距離にわたって集約された情報を必要とし、他のノードは短距離の局所情報を好むような、多様なグラフ構造上での訓練時には最適でない可能性がある。

Our solution is the proposal of a novel GNN architecture dubbed Graph Mixture of Experts (GMoE).
我々の解決策は、グラフ混合エキスパート（GMoE）と名付けられた新規GNNアーキテクチャの提案である。

It comprises multiple "experts" at each layer, with each expert being an independent message-passing function with its own trainable parameters.
これは各層に複数の「エキスパート」を含み、各エキスパートは独自の訓練可能なパラメータを持つ独立したメッセージパッシング関数である。

The idea establishes a new base to address the diversity challenges residing in graph data.
このアイデアは、グラフデータに存在する多様性の課題に対処するための新たな基盤を確立する。

Throughout the training process, GMoE is designed to intelligently select aggregation experts tailored to each node.
訓練プロセス全体を通じて、GMoEは各ノードに合わせた集約エキスパートを知的に選択するよう設計されている。

Consequently, nodes with similar neighborhood information are guided towards the same aggregation experts.
その結果、類似した近傍情報を持つノードは同じ集約エキスパートへと誘導される。

This fosters specialization within each GMoE expert, focusing on specific subsets of training samples with akin neighborhood patterns, regardless of range or aggregation levels.
これにより、各GMoEエキスパート内での専門化が促進され、距離や集約レベルにかかわらず、類似した近傍パターンを持つ訓練サンプルの特定のサブセットに集中する。

In order to harness the full spectrum of diversity, GMoE also incorporates aggregation experts with distinct inductive biases.
多様性の全スペクトルを活用するために、GMoEはまた、異なる帰納的バイアスを持つ集約エキスパートを組み込む。

For example, each GMoE layer is equipped with aggregation experts of varying hop sizes.
例えば、各GMoE層は様々なホップサイズの集約エキスパートを備えている。

Those with larger hop sizes cater to nodes requiring information from more extended ranges, while the opposite holds true for those with smaller hop sizes.
より大きいホップサイズを持つエキスパートは、より広範囲からの情報を必要とするノードに対応し、より小さいホップサイズを持つエキスパートはその逆である。

We have rigorously validated GMoE's effectiveness through a range of comprehensive molecular property prediction tasks, underscoring our commitment to deliberate diversity modeling.
我々は、意図的な多様性モデリングへの取り組みを強調しつつ、包括的な分子特性予測タスクの範囲を通じてGMoEの有効性を厳密に検証した。

Moreover, our analysis demonstrates that GMoE surpasses other GNN models in terms of inference efficiency, even when they possess similar-sized parameters, thanks to the dynamic expert selection.
さらに、動的なエキスパート選択のおかげで、GMoEは同程度のパラメータサイズを持つ場合でも、推論効率において他のGNNモデルを上回ることを我々の分析は示している。

This efficiency proves crucial in real-world scenarios, such as virtual screening in libraries of trillion-scale magnitude or beyond.
この効率性は、兆スケール規模またはそれ以上のライブラリにおけるバーチャルスクリーニングなどの現実世界のシナリオにおいて重要であることが証明される。

The potency of our approach is corroborated by extensive experiments on ten graph learning datasets within the OGB benchmark.
我々のアプローチの有効性は、OGBベンチマーク内の10個のグラフ学習データセットに対する広範な実験によって裏付けられる。

For instance, GMoE enhances the ROC-AUC by 1.81% on ogbg-molhiv, 1.40% on ogbg-molbbbp, 0.95% on ogbn-proteins, and boosts Hits@20 score by 0.89% on ogbl-ddi, when compared to the single-expert baseline.
例えば、GMoEは単一エキスパートベースラインと比較して、ogbg-molhivでROC-AUCを1.81%、ogbg-molbbbpで1.40%、ogbn-proteinsで0.95%向上させ、ogbl-ddiでHits@20スコアを0.89%引き上げる。

To gain deeper insights into our method, we conduct additional ablation studies and comprehensive analyses.
我々の手法をより深く理解するために、追加のアブレーション研究と包括的な分析を実施する。

## 2 Related Work

Graph Neural Networks Graph neural networks (GNNs) [11, 12, 13] have emerged as a powerful approach for learning graph representations.
グラフニューラルネットワーク　グラフニューラルネットワーク（GNN）[11, 12, 13]は、グラフ表現を学習するための強力なアプローチとして台頭してきた。

Variants of GNNs have been proposed [11, 12, 13], achieving state-of-the-art performance in different graph tasks.
GNNの様々なバリアントが提案されており[11, 12, 13]、異なるグラフタスクで最先端の性能を達成している。

Under the message passing framework [14], graph convolutional network (GCN) adopts mean pooling to aggregate the neighborhood and updates embeddings recursively [11]; GraphSAGE [15] adopts sampling and aggregation schemes to eliminate the inductive bias in degree; and graph attention network (GAT) utilizes the learnable attention weights to adaptively aggregate.
メッセージパッシングフレームワーク[14]において、グラフ畳み込みネットワーク（GCN）は近傍を集約するために平均プーリングを採用し、埋め込みを再帰的に更新する[11]；GraphSAGE [15]は次数における帰納的バイアスを排除するためにサンプリングと集約スキームを採用する；グラフアテンションネットワーク（GAT）は適応的集約のために学習可能なアテンション重みを利用する。

To capture long-range dependencies in disassortative graphs, Geom-GCN devises a geometric aggregation scheme [16] to enhance the convolution, benefiting from a continuous space underlying the graph.
非同類グラフにおける長距離依存関係を捉えるために、Geom-GCNはグラフの基礎をなす連続空間から恩恵を受けながら、畳み込みを強化する幾何学的集約スキーム[16]を考案する。

Lately, Graphormer [17] proposes a novel graph transformer model that utilizes attention mechanisms to capture the structural information.
最近、Graphormer [17]は構造情報を捉えるためにアテンション機構を活用する新規グラフトランスフォーマーモデルを提案している。

Mixture of Experts The concept of Mixture of Experts (MoE) [18] has a long history, tracing its origins back to earlier works [19, 20, 21].
混合エキスパート　混合エキスパート（MoE）[18]の概念は長い歴史を持ち、その起源は初期の研究[19, 20, 21]に遡る。

Recently, spurred by advancements in large language models, sparse MoE [22, 23, 24, 25, 26] has re-gained prominence.
近年、大規模言語モデルの進歩に後押しされて、スパースMoE [22, 23, 24, 25, 26]が再び注目を集めている。

This variant selectively activates only a small subset of experts for each input, significantly enhancing efficiency and enabling the development of colossal models with trillions of parameters.
このバリアントは各入力に対してエキスパートの小さなサブセットのみを選択的に活性化し、効率を大幅に向上させ、兆単位のパラメータを持つ巨大モデルの開発を可能にする。

This breakthrough has revolutionized the learning process, particularly on vast language datasets [25, 27].
この突破口は、特に膨大な言語データセット[25, 27]における学習プロセスに革命をもたらした。

Subsequent studies have further refined the stability and efficiency of sparse MoE [28, 29].
後続の研究はスパースMoEの安定性と効率性をさらに改善した[28, 29]。

The remarkable success of sparse MoE in the realm of language has spurred its adoption in diverse domains, including vision [30, 31], multi-modal [32], and multi-task learning [33, 34, 35].
言語領域におけるスパースMoEの顕著な成功は、視覚[30, 31]、マルチモーダル[32]、マルチタスク学習[33, 34, 35]を含む多様な領域への採用を促した。

MoE for GNNs In the domain of graph analysis, prior research has assembled knowledge from multiple ranges by combining various GNNs with different scopes [36, 37], akin to a fixed-weight Mixture of Experts (MoE).
GNNのためのMoE　グラフ分析の領域において、先行研究は固定重みの混合エキスパート（MoE）に類似した形で、異なるスコープを持つ様々なGNNを組み合わせることによって複数の範囲から知識を集積してきた[36, 37]。

Pioneering efforts [38, 39] have also investigated the application of MoE to address the well-known issue of imbalance and to develop unbiased classification or generalization algorithms.
先駆的な取り組み[38, 39]は、不均衡の周知の問題に対処し、偏りのない分類や汎化アルゴリズムを開発するためのMoEの応用も調査している。

However, none of these approaches harnessed the potential advantages of sparsity and adaptivity.
しかし、これらのアプローチはいずれもスパース性と適応性の潜在的な利点を活かしていない。

Recent work [40] introduced the use of a mixture of experts for molecule property prediction.
最近の研究[40]は分子特性予測のための混合エキスパートの使用を導入した。

They employed a GNN as a feature extractor and applied a mixture of experts, where each expert is a linear classifier, on top of the extracted features for graph classification.
彼らはGNNを特徴抽出器として用い、グラフ分類のために抽出された特徴の上に、各エキスパートが線形分類器である混合エキスパートを適用した。

In contrast, each layer of GMoE constitutes a mixture of experts, with each expert being a GCN/GIN layer featuring different aggregation step sizes.
対照的に、GMoEの各層は混合エキスパートを構成し、各エキスパートは異なる集約ステップサイズを持つGCN/GIN層である。

Another distinction from [40] lies in their utilization of domain-specific knowledge (specifically, molecule topology) for expert routing, whereas our approach is designed to operate on general graphs without relying on domain-specific assumptions.
[40]との別の違いは、彼らがエキスパートルーティングにドメイン固有の知識（具体的には分子トポロジー）を利用していることにあり、一方我々のアプローチはドメイン固有の仮定に依存せずに一般的なグラフ上で動作するよう設計されている。

One more concurrent study by [41] employs MoE to achieve fairness in predictions for GNNs.
もう一つの同時研究[41]はGNNの予測における公平性を達成するためにMoEを採用している。

Our study takes a significant stride forward by introducing sparse MoE to scale graph neural networks in an end-to-end fashion, enabling efficient learning on datasets featuring diverse graph structures.
我々の研究は、スパースMoEを導入してグラフニューラルネットワークをエンドツーエンドでスケールさせ、多様なグラフ構造を特徴とするデータセット上での効率的な学習を可能にすることで、大きな前進を遂げる。

We incorporate experts with varying scopes, allowing the gating function to dynamically select neighbors with the desired range.
我々は様々なスコープを持つエキスパートを組み込み、ゲーティング関数が所望の範囲の近傍を動的に選択することを可能にする。

Adapting Deep Architectures for Training Data Diversity Several prior studies have delved into enhancing the capacity of generic deep neural networks to effectively leverage a wide array of training samples without incurring additional inference costs.
訓練データ多様性への深層アーキテクチャの適応　複数の先行研究が、追加の推論コストを生じさせることなく、汎用的な深層ニューラルネットワークが広範な訓練サンプルを効果的に活用する能力を高めることを探求してきた。

For instance, [42] suggested employing two distinct batch normalization (BN) layers for randomly and adversarially augmented training samples, based on the observation that these two sets of augmented samples originate from different distributions.
例えば、[42]はランダムに拡張された訓練サンプルと敵対的に拡張された訓練サンプルに対して2つの異なるバッチ正規化（BN）層を採用することを提案した。これは、これら2つの拡張サンプルセットが異なる分布から発生するという観察に基づいている。

Building upon this concept, [43] extended it by introducing an auxiliary instance normalization layer to further reduce the heterogeneity of input features before reaching the BN layers.
この概念を基に、[43]はBN層に到達する前に入力特徴の異質性をさらに低減するために補助的なインスタンス正規化層を導入することでこれを拡張した。

More recently, [44] demonstrated that normalizer-free convolutional networks (CNNs) [45, 46] exhibit significantly greater capability in accommodating diverse training sets compared to conventional BN-based CNNs.
より最近では、[44]は正規化なし畳み込みネットワーク（CNN）[45, 46]が従来のBNベースのCNNと比較して、多様な訓練セットを受け入れる能力が著しく高いことを実証した。

However, these prior works have primarily concentrated on devising improved normalization strategies for CNNs, while Graph Neural Networks (GNNs) often do not rely on (batch) normalization as heavily.
しかし、これらの先行研究は主にCNNのための改善された正規化戦略の考案に集中しており、一方グラフニューラルネットワーク（GNN）はしばしば（バッチ）正規化にそれほど依存していない。

## 3 Method

Preliminaries: Graph Neural Networks Taking the classical Graph Convolutional Network (GCN) [11] as an example, the propagation mechanism can be formulated as
予備知識：グラフニューラルネットワーク　古典的なグラフ畳み込みネットワーク（GCN）[11]を例として取り上げると、伝播メカニズムは以下のように定式化できる：

$$h'_i = \sigma\left(\sum_{j \in N_i} \frac{1}{\sqrt{|N_i||N_j|}} h_j W^{(i)}\right), \tag{1}$$
$$h'_i = \sigma\left(\sum_{j \in N_i} \frac{1}{\sqrt{|N_i||N_j|}} h_j W^{(i)}\right), \tag{1}$$

where $W^{(i)} \in \mathbb{R}^{s \times s}$ is a trainable weight and $\sigma$ is an element-wise non-linear activation function.
ここで$W^{(i)} \in \mathbb{R}^{s \times s}$は訓練可能な重みであり、$\sigma$は要素ごとの非線形活性化関数である。

$h_j \in \mathbb{R}^{b \times s}$ denotes the input feature of $j$th node while $h'_i \in \mathbb{R}^{b \times s}$ is its output feature in $i$th node.
$h_j \in \mathbb{R}^{b \times s}$は$j$番目のノードの入力特徴を表し、$h'_i \in \mathbb{R}^{b \times s}$は$i$番目のノードの出力特徴である。

$b$ and $s$ are batch size and hidden feature size, respectively.
$b$と$s$はそれぞれバッチサイズと隠れ特徴サイズである。

$N_i$ denotes the collection of neighbors for $i$th node including self-connection.
$N_i$は自己接続を含む$i$番目のノードの近傍の集合を表す。

The output feature is normalized by $\frac{1}{\sqrt{|N_i||N_j|}}$.
出力特徴は$\frac{1}{\sqrt{|N_i||N_j|}}$によって正規化される。

A canonical GCN layer only aggregates the information from immediately adjacent neighbors (hop-1).
標準的なGCN層は直接隣接する近傍（hop-1）からの情報のみを集約する。

### 3.1 Graph Mixture of Experts

The general framework of GMoE is outlined in Figure 1.
GMoEの一般的なフレームワークを図1に概説する。

The GMoE layer comprises multiple experts, each utilizing either the hop-1 or hop-2 aggregation function.
GMoE層は複数のエキスパートを含み、各エキスパートはhop-1またはhop-2の集約関数のいずれかを利用する。

To determine which experts to use for a given node, a gating function is employed.
与えられたノードに対してどのエキスパートを使用するかを決定するために、ゲーティング関数が採用される。

This allows for similar nodes to be assigned to the same experts when learning with diverse graph structures, thereby enabling each expert to specialize in a particular structure type.
これにより、多様なグラフ構造での学習時に類似したノードが同じエキスパートに割り当てられ、各エキスパートが特定の構造タイプに専門化することが可能になる。

By doing so, the model can more effectively capture diverse graph structures present within the training set.
そうすることで、モデルは訓練セット内に存在する多様なグラフ構造をより効果的に捉えることができる。

The GMoE layer's adaptive selection between the hop-1 and hop-2 experts enables the model to dynamically capture short-range or long-range information aggregation for each node.
GMoE層のhop-1エキスパートとhop-2エキスパート間の適応的選択は、モデルが各ノードに対して短距離または長距離の情報集約を動的に捉えることを可能にする。

Formally, a GMoE layer can be written as:
形式的には、GMoE層は以下のように記述できる：

$$h'_i = \sigma\left(\sum_{o=1}^{m} \sum_{j \in N_i} G(h_i)_o E_o(h_j, e_{ij}, W) + \sum_{o=m}^{n} \sum_{j \in N^2_i} G(h_i)_o E_o(h_j, e_{ij}, W)\right), \tag{2}$$
$$h'_i = \sigma\left(\sum_{o=1}^{m} \sum_{j \in N_i} G(h_i)_o E_o(h_j, e_{ij}, W) + \sum_{o=m}^{n} \sum_{j \in N^2_i} G(h_i)_o E_o(h_j, e_{ij}, W)\right), \tag{2}$$

where $m$ and $n$ denote the hop-1 and total experts number, respectively.
ここで$m$と$n$はそれぞれhop-1エキスパートの数と総エキスパート数を表す。

Hence the number of hop-2 experts is $n - m$.
したがってhop-2エキスパートの数は$n - m$である。

$E_o$ and $e_{ij}$ denote the message function and edge feature between $i$th and $j$th nodes, respectively.
$E_o$と$e_{ij}$はそれぞれメッセージ関数と$i$番目と$j$番目のノード間のエッジ特徴を表す。

It can represent multiple types of message-passing functions such as one employed by GCN [47] or GIN [13].
これはGCN [47]やGIN [13]が採用するような複数のタイプのメッセージパッシング関数を表すことができる。

$G$ is the gating function that generates multiple decision scores with the input of $h_i$ while $G(h_i)_o$ denotes the $o$th item in the output vector of $G$.
$G$は$h_i$を入力として複数の判定スコアを生成するゲーティング関数であり、$G(h_i)_o$は$G$の出力ベクトルの$o$番目の要素を表す。

We employ the noisy top-k gating design for $G$ following [22], which can be formalized with
我々は[22]に従って$G$にノイジートップkゲーティング設計を採用し、以下のように形式化できる：

$$G(h_i) = \text{Softmax}(\text{TopK}(Q(h_i), k)), \tag{3}$$
$$G(h_i) = \text{Softmax}(\text{TopK}(Q(h_i), k)), \tag{3}$$

$$Q(h_i) = h_i W_g + \epsilon \cdot \text{Softplus}(h_i W_n), \tag{4}$$
$$Q(h_i) = h_i W_g + \epsilon \cdot \text{Softplus}(h_i W_n), \tag{4}$$

where $k$ denotes the number of selected experts.
ここで$k$は選択されるエキスパートの数を表す。

$\epsilon \in \mathcal{N}(0, 1)$ denotes standard Gaussian noise.
$\epsilon \in \mathcal{N}(0, 1)$は標準ガウスノイズを表す。

$W_g \in \mathbb{R}^{s \times n}$ and $W_n \in \mathbb{R}^{s \times n}$ are learnable weights that control clean and noisy scores, respectively.
$W_g \in \mathbb{R}^{s \times n}$と$W_n \in \mathbb{R}^{s \times n}$はそれぞれクリーンスコアとノイジースコアを制御する学習可能な重みである。

The proposed GMoE layer can be applied to many GNN backbones such as GIN [13] or GCN [11].
提案するGMoE層はGIN [13]やGCN [11]など多くのGNNバックボーンに適用できる。

In practice, we replace every layer of the backbone with its corresponding GMoE layer.
実際には、バックボーンのすべての層をその対応するGMoE層で置き換える。

For simplicity, we name the resultant network GMoE-GCN or GMoE-GIN (for GCN and GIN, respectively).
簡潔のために、得られたネットワークをGMoE-GCNまたはGMoE-GIN（それぞれGCNとGINに対して）と名付ける。

Additional Loss Functions to Mitigate GMoE Collapse Nonetheless, if this model is trained solely using the expectation-maximization loss, it may succumb to a trivial solution wherein only a single group of experts is consistently selected.
GMoEの崩壊を緩和する追加損失関数　しかしながら、このモデルが期待値最大化損失のみを使用して訓練される場合、エキスパートの単一グループのみが常に選択されるという自明な解に陥る可能性がある。

This arises due to the self-reinforcing nature of the imbalance: the chosen experts can proliferate at a much faster rate than others, leading to their increased frequency of selection.
これは不均衡の自己強化的な性質から生じる：選択されたエキスパートは他のエキスパートよりもはるかに速い速度で増殖し、それらの選択頻度の増加につながる。

To mitigate this, we implement two additional loss functions to prevent such collapse [22].
これを緩和するために、このような崩壊を防ぐ2つの追加損失関数を実装する[22]。

The first one is importance loss:
最初のものは重要度損失である：

$$\text{Importance}(H) = \sum_{h_i \in H, g \in G(h_i)} g, \quad L_{\text{importance}}(H) = \text{CV}(\text{Importance}(H))^2, \tag{5}$$
$$\text{Importance}(H) = \sum_{h_i \in H, g \in G(h_i)} g, \quad L_{\text{importance}}(H) = \text{CV}(\text{Importance}(H))^2, \tag{5}$$

where the importance score $\text{Importance}(H)$ is defined as the sum of each node's gate value $g$ across the whole batch.
ここで重要度スコア$\text{Importance}(H)$はバッチ全体にわたる各ノードのゲート値$g$の総和として定義される。

$\text{CV}$ represents the coefficient of variation.
$\text{CV}$は変動係数を表す。

The importance loss $L_{\text{importance}}(H)$ hence measures the variation of importance scores, enforcing all experts to be "similarly important".
重要度損失$L_{\text{importance}}(H)$は重要度スコアの変動を測定し、すべてのエキスパートが「同様に重要」であることを強制する。

While the importance score enforces equal scoring among the experts, there may still be disparities in the load assigned to different experts.
重要度スコアはエキスパート間での均等なスコアリングを強制するが、異なるエキスパートに割り当てられる負荷に依然として格差が生じる可能性がある。

For instance, one expert could receive a few high scores, while another might be selected by many more nodes yet all with lower scores.
例えば、あるエキスパートは少数の高スコアを受け取り、別のエキスパートはより多くのノードから選択されるが全て低スコアであるという状況が生じ得る。

This situation can potentially lead to memory or efficiency issues, particularly on distributed hardware setups.
この状況は、特に分散ハードウェア設定において、メモリや効率の問題を引き起こす可能性がある。

To address this, we introduce an additional load-balanced loss to encourage a more even selection probability per expert.
これに対処するために、エキスパートごとのより均等な選択確率を促すための追加の負荷均衡損失を導入する。

Specifically, $G(h_i) \neq 0$ if and only if $Q(h_i)_o$ is greater than the $k$-th largest element of $Q(h_i)$ excluding itself.
具体的には、$G(h_i) \neq 0$は$Q(h_i)_o$が自身を除く$Q(h_i)$の$k$番目に大きい要素より大きい場合にのみ成立する。

Consequently, the probability of $G(h_i) \neq 0$ can be formulated as:
その結果、$G(h_i) \neq 0$の確率は以下のように定式化できる：

$$P(h_i, o) = Pr(Q(h_i)_o > \text{kth\_ex}(Q(h_i), k, o)), \tag{6}$$
$$P(h_i, o) = Pr(Q(h_i)_o > \text{kth\_ex}(Q(h_i), k, o)), \tag{6}$$

where $\text{kth\_ex}()$ denotes the $k$-th largest element excluding itself.
ここで$\text{kth\_ex}()$は自身を除く$k$番目に大きい要素を表す。

$P(h_i, o)$ can be simplified as
$P(h_i, o)$は以下のように簡略化できる：

$$P(h_i, o) = \Phi\left(\frac{h_i W_g - \text{kth\_ex}(Q(h_i), k, o)}{\text{Softplus}(h_i W_n)}\right), \tag{7}$$
$$P(h_i, o) = \Phi\left(\frac{h_i W_g - \text{kth\_ex}(Q(h_i), k, o)}{\text{Softplus}(h_i W_n)}\right), \tag{7}$$

where $\Phi$ is the CDF of standard normal distribution.
ここで$\Phi$は標準正規分布のCDFである。

The load is then defined as ($p$ is the node-wise probability in the batch):
負荷は次のように定義される（$p$はバッチ内のノードごとの確率）：

$$L_{\text{load}}(H) = \text{CV}\left(\sum_{h_i \in H, p \in P(h_i, o)} p\right)^2. \tag{8}$$
$$L_{\text{load}}(H) = \text{CV}\left(\sum_{h_i \in H, p \in P(h_i, o)} p\right)^2. \tag{8}$$

The final loss employs both the task-specific loss and two load-balance losses, leading to the overall optimization target ($\lambda$ is a hand-tuned scaling factor):
最終損失はタスク固有の損失と2つの負荷均衡損失の両方を採用し、全体的な最適化目標（$\lambda$は手動チューニングされたスケーリング係数）につながる：

$$L = L_{\text{EM}} + \lambda(L_{\text{load}}(H) + L_{\text{importance}}(H)), \tag{9}$$
$$L = L_{\text{EM}} + \lambda(L_{\text{load}}(H) + L_{\text{importance}}(H)), \tag{9}$$

where $L_{\text{EM}}$ denotes the task-specific MoE expectation-maximizing loss.
ここで$L_{\text{EM}}$はタスク固有のMoE期待値最大化損失を表す。

Pre-training GMoE We further discover that GMoE could be combined with and strengthened by the self-supervised graph pre-training techniques.
GMoEの事前学習　我々はさらに、GMoEが自己教師ありグラフ事前学習技術と組み合わせて強化できることを発見する。

We employ GraphMAE [10] as the self-supervised pre-training technique, defined as
我々は自己教師あり事前学習技術としてGraphMAE [10]を採用し、以下のように定義される：

$$L(H, M) = D(d(f(M \cdot H)), H), \tag{10}$$
$$L(H, M) = D(d(f(M \cdot H)), H), \tag{10}$$

where $f$ and $d$ denote the encoder and the decoder networks, and $M$ represents the mask for the input graph $H$.
ここで$f$と$d$はエンコーダとデコーダネットワークを表し、$M$は入力グラフ$H$のマスクを表す。

$f$ and $d$ collaborative conduct the reconstruction task from the corrupted input, whose quality is measured by the distance metric $D$.
$f$と$d$は協調して破損した入力からの再構成タスクを実行し、その品質は距離メトリック$D$によって測定される。

We later will experimentally demonstrate and compare GMoE performance with and without pre-training.
後に、事前学習あり・なしのGMoE性能を実験的に実証・比較する。

### 3.2 Computational Complexity Analysis

We show that GMoE-GNN brings negligible overhead on the inference cost compared with its GNN counterpart.
GMoE-GNNは対応するGNNと比較して推論コストにほぼオーバーヘッドをもたらさないことを示す。

We measure computational cost using the number of floating point operations (FLOPs).
計算コストは浮動小数点演算数（FLOP）を用いて測定する。

The computation cost of a GMoE layer can be defined as
GMoE層の計算コストは以下のように定義できる：

$$C_{\text{GMoE}} = \sum_{h_i \in H} F\left(\sum_{o=1}^{m} G(h_i)_o \sum_{j \in N_i} E_o(h_j, e_{ij}, W) + \sum_{o=m}^{n} G(h_i)_o \sum_{j \in N^2_i} E_o(h_j, e_{ij}, W)\right), \tag{11}$$
$$C_{\text{GMoE}} = \sum_{h_i \in H} F\left(\sum_{o=1}^{m} G(h_i)_o \sum_{j \in N_i} E_o(h_j, e_{ij}, W) + \sum_{o=m}^{n} G(h_i)_o \sum_{j \in N^2_i} E_o(h_j, e_{ij}, W)\right), \tag{11}$$

where $F$ maps functions to its flops number.
ここで$F$は関数をそのFLOP数にマッピングする。

$C_{\text{GMoE}}$ denotes the computation cost of the whole layer in GMoE-GCN.
$C_{\text{GMoE}}$はGMoE-GCNにおける全層の計算コストを表す。

Given there exists an efficient algorithm that can solve hop-1 and hop-2 functions with matching computational complexity [36], we can further simplify $C_{\text{GMoE}}$ as
hop-1とhop-2関数を同等の計算複雑性で解くことができる効率的なアルゴリズムが存在する[36]ことを踏まえ、$C_{\text{GMoE}}$をさらに以下のように簡略化できる：

$$C_{\text{GMoE}} = \sum_{h_i \in H} \sum_{j \in N_i} C \sum_{o=1}^{n} \mathbf{1}(G(h_i)_o), \tag{12}$$
$$C_{\text{GMoE}} = \sum_{h_i \in H} \sum_{j \in N_i} C \sum_{o=1}^{n} \mathbf{1}(G(h_i)_o), \tag{12}$$

$$C = F[E_o(h_j, e_{ij}, W)], \quad \mathbf{1}(G(h_i)_o) = \begin{cases} 0 & \text{if } G(h_i)_o = 0, \\ 1 & \text{otherwise.} \end{cases} \tag{13}$$
$$C = F[E_o(h_j, e_{ij}, W)], \quad \mathbf{1}(G(h_i)_o) = \begin{cases} 0 & \text{if } G(h_i)_o = 0, \\ 1 & \text{otherwise.} \end{cases} \tag{13}$$

Given $\sum_{o=1}^{n} \mathbf{1}(G(h_i)_o) = k$, $C_{\text{GMoE}}$ can be further simplified to
$\sum_{o=1}^{n} \mathbf{1}(G(h_i)_o) = k$を与えると、$C_{\text{GMoE}}$はさらに以下のように簡略化できる：

$$C_{\text{GMoE}} = k \sum_{h_i \in H} \sum_{j \in N_i} C. \tag{14}$$
$$C_{\text{GMoE}} = k \sum_{h_i \in H} \sum_{j \in N_i} C. \tag{14}$$

Here, $C$ is the computation cost of a single message passing in GMoE-GCN.
ここで$C$はGMoE-GCNにおける単一メッセージパッシングの計算コストである。

Denote the computation cost of a single GCN message passing as $C_0$, and the total computational cost in the whole layer as $C_{\text{GCN}}$.
単一GCNメッセージパッシングの計算コストを$C_0$、全層の総計算コストを$C_{\text{GCN}}$とする。

By setting $C = \frac{C_0}{k}$ in GMoE-GCN, we have $C_{\text{GMoE}} = \sum_{h_i \in H} \sum_{j \in N_i} C_0 = C_{\text{GCN}}$.
GMoE-GCNで$C = \frac{C_0}{k}$と設定することにより、$C_{\text{GMoE}} = \sum_{h_i \in H} \sum_{j \in N_i} C_0 = C_{\text{GCN}}$が得られる。

In traditional GMoE-GCN or GMoE-GIN, the adjustment of $C$ can be easily realized by controlling the hidden feature dimension size $s$.
従来のGMoE-GCNまたはGMoE-GINでは、$C$の調整は隠れ特徴次元サイズ$s$を制御することで容易に実現できる。

For instance, GMoE-GCN and GMoE-GIN with hidden dimension size of $s = \sqrt{s_0 / k}$ can have similar FLOPs with its corresponding GCN and GIN with dimension size of $s_0$.
例えば、隠れ次元サイズが$s = \sqrt{s_0 / k}$のGMoE-GCNとGMoE-GINは、次元サイズ$s_0$の対応するGCNとGINと同様のFLOPを持つことができる。

The computation cost of gating functions in GMoE is meanwhile negligible compared to the cost of selected experts, since both $W_g \in \mathbb{R}^{n \times s}$ and $W_n \in \mathbb{R}^{n \times s}$ is in a much smaller dimension than $W^{(i)} \in \mathbb{R}^{s \times s}$ given $n \ll s$.
GMoEにおけるゲーティング関数の計算コストは、$n \ll s$が与えられると、$W_g \in \mathbb{R}^{n \times s}$と$W_n \in \mathbb{R}^{n \times s}$の両方が$W^{(i)} \in \mathbb{R}^{s \times s}$よりもはるかに小さい次元にあるため、選択されたエキスパートのコストと比較して無視できる。

In practice, on our NVIDIA A6000 GPU, the inference times for 10,000 samples are $30.2 \pm 10.6$ms for GCN-MoE and $36.3 \pm 17.2$ms for GCN.
実際には、NVIDIA A6000 GPU上で、10,000サンプルの推論時間はGCN-MoEで$30.2 \pm 10.6$ms、GCNで$36.3 \pm 17.2$msである。

The small variances in GPU clock times align with their nearly identical theoretical FLOPs.
GPUクロック時間の小さな分散は、それらのほぼ同一の理論的FLOPと一致している。

## 4 Experimental Results

In this section, we first describe the detailed settings in Section 4.1.
本節では、まずセクション4.1で詳細な設定を説明する。

We then show our main results on graph learning in Section 4.2.
次にセクション4.2でグラフ学習に関する主要な結果を示す。

Ablation studies and analysis are provided in Section 4.3.
アブレーション研究と分析はセクション4.3で提供される。

### 4.1 Experimental Settings

Datasets and Evaluation Metrics We conduct experiments on ten graph datasets in the OGB benchmark [48], including graph-level (i.e., ogbg-bbbp, ogbg-hiv, ogbg-moltoxcast, ogbg-moltox21, ogbg-molesol, and ogbg-freesolv), node-level (i.e., ogbn-protein, ogbn-arxiv), and link-level prediction (i.e., ogbl-ddi, ogbl-ppa) tasks.
データセットと評価指標　我々はOGBベンチマーク[48]の10個のグラフデータセットで実験を行い、グラフレベル（すなわちogbg-bbbp、ogbg-hiv、ogbg-moltoxcast、ogbg-moltox21、ogbg-molesol、ogbg-freesolv）、ノードレベル（すなわちogbn-protein、ogbn-arxiv）、リンクレベル予測（すなわちogbl-ddi、ogbl-ppa）タスクを含む。

Following [48], we use ROC-AUC (i.e., area under the receiver operating characteristic curve) as the evaluation metric on ogbg-bbbp, ogbg-hiv, ogbg-moltoxcast, ogbg-moltox21, and ogbn-protein; RMSE (i.e., root mean squared error) on ogbg-molesol, and ogbg-freesolv; classification accuracy (Acc) on ogbn-arxiv; Hits@100 score on ogbl-ppa; Hits@20 score on ogbl-ddi.
[48]に従い、ogbg-bbbp、ogbg-hiv、ogbg-moltoxcast、ogbg-moltox21、ogbn-proteinにはROC-AUC（受信者動作特性曲線下面積）を評価指標として使用する；ogbg-molesol、ogbg-freesolvにはRMSE（二乗平均平方根誤差）；ogbn-arxivには分類精度（Acc）；ogbl-ppaにはHits@100スコア；ogbl-ddiにはHits@20スコアを使用する。

Model Architectures and Training Details We use the GCN [11] and GIN [13] provided by OGB benchmark [48] as the baseline models.
モデルアーキテクチャと訓練詳細　我々はOGBベンチマーク[48]が提供するGCN [11]とGIN [13]をベースラインモデルとして使用する。

All model settings (e.g., number of layers, hidden feature dimensions, etc.) and training hyper-parameters (e.g., learning rates, training epochs, batch size, etc.) are identical as those in [48].
すべてのモデル設定（例：層数、隠れ特徴次元など）と訓練ハイパーパラメータ（例：学習率、訓練エポック数、バッチサイズなど）は[48]のものと同一である。

We show the performance gains brought by their GMoE counterparts: GMoE-GCN and GMoE-GIN.
我々は対応するGMoEモデルであるGMoE-GCNとGMoE-GINがもたらす性能向上を示す。

For GMoE models, as described in Section 3, we select $k$ experts out of a total of $n$ experts for each node, where $m$ out of $n$ experts are hop-1 aggregation functions and the rest $n-m$ are hop-2 aggregation functions.
GMoEモデルについては、セクション3で説明したように、各ノードに対して総計$n$エキスパートの中から$k$エキスパートを選択し、$n$エキスパートのうち$m$がhop-1集約関数であり、残りの$n-m$がhop-2集約関数である。

All three hyper-parameters $n$, $m$, $k$, together with the loss trade-off weight $\lambda$ in Eq. (9), are tuned by grid searching: $n \in \{4, 8\}$, $m \in \{0, n/2, n\}$, $k \in \{1, 2, 4\}$, and $\lambda \in \{0.1, 1\}$.
式(9)の損失トレードオフ重み$\lambda$とともに、3つのハイパーパラメータ$n$、$m$、$k$はすべてグリッドサーチによってチューニングされる：$n \in \{4, 8\}$、$m \in \{0, n/2, n\}$、$k \in \{1, 2, 4\}$、$\lambda \in \{0.1, 1\}$。

The hidden feature dimension would be adjusted with $k$ (Section 3.2) to ensure the same flops for all comparisons.
隠れ特徴次元はすべての比較で同じFLOPを確保するために$k$（セクション3.2）に合わせて調整される。

The hyper-parameter values achieving the best performance on validation sets are selected to report results on test sets, following the routine in [48].
[48]の手順に従い、検証セットで最良の性能を達成するハイパーパラメータ値を選択し、テストセットの結果を報告する。

All other training hyper-parameters on GMoE (e.g., batch size, learning rate, training epochs) are kept the same as those used on the single-expert baselines.
GMoEの他のすべての訓練ハイパーパラメータ（例：バッチサイズ、学習率、訓練エポック数）は単一エキスパートベースラインで使用されるものと同じに保たれる。

All experiments are run for ten times with different random seeds, and we report the mean and deviation of the results following [48].
すべての実験は異なるランダムシードで10回実行され、[48]に従い結果の平均と偏差を報告する。

Pre-training Settings Following the transfer learning setting of [49, 6, 8, 10], we pre-train the models on a subset of the ZINC15 dataset [50] containing 2 million unlabeled molecule graphs.
事前学習設定　[49, 6, 8, 10]の転移学習設定に従い、200万個のラベルなし分子グラフを含むZINC15データセット[50]のサブセットでモデルを事前学習する。

For training hyperparameters, we employ a batch size of 1024 to accelerate the training on the large pre-train dataset for both baselines and the proposed method.
訓練ハイパーパラメータについては、ベースラインと提案手法の両方について、大規模事前学習データセット上での訓練を加速するためにバッチサイズ1024を採用する。

We follow [10] employing GIN [13] as the backbone, 0.001 as the learning rate, adam as the optimizer, 0 as the weight decay, 100 as the training epochs number, and 0.25 as the masking ratio.
[10]に従い、バックボーンとしてGIN [13]、学習率として0.001、オプティマイザとしてadam、重み減衰として0、訓練エポック数として100、マスキング比として0.25を採用する。

### 4.2 Main Results

Our evaluation primarily centers around comparing GMoE-GCN with the baseline single-expert GCN using six graph property prediction datasets.
我々の評価は主に、6つのグラフ特性予測データセットを用いてGMoE-GCNとベースライン単一エキスパートGCNを比較することを中心としている。

These datasets encompass four graph classification tasks and two regression tasks within a supervised learning framework.
これらのデータセットは教師あり学習フレームワーク内の4つのグラフ分類タスクと2つの回帰タスクを含む。

In all cases, models are trained from scratch, utilizing only the labeled samples in the training set.
すべての場合において、モデルは訓練セットのラベル付きサンプルのみを使用してスクラッチから訓練される。

The classification and regression results are outlined in Table 1 and 2, respectively.
分類と回帰の結果はそれぞれ表1と表2に概説されている。

It is worth noting that GMoE-GCN consistently outperforms the baseline across all six datasets.
GMoE-GCNが6つのデータセット全体にわたってベースラインを一貫して上回ることは注目に値する。

Notably, there are substantial improvements in ROC-AUC, with increases of 1.81% on the molhiv dataset and 1.41% on the molbbp dataset.
特筆すべきことに、molhivデータセットで1.81%、molbbpデータセットで1.41%の増加とともに、ROC-AUCに実質的な改善がある。

While these enhancements may seem modest, they represent significant progress.
これらの改善は控えめに見えるかもしれないが、重要な進歩を表している。

Additionally, lifts of 1.40% on ogbg-moltox21, 1.43% on ogbg-molbbbq, and 1.18% on ogbg-moltoxcast have been observed.
さらに、ogbg-moltox21で1.40%、ogbg-molbbbqで1.43%、ogbg-moltoxcastで1.18%の向上が観察されている。

The uniformity of these improvements across diverse tasks and datasets underscores the reliability and effectiveness of GMoE-GCN.
多様なタスクとデータセットにわたるこれらの改善の均一性は、GMoE-GCNの信頼性と有効性を強調している。

Leveraging large-scale pretraining on auxiliary unlabeled data has notably enhanced the generalization capabilities of GNNs even further.
補助的なラベルなしデータに対する大規模事前学習を活用することで、GNNの汎化能力がさらに顕著に強化された。

Expanding on this, our GMoE consistently improves performance when integrated with large-scale pretraining methods.
これを発展させ、我々のGMoEは大規模事前学習手法と統合したときに一貫して性能を向上させる。

Following the methodology outlined in [10], we employ GIN [13] as the baseline model for comparison with GMoE-GIN.
[10]に概説された手法に従い、GMoE-GINとの比較のためにGIN [13]をベースラインモデルとして採用する。

As illustrated in Table 3, GMoE-GIN outperforms GIN on 3 out of 4 datasets, enhancing the average performance by 0.54%, even without pretraining.
表3に示すように、GMoE-GINは事前学習なしでも4つのデータセットのうち3つでGINを上回り、平均性能を0.54%向上させる。

This underscores the versatility of GMoE in enhancing various model architectures.
これはGMoEが様々なモデルアーキテクチャを強化する汎用性を強調している。

When coupled with the pretraining, GMoE-GIN further widens the performance gap with the GIN baseline, achieving a slightly more pronounced improvement margin of 0.6%.
事前学習と組み合わせると、GMoE-GINはGINベースラインとの性能差をさらに広げ、わずかに顕著な0.6%の改善マージンを達成する。

Additionally, GMoE showcases its potential in node and link prediction tasks.
さらに、GMoEはノードおよびリンク予測タスクにおけるその潜在能力を示している。

Experiments conducted on ogbn-protein and ogbn-arxiv for node prediction, as well as ogbl-ddi and ogbl-ppa for link prediction, further validate this observation.
ノード予測のためのogbn-proteinとogbn-arxiv、リンク予測のためのogbl-ddiとogbl-ppaで実施された実験は、この観察をさらに検証する。

The results, detailed in Table 4 and Table 5, demonstrate GMoE-GCN's superiority over the single-expert GCN.
表4と表5に詳述された結果は、単一エキスパートGCNに対するGMoE-GCNの優位性を実証している。

Notably, it enhances performance metrics like ROC-AUC by 0.95% and Hits@20 by 0.89% on the ogbn-protein and ogbl-ddi datasets.
特筆すべきことに、ogbn-proteinとogbl-ddiデータセットにおいてROC-AUCを0.95%、Hits@20を0.89%向上させる。

### 4.3 Ablation Study and Analysis

Observation 1: Larger graphs prefer larger hop sizes We conducted an ablation study on two prominent molecule datasets, namely ogbg-molhiv and ogbg-molfreesolv, which exhibit the largest and smallest average graph sizes, respectively, among all molecular datasets in the OGB benchmark.
観察1：大きなグラフはより大きいホップサイズを好む　OGBベンチマークのすべての分子データセットの中でそれぞれ最大と最小の平均グラフサイズを示す、ogbg-molhivとogbg-molfreesolvという2つの著名な分子データセットに対してアブレーション研究を実施した。

As illustrated in the third column of Table 6, the average size of molecular graphs in ogbg-molhiv is approximately three times greater than that of the ogbg-molfreesolv dataset.
表6の第3列に示すように、ogbg-molhivの分子グラフの平均サイズはogbg-molfreesolvデータセットの約3倍である。

Remarkably, on ogbg-molfreesolv, if all experts utilize hop-2 aggregation functions (i.e., when $m = 0$), the performance substantially lags behind the scenario where all experts employ hop-1 aggregations (i.e., when $m = n$).
注目すべきことに、ogbg-molfreesolvにおいて、すべてのエキスパートがhop-2集約関数を利用する場合（すなわち$m = 0$のとき）、すべてのエキスパートがhop-1集約を採用する場合（すなわち$m = n$のとき）のシナリオに比べて性能が著しく劣る。

In contrast, on ogbg-molhiv, characterized by significantly larger graphs, leveraging all hop-2 experts (i.e., when $m = 0$) yields superior performance compared to employing all hop-1 experts (i.e., when $m = n$).
対照的に、著しく大きなグラフを特徴とするogbg-molhivでは、すべてのhop-2エキスパートを活用すること（すなわち$m = 0$のとき）は、すべてのhop-1エキスパートを採用すること（すなわち$m = n$のとき）と比較して優れた性能をもたらす。

This observation suggests that larger graphs exhibit a preference for aggregation experts with greater hop sizes.
この観察は、大きなグラフがより大きいホップサイズを持つ集約エキスパートへの選好を示すことを示唆している。

This alignment with intuition stems from the notion that larger molecular graphs may necessitate more extensive long-range aggregation information in contrast to their smaller counterparts.
この直感との一致は、大きな分子グラフは小さな分子グラフと比較して、より広範な長距離集約情報を必要とする可能性があるという概念から生じる。

Observation 2: Sparse expert selection helps not only efficiency, but also generalization As depicted in Table 6, the optimal performance on both datasets is attained with sparse MoEs (i.e., when $k < n$), as opposed to a full dense model (i.e., when $k = n$).
観察2：スパースなエキスパート選択は効率だけでなく汎化にも役立つ　表6に示すように、両データセットにおける最適な性能は、完全密なモデル（すなわち$k = n$のとき）とは対照的に、スパースMoE（すなわち$k < n$のとき）で達成される。

This seemingly counter-intuitive finding shows another benefit of sparsity besides significantly reducing inference computational cost: that is, sparsity is also promising to improve model *generalization*, particularly when dealing with multi-domain data, as it allows a group of experts to learn collaboratively and generalize to unseen domains compositionally.
この一見直感に反する発見は、推論計算コストを大幅に削減する以外のスパース性のもう一つの利点を示している：すなわち、スパース性はまたモデルの*汎化*を改善する可能性があり、特にマルチドメインデータを扱う際には、エキスパートのグループが協調的に学習し、見知らぬドメインへ合成的に汎化することを可能にする。

Our finding also echoes prior work, e.g., [51], which empirically shows sparse MoEs are strong domain generalizable learners.
我々の発見はまた、スパースMoEが強いドメイン汎化可能学習器であることを実証的に示す[51]などの先行研究と共鳴している。

Observation 3: GMoE demonstrates performance gains, though converging over more epochs We compared the convergence curves of GMoE-GCN and the single-expert GCN, illustrated in Figure 2.
観察3：GMoEはより多くのエポックをかけて収束するものの性能向上を示す　GMoE-GCNと単一エキスパートGCNの収束曲線を比較し、図2に示した。

Specifically, we plotted the validation and test ROC-AUC at different epochs while training on the protein dataset.
具体的には、proteinデータセットで訓練しながら、異なるエポックでの検証とテストのROC-AUCをプロットした。

As observed, the performance of GMoE-GCN reaches a plateau later than that of GCN.
観察されるように、GMoE-GCNの性能はGCNよりも遅くプラトーに達する。

However, GMoE-GCN eventually achieves a substantial performance improvement after a sufficient number of training epochs.
しかし、GMoE-GCNは十分な数の訓練エポックの後、最終的に実質的な性能向上を達成する。

We provide an explanation for this phenomenon below.
以下にこの現象の説明を提供する。

In the initial stages of training, each expert in GMoE has been updated for $k$ times fewer iterations compared to the single expert GNN.
訓練の初期段階では、GMoEの各エキスパートは単一エキスパートGNNと比較して$k$倍少ないイテレーションで更新されている。

Consequently, all experts in GMoE are relatively weak, leading to GMoE's inferior performance compared to GCN during this early phase.
その結果、GMoEのすべてのエキスパートは比較的弱く、この初期段階でGCNと比較してGMoEの性能が劣ることにつながる。

However, after GMoE has undergone enough epochs of training, all experts have received ample updates, enabling them to effectively model their respective subgroups of data.
しかし、GMoEが十分なエポックの訓練を経た後、すべてのエキスパートは十分な更新を受け、それぞれのデータのサブグループを効果的にモデル化できるようになる。

As a result, the performance of GMoE surpasses that of the single-expert GCN.
その結果、GMoEの性能は単一エキスパートGCNを上回る。

Observation 4: Load balancing is essential We conducted an investigation into the scaling factor for the load balancing loss, denoted by $\lambda$.
観察4：負荷均衡は不可欠である　$\lambda$で表される負荷均衡損失のスケーリング係数についての調査を実施した。

As shown in Table 7, utilizing $\lambda = 0.1$ resulted in significantly improved performance, exceeding 2.58% in terms of ROC-AUC compared to when $\lambda = 0$.
表7に示すように、$\lambda = 0.1$を利用することで、$\lambda = 0$の場合と比較してROC-AUCの観点で2.58%を超える大幅な性能向上がもたらされた。

This underscores the crucial role of implementing load-balancing losses.
これは負荷均衡損失の実装の重要な役割を強調している。

Conversely, the choice of $\lambda$ exhibits less sensitivity; opting for $\lambda = 1$ would yield a similar performance of 75.27%.
逆に、$\lambda$の選択はより低い感度を示す；$\lambda = 1$を選択すると75.27%という同様の性能が得られる。

Observation 5: GMoE improves other state-of-the-art GNN methods Finally, we explore whether our proposed GMoE can yield an improvement in the performance of other state-of-the-art models listed on the OGB leaderboard.
観察5：GMoEは他の最先端GNN手法を改善する　最後に、提案するGMoEがOGBリーダーボードに掲載されている他の最先端モデルの性能向上をもたらすことができるかどうかを探索する。

We selected Neural FingerPrints [52] as our baseline.
Neural FingerPrints [52]をベースラインとして選択した。

As of the time of this submission, Neural FingerPrints holds the fifth position in the ogbg-molhiv benchmark.
本提出時点で、Neural FingerPrintsはogbg-molhivベンチマークで第5位を占めている。

It is noteworthy that this methodology has gained significant acclaim, as it serves as the foundation for the top four current methods [53, 54, 55, 56].
この方法論は現在のトップ4の手法[53, 54, 55, 56]の基盤として機能しているため、大きな評価を得ていることは注目に値する。

After integrating the GMoE framework into the Neural FingerPrints architecture, we achieved an accuracy of 82.72% ± 0.53%, while maintaining the same computational resource requirements.
GMoEフレームワークをNeural FingerPrintsアーキテクチャに統合した後、同じ計算リソース要件を維持しながら82.72% ± 0.53%の精度を達成した。

This performance outperforms Neural FingerPrints by a margin of 0.4%, underlining the broad and consistent adaptability of the GMoE framework.
この性能はNeural FingerPrintsを0.4%のマージンで上回り、GMoEフレームワークの幅広く一貫した適応性を強調している。

## 5 Conclusion

In this work, we propose the Graph Mixture of Experts (GMoE) model, aiming at addressing the challenges posed by diverse graph structures.
本研究では、多様なグラフ構造がもたらす課題に対処することを目的として、グラフ混合エキスパート（GMoE）モデルを提案する。

By incorporating multiple experts at each layer, each equipped with its own trainable parameters, GMoE introduces a novel approach to modeling graph data.
各層に複数のエキスパートを組み込み、各エキスパートが独自の訓練可能なパラメータを備えることで、GMoEはグラフデータをモデル化するための新しいアプローチを導入する。

Through intelligent expert selection during training, GMoE ensures nodes with similar neighborhood information are directed towards the same aggregation experts, promoting specialization within each expert for specific subsets of training samples.
訓練中の知的なエキスパート選択を通じて、GMoEは類似した近傍情報を持つノードが同じ集約エキスパートに向けられることを保証し、特定の訓練サンプルのサブセットに対する各エキスパート内での専門化を促進する。

Additionally, the inclusion of aggregation experts with distinct inductive biases further enhances GMoE's adaptability to different graph structures.
さらに、異なる帰納的バイアスを持つ集約エキスパートを含めることで、GMoEの異なるグラフ構造への適応性がさらに強化される。

Our extensive experimentation and analysis demonstrate GMoE's notable accuracy-efficiency trade-off improvements over baselines.
我々の広範な実験と分析は、ベースラインに対するGMoEの顕著な精度-効率トレードオフの改善を実証している。

These advancements hold great promise for real-world applications, particularly in scenarios requiring the efficient processing of vast amounts of candidate samples.
これらの進歩は現実世界の応用、特に膨大な量の候補サンプルの効率的な処理を必要とするシナリオにおいて大きな可能性を秘めている。

Limitations: As an empirical solution to enhance the capability of GNNs to encode diverse graph data, we primarily assess the effectiveness of the proposed method using empirical experimental results.
限界：多様なグラフデータを符号化するGNNの能力を高めるための経験的解決策として、我々は主に経験的実験結果を用いて提案手法の有効性を評価している。

It is important to note that our initial comparison primarily focused on fundamental backbones such as GCN/GIN to elucidate our concept.
我々の初期比較が概念を明確にするためにGCN/GINなどの基本的なバックボーンに主に焦点を当てたことに注意することが重要である。

Recognizing the crucial importance of a comprehensive evaluation, we are actively broadening our comparative scope to include state-of-the-art models derived from GCN and other MoE models.
包括的な評価の重要性を認識し、我々はGCNおよび他のMoEモデルから派生した最先端モデルを含むように比較範囲を積極的に拡大している。

Future iterations will thus incorporate a more exhaustive evaluation.
将来のイテレーションではより徹底的な評価が組み込まれる。

Moreover, given the prevalence of GCN in semi-supervised learning, there is potential in exploring the benefits of our proposed approach in such tasks – an avenue we are eager to explore further.
さらに、半教師あり学習におけるGCNの普及を考えると、そのようなタスクにおける提案アプローチの利点を探索する可能性がある—これはさらに探索することに熱心な研究方向である。

Another open question stemming from this work is whether we can apply GMoE on GNNs with heterogeneous aggregation mechanisms, such as GAT and GraphTransformer, which may potentially further improve the performance on diverse graph data.
本研究から生じる別の未解決の問いは、GATやGraphTransformerなどの異種集約メカニズムを持つGNNにGMoEを適用できるかどうかであり、これは多様なグラフデータ上の性能をさらに向上させる可能性がある。

## Acknowledgement

The work is sponsored by a Cisco Research Grant (UTAUS-FA00002062).
本研究はシスコリサーチグラント（UTAUS-FA00002062）による支援を受けている。

## References

[1] Shiwen Wu, Fei Sun, Wentao Zhang, Xu Xie, and Bin Cui. Graph neural networks in recommender systems: A survey. ACM Computing Surveys, 55(5):1–37, 2022.
[1] Shiwen Wu, Fei Sun, Wentao Zhang, Xu Xie, and Bin Cui. Graph neural networks in recommender systems: A survey. ACM Computing Surveys, 55(5):1–37, 2022.

[2] Weiwei Jiang and Jiayun Luo. Graph neural network for traffic forecasting: A survey. Expert Systems with Applications, page 117921, 2022.
[2] Weiwei Jiang and Jiayun Luo. Graph neural network for traffic forecasting: A survey. Expert Systems with Applications, page 117921, 2022.

[3] Oliver Wieder, Stefan Kohlbacher, Mélaine Kuenemann, Arthur Garon, Pierre Ducrot, Thomas Seidel, and Thierry Langer. A compact review of molecular property prediction with graph neural networks. Drug Discovery Today: Technologies, 37:1–12, 2020.
[3] Oliver Wieder, Stefan Kohlbacher, Mélaine Kuenemann, Arthur Garon, Pierre Ducrot, Thomas Seidel, and Thierry Langer. A compact review of molecular property prediction with graph neural networks. Drug Discovery Today: Technologies, 37:1–12, 2020.

[4] Xiaotian Han, Zhimeng Jiang, Ninghao Liu, and Xia Hu. G-Mixup: Graph data augmentation for graph classification. arXiv preprint arXiv:2202.07179, 2022.
[4] Xiaotian Han, Zhimeng Jiang, Ninghao Liu, and Xia Hu. G-Mixup: Graph data augmentation for graph classification. arXiv preprint arXiv:2202.07179, 2022.

[5] Songtao Liu, Rex Ying, Hanze Dong, Lanqing Li, Tingyang Xu, Yu Rong, Peilin Zhao, Junzhou Huang, and Dinghao Wu. Local augmentation for graph neural networks. In ICML, 2022.
[5] Songtao Liu, Rex Ying, Hanze Dong, Lanqing Li, Tingyang Xu, Yu Rong, Peilin Zhao, Junzhou Huang, and Dinghao Wu. Local augmentation for graph neural networks. In ICML, 2022.

[6] Yuning You, Tianlong Chen, Yongduo Sui, Ting Chen, Zhangyang Wang, and Yang Shen. Graph contrastive learning with augmentations. Advances in Neural Information Processing Systems, 33:5812–5823, 2020.
[6] Yuning You, Tianlong Chen, Yongduo Sui, Ting Chen, Zhangyang Wang, and Yang Shen. Graph contrastive learning with augmentations. Advances in Neural Information Processing Systems, 33:5812–5823, 2020.

[7] Yuning You, Tianlong Chen, Zhangyang Wang, and Yang Shen. When does self-supervision help graph convolutional networks? In International Conference on Machine Learning, pages 10871–10880, 2020.
[7] Yuning You, Tianlong Chen, Zhangyang Wang, and Yang Shen. When does self-supervision help graph convolutional networks? In International Conference on Machine Learning, pages 10871–10880, 2020.

[8] Yuning You, Tianlong Chen, Yang Shen, and Zhangyang Wang. Graph contrastive learning automated. In International Conference on Machine Learning, pages 12121–12132, 2021.
[8] Yuning You, Tianlong Chen, Yang Shen, and Zhangyang Wang. Graph contrastive learning automated. In International Conference on Machine Learning, pages 12121–12132, 2021.

[9] Yuning You, Tianlong Chen, Zhangyang Wang, and Yang Shen. Bringing your own view: Graph contrastive learning without prefabricated data augmentations. In Proceedings of the Fifteenth ACM International Conference on Web Search and Data Mining, pages 1300–1309, 2022.
[9] Yuning You, Tianlong Chen, Zhangyang Wang, and Yang Shen. Bringing your own view: Graph contrastive learning without prefabricated data augmentations. In Proceedings of the Fifteenth ACM International Conference on Web Search and Data Mining, pages 1300–1309, 2022.

[10] Zhenyu Hou, Xiao Liu, Yuxiao Dong, Chunjie Wang, Jie Tang, et al. GraphMAE: Self-supervised masked graph autoencoders. arXiv preprint arXiv:2205.10803, 2022.
[10] Zhenyu Hou, Xiao Liu, Yuxiao Dong, Chunjie Wang, Jie Tang, et al. GraphMAE: Self-supervised masked graph autoencoders. arXiv preprint arXiv:2205.10803, 2022.

[11] Thomas N Kipf and Max Welling. Semi-supervised classification with graph convolutional networks. arXiv preprint arXiv:1609.02907, 2016.
[11] Thomas N Kipf and Max Welling. Semi-supervised classification with graph convolutional networks. arXiv preprint arXiv:1609.02907, 2016.

[12] Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Lio, and Yoshua Bengio. Graph attention networks. arXiv preprint arXiv:1710.10903, 2017.
[12] Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Lio, and Yoshua Bengio. Graph attention networks. arXiv preprint arXiv:1710.10903, 2017.

[13] Keyulu Xu, Weihua Hu, Jure Leskovec, and Stefanie Jegelka. How powerful are graph neural networks? arXiv preprint arXiv:1810.00826, 2018.
[13] Keyulu Xu, Weihua Hu, Jure Leskovec, and Stefanie Jegelka. How powerful are graph neural networks? arXiv preprint arXiv:1810.00826, 2018.

[14] Justin Gilmer, Samuel S Schoenholz, Patrick F Riley, Oriol Vinyals, and George E Dahl. Neural message passing for quantum chemistry. In ICML, pages 1263–1272, 2017.
[14] Justin Gilmer, Samuel S Schoenholz, Patrick F Riley, Oriol Vinyals, and George E Dahl. Neural message passing for quantum chemistry. In ICML, pages 1263–1272, 2017.

[15] Will Hamilton, Zhitao Ying, and Jure Leskovec. Inductive representation learning on large graphs. In Advances in neural information processing systems, 2017.
[15] Will Hamilton, Zhitao Ying, and Jure Leskovec. Inductive representation learning on large graphs. In Advances in neural information processing systems, 2017.

[16] Hongbin Pei, Bingzhe Wei, Kevin Chen-Chuan Chang, Yu Lei, and Bo Yang. Geom-GCN: Geometric graph convolutional networks. arXiv preprint arXiv:2002.05287, 2020.
[16] Hongbin Pei, Bingzhe Wei, Kevin Chen-Chuan Chang, Yu Lei, and Bo Yang. Geom-GCN: Geometric graph convolutional networks. arXiv preprint arXiv:2002.05287, 2020.

[17] Chengxuan Ying, Tianle Cai, Shengjie Luo, Shuxin Zheng, Guolin Ke, Di He, Yanming Shen, and Tie-Yan Liu. Do transformers really perform badly for graph representation? In NeurIPS, 2021.
[17] Chengxuan Ying, Tianle Cai, Shengjie Luo, Shuxin Zheng, Guolin Ke, Di He, Yanming Shen, and Tie-Yan Liu. Do transformers really perform badly for graph representation? In NeurIPS, 2021.

[18] Robert A Jacobs, Michael I Jordan, Steven J Nowlan, and Geoffrey E Hinton. Adaptive mixtures of local experts. Neural computation, 3(1):79–87, 1991.
[18] Robert A Jacobs, Michael I Jordan, Steven J Nowlan, and Geoffrey E Hinton. Adaptive mixtures of local experts. Neural computation, 3(1):79–87, 1991.

[19] Michael I Jordan and Robert A Jacobs. Hierarchical mixtures of experts and the em algorithm. Neural computation, 6(2):181–214, 1994.
[19] Michael I Jordan and Robert A Jacobs. Hierarchical mixtures of experts and the em algorithm. Neural computation, 6(2):181–214, 1994.

[20] Ke Chen, Lei Xu, and Huisheng Chi. Improved learning algorithms for mixture of experts in multiclass classification. Neural networks, 12(9):1229–1252, 1999.
[20] Ke Chen, Lei Xu, and Huisheng Chi. Improved learning algorithms for mixture of experts in multiclass classification. Neural networks, 12(9):1229–1252, 1999.

[21] Seniha Esen Yuksel, Joseph N Wilson, and Paul D Gader. Twenty years of mixture of experts. IEEE Transactions on Neural Networks and Learning Systems, 23(8):1177–1193, 2012.
[21] Seniha Esen Yuksel, Joseph N Wilson, and Paul D Gader. Twenty years of mixture of experts. IEEE Transactions on Neural Networks and Learning Systems, 23(8):1177–1193, 2012.

[22] Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. arXiv preprint arXiv:1701.06538, 2017.
[22] Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. arXiv preprint arXiv:1701.06538, 2017.

[23] Dmitry Lepikhin, HyoukJoong Lee, Yuanzhong Xu, Dehao Chen, Orhan Firat, Yanping Huang, Maxim Krikun, Noam Shazeer, and Zhifeng Chen. Gshard: Scaling giant models with conditional computation and automatic sharding. arXiv preprint arXiv:2006.16668, 2020.
[23] Dmitry Lepikhin, HyoukJoong Lee, Yuanzhong Xu, Dehao Chen, Orhan Firat, Yanping Huang, Maxim Krikun, Noam Shazeer, and Zhifeng Chen. Gshard: Scaling giant models with conditional computation and automatic sharding. arXiv preprint arXiv:2006.16668, 2020.

[24] William Fedus, Barret Zoph, and Noam Shazeer. Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity, 2021.
[24] William Fedus, Barret Zoph, and Noam Shazeer. Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity, 2021.

[25] Aidan Clark, Diego de Las Casas, Aurelia Guy, Arthur Mensch, Michela Paganini, Jordan Hoffmann, Bogdan Damoc, Blake Hechtman, Trevor Cai, Sebastian Borgeaud, et al. Unified scaling laws for routed language models. In ICML, pages 4057–4086, 2022.
[25] Aidan Clark, Diego de Las Casas, Aurelia Guy, Arthur Mensch, Michela Paganini, Jordan Hoffmann, Bogdan Damoc, Blake Hechtman, Trevor Cai, Sebastian Borgeaud, et al. Unified scaling laws for routed language models. In ICML, pages 4057–4086, 2022.

[26] Stephen Roller, Sainbayar Sukhbaatar, Jason Weston, et al. Hash layers for large sparse models. In Advances in Neural Information Processing Systems, pages 17555–17566, 2021.
[26] Stephen Roller, Sainbayar Sukhbaatar, Jason Weston, et al. Hash layers for large sparse models. In Advances in Neural Information Processing Systems, pages 17555–17566, 2021.

[27] Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. Training compute-optimal large language models. arXiv preprint arXiv:2203.15556, 2022.
[27] Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. Training compute-optimal large language models. arXiv preprint arXiv:2203.15556, 2022.

[28] Mike Lewis, Shruti Bhosale, Tim Dettmers, Naman Goyal, and Luke Zettlemoyer. Base layers: Simplifying training of large, sparse models. In International Conference on Machine Learning, pages 6265–6274, 2021.
[28] Mike Lewis, Shruti Bhosale, Tim Dettmers, Naman Goyal, and Luke Zettlemoyer. Base layers: Simplifying training of large, sparse models. In International Conference on Machine Learning, pages 6265–6274, 2021.

[29] Barret Zoph, Irwan Bello, Sameer Kumar, Nan Du, Yanping Huang, Jeff Dean, Noam Shazeer, and William Fedus. Designing effective sparse expert models. arXiv preprint arXiv:2202.08906, 2022.
[29] Barret Zoph, Irwan Bello, Sameer Kumar, Nan Du, Yanping Huang, Jeff Dean, Noam Shazeer, and William Fedus. Designing effective sparse expert models. arXiv preprint arXiv:2202.08906, 2022.

[30] Carlos Riquelme, Joan Puigcerver, Basil Mustafa, Maxim Neumann, Rodolphe Jenatton, André Susano Pinto, Daniel Keysers, and Neil Houlsby. Scaling vision with sparse mixture of experts. In Advances in Neural Information Processing Systems, volume 34, pages 8583–8595, 2021.
[30] Carlos Riquelme, Joan Puigcerver, Basil Mustafa, Maxim Neumann, Rodolphe Jenatton, André Susano Pinto, Daniel Keysers, and Neil Houlsby. Scaling vision with sparse mixture of experts. In Advances in Neural Information Processing Systems, volume 34, pages 8583–8595, 2021.

[31] Xin Wang, Fisher Yu, Lisa Dunlap, Yi-An Ma, Ruth Wang, Azalia Mirhoseini, Trevor Darrell, and Joseph E Gonzalez. Deep mixture of experts via shallow embedding. In Uncertainty in Artificial Intelligence, pages 552–562, 2020.
[31] Xin Wang, Fisher Yu, Lisa Dunlap, Yi-An Ma, Ruth Wang, Azalia Mirhoseini, Trevor Darrell, and Joseph E Gonzalez. Deep mixture of experts via shallow embedding. In Uncertainty in Artificial Intelligence, pages 552–562, 2020.

[32] Basil Mustafa, Carlos Riquelme, Joan Puigcerver, Rodolphe Jenatton, and Neil Houlsby. Multimodal contrastive learning with limoe: the language-image mixture of experts. arXiv preprint arXiv:2206.02770, 2022.
[32] Basil Mustafa, Carlos Riquelme, Joan Puigcerver, Rodolphe Jenatton, and Neil Houlsby. Multimodal contrastive learning with limoe: the language-image mixture of experts. arXiv preprint arXiv:2206.02770, 2022.

[33] Jiaqi Ma, Zhe Zhao, Xinyang Yi, Jilin Chen, Lichan Hong, and Ed H Chi. Modeling task relationships in multi-task learning with multi-gate mixture-of-experts. In ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, pages 1930–1939, 2018.
[33] Jiaqi Ma, Zhe Zhao, Xinyang Yi, Jilin Chen, Lichan Hong, and Ed H Chi. Modeling task relationships in multi-task learning with multi-gate mixture-of-experts. In ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, pages 1930–1939, 2018.

[34] Jinguo Zhu, Xizhou Zhu, Wenhai Wang, Xiaohua Wang, Hongsheng Li, Xiaogang Wang, and Jifeng Dai. Uni-Perceiver-MoE: Learning sparse generalist models with conditional moes. arXiv preprint arXiv:2206.04674, 2022.
[34] Jinguo Zhu, Xizhou Zhu, Wenhai Wang, Xiaohua Wang, Hongsheng Li, Xiaogang Wang, and Jifeng Dai. Uni-Perceiver-MoE: Learning sparse generalist models with conditional moes. arXiv preprint arXiv:2206.04674, 2022.

[35] Hanxue Liang, Zhiwen Fan, Rishov Sarkar, Ziyu Jiang, Tianlong Chen, Kai Zou, Yu Cheng, Cong Hao, Zhangyang Wang, et al. M3vit: Mixture-of-experts vision transformer for efficient multi-task learning with model-accelerator co-design. In Advances in Neural Information Processing Systems, 2022.
[35] Hanxue Liang, Zhiwen Fan, Rishov Sarkar, Ziyu Jiang, Tianlong Chen, Kai Zou, Yu Cheng, Cong Hao, Zhangyang Wang, et al. M3vit: Mixture-of-experts vision transformer for efficient multi-task learning with model-accelerator co-design. In Advances in Neural Information Processing Systems, 2022.

[36] Sami Abu-El-Haija, Bryan Perozzi, Amol Kapoor, Nazanin Alipourfard, Kristina Lerman, Hrayr Harutyunyan, Greg Ver Steeg, and Aram Galstyan. MixHop: Higher-order graph convolutional architectures via sparsified neighborhood mixing. In ICML, pages 21–29, 2019.
[36] Sami Abu-El-Haija, Bryan Perozzi, Amol Kapoor, Nazanin Alipourfard, Kristina Lerman, Hrayr Harutyunyan, Greg Ver Steeg, and Aram Galstyan. MixHop: Higher-order graph convolutional architectures via sparsified neighborhood mixing. In ICML, pages 21–29, 2019.

[37] Sami Abu-El-Haija, Amol Kapoor, Bryan Perozzi, and Joonseok Lee. N-GCN: Multi-scale graph convolution for semi-supervised node classification. In Uncertainty in Artificial Intelligence, pages 841–851, 2020.
[37] Sami Abu-El-Haija, Amol Kapoor, Bryan Perozzi, and Joonseok Lee. N-GCN: Multi-scale graph convolution for semi-supervised node classification. In Uncertainty in Artificial Intelligence, pages 841–851, 2020.

[38] Fenyu Hu, W Liping, L Qiang, Shu Wu, Liang Wang, and Tieniu Tan. Graphdive: graph classification by mixture of diverse experts. In IJCAI, 2022.
[38] Fenyu Hu, W Liping, L Qiang, Shu Wu, Liang Wang, and Tieniu Tan. Graphdive: graph classification by mixture of diverse experts. In IJCAI, 2022.

[39] Liguang Zhou, Yuhongze Zhou, Tin Lun Lam, and Yangsheng Xu. CAME: Context-aware mixture-of-experts for unbiased scene graph generation. arXiv preprint arXiv:2208.07109, 2022.
[39] Liguang Zhou, Yuhongze Zhou, Tin Lun Lam, and Yangsheng Xu. CAME: Context-aware mixture-of-experts for unbiased scene graph generation. arXiv preprint arXiv:2208.07109, 2022.

[40] Suyeon Kim, Dongha Lee, SeongKu Kang, Seonghyeon Lee, and Hwanjo Yu. Learning topology-specific experts for molecular property prediction. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 37, pages 8291–8299, 2023.
[40] Suyeon Kim, Dongha Lee, SeongKu Kang, Seonghyeon Lee, and Hwanjo Yu. Learning topology-specific experts for molecular property prediction. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 37, pages 8291–8299, 2023.

[41] Zheyuan Liu, Chunhui Zhang, Yijun Tian, Erchi Zhang, Chao Huang, Yanfang Ye, and Chuxu Zhang. Fair graph representation learning via diverse mixture of experts. In The Web Conference, 2023.
[41] Zheyuan Liu, Chunhui Zhang, Yijun Tian, Erchi Zhang, Chao Huang, Yanfang Ye, and Chuxu Zhang. Fair graph representation learning via diverse mixture of experts. In The Web Conference, 2023.

[42] Cihang Xie, Mingxing Tan, Boqing Gong, Jiang Wang, Alan L Yuille, and Quoc V Le. Adversarial examples improve image recognition. In IEEE Conference on Computer Vision and Pattern Recognition, pages 819–828, 2020.
[42] Cihang Xie, Mingxing Tan, Boqing Gong, Jiang Wang, Alan L Yuille, and Quoc V Le. Adversarial examples improve image recognition. In IEEE Conference on Computer Vision and Pattern Recognition, pages 819–828, 2020.

[43] Haotao Wang, Chaowei Xiao, Jean Kossaifi, Zhiding Yu, Anima Anandkumar, and Zhangyang Wang. AugMax: Adversarial composition of random augmentations for robust training. In Advances in Neural Information Processing Systems, volume 34, pages 237–250, 2021.
[43] Haotao Wang, Chaowei Xiao, Jean Kossaifi, Zhiding Yu, Anima Anandkumar, and Zhangyang Wang. AugMax: Adversarial composition of random augmentations for robust training. In Advances in Neural Information Processing Systems, volume 34, pages 237–250, 2021.

[44] Haotao Wang, Aston Zhang, Shuai Zheng, Xingjian Shi, Mu Li, and Zhangyang Wang. Removing batch normalization boosts adversarial training. In International Conference on Machine Learning, pages 23433–23445, 2022.
[44] Haotao Wang, Aston Zhang, Shuai Zheng, Xingjian Shi, Mu Li, and Zhangyang Wang. Removing batch normalization boosts adversarial training. In International Conference on Machine Learning, pages 23433–23445, 2022.

[45] Andrew Brock, Soham De, and Samuel L Smith. Characterizing signal propagation to close the performance gap in unnormalized resnets. arXiv preprint arXiv:2101.08692, 2021.
[45] Andrew Brock, Soham De, and Samuel L Smith. Characterizing signal propagation to close the performance gap in unnormalized resnets. arXiv preprint arXiv:2101.08692, 2021.

[46] Andy Brock, Soham De, Samuel L Smith, and Karen Simonyan. High-performance large-scale image recognition without normalization. In ICML, pages 1059–1071, 2021.
[46] Andy Brock, Soham De, Samuel L Smith, and Karen Simonyan. High-performance large-scale image recognition without normalization. In ICML, pages 1059–1071, 2021.

[47] Guohao Li, Chenxin Xiong, Ali Thabet, and Bernard Ghanem. DeeperGCN: All you need to train deeper GCNs. arXiv preprint arXiv:2006.07739, 2020.
[47] Guohao Li, Chenxin Xiong, Ali Thabet, and Bernard Ghanem. DeeperGCN: All you need to train deeper GCNs. arXiv preprint arXiv:2006.07739, 2020.

[48] Weihua Hu, Matthias Fey, Marinka Zitnik, Yuxiao Dong, Hongyu Ren, Bowen Liu, Michele Catasta, and Jure Leskovec. Open graph benchmark: Datasets for machine learning on graphs. arXiv preprint arXiv:2005.00687, 2020.
[48] Weihua Hu, Matthias Fey, Marinka Zitnik, Yuxiao Dong, Hongyu Ren, Bowen Liu, Michele Catasta, and Jure Leskovec. Open graph benchmark: Datasets for machine learning on graphs. arXiv preprint arXiv:2005.00687, 2020.

[49] Weihua Hu, Bowen Liu, Joseph Gomes, Marinka Zitnik, Percy Liang, Vijay Pande, and Jure Leskovec. Strategies for pre-training graph neural networks. arXiv preprint arXiv:1905.12265, 2019.
[49] Weihua Hu, Bowen Liu, Joseph Gomes, Marinka Zitnik, Percy Liang, Vijay Pande, and Jure Leskovec. Strategies for pre-training graph neural networks. arXiv preprint arXiv:1905.12265, 2019.

[50] Teague Sterling and John J Irwin. Zinc 15–ligand discovery for everyone. Journal of Chemical Information and Modeling, 55(11):2324–2337, 2015.
[50] Teague Sterling and John J Irwin. Zinc 15–ligand discovery for everyone. Journal of Chemical Information and Modeling, 55(11):2324–2337, 2015.

[51] Bo Li, Yifei Shen, Jingkang Yang, Yezhen Wang, Jiawei Ren, Tong Che, Jun Zhang, and Ziwei Liu. Sparse mixture-of-experts are domain generalizable learners. arXiv preprint arXiv:2206.04046, 2022.
[51] Bo Li, Yifei Shen, Jingkang Yang, Yezhen Wang, Jiawei Ren, Tong Che, Jun Zhang, and Ziwei Liu. Sparse mixture-of-experts are domain generalizable learners. arXiv preprint arXiv:2206.04046, 2022.

[52] Weibin Li, Shanzhuo Zhang, Lihang Liu, Zhengjie Huang, Jieqiong Lei, Xiaomin Fang, Shikun Feng, and Fan Wang. Molecule representation learning by leveraging chemical information. Technical report, 2021.
[52] Weibin Li, Shanzhuo Zhang, Lihang Liu, Zhengjie Huang, Jieqiong Lei, Xiaomin Fang, Shikun Feng, and Fan Wang. Molecule representation learning by leveraging chemical information. Technical report, 2021.

[53] Lanning Wei, Huan Zhao, Quanming Yao, and Zhiqiang He. Pooling architecture search for graph classification. In Proceedings of the 30th ACM International Conference on Information & Knowledge Management, pages 2091–2100, 2021.
[53] Lanning Wei, Huan Zhao, Quanming Yao, and Zhiqiang He. Pooling architecture search for graph classification. In Proceedings of the 30th ACM International Conference on Information & Knowledge Management, pages 2091–2100, 2021.

[54] Yan Wang, Hao Zhang, Jing Yang, Ruixin Zhang, and Shouhong Ding. Technical report for ogb graph property prediction. In Technical Report, 2021.
[54] Yan Wang, Hao Zhang, Jing Yang, Ruixin Zhang, and Shouhong Ding. Technical report for ogb graph property prediction. In Technical Report, 2021.

[55] Zhuoning Yuan, Yan Yan, Milan Sonka, and Tianbao Yang. Large-scale robust deep auc maximization: A new surrogate loss and empirical studies on medical image classification. In CVPR, pages 3040–3049, 2021.
[55] Zhuoning Yuan, Yan Yan, Milan Sonka, and Tianbao Yang. Large-scale robust deep auc maximization: A new surrogate loss and empirical studies on medical image classification. In CVPR, pages 3040–3049, 2021.

[56] Hao Zhang, Jiaxin Gu, and Pengcheng Shen. Gman and bag of tricks for graph classification, 2021.
[56] Hao Zhang, Jiaxin Gu, and Pengcheng Shen. Gman and bag of tricks for graph classification, 2021.
