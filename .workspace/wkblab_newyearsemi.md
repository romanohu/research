---
marp: true
theme: freud
paginate: true
math: mathjax
---

# ニューイヤーランチ会論文紹介
klis3年 鈴木史麿

---
## 紹介する論文
- Proximal Policy Optimization Algorithms
- Graph Attention-Guided Search for Dense Multi-Agent Pathfinding

---

### Proximal Policy Optimization Algorithms(2017)
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov

---

#### 流れ

- 強化学習（RL）の基礎を復習
- Policy Gradient と Actor-Critic の位置づけ
- TRPO の課題を理解
- PPO の目的関数を数式で理解する

---

#### 強化学習の基本設定

- 状態: $s_t \in \mathcal{S}$
- 行動: $a_t \in \mathcal{A}$
- 報酬: $r_t = r(s_t, a_t)$
- 方策:
$$
\pi_\theta(a|s)
$$

- 目的関数:
$$
J(\theta)
= \mathbb{E}_\pi \left[\sum_{t=0}^\infty \gamma^t r_t \right]
$$

---

#### Policy Gradient の基本

方策を直接最適化する：

$$
\nabla_\theta J(\theta)
=
\mathbb{E}_{\pi_\theta}
\left[
\nabla_\theta \log \pi_\theta(a_t|s_t) \, G_t
\right]
$$

- $G_t$: 時刻 $t$ からの累積報酬
- REINFORCE の基本式

---

#### 分散削減：Advantage 関数

- 状態価値関数:
$$
V^\pi(s)
=
\mathbb{E}_\pi[G_t | s_t=s]
$$

- Advantage:
$$
A^\pi(s_t,a_t)
=
Q^\pi(s_t,a_t) - V^\pi(s_t)
$$

- 勾配は次の形に書ける：
$$
\nabla_\theta J(\theta)
=
\mathbb{E}
\left[
\nabla_\theta \log \pi_\theta(a_t|s_t) A_t
\right]
$$

---

#### Actor-Critic 法

- Actor: 方策 $\pi_\theta(a|s)$
- Critic: 価値関数 $V_\phi(s)$

TD 誤差による Advantage 近似：
$$
A_t
\approx
r_t + \gamma V_\phi(s_{t+1}) - V_\phi(s_t)
$$

→ 分散が小さく、安定した学習が可能

---

#### Policy Gradient の課題

- 学習が不安定
- 一度集めたデータで 1回しか更新できない
- 更新が大きすぎると性能崩壊

→ 方策の更新量を制御したい

---

#### Trust Region Policy Optimization (TRPO)

制約付き最適化問題：

$$
\max_\theta
\;
\mathbb{E}
\left[
\frac{\pi_\theta(a|s)}
{\pi_{\theta_{\text{old}}}(a|s)}
A^{\pi_{\text{old}}}(s,a)
\right]
$$

subject to:
$$
D_{KL}
\left(
\pi_{\theta_{\text{old}}}
\;\|\;
\pi_\theta
\right)
\le \delta
$$

---

#### TRPO の問題点

- KL 制約の二次近似が必要
- 共役勾配法など実装が複雑
- ミニバッチ SGD が使いにくい

→ より簡単な trust region が必要

---

#### PPO の基本アイデア

- TRPO の「安全な更新」を
- 制約ではなく目的関数で実現
- ミニバッチで複数 epoch 更新可能

---

#### 確率比 $r_t(\theta)$

$$
r_t(\theta)
=
\frac{\pi_\theta(a_t|s_t)}
{\pi_{\theta_{\text{old}}}(a_t|s_t)}
$$

- 新旧方策の変化量を表す

---

#### PPO の Clipped Objective

$$
L^{\text{CLIP}}(\theta)
=
\mathbb{E}_t
\Big[
\min(
r_t(\theta) A_t,\;
\text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) A_t
)
\Big]
$$

---

#### Clip の役割

- $r_t(\theta) > 1+\epsilon$
- $r_t(\theta) < 1-\epsilon$

→ それ以上の改善・悪化を 打ち切る

→ 方策を「近接（proximal）」に保つ

---

#### PPO の直感

- $A_t > 0$  
  → 行動確率を適度に増やす
- $A_t < 0$  
  → 行動確率を適度に減らす

→ 極端な更新を防ぐ仕組み

---

#### Value Loss & Entropy Bonus

実際に最適化する目的関数：

$$
L(\theta)
=
L^{\text{CLIP}}
- c_1 (V_\phi(s_t) - V_t^{\text{target}})^2
+ c_2 \mathcal{H}(\pi_\theta)
$$

- Value loss: Critic 学習
- Entropy bonus: 探索の促進

---

#### PPO アルゴリズム

1. 方策 $\pi_{\theta_{\text{old}}}$ で軌道収集
2. Advantage を計算
3. データをミニバッチ化
4. $L^{\text{CLIP}}$ を複数 epoch 最適化
5. 方策更新

---

#### PPO の特徴

