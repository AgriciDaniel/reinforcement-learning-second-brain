---
type: "concept"
title: "Multi-agent RL"
domain: "reinforcement learning"
status: "active"
created: "2026-07-22"
updated: "2026-07-22"
tags:
  - "#domain/reinforcement-learning"
  - "#type/concept"
  - "#confidence/evidence-based"
confidence: "evidence-based"
related:
  - "[[Index]]"
  - "[[CONVENTIONS]]"
  - "[[Best Practices Kernel]]"
  - "[[Source Intake Workflow]]"
  - "[[Research Refresh Workflow]]"
  - "[[Synthesis Workflow]]"
  - "[[wiki/concepts/_index|Concepts Hub]]"
  - "[[Dashboard]]"
  - "[[Tag Taxonomy]]"
  - "[[Claim Verification Flow]]"
  - "[[Reporting Workflow]]"
  - "[[Source Manifest Guide]]"
  - "[[Health Scorecard]]"
  - "[[Action Roadmap]]"
  - "[[Weekly Report]]"
  - "[[Approval Queue]]"
  - "[[wiki/flows/_index|Flows Hub]]"
  - "[[wiki/sources/_index|Sources Hub]]"
  - "[[wiki/decisions/_index|Decisions Hub]]"
  - "[[wiki/deliverables/_index|Deliverables Hub]]"
  - "[[wiki/reports/_index|Reports Hub]]"
  - "[[wiki/questions/_index|Questions Hub]]"
  - "[[wiki/gaps/_index|Gaps Hub]]"
  - "[[wiki/experiments/_index|Experiments Hub]]"
source_urls:
  - "https://proceedings.neurips.cc/paper_files/paper/2017/hash/68a9750337a418a86fe06c1991a1d64c-Abstract.html"
  - "https://proceedings.mlr.press/v80/rashid18a.html"
---

# Multi-agent RL

Confidence tag: evidence-based. Folded from canon `014-multi-agent-rl.md` on the date in `updated`.

## Sourced Takeaways

Multi-agent reinforcement learning studies sequential decisions when several adaptive agents jointly affect transitions and rewards. Each learner faces strategic dependence, partial information, and moving co-learners, so a process that appears stationary in the joint state can be nonstationary from one agent's local perspective. Centralized training with decentralized execution uses joint information to improve learning while preserving the information and action constraints imposed at execution.

- The relevant formal object is a joint policy in a Markov game or partially observable stochastic game, even when learning code exposes one agent at a time. [evidence-based]
- Simultaneously changing policies create nonstationarity for local learners and complicate replay, exploration, and attribution of reward. [evidence-based]
- Centralized training may use joint observations, actions, or global state, but decentralized execution must not depend on information unavailable to an acting agent. [evidence-based]
- MADDPG conditions each agent's critic on joint actions while keeping its actor local, which supports cooperative, competitive, and mixed reward structures considered in the paper. [evidence-based]
- QMIX makes joint greedy maximization tractable by monotonic value factorization, but this restriction excludes some joint value functions. [evidence-based]
- Parameter sharing, a centralized critic, and a shared team reward are separate design choices and should not be conflated. [practitioner]
- Training against a narrow population can produce coordination conventions or exploits that fail with new partners, opponents, or population sizes. [practitioner]

## Best Practices

- Specify observations, action timing, rewards, communication, agent identities, termination semantics, and which information exists only during training before choosing an algorithm. [practitioner]
- Match the method to the game: MADDPG is naturally aligned with the paper's continuous-action mixed settings, while QMIX assumes a cooperative objective and decentralized discrete greedy actions. [evidence-based]
- Store synchronized joint transitions for centralized critics or mixers, and mask unavailable actions plus terminated agents consistently in both online and target calculations. [practitioner]
- Test execution code with privileged state removed; a centralized-training feature leak can create an apparently strong policy that is not deployable. [practitioner]
- Use target networks, controlled replay age, gradient diagnostics per agent, and explicit checks for one learner dominating the joint loss. [practitioner]
- Evaluate independent seeds and held-out partner or opponent populations, including cross-play rather than only self-play with the final training cohort. [practitioner]
- Report per-agent returns, team return where applicable, success criteria, and dispersion across runs; a single aggregate can hide asymmetric failure. [practitioner]

## Evidence Caveats

- MADDPG's experiments use a limited collection of particle-world cooperative and competitive tasks. They do not establish universal scaling, robustness, or superiority over later methods.
- The policy-ensemble results in MADDPG are empirical and environment-specific; ensemble training does not prove generalization to arbitrary strategic behavior.
- QMIX's original evidence comes from cooperative StarCraft II micromanagement tasks and contemporaneous baselines under the paper's protocol. Reported comparisons should remain scoped to that setup.
- QMIX's monotonic mixing is sufficient for decentralized argmax consistency, but some coordination problems require action rankings that depend non-monotonically on other agents' actions.
- Centralized training assumes privileged joint information and a training infrastructure that can align experience across agents. Those assumptions may fail in distributed or privacy-constrained systems.
- Neither source resolves equilibrium selection, opponent adaptation, communication learning, open populations, or reliable generalization across numbers and types of agents.
- Apparent nonstationarity does not by itself identify the root cause of a failed run; representation, exploration, reward design, and implementation errors remain competing explanations.
- Results can vary with seeds, teammate populations, evaluation opponents, environment versions, and tie-breaking, so single-seed win rates are weak evidence.

## Sources

- Canon evidence file: `references/topics/014-multi-agent-rl.md`
- Ryan Lowe, Yi Wu, Aviv Tamar, Jean Harb, Pieter Abbeel, and Igor Mordatch (2017), *Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments*, Advances in Neural Information Processing Systems 30, arXiv:1706.02275. https://proceedings.neurips.cc/paper_files/paper/2017/hash/68a9750337a418a86fe06c1991a1d64c-Abstract.html
- Tabish Rashid, Mikayel Samvelyan, Christian Schroeder de Witt, Gregory Farquhar, Jakob Foerster, and Shimon Whiteson (2018), *QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning*, Proceedings of the 35th International Conference on Machine Learning, PMLR 80, arXiv:1803.11485. https://proceedings.mlr.press/v80/rashid18a.html
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]
