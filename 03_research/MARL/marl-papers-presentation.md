---
marp: true
theme: default
paginate: true
size: 16:9
---

<style>
section {
  font-size: 28px;
  line-height: 1.4;
}
h1, h2 {
  letter-spacing: 0.01em;
}
ul {
  margin-top: 0.8em;
  margin-bottom: 0.8em;
}
</style>

---

# CMARL MARL Paper Highlights
## Synthesizing notes from `03_research/MARL/papers.md`

- Each slide distills a single paper from the collected notes.
- Focus on cooperation, coordination, and intrinsic motivation.
- Ideal for high-level briefing or review prep.

---

## Agenda
1. Sequential social dilemmas & intrinsic drives (2017–2018)
2. Reciprocity, social preferences, and coordination (2019–2020)
3. Surveys & cooperation panoramas (2021–2023)
4. Benchmarks & evaluation suites (2025)
5. Summary and Q&A

---

## Section: 2017–2018 Social Dilemmas & Intrinsic Motivation
- SSD as a foundation for subsequent cooperative RL work.
- Intrinsic rewards emerge as a recurring lever for guiding agents.
- These slides cover the formative papers in the notes.

---

## Multi-agent Reinforcement Learning in Sequential Social Dilemmas (2017)
- Introduced Sequential Social Dilemma (SSD) as temporally extended Markov games showing policy-level cooperation.
- SSD can distinguish games that appear identical in traditional payoff matrices.
- Emphasized descriptive analysis of emergent behaviors and hyperparameter sensitivity.

---

## Multiagent cooperation and competition with deep reinforcement learning (2017)
- Pong env with tunable reward parameter \(p\) reveals cooperation vs competition regimes.
- Multiplayer DQN without a fixed-policy opponent develops more robust strategies than single-player DQN.
- Perspective: reward shaping can steer multi-agent emergent behavior.

---

## Maintaining cooperation in complex social dilemmas using deep reinforcement learning (2018)
- Tackled TFT-style cooperative agents by expanding into amTFT for deep RL.
- Aim: create single-agent architectures that behave cooperatively without multi-agent training tricks.
- Frames cooperation as policy design rather than centralized control.

---

## Inequity aversion improves cooperation in intertemporal social dilemmas (2018)
- Adds inequity aversion to SSD rewards to align self-interest with social welfare.
- Agents penalize disparities, leading to more collaborative trajectories.
- Shows social considerations can be baked directly into reward shaping.

---

## Learning through Probing (2018)
- Proposes LTP, splitting probing and learning to observe opponent reactions.
- Adjusts learning rewards using η to value how one’s action shifts others’ future policies.
- Enables Q-learning agents to internalize the long-term social impact without opponent modeling.

---

## Evolving intrinsic motivations for altruistic behavior (2018)
- Two-level architecture: RL at episode level, evolution of intrinsic-motivation modules across generations.
- Intrinsic rewards evolve to prefer altruistic behaviors that benefit group fitness.
- Demonstrated stable cooperation in intertemporal social dilemma simulations without engineered rewards.

---

## Exploration by Random Network Distillation (2018)
- Introduces RND intrinsic reward: prediction error of a learned network versus fixed random target.
- Encourages visiting novel states, avoids noisy-TV pitfalls by keeping target static.
- Learns intrinsic value separately from extrinsic returns for stability.

---

## Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning (2018)
- Adds influence reward measuring KL divergence between predicted opponent actions with/without current action.
- Encourages actions that meaningfully steer others’ behavior while remaining self-consistent.
- Short-term coercive moves lose long-term influence, keeping behavior grounded.

---

## Section: 2019–2020 Reciprocity & Social Preferences
- Papers shift toward reciprocity, policy regularization, and explicit preference diversity.
- Continued emphasis on intrinsic motivation and stable coordination.
- Highlights how reward design and regularization sculpt cooperation.

---

## Learning Reciprocity in Complex Sequential Social Dilemmas (2019)
- Builds on SSD to reward reciprocity: agents track how their actions affect others’ rewards.
- Intrinsic reciprocity reward augments environment reward for responsive strategies.
- Focuses on mutual adaptation to sustain cooperation in complex games.

