---
marp: true
theme: freud
paginate: true
math: mathjax
---

# 論文紹介
klis3年 鈴木史麿

---

## 紹介する論文
- Formal contracts mitigate social dilemmas in multi‑agent reinforcement learning

---

### [Formal contracts mitigate social dilemmas in multi‑agent reinforcement learning](https://arxiv.org/abs/2208.10469)
Andreas A. Haupt, Phillip J.K. Christoffersen, Mehul Damani, Dylan Hadfield-Menell

---
<!-- _footer: "Section 1 Introduction, pp.1–4" -->

### 背景と問い
マルチエージェント強化学習(MARL)では、各エージェントが自分の報酬を最大化しようとすると、個人の利益と全体の利益がずれて社会的ジレンマが起きやすい

人間にはこういった個人の利益と全体の利益の衝突を解決する能力があるが、MARLの独立したエージェントにこれを何の契機も無しに学習させることは難しい  
→ 何かしらの工夫が必要

著者らは人間社会で使われる契約(formal contracts)の発想を取り入れ、エージェント同士が報酬移転を伴う拘束的な契約を自発的に結べれば、このジレンマを緩和できるのではないかと考えている

---

<!-- _footer: "Section 1 Introduction, p.1 Abstract / pp.1–4" -->

#### 自己利益で動くMARLエージェントに、契約による報酬移転の仕組みを与えると、社会的に望ましい協調行動を安定的に実現できるか

---

<!-- _footer: "Section 1 Introduction, p.2" -->

### どのような契約か？①
This article studies contracts as voluntary commitments by all agents to zero-sum modifications of the environment reward, so-called social contracts, as a detail-free method of mitigating social dilemmas. 

本稿では、社会的ジレンマを緩和するための詳細不要型手法として、すべてのエージェントによる自発的なコミットメントとしての契約、すなわち「社会的契約」をゼロサム型環境報酬の修正手段として考察する

---

<!-- _footer: "Definition 3–5, Section 2.2 Formal contracting, pp.6–9" -->

### どのような契約か？②
契約$\theta$は、契約観測に応じて各エージェントへどれだけ報酬移転するかを定める関数

$$
\theta : \Omega_0 \to \mathbb{R}^N
$$

ただし、契約はゼロサム移転なので以下が成り立つ

$$
\sum_{i=1}^N \theta_i(o) = 0
\qquad
(\forall o \in \Omega_0)
$$

→ 契約は新しい報酬を生み出すのではなく、エージェント間で報酬を移し替えるだけ

$$
\tilde{R}((s,0), a) = R(s,a)
\to
\tilde{R}((s,\theta), a) = R(s,a) + \theta(s,a)
$$

---

<!-- _footer: "Cleanup example, Section 1 Introduction, p.2" -->

### どのような契約か？③
例 : clean_up
- 通常 : りんごを得たエージェント$i$が報酬を得る
- 契約あり :  
    - りんごを得たエージェント$i$が報酬を得る
    - 川を掃除することによってもエージェント$i$は少量の報酬$r_{clean}$を得る
        - さらにその他のエージェント$!i$はそれぞれ$-r_{clean}/(n-1)$を負担する

---

<!-- _footer: "Cleanup example, Section 1 Introduction, p.2" -->

Harvesting agents prefer this to an outcome with no apples as long as the bonus from
picking apples offsets the cost. Non-harvesting agents prefer this contract as long as the
bonus is small enough to be offset by the benefits of having apples grow.

収穫エージェントは、リンゴのボーナスがコストを相殺する限り、リンゴが実らない結果よりもこの契約を好みます。一方、非収穫エージェントは、リンゴが育つことによる利益でボーナスの影響が十分に相殺できる場合に限り、この契約を選択します。

---

<!-- _footer: "Section 2.1.2–2.2, pp.5–9" -->

### 契約観測とは？①
契約は環境の生の状態そのものではなく、契約が参照できる観測に基づいて報酬移転を決める

論文では契約観測を以下のように定義
$$
O_0 : S \times A \to \Delta(\Omega_0)
$$

