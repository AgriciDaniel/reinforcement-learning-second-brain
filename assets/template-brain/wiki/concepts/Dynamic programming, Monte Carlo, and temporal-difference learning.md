---
type: "concept"
title: "Dynamic programming, Monte Carlo, and temporal-difference learning"
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
  - "https://mitpress.mit.edu/9780262039246/reinforcement-learning/"
  - "http://incompleteideas.net/book/RLbook2020.pdf"
  - "https://doi.org/10.1007/BF00115009"
---

# Dynamic programming, Monte Carlo, and temporal-difference learning

Confidence tag: evidence-based. Folded from canon `003-dynamic-programming-monte-carlo-and-temporal-difference-learning.md` on the date in `updated`.

## Sourced Takeaways

Dynamic programming (DP), Monte Carlo (MC), and temporal-difference (TD) learning are three complementary ways to estimate value functions and improve policies in finite Markov decision processes. DP backs up expected values using a known environment model, MC learns from complete sampled returns without a model, and TD learns from sampled transitions while bootstrapping from its own current estimates. Their differing use of models, sampling, and bootstrapping is a central design axis for reinforcement-learning algorithms.

- DP uses full model-based expectations, MC uses complete sampled returns, and TD uses sampled one-step or multi-step bootstrapped targets. [evidence-based]
- Bootstrapping means updating an estimate from another learned estimate, not merely reusing data or resampling a dataset. [evidence-based]
- Tabular Bellman operators explain why repeated evaluation and greedy improvement can be interleaved as generalized policy iteration. [evidence-based]
- MC prediction does not require a transition model, but its basic episodic form must wait until the sampled return is known. [evidence-based]
- TD can learn online before an episode ends and can be applied naturally to continuing tasks. [evidence-based]
- MC targets are unbiased samples of the return under the sampled policy, whereas one-step TD targets generally introduce bootstrap bias and often lower variance. [evidence-based]
- The choice of backup depth changes bias, variance, delay, and computational allocation, so no single depth is uniformly best across tasks. [practitioner]
- Off-policy correction can have high variance because products of importance ratios may become extremely large or collapse to zero. [evidence-based]

## Best Practices

- Start with exact DP when the finite model is available and small enough to sweep, because it provides a useful correctness oracle for sampled implementations. [practitioner]
- For iterative policy evaluation, monitor a documented maximum value change and treat the stopping tolerance as an approximation choice, not a proof that the policy is exact. [practitioner]
- Use action values rather than state values for model-free control unless a separate model supplies the one-step action comparison. [evidence-based]
- Use incremental sample averages when stationarity and equal weighting are intended, and a constant step size when recent data should retain influence. [practitioner]
- Handle terminal transitions explicitly by setting the bootstrap contribution after termination to zero. [evidence-based]
- Sweep step size, exploration, backup depth, and trace decay across multiple seeds, because their interactions can dominate tabular learning curves. [practitioner]
- Prefer weighted importance sampling when bounded, lower-variance estimates are operationally more important than preserving ordinary importance sampling's unbiasedness. [practitioner]
- Test tiny deterministic and stochastic MDPs with known values before trusting an implementation on a larger environment. [practitioner]

## Evidence Caveats

- The textbook's tabular convergence results rely on assumptions such as finite representations, appropriate step-size schedules, adequate visitation, and stationary Markov dynamics. They do not automatically transfer to nonlinear function approximation. [evidence-based]
- DP sweeps are computational abstractions, and a known model can still be too large for exhaustive backups. [evidence-based]
- The broad bias-variance comparison between MC and TD does not determine which method learns faster on a particular task, representation, or data stream. [practitioner]
- Importance-sampled off-policy estimates can be dominated by rare trajectories, so small experiments may show severe seed and episode-length variance. [evidence-based]
- The cited sources establish algorithms and theory, not a universal hyperparameter setting, benchmark ranking, or state-of-the-art empirical claim. [evidence-based]
- Reported results should distinguish environment stochasticity, exploratory-policy randomness, initialization, and implementation details rather than attributing all variation to the algorithm family. [practitioner]

## Sources

- Canon evidence file: `references/topics/003-dynamic-programming-monte-carlo-and-temporal-difference-learning.md`
- Richard S. Sutton and Andrew G. Barto (2018), *Reinforcement Learning: An Introduction*, second edition, Chapters 4 to 7, The MIT Press: https://mitpress.mit.edu/9780262039246/reinforcement-learning/
- Richard S. Sutton and Andrew G. Barto (2020), complete second-edition author-hosted text: http://incompleteideas.net/book/RLbook2020.pdf
- Richard S. Sutton (1988), “Learning to Predict by the Methods of Temporal Differences,” *Machine Learning* 3, DOI: https://doi.org/10.1007/BF00115009
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]