---

## Promoting Coordination through Policy Regularization in Multi-Agent Deep Reinforcement Learning (2020)
- Introduces policy regularizers that penalize deviations from coordination-friendly behavior.
- Regularization smooths updates so agents avoid destabilizing selfish swings.
- Shows coordination improves when policies stay aligned via shared regularization terms.

---

## Social diversity and social preferences in mixed-motive reinforcement learning (2020)
- Injects Social Value Orientation (SVO) per agent to capture ideal reward splits.
- Defines reward angle \( \theta \) to blend self vs others’ payoffs and derive intrinsic reward.
- Demonstrates how preference diversity produces richer, more cooperative populations.

---

## Section: 2021–2023 Surveys & Cooperation Panoramas
- Comprehensive reviews synthesize trends across social dilemmas, coordination, and learning dynamics.
- These surveys are helpful springboards for spotting open challenges.
- Notes mention distributed training insights and the role of actor similarity.

---

## Multi-agent deep reinforcement learning: a survey (2021)
- Survey covers mixed settings (general-sum games), independent learners, and POMG experiments.
- Deep dive into Distributed Training, Distributed Execution (DTDE) and its clarity.
- Lists key references to trace foundational works like Leibo (2017).

---

## Birds of a Feather Flock Together: Cooperation Emergence via Multi-Agent RL (2021)
- Diagnoses instability from selfish incentive-giving as a “second-order social dilemma.”
- Introduces homophilic incentives to keep agents aligned with like-minded partners.
- Homophily stabilizes cooperation in the Public Goods and Commons dilemmas.

---

## A Review of Cooperative Multi-Agent Deep Reinforcement Learning (2022)
- Notes many MARL problems are NP-hard and focus on distributed cooperative objectives.
- Highlights practical tactics: parameter sharing, tuned learning rates, and role assignments.
- Offers a structured lens on how to relax limits of independent learners (ILs).

---

## A Review of Cooperation in Multi-agent Learning (2023)
- Synthesizes cooperation-focused results beyond pure RL, touching on behavioral lenses.
- Co-authors include Leibo, Islam, Willis, and Sunehag, tying earlier threads together.
- Serves as a checklist of models, mechanisms, and mathematical challenges for cooperation.

---

## Section: 2025 Benchmarks & Evaluation Suites
- Future-facing work refines evaluation tools for zero-shot coordination and social dilemmas.
- Includes both empirical benchmarks and abstracted simulators.
- Sets stage for verifying MARL methods under structured diversity.

---

## A Comprehensive Survey on Multi-Agent Cooperative Decision-Making (2025)
- Maps scenarios, approaches, and persistent challenges in cooperative decision-making.
- Emphasizes multi-agent perspectives across decentralization, observability, and communication.
- Points toward emerging perspectives for future MARL deployments.

---

## OVERCOOKEDV2: RETHINKING OVERCOOKED FOR ZERO-SHOT COORDINATION (2025)
- Frames Zero-Shot Coordination (ZSC) with the SP-XP gap between self-play and cross-play.
- Argues limited state diversity during training causes ZSC failures; proposes state augmentation.
- Proposes OvercookedV2 benchmark with partial observations, asymmetries, and optional communication.

---

## SocialJax: An Evaluation Suite for Multi-agent Reinforcement Learning in SSDs (2025)
- Offers SocialJax for SSD evaluation with abstracted 11×11 grid instead of pixel inputs.
- Environment encodes payoff structure mathematically rather than via RGB observations.
- Links to Google Sites and GitHub for the suite and documentation.

---

## Summary & Next Steps
- SSD formulations plus intrinsic rewards have shaped MARL cooperation design choices.
- Reciprocity, regularization, and social preference modeling stabilize multi-agent outcomes.
- Surveys and benchmarks (OvercookedV2, SocialJax) highlight where future coordination research should land.

---

## Q&A / Further Reading
- Slides derived from `03_research/MARL/papers.md` notes.
- Happy to expand slides with diagrams, experiments, or extra papers.
- Questions, gaps in the notes, or preferred focus for the next review?