- $S$ : 状態
- $A$ : 行動
- $\Omega_0$ : 契約が利用できる観測空間(確率的分布で揺れる)

---

<!-- _footer: "Section 1 Introduction, p.3 / Section 2.1.2, p.5 / Section 4, pp.13–15" -->

### 契約観測とは？②
通常のエージェント観測とは別に、契約側だけが参照する観測チャネルを導入するイメージ

例えば
- 誰が defection したか
- 誰が clean したか
- 望ましい行動が何回起きたか

などを契約観測に含めれば、それに応じた報酬移転を設計できる

---

<!-- _footer: "Definition 5 and transitions, Section 2.2, pp.7–9 / Repeated proposals generalization Appendix B, pp.33–34" -->

### 契約のタイミング
基本設定では、各エピソードの開始前に契約フェーズが入る

1. 提案者が契約 $\theta$ を提案
2. 他のエージェントが受諾/拒否
3. 全員受諾なら契約ありでゲーム開始
4. 誰かが拒否なら契約なしでゲーム開始

MARLの学習では環境のリセットが入るたびに契約フェーズが差し込まれる

※ どうやらゲーム中にも契約提案をするバージョンもあるようだが、主にゲーム前提案の形を扱っていた

---

<!-- _footer: "Section 1 Introduction, p.2 / Rewards in Section 2.2.4–2.2.5, pp.8–9" -->

### この枠組みの重要な点
契約を受諾したあとも、エージェントは依然として好きな行動を選べる

- 「clean しなければならない」と強制されるわけではない
- ただし契約により、clean した方が自分にとって得になる(かもしれない)

→ 望ましい行動を強制するのではなく、インセンティブを組み替える(選択肢を与える)

---

<!-- _footer: "Theorem 1–2, Section 3 Formal contracting mitigates social dilemmas, pp.9–11" -->

### 理論結果：十分に豊かな契約空間なら最適協調を実現
論文の中心的な理論結果は次の通り

- 契約が十分に表現力を持ち
- 逸脱行動を契約観測から検出できるなら

契約付きゲームの部分ゲーム完全均衡(SPE)では、環境全体の報酬(論文では社会厚生)を最大化する行動が実現される

$$
W(s_0)=\sum_i V_i(s_0)
$$

※SPEとはゲームの途中のどの局面から見ても、どのプレイヤーも一人で行動を変える得をしない均衡

---

<!-- _footer: "Theorem 4 / Corollary 5 / Proposition 6, Section 4, pp.11–15" -->

### 契約空間が豊かになるほど 社会厚生 は上がる
論文のもう一つの重要な結果は単調性(monotonicity)

- より多くの契約を表現できる
- より多くの契約特徴を参照できる

ほど、達成可能な均衡厚生の上下限が改善する

直感的には
- 契約の表現力が低い  
  → 欲しいインセンティブを細かく作れない
- 契約の表現力が高い  
  → 社会的に望ましい行動へ報酬構造を近づけやすい

---

<!-- _footer: "Section 4.1–4.3, pp.13–15 / Contract spaces in Section 5.3, p.19" -->

### 契約特徴(feature)の設計が重要
論文では、契約は状態そのものではなく特徴量に基づいてもよいと示す

たとえば Cleanup / Harvest なら以下のものを契約特徴にできる

- 誰が clean したか
- 低密度領域のリンゴを取ったか
- 周囲のリンゴ密度
- ゴミの数

→ 契約設計とは、ある意味で「何を観測可能・契約可能にするか」の設計問題

---

<!-- _footer: "Definition 7 / Proposition 3, Section 4, pp.11–13" -->

### 任意の報酬の無条件移転が重要
単調性の結果には、署名時点で任意の無条件移転ができることが本質的に効いている

これがあると提案者は
- 他エージェントを受諾ギリギリまで補償しつつ
- 増えた総厚生の余剰を自分に内部化できる

その結果、提案者自身が高 社会厚生 の契約を選ぶ誘因を持つ

---

<!-- _footer: "Section 5.2 Games, pp.17–19" -->

