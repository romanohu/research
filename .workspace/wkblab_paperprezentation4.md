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
- Partner Selection for the Emergence of Cooperation in Multi-Agent Systems Using Reinforcement Learning (AAAI 2020)
- Learning Partner Selection Rules that Sustain Cooperation in Social Dilemmas with the Option of Opting Out (AAMAS 2024)

---

### Partner Selection for the Emergence of Cooperation in Multi-Agent Systems Using Reinforcement Learning
Nicolas Anastassacos, Stephen Hailes, Mirco Musolesi (UCL/Turing)

---

### 背景と問い
- 社会的ジレンマで協力を安定させる鍵は「誰と組むか」
- 従来は報酬設計や中央集権的制御で協力を誘導
- 自律的なパートナー選択だけで協力は創発するか

---

### 環境設定
- 集団サイズ $N$ のエージェントが反復PDをプレイ
- 各ラウンド
  1. 過去1手の履歴を見て相手を指名
  2. 指名された相手と1回のPD (行動: C / D)
- 目的は自己利得のみ最大化 (利他的報酬なし)

---

### 囚人のジレンマの利得例
|        | 相手 C          | 相手 D          |
|--------|-----------------|-----------------|
| 自分 C | (R, R) = (3,3)  | (S, T) = (0,4)  |
| 自分 D | (T, S) = (4,0)  | (P, P) = (1,1)  |

- T > R > P > S かつ 2R > T + S を満たすときPD

---

### 状態と行動
- 選択Qの状態: 他全員の直前行動ベクトル (C/D)
- 選択Qの行動: 指名する相手 (1エージェントを選ぶ)
- 行動Qの状態: 現パートナーの直前行動のみ
- 行動Qの行動: C か D を出す

---

### 報酬設計
- 報酬はPD1回分の利得のみ
- 誰にも指名されないと報酬0 (社会的罰として働く)
- 選択Qは「指名後に得たPD報酬」を遡及して更新
- 使う履歴情報は直前1手だけ

---

### 学習構造
- 2つの独立Q-learning
  - 選択Q: 相手指名方策
  - 行動Q: PDでのC/D方策
- $\epsilon$-greedy 探索。割引率0.9、学習率0.1 (論文設定)
- 選択Qの更新は「指名後に得たPD報酬」を遡及的に使用

---

### 実験観察 (学習が進む順序)
1. 全員D: 初期は利己的裏切り
2. 搾取期: 協力者を選んで一方的に得する戦略が台頭
3. 報復期: 協力者が減少し、TFT的応報が登場
4. 協力定着: TFT/ALLCが主流となり、裏切り者は指名されず孤立

---

### 成果と示唆
- 選ばれないことが罰となり、外的懲罰なしで協力が安定
- 観測は1手履歴でも評判の代替になる
- マッチングをランダムに戻すと協力が崩壊 → 指名権が本質

---

### 制約と今後
- 全員の直前行動を観測できる前提は大規模・部分観測で非現実的
- 指名を拒否する仕組みがなく合意形成型環境への一般化は未検証
- 今後: 部分観測、拒否権付き指名、多人数公共財ゲームへの拡張

---

### Learning Partner Selection Rules that Sustain Cooperation in Social Dilemmas with the Option of Opting Out
Chin-wing Leung, Paolo Turrini (Warwick)

---

### 研究の狙い
- 固定ルールに頼らず、行動方策と退出方策を同時に学習すると何が生まれるか
- 現相手の前手のみという情報制約下で協力を維持できるか
- Out-for-Tatのような退出規則を自発的に再発見できるか

---

### 環境・行動空間
- 2人反復PDに Opt-Out 行動を追加
  - Stay: 同じ相手と次ラウンドへ
  - Opt-Out: 無作為再マッチ + loner報酬 $L$
- 観測: 相手の直前行動のみ (全体履歴や評判共有なし)
- 方策: 行動と退出を1つのネットワークで同時学習 (方策勾配)

---

### 学習で現れた規則
- Tit-for-Tatに近い応報を獲得
- Out-for-Tat (Dされたら退出) を自発的に再発見
- 追加観測された挙動
  - 協力相手には滞在、疑わしい相手は一度試して離脱
  - 序盤のみDで様子見し、反応を見て協力へ移るハジング的行動

---

### パラメータ感度
- loner報酬 $L$ が高すぎると退出濫用で協力低下
- 再マッチ待ち時間や確率を変えると退出方策の積極性が滑らかに変化
- 観測を複数手に広げると協力立ち上がりが早まる傾向

---

### 課題と展望
- 2人PDに限定。公共財ゲームやネットワーク上の多人数設定は未検証
- loner報酬設計に強く依存し、環境デザイン次第で協力が崩れる
- 今後: マッチング市場での退出権と評判共有の併用、部分観測・大規模環境への拡張

---

### 補足: 2つの研究の違い
- 相手選定の自由度: 指名制 (拒否なし) / 退出制 (再マッチ)
- 必要な観測: 全員の直前行動 / 現相手のみ
- 協力を守る仕組み: 選ばれない罰 / 関係解消の権利
- 学習方式: 2本のQ-learning分離 / 行動と退出を同時に方策勾配
- 想定応用: 評判共有がある組織・コミュニティ / プラットフォームやマッチング市場

---

## 参考
- AAAI20: Partner Selection for the Emergence of Cooperation in Multi-Agent Systems Using RL
- AAMAS24: Learning Partner Selection Rules that Sustain Cooperation in SD with Opt-Out
