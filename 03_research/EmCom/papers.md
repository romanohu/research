# EmCom 論文
- [Multi-Agent Cooperation and the Emergence of (Natural) Language(2016)](https://arxiv.org/abs/1612.07182)
- [Capacity, Bandwidth, and Compositionality in Emergent Language Learning(2019)](https://arxiv.org/abs/1910.11424)
- [Anti-efficient encoding in emergent communication(2019)](#anti-efficient-encoding-in-emergent-communication)
- [Compositionality and Generalization in Emergent Languages(2020)](https://arxiv.org/abs/2004.09124)
- [On the interaction between supervision and self-play in emergent communication(2020)](https://arxiv.org/abs/2002.01093)
- [Emergent Multi-Agent Communication in the Deep Learning  Era(2020)](https://arxiv.org/abs/2006.02419)
- [Emergent Communication of Generalizations(2021)](https://arxiv.org/abs/2106.02668)
- [Emergent Communication: Generalization and Overfitting in Lewis Games(2022)](https://arxiv.org/abs/2209.15342)
- [Emergent Communication at Scale(2022)](https://openreview.net/forum?id=AUGBfDIV9rL)
- [Linking Emergent and Natural Languages via Corpus Transfer(2022)](https://arxiv.org/abs/2203.13344)
- [On the Word Boundaries of Emergent Languages Based on Harris's Articulation Scheme(2023)](https://openreview.net/forum?id=b4t9_XASt6G)
- [One-to-Many Communication and Compositionality  in Emergent Communication(2024)](https://openreview.net/forum?id=mfgcxMm5aa)
- [Speaking Your Language: Spatial Relationships in Interpretable Emergent Communication(2024)](https://arxiv.org/abs/2406.07277)
- [Knowledge Distillation from Language-Oriented to Emergent Communication for Multi-Agent Remote Control(2024)](#knowledge-distillation-from-language-oriented-to-emergent-communication-for-multi-agent-remote-control)
- [Unsupervised Translation of Emergent Communication](#unsupervised-translation-of-emergent-communication)

## サーベイ
- [言語とコミュニケーションの創発に関する構成論的研究の展開(2024)](https://www.jstage.jst.go.jp/article/jcss/31/1/31_2023.073/_article/-char/ja/)
- [Emergent language: a survey and taxonomy(2025)](#emergent-language-a-survey-and-taxonomy)
- [The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs](#the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why----a-survey-from-marl-to-emergent-language-and-llms)

---

## 論文メモ
### 2019
#### [Anti-efficient encoding in emergent communication](https://arxiv.org/abs/1905.12561)
[Rahma Chaabouni](../Authors/overseas/RahmaChaabouni.html) [Eugene Kharitonov](../Authors/overseas/EugeneKharitonov.html) [Emmanuel Dupoux](../Authors/overseas/EmmanuelDupoux.html) [Marco Baroni](../Authors/overseas/MarcoBaroni.html)
### 2021
#### Emergent Communication of Generalizations
[Jesse Mu](../Authors/overseas/JesseMu.html)
従来のLewis形式の参照ゲームは、それから発生するコミュニケーションは対象となる単一のオブジェクトに特化した一意なメッセージの出現しか促さず、人間的な抽象概念を持つ言語の出現が促されることはなかった．それは、例えば対象オブジェクトがとある画像であったとすると、それに含まれる微細なノイズや擬似的なパターンにまでも適応(過学習)してしまうことや、複数の物体に跨って初めて意味を持つ概念(xorなど)を理解できないことが原因だとしている．そこで、setrefゲームとconceptゲームを提案する．
setrefゲームは教師が(単一の物体ではなく)とある概念に属する物体のグループを見て、それを生徒に伝達するタスク．ただし、教師と生徒は同じ入力を見る．
conceptゲームは、それに加えて教師と生徒が異なる入力を見る．
これらはLewis型のシグナルゲームを集合へと拡張したものと捉えることができる．
**後半の評価指標や数式への理解が足りないので、また読む**

### 2022
#### [Linking Emergent and Natural Languages via Corpus Transfer](https://arxiv.org/abs/2203.13344)
[Shunyu Yao](../Authors/overseas/ShunyuYao.html) [Mo Yu](../Authors/overseas/MoYu.html) [Yang Zhang](../Authors/overseas/YangZhang.html) [Karthik R Narasimhan](../Authors/overseas/KarthikRNarasimhan.html) [Joshua B. Tenenbaum](../Authors/overseas/JoshuaBTenenbaum.html) [Chuang Gan](../Authors/overseas/ChuangGan.html)
創発言語と自然言語の接続．創発言語のコーパスを作り、それを自然言語と結びつきつかせようとしている．創発言語の評価を自然言語で行う．

### 2024
#### One-to-Many Communication and Compositionality  in Emergent Communication
[Heeyoung Lee](../Authors/overseas/HeeyoungLee.html)
多対一コミュニケーション環境における構成性の出現に着眼した論文．主張としては、リスナが「多」であることにより発生する環境的な圧力が、スピーカのメッセージの構成性を促進する．
環境的圧力1:リスナがそれぞれ異なるメッセージの特定の部分(特定の要素)にのみ関心を持つことで、スピーカに「メッセージの一部にしか関心が無いリスナに対してもより理解しやすい」ようにメッセージを構成するような圧力が働く
環境的圧力2:メッセージが複数のリスナに同時に処理されるという協調圧力によって、スピーカは「メッセージを誰が受け取っても分かるような形に」構成する?

#### [Knowledge Distillation from Language-Oriented to Emergent Communication for Multi-Agent Remote Control](https://arxiv.org/abs/2401.12624)
[Yongjun Kim](../Authors/overseas/YongjunKim.html) [Sejin Seo](../Authors/overseas/SejinSeo.html) [Jihong Park](../Authors/overseas/JihongPark.html) [Mehdi Bennis](../Authors/overseas/MehdiBennis.html) [Seong-Lyun Kim](../Authors/overseas/SeongLyunKim.html) [Junil Choi](../Authors/overseas/JunilChoi.html)

### 2025
#### [Emergent language: a survey and taxonomy](https://arxiv.org/abs/2409.02645)
[Jannik Peters](../Authors/overseas/JannikPeters.html) [Constantin Waubert de Puiseau](../Authors/overseas/ConstantinWaubertDePuiseau.html) [Hasan Tercan](../Authors/overseas/HasanTercan.html) [Arya Gopikrishnan](../Authors/overseas/AryaGopikrishnan.html) [Gustavo Adolpho Lucas De Carvalho](../Authors/overseas/GustavoAdolphoLucasDeCarvalho.html) [Christian Bitter](../Authors/overseas/ChristianBitter.html) [Tobias Meisen](../Authors/overseas/TobiasMeisen.html)

#### [Unsupervised Translation of Emergent Communication](https://arxiv.org/abs/2502.07552)
[Ido Levy](../Authors/overseas/IdoLevy.html) [Orr Paradise](../Authors/overseas/OrrParadise.html) [Boaz Carmeli](../Authors/overseas/BoazCarmeli.html) [Ron Meir](../Authors/overseas/RonMeir.html) [Shafi Goldwasser](../Authors/overseas/ShafiGoldwasser.html) [Yonatan Belinkov](../Authors/overseas/YonatanBelinkov.html)


### 2026
#### [The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs](https://arxiv.org/abs/2602.11583)
