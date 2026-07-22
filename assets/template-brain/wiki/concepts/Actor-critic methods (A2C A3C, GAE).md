---
type: "concept"
title: "Actor-critic methods (A2C A3C, GAE)"
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
  - "https://proceedings.neurips.cc/paper_files/paper/1999/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html"
  - "https://arxiv.org/abs/1602.01783"
  - "https://arxiv.org/abs/1506.02438"
  - "https://openai.com/index/openai-baselines-acktr-a2c/"
  - "https://mitpress.mit.edu/9780262039246/reinforcement-learning/"
---

# Actor-critic methods (A2C A3C, GAE)

Confidence tag: evidence-based. Folded from canon `008-actor-critic-methods-a2c-a3c-gae.md` on the date in `updated`.

## Sourced Takeaways

Actor-critic methods couple a parameterized policy, the actor, with a learned value estimator, the critic, that supplies lower-variance credit signals.
They trade the pure Monte Carlo estimator of REINFORCE for bootstrapped targets that can reduce variance while introducing bias from value approximation.
A3C organizes many actor-learners asynchronously, A2C is the later synchronous batching convention, and generalized advantage estimation (GAE) exposes a tunable bias-variance continuum for the actor's advantage target.

- The critic is a learned control variate and bootstrap mechanism, not an oracle; critic error directly shapes the actor's update signal. [evidence-based]
- Actor-critic updates combine policy-gradient learning with temporal-difference value estimation, often on different effective time scales. [evidence-based]
- Multi-step returns interpolate between short bootstrapped targets and longer sampled returns. [evidence-based]
- GAE is an exponentially weighted sum of TD residuals and is equivalent to a particular mixture of multi-step advantage estimators. [evidence-based]
- A3C's defining systems feature is asynchronous shared-parameter learning from parallel environment workers. [evidence-based]
- A2C synchronizes actor rollouts and updates, which changes batching, staleness, throughput, and reproducibility properties without changing the core actor-critic estimator family. [practitioner]
- Shared policy and value representations can improve computational reuse, but joint gradients can also create interference between the two objectives. [practitioner]

## Best Practices

- Distinguish true termination from time-limit truncation; bootstrap across a truncation when the continuing-task semantics require it. [evidence-based]
- Detach GAE or return targets in the policy loss, and prevent the bootstrap target from moving through the critic target unless a derived residual-gradient method is intended. [practitioner]
- Tune rollout length and \(\lambda\) together because both control how much bootstrapping and temporal credit enter the update. [evidence-based]
- Normalize advantages only within a clearly defined batch and record the choice, since it changes sample weighting and gradient scale even when it often helps optimization. [practitioner]
- Monitor value loss, explained variance, policy entropy, gradient norms, policy change, and return distributions across several seeds. [practitioner]
- For A3C, measure worker policy lag and nondeterminism; for A2C, measure synchronization idle time and the effect of larger correlated batches. [practitioner]
- Treat entropy and value-loss coefficients, gradient clipping, optimizer state, reward scaling, and recurrent-state masks as first-class experimental settings. [practitioner]
- Recompute recurrent hidden-state boundaries and masks carefully when batching partial episodes, especially after truncation or environment reset. [practitioner]

## Evidence Caveats

Konda and Tsitsiklis analyze two-time-scale actor-critic algorithms under assumptions including linear critic structure; those results do not automatically establish convergence for deep shared networks.
The A3C paper reports empirical outcomes for its tasks, architectures, preprocessing, and compute setting, not a universal benefit from asynchronous updates.
A2C's synchronous label covers implementation variants, and its performance relative to A3C depends on hardware, batch construction, policy lag, and environment cost.
GAE's bias and variance depend jointly on \(\gamma\), \(\lambda\), critic error, rollout truncation, and the objective being approximated.
Single-seed curves and aggregate means can conceal instability, while value loss alone does not establish that the critic produces useful policy-gradient directions.

## Sources

- Canon evidence file: `references/topics/008-actor-critic-methods-a2c-a3c-gae.md`
- Vijay R. Konda and John N. Tsitsiklis (2000; NeurIPS 12 conference proceedings), "Actor-Critic Algorithms": https://proceedings.neurips.cc/paper_files/paper/1999/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html
- Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, and Koray Kavukcuoglu (2016), "Asynchronous Methods for Deep Reinforcement Learning," ICML, arXiv:1602.01783: https://arxiv.org/abs/1602.01783
- John Schulman, Philipp Moritz, Sergey Levine, Michael I. Jordan, and Pieter Abbeel (2015), "High-Dimensional Continuous Control Using Generalized Advantage Estimation," arXiv:1506.02438: https://arxiv.org/abs/1506.02438
- Yuhuai Wu, Elman Mansimov, Shun Liao, Alec Radford, and John Schulman (2017), "OpenAI Baselines: ACKTR & A2C," official implementation note: https://openai.com/index/openai-baselines-acktr-a2c/
- Richard S. Sutton and Andrew G. Barto (2018), *Reinforcement Learning: An Introduction*, second edition, Chapter 13, MIT Press: https://mitpress.mit.edu/9780262039246/reinforcement-learning/
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]