- TRPO 並みの安定性
- 実装が非常に簡単
- Adam / SGD と相性良好
- 実用 RL のデファクト

---

#### 実験結果（論文）

- MuJoCo（連続制御）
- Atari（離散制御）
- A2C / TRPO を多くのタスクで上回る

---

#### まとめ

- PPO = 安定な Policy Gradient
- 核心は Clipped Objective
- Actor-Critic と自然に統合
- 現代 RL の基盤技術

---

### Graph Attention-Guided Search for Dense Multi-Agent Pathfinding(2025)
Rishabh Jain, Keisuke Okumura, Michael Amir, Amanda Prorok

---

#### 背景：Multi-Agent Pathfinding（MAPF）

MAPF問題
- 複数エージェントが
  - 同一セル占有なし
  - エッジ衝突なし
- 各自のスタート → ゴールへ移動
- 目的：総コスト（makespan / sum of costs）最小化

---

応用例
- 倉庫ロボット
- 群ロボット
- ゲームAI

---

#### MAPFの難しさ

- エージェント数 $N$ に対して状態空間が 指数的
- 特に 高密度（dense）環境では
  - 局所的な衝突回避が全体最適を破壊
  - デッドロックが頻発

→ 最適性・計算時間・スケーラビリティのトレードオフ

---

#### MAPF 解法の系譜

##### 探索ベース手法
- 完備性・最適性保証
- 例：CBS, LaCAM
- 高密度では遅い

##### 学習ベース手法
- 高速・スケーラブル
- 例：GNN, Transformer
- 完全性なし・失敗例あり

→「学習で探索を導く」ハイブリッドが理想かもしれない

---

#### LaCAM（Large-scale Conflict-Aware MAPF）

LaCAMの特徴
- 探索ベース MAPF アルゴリズム
- エージェントの優先度順序を探索
- 局所的な衝突を抑えつつスケーラブル

強み
- 完備性あり
- 大規模問題に比較的強い

弱み
- 優先度探索が盲目的
- 密集環境では near-optimal 解が遅い

---

#### MAGAT（Message-Aware Graph Attention）

MAGATとは
- MAPF専用の GNN ポリシー
- ノード：エージェント
- エッジ：近傍関係
- Graph Attention により相互作用を学習

出力
- 各エージェントの行動分布（次の移動）

課題
- 単体では
  - デッドロック
  - グローバル整合性不足

---

#### 問題意識（この論文の動機）

なぜ過去の「学習誘導探索」は失敗してきたのか？

- 学習ヒューリスティックが 不安定
- 探索アルゴリズムの理論保証を破壊
- 密集環境で誤誘導 → 探索破綻

→ 慎重に設計された統合が必要

---

#### 提案手法：LaGAT

LaGAT = LaCAM + GAT-based Heuristic

- MAGAT を改良した MAGAT+
- LaCAM の探索を
  - 学習済みヒューリスティックで誘導
- 完全性は LaCAM 側で保証

「探索の骨格は壊さず、賢く案内する」

---

#### MAGAT+ の改良点

- より表現力の高い Graph Attention
- エージェント間の密な相互作用を明示的にモデル化
- Dense MAPF に特化した設計

ポイント
- 行動そのものを強制しない
- あくまで「探索の優先度」を提示

---

#### 学習戦略：Pre-train → Fine-tune

1. 事前学習
   - 汎用 MAPF 環境
   - 一般的な協調パターンを獲得

2. ファインチューニング
   - 対象マップ特化
   - 密集構造に適応

→ 実環境・特定レイアウトへの適応が可能

---

#### 安全装置：デッドロック検出

問題
- 学習ヒューリスティックは誤る

対策
- 探索中にデッドロックを検出
- MAGAT 誘導を一時停止
- 通常の LaCAM 探索へフォールバック

 完備性・堅牢性を維持

---

#### 実験設定

- 高密度 MAPF ベンチマーク
- エージェント数：多
- 狭い通路・ボトルネックあり

比較手法
- 純探索（LaCAM）
- 純学習（MAGAT）
- 提案手法（LaGAT）

---

#### 実験結果

結果
- LaGAT が最良性能
  - 解の質（near-optimal）
  - 成功率
  - 計算時間

特に
- Dense 環境で顕著な改善
- 学習単体・探索単体の弱点を補完

---

#### なぜうまくいったのか？

- 学習は「決定」ではなく「誘導」
- 探索の理論保証を維持
- デッドロック対策を明示的に設計

→ ハイブリッド設計の教科書的成功例

---

#### 本論文の貢献

- Dense MAPF における
  - 実用的な near-optimal 解法
- 学習 × 探索の統合設計指針を提示
- 「学習誘導探索は使える」ことを実証

---

#### 限界と今後

限界
- 学習コスト
- マップ依存性

今後
- 汎化性能の向上
- 他の探索アルゴリズムへの応用
- 実ロボット展開

---

#### まとめ

- MAPFの難所：高密度・強結合
- LaGAT：
  - 探索の強さ × 学習の直感
- ハイブリッドは強力

