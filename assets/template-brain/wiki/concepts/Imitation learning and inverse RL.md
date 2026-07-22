---
type: "concept"
title: "Imitation learning and inverse RL"
domain: "reinforcement learning: fundamentals, deep RL, RLHF/RLAIF and preference optimization, evaluation, tooling, and applied best practices"
status: "active"
created: "{{date}}"
updated: "{{date}}"
tags:
  - "#domain/reinforcement-learning-fundamentals-deep-rl-rlhf-rlaif-and-prefe"
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
  - "https://ai.stanford.edu/~ang/papers/icml00-irl.pdf"
  - "https://proceedings.mlr.press/v15/ross11a.html"
  - "https://proceedings.neurips.cc/paper/2016/hash/cc7e2b878868cbae992d1fb743995d8f-Abstract.html"
  - "https://arxiv.org/abs/1606.03476"
---

# Imitation learning and inverse RL

Confidence tag: evidence-based. Folded from canon `016-imitation-learning-and-inverse-rl.md` on the date in `updated`.

## Sourced Takeaways

Imitation learning uses demonstrations to learn behavior, while inverse reinforcement learning asks which reward could make demonstrated behavior optimal. Behavioral cloning learns actions directly by supervised learning, classical inverse RL searches over rewards, and GAIL learns a policy by adversarially matching the expert's discounted state-action occupancy. These objectives are related but not interchangeable, especially when the desired artifact is a transferable reward rather than a policy for the demonstrated environment.

- Behavioral cloning is supervised policy estimation and does not require environment interaction during fitting. [evidence-based]
- One-step imitation loss is measured on the expert's state distribution, while deployment decisions are made on the learner's induced state distribution, allowing errors to compound through covariate shift. [evidence-based]
- Inverse RL is underdetermined without extra assumptions because multiple rewards, including a trivial constant reward, can make the same policy optimal. [evidence-based]
- Any recovered reward is conditional on the modeled dynamics, discount, observation representation, reward class, and assumptions about demonstrator optimality. [evidence-based]
- GAIL bypasses an explicit intermediate reward-recovery stage and learns a policy by adversarial occupancy matching. [evidence-based]
- The GAIL derivation links a regularized IRL-plus-RL construction to occupancy matching, but it does not make the discriminator a uniquely identified human objective. [evidence-based]
- Model-free GAIL still needs learner rollouts from the environment, so expert-data efficiency and environment-interaction efficiency are separate quantities. [evidence-based]
- Policy imitation, behavior prediction, and transferable reward inference are distinct deliverables and should be evaluated against different success criteria. [practitioner]

## Best Practices

- Decide first whether the required output is an action policy, a reward for downstream planning, or an explanation of behavior; this choice determines whether cloning, direct imitation, or IRL fits the use case. [practitioner]
- Train behavioral cloning as a transparent baseline and evaluate it with closed-loop rollouts from deployment-relevant initial states, not only held-out action accuracy. [practitioner]
- Split validation data by complete trajectories or demonstrators when possible so adjacent state-action pairs from one rollout do not leak across evaluation partitions. [practitioner]
- For inverse RL, document the transition model, discount, reward feature class, optimality model, and regularization, then test how the inferred reward changes under plausible alternatives. [practitioner]
- For GAIL, track discriminator accuracy and loss together with policy return, occupancy summaries, entropy, KL movement, and environment steps; classifier saturation alone is not evidence of successful imitation. [practitioner]
- Balance discriminator and policy updates empirically, and rerun multiple seeds, because the cited paper does not establish a universal update ratio or architecture. [practitioner]
- Consider behavioral-cloning initialization when environment interaction is costly, while treating its benefit as task-dependent rather than guaranteed. [practitioner]
- Evaluate safety-relevant and task-relevant state visitation, not only aggregate return, because two policies can receive similar evaluation scores while differing on rare states. [practitioner]

## Evidence Caveats

- Ng and Russell's formal algorithms depend on known or estimated MDP structure and an optimality interpretation of behavior; they do not identify a unique true reward from demonstrations alone.
- Margin and norm choices resolve an optimization ambiguity by preference, not by proving that the selected reward is the demonstrator's internal objective.
- GAIL's occupancy and divergence characterization is exact for the stated mathematical setup. Finite trajectories, restricted networks, approximate discriminator updates, and approximate policy optimization introduce gaps.
- The GAIL experiments use simulated control tasks and generated expert policies. They do not establish reliability for human demonstrations, partial observability, real-world safety constraints, or severe dynamics mismatch.
- The GAIL paper reports strong results in its tested suite but also a task where behavioral cloning was more sample efficient, so it does not support universal superiority over cloning.
- Ho and Ermon explicitly note that their model-free method is not especially efficient in environment interaction, despite using expert demonstrations efficiently in their experiments.
- Neither source proves robustness to imperfect, heterogeneous, strategically misleading, or out-of-distribution demonstrations.
- Matching demonstrated occupancy can reproduce behavior without recovering intent, causal preferences, or a reward that transfers when dynamics or available actions change.
- Adversarial training and policy optimization can introduce seed sensitivity and optimization failures that the underlying occupancy objective does not eliminate.

## Sources

- Canon evidence file: `references/topics/016-imitation-learning-and-inverse-rl.md`
- Andrew Y. Ng and Stuart Russell (2000), "Algorithms for Inverse Reinforcement Learning," Proceedings of the Seventeenth International Conference on Machine Learning (ICML 2000). [Author-hosted primary paper PDF](https://ai.stanford.edu/~ang/papers/icml00-irl.pdf)
- Jonathan Ho and Stefano Ermon (2016), "Generative Adversarial Imitation Learning," Advances in Neural Information Processing Systems 29, arXiv:1606.03476. [Official NeurIPS proceedings](https://proceedings.neurips.cc/paper/2016/hash/cc7e2b878868cbae992d1fb743995d8f-Abstract.html) and [arXiv record](https://arxiv.org/abs/1606.03476)
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]
