---
type: "concept"
title: "Exploration strategies and intrinsic motivation"
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
  - "http://incompleteideas.net/book/the-book-2nd.html"
  - "https://arxiv.org/abs/1801.01290"
  - "https://arxiv.org/abs/1606.01868"
  - "https://proceedings.mlr.press/v70/pathak17a.html"
  - "https://arxiv.org/abs/1705.05363"
  - "https://arxiv.org/abs/1810.12894"
---

# Exploration strategies and intrinsic motivation

Confidence tag: evidence-based. Folded from canon `012-exploration-strategies-and-intrinsic-motivation.md` on the date in `updated`.

## Sourced Takeaways

Exploration is the problem of choosing actions that improve both immediate control and the information available for later decisions.
Random action selection, optimism, count bonuses, entropy, and learned intrinsic rewards induce different data distributions, so they are not interchangeable forms of noise.
Intrinsic-motivation methods such as ICM and RND can make sparse-reward learning possible in some domains, but their prediction errors are proxy objectives whose scale, nonstationarity, and failure modes must be measured directly.

- Exploration changes what the learner can observe, so an unbiased update cannot recover values for consequential trajectories that behavior never visits. [evidence-based]
- Epsilon-greedy and entropy encourage action diversity locally, while count and prediction-error bonuses explicitly value forms of state novelty. [evidence-based]
- Tabular counts have clear visitation semantics, but generalizing novelty in high-dimensional observations requires a representation or density model. [evidence-based]
- ICM computes novelty as forward prediction error in features shaped by an inverse-dynamics objective. [evidence-based]
- RND computes novelty as error in matching fixed random target features, without learning a forward action-conditioned dynamics model. [evidence-based]
- Prediction error mixes novelty with model capacity, optimization progress, observation noise, and nonstationarity, so it is not calibrated epistemic uncertainty by default. [practitioner]
- Persistent intrinsic reward changes the optimized return and can keep rewarding novelty after it stops helping the extrinsic task. [practitioner]
- No exploration method is uniformly best across short-horizon bandits, sparse-reward navigation, stochastic environments, and safety-constrained control. [contested]

## Best Practices

- In small discrete problems, establish epsilon-greedy, upper-confidence, or exact-count baselines before adding learned novelty machinery. [evidence-based]
- Log extrinsic reward, intrinsic reward, entropy, visitation coverage, and goal-reaching success as separate time series. [practitioner]
- Normalize observations and bonus-derived returns using a documented procedure, and monitor the normalization statistics for drift. [evidence-based]
- Sweep the intrinsic-reward coefficient and entropy coefficient independently because they alter different parts of the behavior objective. [practitioner]
- Test the exploration module against stochastic distractors, uncontrollable pixels, and revisitable novelty sources that can generate prediction error without progress. [practitioner]
- Keep the RND target frozen, prevent accidental gradient flow into it, and verify that predictor loss decreases on replayed familiar observations. [evidence-based]
- Evaluate with intrinsic reward disabled from the reported task score, while documenting whether the behavior policy itself remains stochastic. [practitioner]
- Use multiple seeds and report both final task return and exploration-process metrics, since rare discovery events can make averages unstable. [practitioner]

## Evidence Caveats

Finite-time guarantees for particular bandit confidence bounds or tabular count schemes do not automatically transfer to deep RL with aliased observations, replay, bootstrapping, and changing representations.
Pseudo-count behavior depends on properties of the density model and its update, so an arbitrary likelihood or reconstruction error is not automatically a valid count.

ICM was evaluated in specific visual-control settings including VizDoom and Super Mario Bros.
Its inverse-dynamics representation can suppress some uncontrollable variation, but the paper does not prove immunity to every stochastic distractor or preservation of every task-relevant but uncontrollable feature.

RND's main evidence comes from hard-exploration Atari experiments with a particular policy-optimization and normalization design.
RND error is affected by predictor architecture, training frequency, data order, and generalization, and the fixed random target does not make the error a calibrated posterior uncertainty estimate.

Headline results in sparse-reward environments can depend on seeds, environment versions, sticky-action settings, termination rules, and evaluation protocols.
Intrinsic motivation alone does not impose safety constraints, prevent irreversible exploration, or guarantee that discovered behavior aligns with the intended task reward.
Comparisons should therefore match interaction budgets and implementation details, report dispersion across runs, and distinguish discovery probability from performance conditional on discovery.

## Sources

- Canon evidence file: `references/topics/012-exploration-strategies-and-intrinsic-motivation.md`
- Richard S. Sutton and Andrew G. Barto (2018), *Reinforcement Learning: An Introduction*, second edition, Chapter 2, "Multi-armed Bandits," [official book site](https://incompleteideas.net/book/the-book-2nd.html).
- Marc G. Bellemare, Sriram Srinivasan, Georg Ostrovski, Tom Schaul, David Saxton, and Remi Munos (2016), "Unifying Count-Based Exploration and Intrinsic Motivation," NeurIPS 2016, [arXiv:1606.01868](https://arxiv.org/abs/1606.01868).
- Deepak Pathak, Pulkit Agrawal, Alexei A. Efros, and Trevor Darrell (2017), "Curiosity-driven Exploration by Self-supervised Prediction," ICML 2017, [arXiv:1705.05363](https://arxiv.org/abs/1705.05363).
- Yuri Burda, Harrison Edwards, Amos Storkey, and Oleg Klimov (2018), "Exploration by Random Network Distillation," [arXiv:1810.12894](https://arxiv.org/abs/1810.12894).
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]
