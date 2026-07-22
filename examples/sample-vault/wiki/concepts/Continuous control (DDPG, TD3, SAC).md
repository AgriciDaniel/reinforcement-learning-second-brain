---
type: "concept"
title: "Continuous control (DDPG, TD3, SAC)"
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
  - "https://proceedings.mlr.press/v32/silver14.html"
  - "https://arxiv.org/abs/1509.02971"
  - "https://proceedings.mlr.press/v80/fujimoto18a.html"
  - "https://proceedings.mlr.press/v80/haarnoja18b.html"
  - "https://arxiv.org/abs/1812.05905"
  - "https://mitpress.mit.edu/9780262039246/reinforcement-learning/"
---

# Continuous control (DDPG, TD3, SAC)

Confidence tag: evidence-based. Folded from canon `010-continuous-control-ddpg-td3-sac.md` on the date in `updated`.

## Sourced Takeaways

DDPG, TD3, and SAC are model-free, off-policy actor-critic algorithms designed for continuous action spaces, where enumerating actions for a greedy value update is impractical. DDPG learns a deterministic actor, TD3 adds mechanisms that reduce exploitation of critic error, and SAC learns a stochastic policy under a maximum-entropy objective. Their replay-based data reuse can improve interaction efficiency, but their bootstrapped critics still make optimization sensitive to data coverage, reward scale, and function-approximation error.

- DDPG applies the deterministic policy-gradient theorem, so the actor gradient differentiates the critic with respect to the action rather than integrating over all continuous actions. [evidence-based]
- Replay and target networks improve data reuse and target stability, but together with bootstrapping and nonlinear approximation they do not guarantee convergence. [evidence-based]
- TD3's twin critics, delayed actor updates, and target-policy smoothing address distinct routes by which critic error can corrupt a deterministic actor. [evidence-based]
- The clipped double target controls overestimation by introducing pessimism, but it does not make either critic unbiased or accurate outside replay coverage. [evidence-based]
- SAC's entropy term belongs inside its soft Bellman target and actor objective, not merely as action noise added at collection time. [evidence-based]
- A tanh-squashed stochastic policy requires the change-of-variables correction in its log probability for correct SAC losses. [evidence-based]
- Action bounds, reward scale, terminal semantics, and replay coverage are part of the algorithm's effective specification. [practitioner]

## Best Practices

- Normalize observations using statistics that are applied consistently to online interactions, replayed samples, target evaluation, and deployment. [practitioner]
- Map normalized actor outputs to each action dimension's physical bounds and test asymmetric bounds, clipping, and log-probability corrections. [practitioner]
- Warm the replay buffer with sufficiently diverse behavior before relying heavily on an initially inaccurate critic and actor. [practitioner]
- For DDPG and TD3, keep collection noise separate from TD3 target-smoothing noise because they serve different purposes and need not share a schedule. [evidence-based]
- For SAC, log policy entropy, temperature, target entropy, critic disagreement, and both reward and entropy contributions to the target. [practitioner]
- Monitor Q magnitudes, Bellman targets, saturation at action bounds, replay age, and actor-gradient norms to detect critic exploitation early. [practitioner]
- Tune update-to-data ratio, batch size, target-network rate, learning rates, exploration, and reward scaling as a coupled system. [practitioner]
- Report multiple seeds and equal environment-interaction budgets, with evaluation noise and checkpoint selection rules fixed in advance. [evidence-based]

## Evidence Caveats

The original papers evaluate particular simulated-control tasks, architectures, environment versions, and tuning protocols. Their reported comparisons do not prove a universal ordering among DDPG, TD3, SAC, on-policy methods, or model-based control.

DDPG can be especially sensitive to critic error and exploration, while TD3 mitigates rather than eliminates those failures. Taking a minimum over two learned critics can trade overestimation for pessimism, and target smoothing can blur genuinely narrow optima.

SAC's entropy can aid exploration and robustness in the tested settings, but a target-entropy heuristic is not a task-independent optimum. Fixed-temperature SAC, automatic-temperature SAC, the original value-network architecture, and later no-value-network implementations are materially different experimental specifications.

Seed variance, simulator determinism, action scaling, time-limit bootstrapping, replay initialization, update-to-data ratio, and evaluation mode can change conclusions. None of these sources establishes safety, real-world transfer, or reliable learning from a fixed dataset without additional assumptions.

## Sources

- Canon evidence file: `references/topics/010-continuous-control-ddpg-td3-sac.md`
- David Silver, Guy Lever, Nicolas Heess, Thomas Degris, Daan Wierstra, and Martin Riedmiller (2014), [Deterministic Policy Gradient Algorithms](https://proceedings.mlr.press/v32/silver14.html), ICML, PMLR 32.
- Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, and Daan Wierstra (2015), [Continuous Control with Deep Reinforcement Learning](https://arxiv.org/abs/1509.02971), arXiv:1509.02971, presented at ICLR 2016.
- Scott Fujimoto, Herke van Hoof, and David Meger (2018), [Addressing Function Approximation Error in Actor-Critic Methods](https://proceedings.mlr.press/v80/fujimoto18a.html), ICML, PMLR 80, arXiv:1802.09477.
- Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine (2018), [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html), ICML, PMLR 80, arXiv:1801.01290.
- Tuomas Haarnoja et al. (2018), [Soft Actor-Critic Algorithms and Applications](https://arxiv.org/abs/1812.05905), arXiv:1812.05905, including the automatic-temperature formulation.
- Richard S. Sutton and Andrew G. Barto (2018), [Reinforcement Learning: An Introduction, second edition](http://incompleteideas.net/book/the-book-2nd.html), Chapter 13 on policy-gradient methods.
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]