### 実験設定①
評価は以下の環境で行われる

- 静的ゲーム
  - Prisoner’s Dilemma
  - Public Goods
- 動的ゲーム
  - Harvest
  - Cleanup
  - Emergency Merge

---

<!-- _footer: "Section 5.1 Evaluation, pp.16–17" -->

### 実験設定⓶
比較対象は
- Joint Training(全体報酬を中央集権的に最適化)
- Separate Training(各自が自己報酬だけ最大化)
- Gifting(各時刻に任意送金)
- Vanilla Contracting ← 純粋な契約
- MOCA(提案手法)

---

<!-- _footer: "Section 5.4 Training / Algorithm 1 MOCA, pp.19–24" -->

### 提案アルゴリズム：MOCA
Phase 1
- 契約をランダムにサンプル
- 各契約の下でのプレイを学習
- 各エージェントにとって「この契約だとどれくらい得か」の見積もりを作る

Phase 2
- 契約下の行動方策をほぼ固定
- 今度は「どの契約を提案・受諾するか」を重点的に学習

---

<!-- _footer: "Results for simple games, Section 6.1–6.2 / Fig.7 and Fig.9, pp.20–22, 25–26" -->

### 実験結果①：単純な静的ゲーム
Prisoner’s Dilemma や Public Goods では

- Contracting は Separate / Gifting より高 社会厚生
- 多くの設定で Joint Training に匹敵
- Prisoner’s Dilemma では agent 数が増えるとjoint action 空間の爆発のため？、contracting が joint training を上回る場合もある

---

<!-- _footer: "Results for dynamic games, Section 6.1–6.2 / Fig.8 and Fig.10, pp.21–23, 25–26" -->

### 実験結果②：複雑な動的ゲーム
Harvest, Cleanup, Merge では差がより明確

- Vanilla Contracting は複雑環境で不安定
- MOCA は 社会厚生 を大きく改善し、多くの設定で Joint Training に匹敵または上回る

---

<!-- _footer: "Section 6.1–6.2, pp.25–26" -->

### なぜ joint training を上回ることがあるのか
一見不思議だが、著者の解釈は明快

- Joint Training は合同行動空間を直接扱う必要がある
- エージェント数が増えると探索が急激に難しくなる
- Contracting は分散実行のまま、契約だけでインセンティブを調整する

つまり「中央集権的に全部まとめて最適化する難しさ」を回避できるケースがある

---

<!-- _footer: "Section 8.1 Limitations for formal contracting / Appendix B.1, pp.28–29, 33" -->

### 限界と注意点①：提案者が1人という仮定
理論結果には単一の提案者という仮定が重要

複数の提案者がいると
- 他人の契約提案を見越した駆け引き
- 拒否時の利得を狙う行動

が入り、社会的に最適でない SPE が出うると議論している

---

<!-- _footer: "Section 8.3 Fairness, p.29" -->

### 限界と注意点②：公平性

- 非提案者は「受諾しても拒否しても同じ」程度までしか補償されず
- 追加で生まれた余剰の多くを提案者が取る

→ 社会厚生 は改善しても分配の公平性は別問題

fairness と 社会厚生 のトレードオフを将来課題として挙げている

---

<!-- _footer: "Section 8.2 Scaling formal contracting / Section 9 Conclusion, pp.28–30" -->

### 限界と注意点③：契約設計の手作業性
本論文の契約空間や契約特徴はかなり手設計されている

そのためスケールさせるには

- 有効な契約特徴を自動抽出すること
- 表現力と学習容易性のバランスを取ること
- よりサンプル効率の高い契約学習法を作ること

が必要だと議論されている

---

### まとめ
- 社会的ジレンマは、行動制約ではなくインセンティブの再設計で緩和できる
- 十分に豊かな契約空間と逸脱検出可能性があれば、SPE は社会最適に到達
- 契約空間・契約特徴が豊かなほど 社会厚生は改善
- 実験でも、特に MOCA により複雑環境で高い性能を確認
- 一方で、公平性・複数提案者・契約設計の自動化は今後の課題
