# MAPF 論文
- 読んだ方が良い論文
    - [Finding Optimal Solutions to Cooperative Pathfinding Problems(2010)](https://ojs.aaai.org/index.php/AAAI/article/view/7564)
    - [Conflict-based search for optimal multi-agent pathfinding(2015)](#conflict-based-search-for-optimal-multi-agent-pathfinding)
    - [Priority Inheritance with Backtracking for Iterative Multi-agent Path Finding(2019)](https://arxiv.org/abs/1901.11282)
    - [Message-Aware Graph Attention Networks for Large-Scale Multi-Robot Path Planning](#message-aware-graph-attention-networks-for-large-scale-multi-robot-path-planning)
    - [LaCAM: Search-Based Algorithm for Quick Multi-Agent Pathfinding(2022)](#lacam-search-based-algorithm-for-quick-multi-agent-pathfinding)
    - [Improving LaCAM for Scalable Eventually Optimal Multi-Agent Pathfinding(2023)](#improving-lacam-for-scalable-eventually-optimal-multi-agent-pathfinding)
    - [Traffic Flow Optimisation for Lifelong Multi-Agent Path Finding(2024)](https://arxiv.org/abs/2308.11234)
    - [Lifelong Multi-Agent Path Finding in Large-Scale Warehouses(2021)](https://ojs.aaai.org/index.php/AAAI/article/view/17344)
    - [MAPF-LNS2: Fast Repairing for Multi-Agent Path Finding via Large Neighborhood Search(2022)](https://ojs.aaai.org/index.php/AAAI/article/view/21266)
    - [SCRIMP: Scalable Communication for Reinforcement- and Imitation-Learning-Based Multi-Agent Pathfinding](https://ieeexplore.ieee.org/document/10342305?denied=)
    - [A Comprehensive Review on Leveraging Machine Learning for Multi-Agent Path Finding(2024)](#a-comprehensive-review-on-leveraging-machine-learning-for-multi-agent-path-finding)
    - [MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale(2024)](#mapf-gpt-imitation-learning-for-multi-agent-pathfinding-at-scale)
    - [Graph Attention-Guided Search for Dense Multi-Agent Pathfinding(2025)](#graph-attention-guided-search-for-dense-multi-agent-pathfinding)
    - [Pairwise is Not Enough: Hypergraph Neural Networks for Multi-Agent Pathfinding(2025)](#pairwise-is-not-enough-hypergraph-neural-networks-for-multi-agent-pathfinding)

## 論文メモ
### 2015
#### [Conflict-based search for optimal multi-agent pathfinding](https://www.sciencedirect.com/science/article/pii/S0004370214001386)


### 2021
#### [Message-Aware Graph Attention Networks for Large-Scale Multi-Robot Path Planning](https://arxiv.org/abs/2011.13219)

MAGAT

### 2022
#### [LaCAM: Search-Based Algorithm for Quick Multi-Agent Pathfinding](https://arxiv.org/abs/2211.13432)
[奥村圭佑](../Authors/japanese/奥村圭佑.md)
二層探索．高レベル探索では構成（configuration）の列を探索し、低レベル探索では次の構成に対する制約（constraints）を段階的に生成する．重要な考えとして、制約は最初から全部作らず「必要になった時だけ」追加するという設計（Lazy Constraints）がある．ここでいう制約とは「次の構成でエージェント i は頂点 v にいる」という局所的なものである．通常の非 Lazy な構成生成では、全エージェントに対する衝突の起こらない割当を全探索するため計算量が指数爆発するのに対し、LaCAM では制約を課さない状態から「connected な構成を生成できるかをまず試し」、失敗した場合にのみ制約を追加する．この操作を繰り返すことで、必要最小限の制約のみを扱いながら探索を進め、計算量を大きく削減している．
さらに重要なのは、LaCAM では一つの高レベル構成に対して低レベル探索を一度だけ行うのではなく、低レベル探索が尽きるまで同一の高レベルノードを保持し続け、制約集合を変えながら複数の後続構成を段階的に生成する点である．このため、高レベル探索におけるノード展開は「一度で完結する操作」ではなく、制約木の成長に応じて繰り返し呼び出される操作となる．また、制約は衝突を直接禁止する形では与えられず、制約を満たした上で connected な構成が生成できるかどうかを試す過程で、衝突は構成生成の失敗として間接的に検出される．低レベル探索は幅優先で制約を追加していくため、最終的には全エージェントに対する割当を網羅し、lazy な制約生成でありながら探索の完全性は保たれる．さらに、ある高レベル構成から到達可能なすべての connected な構成が生成し尽くされた時点で、その高レベルノードは破棄されるため、探索空間の重複展開も抑制されている．
簡単な流れ(論文中の例)
- ステップ1 初期構成
  - ハイレベル: 開始構成(a,c)をopenリスト(スタック)に入れる
  - ローレベル: エージェント1を選択し、移動先の候補としての制約を作る
  - 構成生成: PIBTなどのアルゴリズムを使い制約なしで次の配置を計算する．ここでは(b,c)が作成されたと仮定する．
  - 結果: 新しい構成(b,c)をハイレベルノードとしてopenリストに追加する．
- ステップ2 既知の構成
  - ハイレベル: 直前に作った(b,c)を選択
  - ローレベル: 再びエージェントの移動先を検討する．
  - 構成生成: ここでは、同じ(b,c)が作られたとする
  - 結果: 既に探索済みであるので、新しいハイレベルノードは作られない
- ステップ3 遅延制約の追加
  - ハイレベル: (b,c)を捨てずに再利用し、ローレベル探索を続ける
  - ローレベル: 今度はエージェント2に対しても制約を広げる
  - 構成生成: しかし制約を守って計算すると、また同じく(b,c)が生成される
  - 結果: ハイレベルノードは作られない
- ステップ4 進展
  - ハイレベル: 引き続きローレベル探索を続ける
  - ローレベル: 「エージェント1はdに動く」という制約を作る
  - 構成生成: すると衝突のない構成(d,b)が見つかる
  - 結果: (b,d)を新しいハイレベルノードとして登録
- 以下繰り返しでゴール構成が出来たらハイレベルノードを逆順に辿ることで衝突の無い経路が完成する
- ノードの破棄
  - ハイレベルノードから派生する全てのローレベルノードを調べ尽くしても次へ進めない場合にそのハイレベルノードは破棄される．

### 2023
#### [Improving LaCAM for Scalable Eventually Optimal Multi-Agent Pathfinding](https://arxiv.org/abs/2305.03632)
[奥村圭佑](../Authors/japanese/奥村圭佑.md)
本論文ではLaCAMを拡張し、探索の進め方に理論的な裏付けと実用上の改良を加えている．まず、高レベル探索において各構成遷移に明示的なコストを割り当て、構成列全体の累積コストに基づいて探索順序を管理することで、探索全体を anytimeアルゴリズムとして再定式化している．これにより、探索の初期段階では制約の少ない粗い構成遷移を用いて低コストの近似解を素早く得ることができ、探索を継続するにつれて、より多くの制約を考慮した高コストな遷移が段階的に展開される．低レベル探索で制約が追加されることは、高レベル探索における遷移コストの増加として自然に解釈できるため、lazyに制約を生成するという設計を保ったまま、時間を十分に与えれば最終的に最適な構成列に必ず到達することが保証される．
また、本論文では低レベル探索そのものの振る舞いも改善されている．元のLaCAMでは、制約は幅優先的に追加されるため完全性は保たれるものの、初期段階ではconnectedな構成に結びつきにくい制約も同列に扱われていた．本論文では、衝突を起こしやすいエージェントや、構成生成の失敗に直接関与しやすい割当を優先的に制約として導入することで、制約木の初期成長をより解に近い方向へ誘導している．この結果、高レベル探索において有効な後続構成が早い段階で得られ、anytimeアルゴリズムとして重要な「まず動く解を返す」性能が大きく向上している．


### 2024
#### [MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale](https://arxiv.org/abs/2409.00134)
> [リンク集](https://sites.google.com/view/mapf-gpt/)

[AntonAndreychuk](../Authors/overseas/AntonAndreychuk.md) 
最適・準最適ソルバの解法データを学習データとし、トランスフォーマーベースのニューラルネットワークを活用した模倣学習によって構築される基盤モデル、MAPF-GPTを提案している．これは学習データセットに含まれていない新規のMAPF問題を開設する際にゼロショット学習能力を発揮する．結論として「純粋な模倣学習だけで強力な学習型MAPFソルバを作ることは可能か」という問いに対して、明確に肯定的な答えを与える．
まず個々のエージェントが知覚し得るあらゆる観測結果と実行可能なあらゆる行動を表現した語彙体系(トークン)を構築する．次にソルバの解法データをトークンで符号化された観測-行動ペアの系列に変換する．それを用いてトランスフォーマーベースの非自己回帰型ニューラルネットワークを用いて与えられた観測結果に対して適切な行動を予測する学習を行う．非自己回帰型(NAR)は過去に自分が出した出力に依存させずに予測するモデルである．(そのまんまやった)
入力トークンは固定長で「 地形 + cost-to-go + 自分と近傍エージェントの状態 」が含まれる．cost-to-goにはゴールを始点としたマップ全体の最短距離マップを作り、次の行動との距離の差分を利用する．(生成はBFS/Dijkstra)
気になりポイントの衝突に関しては、衝突制約を明示的に扱う訳ではなく、学習を通して制約違反を回避する．(サイズは256)
出力は各エージェントが取り得る5種類の離散行動に対応した確率分布であり、即ち1ステップ先の行動である．(サイズは5)

#### [A Comprehensive Review on Leveraging Machine Learning for Multi-Agent Path Finding](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10506521)
MAPF分野におけるMLを利用した研究に注目してサーベイしている論文．計画手法に対して表現手法?と実行手法?に関する論文は少ないらしい．
経路生成、動的障害配置が面白そう．
模倣学習および強化学習
ベンチマークが一覧で載っている(Unityはやっぱり重い)
Open Question(未解決研究課題一覧)
```
Open Question 1
What can be beneficial criteria and reliable benchmarks for assessing the quality of environment representation?

Open Question 2
What are efficient transition mechanisms between offline and online environment optimization?

Open Question 3
What is the appropriate input instance representation for algorithm selection?

Open Question 4
What is the appropriate representation for MAPF on non-grid worlds?

Open Question 5
How can learning from experience be transferred from smaller to larger instances?

Open Question 6
How can we identify and extract effective features to maximize the performance of ML-assisted MAPF algorithms?

Open Question 7
Which benchmarking suite of environments and evaluation metrics would best reflect the performance of different techniques?

Open Question 8
Which communication strategy is most effective in real-world environments with their inherent challenges?

Open Question 9
How can effectively learned implicit communication minimize the need and overhead of explicit communication while achieving comparable outcomes?

Open Question 10
How could more advanced IL methods improve the performance of agent-based approaches beyond naive behavior cloning (BC)?

Open Question 11
How can we avoid reward shaping to eliminate human bias in the learning process?

Open Question 12
How can one construct a dataset of MAPF instances that progressively increases in difficulty?

Open Question 13
To what extent should the real-world agent dynamics captured by ML be reflected in MAPF?

Open Question 14
How can ML enhance the fault tolerance of MAPF systems?
```
### 2025
#### [Graph Attention-Guided Search for Dense Multi-Agent Pathfinding](https://arxiv.org/abs/2510.17382)
[奥村圭佑](../Authors/japanese/奥村圭佑.md) [Rishabh Jain](../Authors/overseas/RishabhJain.md)
LaGATの提案．LaGAT = LaCAM(Okumura 2023) + MAGAT+(MAGAT(Li et al 2021b)の改良版)
MAGAT+の事前学習としてlacam3が生成した準最適軌道を模倣学習．その後、対象のMapに対してFineTuningする．それをLaCAMの探索の中でヒューリスティックとして使用する．通常のLaCAM(の中のPIBT)がcost-to-goで候補行動vを決めるのに対して、MAGAT+を用いた場合は現在の観測に基づいた情報をもとに行動に対して確率を出力し、それをPIBTのpreferenceとして使用する．
もしMAGAT+の誘導が反復や振動を引き起こしている場合に備えてデッドロック検出機構が備わっている．検出の基本アイディアは「最近のdステップ以内に同じ局所的状況に戻ってきたら異常」であり、LaCAMの探索木を使って過去の構成を遡り、エージェントごとに局所的な停滞を検出する．そして、その対処としてノードの制約を全消去し、Openリストに再挿入する．その後、通常のLaCAMアルゴリズムで探索をする．
注意点としてMAGAT+によるガイドはエージェント単位で管理されており、一度通常に戻ったエージェントは二度とガイド付きには戻らない．つまり、ガイド付きで上手くいかない場合、最終的にはすべてのエージェントのガイドが外れて、通常のLaCAMと等しくなる．

#### [Pairwise is Not Enough: Hypergraph Neural Networks for Multi-Agent Pathfinding](https://openreview.net/forum?id=WUbGQQ9C0E)
[奥村圭佑](../Authors/japanese/奥村圭佑.md) [Rishabh Jain](../Authors/overseas/RishabhJain.md)
