---
type: "concept"
title: "Offline batch RL and conservatism"
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
  - "https://arxiv.org/abs/2005.01643"
  - "https://proceedings.mlr.press/v97/fujimoto19a.html"
  - "https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html"
---

# Offline batch RL and conservatism

Confidence tag: evidence-based. Folded from canon `013-offline-batch-rl-and-conservatism.md` on the date in `updated`.

## Sourced Takeaways

Offline reinforcement learning learns a policy only from a fixed dataset of logged transitions, without collecting corrective experience during training. Its central difficulty is distributional shift: policy improvement can select actions that are poorly represented in the data, while bootstrapping assigns those actions unsupported values. Conservative methods control this failure by restricting the learned policy toward dataset support, lowering values for unsupported actions, or combining both mechanisms.

- Offline RL differs from ordinary replay-based off-policy RL because fresh interaction cannot repair critic errors or missing coverage. [evidence-based]
- Bootstrapping, function approximation, and policy-induced distribution shift interact: an out-of-distribution action can receive an erroneous value and then be amplified by maximization. [evidence-based]
- Dataset quality includes state coverage, action coverage, reward validity, terminal semantics, and the mixture of behavior policies, not merely transition count. [practitioner]
- BCQ constrains candidate actions through a learned behavior-support model and a bounded perturbation, rather than trusting unconstrained actor maximization. [evidence-based]
- CQL regularizes the critic so that unsupported actions are assigned lower values relative to logged actions; its theoretical lower-bound statements depend on the paper's assumptions and objective variant. [evidence-based]
- Behavior constraint and value pessimism address related distribution-shift failures but are not mathematically interchangeable. [evidence-based]
- No offline objective can infer reliable consequences for state-action regions that the data and modeling assumptions leave unidentified. [evidence-based]

## Best Practices

- Preserve trajectories, time-limit flags, true terminal flags, behavior metadata, and reward transformations before training; a malformed dataset changes the learning problem. [practitioner]
- Start with behavior cloning and an unconstrained off-policy baseline to expose whether claimed gains come from return optimization, conservatism, or simple imitation. [practitioner]
- Tune CQL's conservatism coefficient or BCQ's perturbation radius on multiple dataset regimes, and report the selection rule without using hidden online returns. [practitioner]
- Monitor critic values on logged actions and deliberately perturbed actions; widening gaps or extreme extrapolated values are useful alarms, not proof of policy quality. [practitioner]
- Use separate random seeds for dataset generation, optimization, and evaluation, and report uncertainty across datasets when data collection itself is stochastic. [practitioner]
- Treat offline policy selection as a first-class problem: combine held-out diagnostics, behavior-relative checks, and a separately justified off-policy evaluation procedure. [practitioner]
- Require staged, bounded evaluation before real deployment in safety-sensitive domains; the cited algorithms do not provide an operational safety guarantee. [evidence-based]

## Evidence Caveats

- The survey organizes mechanisms and open problems; it does not certify any one algorithm for every dataset, domain, or deployment.
- BCQ's reported continuous-control results establish behavior in the paper's fixed-batch tasks, not universal superiority or reliable density estimation in high-dimensional action spaces.
- CQL's lower-bound and policy-improvement results apply to specified objectives, sampling assumptions, and sufficient regularization conditions. A neural implementation with arbitrary tuning does not automatically inherit every guarantee.
- Comparative results in BCQ and CQL depend on the paper-specific datasets, baselines, architectures, and evaluation protocols. They should not be transferred as state-of-the-art claims.
- Bellman error on held-out logged transitions is not the same as value error under the learned policy, especially when its occupancy differs from the dataset.
- Conservatism can discard genuine improvement when the dataset has useful but sparse high-return actions, and weak conservatism can still exploit estimation error.
- A fixed dataset can encode confounding, observation aliasing, corrupted rewards, or unsafe behavior. None of the three sources proves those problems are removed by offline RL.
- Seed variance and checkpoint selection remain material, while fully offline model selection prevents routine use of true environment return during tuning.

## Sources

- Canon evidence file: `references/topics/013-offline-batch-rl-and-conservatism.md`
- Sergey Levine, Aviral Kumar, George Tucker, and Justin Fu (2020), *Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems*, arXiv:2005.01643. https://arxiv.org/abs/2005.01643
- Scott Fujimoto, David Meger, and Doina Precup (2019), *Off-Policy Deep Reinforcement Learning without Exploration*, Proceedings of the 36th International Conference on Machine Learning, PMLR 97, arXiv:1812.02900. https://proceedings.mlr.press/v97/fujimoto19a.html
- Aviral Kumar, Aurick Zhou, George Tucker, and Sergey Levine (2020), *Conservative Q-Learning for Offline Reinforcement Learning*, Advances in Neural Information Processing Systems 33, arXiv:2006.04779. https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]
