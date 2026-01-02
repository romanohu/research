# MAPF 論文
- 読んだ方が良い論文
    - [Priority Inheritance with Backtracking for Iterative Multi-agent Path Finding(2019)](https://arxiv.org/abs/1901.11282)
    - [LaCAM: Search-Based Algorithm for Quick Multi-Agent Pathfinding(2022)](#lacam-search-based-algorithm-for-quick-multi-agent-pathfinding2022)
    - [Improving LaCAM for Scalable Eventually Optimal Multi-Agent Pathfinding(2023)](#improving-lacam-for-scalable-eventually-optimal-multi-agent-pathfinding2023)
    - [Traffic Flow Optimisation for Lifelong Multi-Agent Path Finding(2024)](https://arxiv.org/abs/2308.11234)
    - [Finding Optimal Solutions to Cooperative Pathfinding Problems(2010)](https://ojs.aaai.org/index.php/AAAI/article/view/7564)
    - [Lifelong Multi-Agent Path Finding in Large-Scale Warehouses(2021)](https://ojs.aaai.org/index.php/AAAI/article/view/17344)
    - [MAPF-LNS2: Fast Repairing for Multi-Agent Path Finding via Large Neighborhood Search(2022)](https://ojs.aaai.org/index.php/AAAI/article/view/21266)
    - [Section 3 "Planning",  A Comprehensive Review on Leveraging Machine Learning for Multi-Agent Path Finding](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10506521)
    - [MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale(2024)](#mapf-gpt-imitation-learning-for-multi-agent-pathfinding-at-scale)
    - [Graph Attention-Guided Search for Dense Multi-Agent Pathfinding(2025)](#graph-attention-guided-search-for-dense-multi-agent-pathfinding2025)

## 論文メモ
### 2022
#### [LaCAM: Search-Based Algorithm for Quick Multi-Agent Pathfinding(2022)](https://arxiv.org/abs/2211.13432)
[奥村圭佑](../Authors/japanese/奥村圭佑.md)
二層探索．高レベル探索では構成（configuration）の列を探索し，低レベル探索では次の構成に対する制約（constraints）を段階的に生成する．重要な考えとして，制約は最初から全部作らず「必要になった時だけ」追加するという設計（Lazy Constraints）がある．ここでいう制約とは「次の構成でエージェント i は頂点 v にいる」という局所的なものである．通常の非 Lazy な構成生成では，全エージェントに対する衝突の起こらない割当を全探索するため計算量が指数爆発するのに対し，LaCAM では制約を課さない状態から「connected な構成を生成できるかをまず試し」，失敗した場合にのみ制約を追加する．この操作を繰り返すことで，必要最小限の制約のみを扱いながら探索を進め，計算量を大きく削減している．
さらに重要なのは、LaCAM では一つの高レベル構成に対して低レベル探索を一度だけ行うのではなく、低レベル探索が尽きるまで同一の高レベルノードを保持し続け、制約集合を変えながら複数の後続構成を段階的に生成する点である．このため、高レベル探索におけるノード展開は「一度で完結する操作」ではなく、制約木の成長に応じて繰り返し呼び出される操作となる．また、制約は衝突を直接禁止する形では与えられず、制約を満たした上で connected な構成が生成できるかどうかを試す過程で、衝突は構成生成の失敗として間接的に検出される．低レベル探索は幅優先で制約を追加していくため、最終的には全エージェントに対する割当を網羅し、lazy な制約生成でありながら探索の完全性は保たれる．さらに、ある高レベル構成から到達可能なすべての connected な構成が生成し尽くされた時点で、その高レベルノードは破棄されるため、探索空間の重複展開も抑制されている．

### 2023
#### [Improving LaCAM for Scalable Eventually Optimal Multi-Agent Pathfinding(2023)](https://arxiv.org/abs/2305.03632)
[奥村圭佑](../Authors/japanese/奥村圭佑.md)

### 2024
#### [MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale](https://arxiv.org/abs/2409.00134)
> [リンク集](https://sites.google.com/view/mapf-gpt/)

[AntonAndreychuk](../Authors/overseas/AntonAndreychuk.md) 
最適・準最適ソルバの解法データを学習データとし、トランスフォーマーベースのニューラルネットワークを活用した模倣学習によって構築される基盤モデル、MAPF-GPTを提案している．これは学習データセットに含まれていない新規のMAPF問題を開設する際にゼロショット学習能力を発揮する．結論として「純粋な模倣学習だけで強力な学習型MAPFソルバを作ることは可能か」という問いに対して、明確に肯定的な答えを与える．
まず個々のエージェントが知覚し得るあらゆる観測結果と実行可能なあらゆる行動を表現した語彙体系(トークン)を構築する．次にソルバの解法データをトークンで符号化された観測-行動ペアの系列に変換する．それを用いてトランスフォーマーベースの非自己回帰型ニューラルネットワークを用いて与えられた観測結果に対して適切な行動を予測する学習を行う．非自己回帰型(NAR)は過去に自分が出した出力に依存させずに予測するモデルである．(そのまんまやった)
入力トークンは固定長で「 地形 + cost-to-go + 自分と近傍エージェントの状態 」が含まれる．cost-to-goにはゴールを始点としたマップ全体の最短距離マップを作り、次の行動との距離の差分を利用する．(生成はBFS/Dijkstra)
気になりポイントの衝突に関しては、衝突制約を明示的に扱う訳ではなく、学習を通して制約違反を回避する．(サイズは256)
出力は各エージェントが取り得る5種類の離散行動に対応した確率分布であり、即ち1ステップ先の行動である．(サイズは5)

### 2025
#### [Graph Attention-Guided Search for Dense Multi-Agent Pathfinding(2025)](https://arxiv.org/abs/2510.17382)
