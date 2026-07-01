# MARL 論文
## モデル
- [Planning Problems for Sophisticated Agents with Present Bias(2016)](https://arxiv.org/abs/1603.08177)
- [Learning Multiagent Communication with Backpropagation(2016)](https://arxiv.org/abs/1605.07736)
- [Multiagent cooperation and competition with deep reinforcement learning(2017)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0172395)
- [Trust Region Policy Optimisation in Multi-Agent Reinforcement Learning(2018)](https://arxiv.org/abs/2109.11251?utm_source=chatgpt.com)
- [The Surprising Effectiveness of PPO in Cooperative, Multi-Agent Games(2021)](https://arxiv.org/abs/2103.01955?utm_source=chatgpt.com)
- [RPM: Generalizable Behaviors for Multi-Agent Reinforcement Learning(2022)](https://arxiv.org/abs/2210.09646)
- [Multi-Agent Reinforcement Learning is a Sequence Modeling Problem(2023)](https://arxiv.org/abs/2205.14953?utm_source=chatgpt.com)
- [HyperMARL: Adaptive Hypernetworks for Multi-Agent RL(2024)](#hypermarl-adaptive-hypernetworks-for-multi-agent-rl)
- [Mixture of Experts in a Mixture of RL settings(2024)](#mixture-of-experts-in-a-mixture-of-rl-settings)
- [Partner Selection for the Emergence of Cooperation in Multi-Agent Systems Using Reinforcement Learning(2020)](https://arxiv.org/abs/1902.03185)
- [Cooperation and Reputation Dynamics with Reinforcement Learning(2021)](https://www.ifaamas.org/Proceedings/aamas2021/pdfs/p115.pdf)
- [Investigating the impact of direct punishment on the emergence of cooperation in multi-agent reinforcement learning systems(2025)](https://doi.org/10.1007/s10458-025-09698-5)

## 環境・ベンチマーク・フレームワーク
- [Playing Atari with Deep Reinforcement Learning(2013)](https://arxiv.org/abs/1312.5602)

## サーベイ
- [An Introduction to Centralized Training for Decentralized Execution in Cooperative Multi-Agent Reinforcement Learning(2024)](#an-introduction-to-centralized-training-for-decentralized-execution-in-cooperative-multi-agent-reinforcement-learning)

---

## 論文メモ
### 2024
#### [HyperMARL: Adaptive Hypernetworks for Multi-Agent RL](https://arxiv.org/abs/2412.04233?utm_source=chatgpt.com)
[Kale-ab Abebe Tessera](../Authors/overseas/TesseraKaleabAbebe.html) [Arrasy Rahman](../Authors/overseas/ArrasyRahman.html) [Amos Storkey](../Authors/overseas/AmosStorkey.html) [Stefano V. Albrecht](../Authors/overseas/StefanoVAlbrecht.html)

#### [Mixture of Experts in a Mixture of RL settings](https://arxiv.org/abs/2406.18420)
[Timon Willi](../Authors/overseas/TimonWilli.html) [Johan Obando-Ceron](../Authors/overseas/JohanObandoCeron.html) [Jakob Foerster](../Authors/overseas/JakobNFoerster.html) [Karolina Dziugaite](../Authors/overseas/KarolinaDziugaite.html) [Pablo Samuel Castro](../Authors/overseas/PabloSamuelCastro.html)

#Unread

強い非定常性をもつRL条件でMoEの構成要素（routing, expert specialization, regularization）が学習安定性と最終性能にどう効くかを分解評価した研究．複数のRL設定で有効性を示し，マルチエージェント系に適用する際には「どの経験データをどのexpertへ送るか」というrouter学習データ分配が主要論点になることを示唆している．


#### [An Introduction to Centralized Training for Decentralized Execution in Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/pdf/2409.03052)
[Christopher Amato](../Authors/overseas/ChristopherAmato.html)


### 2025
#### [Investigating the impact of direct punishment on the emergence of cooperation in multi-agent reinforcement learning systems](https://doi.org/10.1007/s10458-025-09698-5)
[Nayana Dasgupta](../Authors/overseas/NayanaDasgupta.html) [Mirco Musolesi](../Authors/overseas/MircoMusolesi.html)
Paper: Autonomous Agents and Multi-Agent Systems (Springer), 2025, Anastassacos et al.

MARL社会的ジレンマにおいて，直接罰・第三者罰・評判・パートナー選択が協調創発へ与える寄与を比較した研究．新規性は単一メカニズム評価ではなく制度設計の組み合わせ効果を同一枠組みで検証した点で，手法は反復ゲーム環境での強化学習エージェント比較実験，検証は協調率と社会厚生の時系列評価が中心．未解決論点は，罰のコスト設定や情報可視性の違いで得られる結論の外的妥当性である．

### 2021
#### [Cooperation and Reputation Dynamics with Reinforcement Learning](https://www.ifaamas.org/Proceedings/aamas2021/pdfs/p115.pdf)
[Julian Garcia](../Authors/overseas/JulianGarcia.html) [Nicolas Anastassacos](../Authors/overseas/NicolasAnastassacos.html) [Stephen Hailes](../Authors/overseas/StephenHailes.html) [Mirco Musolesi](../Authors/overseas/MircoMusolesi.html)
Paper: AAMAS 2021, Julian García, Nicolas Anastassacos, Stephen Hailes, Mirco Musolesi

評判形成が協調維持に効く条件を，MARLエージェントが社会規範を学習する過程として分析した研究．新規性は「評判メカニズム自体の学習ダイナミクス」に踏み込んだ点で，手法は社会的ジレンマ設定でのRLシミュレーションと規範パターン解析，検証は協調率・評判信号の安定性・制度条件比較で行う．論点は，評判ノイズや誤報が大きい環境での制度脆弱性と，partner selectionとの相互依存の切り分けである．

### 2020
#### [Partner Selection for the Emergence of Cooperation in Multi-Agent Systems Using Reinforcement Learning](https://arxiv.org/abs/1902.03185)
[Nicolas Anastassacos](../Authors/overseas/NicolasAnastassacos.html) [Stephen Hailes](../Authors/overseas/StephenHailes.html) [Mirco Musolesi](../Authors/overseas/MircoMusolesi.html)
Paper: AAAI 2020, Nicolas Anastassacos, Stephen Hailes, Mirco Musolesi

社会的ジレンマにおける協調創発を，行動選択に加えて「誰と相互作用するか」を学習対象に含めて検証した基盤研究．新規性は，自己利得最大化エージェントでもパートナーセレクション機構により協調クラスタが形成されうることを示した点で，手法は反復PD系設定でのMARL（行動＋相手選択の二重意思決定）である．検証は協調率・報酬分布・選択行動の推移で実施し，未解決点はスケール拡大時や部分観測下での再現性にある．
