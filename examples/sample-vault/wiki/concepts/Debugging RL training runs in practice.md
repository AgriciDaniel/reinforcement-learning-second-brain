---
type: "concept"
title: "Debugging RL training runs in practice"
domain: "reinforcement learning: fundamentals, deep RL, RLHF/RLAIF and preference optimization, evaluation, tooling, and applied best practices"
status: "active"
created: "2026-07-22"
updated: "2026-07-22"
tags:
  - "#domain/reinforcement-learning-fundamentals-deep-rl-rlhf-rlaif-and-prefe"
  - "#type/concept"
  - "#confidence/practitioner"
confidence: "practitioner"
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
  - "https://andyljones.com/posts/rl-debugging.html"
  - "https://karpathy.github.io/2019/04/25/recipe/"
  - "https://mitpress.mit.edu/9780262039246/reinforcement-learning/"
  - "https://arxiv.org/abs/2005.12729"
  - "https://gymnasium.farama.org/api/env/"
  - "https://gymnasium.farama.org/api/utils/"
  - "https://gymnasium.farama.org/tutorials/gymnasium_basics/handling_time_limits/"
  - "https://stable-baselines3.readthedocs.io/en/master/guide/rl_tips.html"
---

# Debugging RL training runs in practice

Confidence tag: practitioner. Folded from canon `023-debugging-rl-training-runs-in-practice.md` on the date in `updated`.

## Sourced Takeaways

Debugging reinforcement learning is an exercise in validating a coupled data-generating system, not merely watching whether a loss decreases. [evidence-based]
The fastest path to a cause is usually to make the failure deterministic, inspect one transition and one update, and replace complex components with controlled probes. [practitioner]
Training curves become useful evidence only after environment semantics, target construction, batching, and evaluation have independent checks. [practitioner]

- Reward is often a weak failure locator because observation processing, reset logic, target construction, and optimization can all produce the same flat curve. [practitioner]
- Returns, advantages, masks, reset boundaries, and batch transforms should have deterministic unit tests with hand-computed expected values. [practitioner]
- `terminated` and `truncated` encode different learning semantics, so collapsing them into one `done` flag can create an incorrect bootstrap target. [evidence-based]
- Small implementation choices can materially alter deep RL results even when the named algorithm is unchanged. [evidence-based]
- Fixed seeds help reproduce a bug, but one seed cannot establish that an algorithm or repair is reliable. [evidence-based]
- Metrics such as entropy, KL divergence, clip fraction, explained variance, and gradient norm are diagnostic signals, not universal pass thresholds. [practitioner]
- Distributed execution, wrappers, normalization, and mixed precision multiply possible failure surfaces and should follow validation of the minimal loop. [practitioner]

## Best Practices

- Freeze the failing configuration, seed, dependency lock, code revision, and a short trajectory before changing the implementation. [practitioner]
- Run an environment checker, then add task-specific tests for observation bounds, reward timing, termination, truncation, and reset behavior. [evidence-based]
- Maintain probe environments for immediate reward, delayed reward, terminal reward, and an intentionally impossible task. [practitioner]
- Differential-test log-probabilities, targets, losses, and parameter updates against a trusted implementation on the same fixed batch. [practitioner]
- Log raw and transformed observations, reward components, episode statistics, optimizer state, and policy version at boundaries where bugs can enter. [practitioner]
- Apply anomaly detection, gradient hooks, and full trajectory capture to a minimal reproducer because these tools can be too expensive for every production step. [evidence-based]
- After a repair passes deterministic checks, rerun an unchanged baseline and multiple independent seeds under the same evaluation protocol. [evidence-based]

## Evidence Caveats

- The Jones and Karpathy sources are practitioner guidance, not controlled comparisons of debugging procedures. [practitioner]
- An environment checker validates parts of an interface contract but cannot determine whether a task's reward or terminal semantics match the intended problem. [verified]
- The displayed target assumes a continuing-value interpretation after truncation; finite-horizon tasks may require remaining time in the state and different semantics. [evidence-based]
- A near-one initial importance ratio is expected only when the old and current log-probabilities use the same observations, actions, transformations, and parameters. [evidence-based]
- PPO and TRPO implementation findings do not quantify every algorithm, environment, library, or accelerator stack. [evidence-based]
- Diagnostic metric ranges depend on algorithm, task, reward scale, batch construction, and hyperparameters; universal cutoffs are not established here. [practitioner]
- Passing toy tasks is necessary evidence for many implementations but is not proof of correct scaling or strong real-task performance. [practitioner]
- A single repaired run can show that a failure disappeared under one condition, but reproducibility requires repeated evaluation. [evidence-based]

## Sources

- Canon evidence file: `references/topics/023-debugging-rl-training-runs-in-practice.md`
- Andy Jones, 2021, [Debugging Reinforcement Learning Systems](https://andyljones.com/posts/rl-debugging.html). A practitioner workflow centered on unit tests, toy environments, and checking the full data path. [practitioner]
- Andrej Karpathy, 2019, [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/). General neural-network debugging guidance that transfers to RL learners, including small-batch overfitting and staged complexity. [practitioner]
- Richard S. Sutton and Andrew G. Barto, 2018, [Reinforcement Learning: An Introduction, second edition](https://mitpress.mit.edu/9780262039246/reinforcement-learning/). Defines returns, value targets, bootstrapping, and core algorithmic semantics used in diagnostic calculations. [verified]
- Logan Engstrom et al., 2020, [Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO](https://arxiv.org/abs/2005.12729). Isolates code-level implementation choices that influence policy-gradient results. [evidence-based]
- Farama Foundation, [Gymnasium Env API](https://gymnasium.farama.org/api/env/) and [environment checker utilities](https://gymnasium.farama.org/api/utils/). Official contracts for observations, actions, resets, termination, truncation, and automated checks. [verified]
- Farama Foundation, [Handling Time Limits](https://gymnasium.farama.org/tutorials/gymnasium_basics/handling_time_limits/). Official explanation of termination, truncation, and bootstrapping implications. [verified]
- Stable-Baselines3 maintainers, [Reinforcement Learning Tips and Tricks](https://stable-baselines3.readthedocs.io/en/master/guide/rl_tips.html). Library guidance on evaluation, normalization, custom environments, and reproducibility. [verified]
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]
