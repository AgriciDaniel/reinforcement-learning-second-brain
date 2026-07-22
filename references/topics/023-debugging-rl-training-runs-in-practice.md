---
type: "canon"
title: "023. Debugging RL training runs in practice"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 023. Debugging RL training runs in practice

Ledger: 023 | target: Debugging RL training runs in practice | confidence: practitioner | fold: [[Debugging RL training runs in practice]] | status: active.

## Core Thesis

Debugging reinforcement learning is an exercise in validating a coupled data-generating system, not merely watching whether a loss decreases. [evidence-based]
The fastest path to a cause is usually to make the failure deterministic, inspect one transition and one update, and replace complex components with controlled probes. [practitioner]
Training curves become useful evidence only after environment semantics, target construction, batching, and evaluation have independent checks. [practitioner]

## How It Works

### 1. Capture the closed loop

Treat the environment, rollout collector, learner, evaluator, and logger as one causal loop.
For a reproducible failing run, retain at least:

- observation, action, reward components, next observation, `terminated`, `truncated`, and episode identifier;
- policy version, action log-probability, value prediction, and any recurrent state used during collection;
- random seeds, dependency versions, hardware, precision mode, configuration, and source revision;
- raw evaluation returns and episode lengths, separate from training summaries.

The first useful artifact is often a short trajectory plus the exact batch derived from it.
That artifact lets an operator ask whether the learner received the data the environment actually emitted.

### 2. Verify trajectory and target semantics

For a finite segment beginning at time \(t\), the discounted return is

\[
G_t = \sum_{k=0}^{T-t-1} \gamma^k r_{t+k}.
\]

A one-step bootstrapped target can be written as

\[
y_t = r_t + \gamma\left(1 - \mathbb{1}[\mathrm{terminated}_t]\right)V(s_{t+1}).
\]

A true terminal state removes the bootstrap term.
A time-limit truncation usually preserves the bootstrap term when the continuing task has not ended, while the rollout recursion must still stop at the reset boundary.
Test these cases with hand-computed trajectories before trusting generalized advantage estimation, replay-buffer sampling, or vectorized collectors.

### 3. Verify one learner update

Freeze one collected batch and run a single optimizer step.
In an importance-ratio policy update such as PPO, inspect

\[
\rho_t(\theta) = \exp\left(\log \pi_\theta(a_t\mid s_t) - \log \pi_{\mathrm{old}}(a_t\mid s_t)\right).
\]

Before parameters change, the ratio should be numerically close to one when both log-probabilities describe the same policy and action transformation.
Check tensor shapes, dtypes, masks, finite values, gradient norms, parameter deltas, advantage normalization, and value targets.
For a value learner, compare the implemented target and temporal-difference error with a scalar calculation on a tiny batch.

### 4. Use controlled substitutions

Reduce uncertainty by swapping one component at a time:

- replace the real task with a one-state or two-action environment whose optimal behavior is obvious;
- replace a learned value function with a table or known target;
- replay a fixed batch repeatedly to determine whether the optimizer can fit it;
- compare the same transition batch against a trusted reference implementation;
- turn reward shaping, normalization, recurrence, distributed sampling, and mixed precision on one at a time.

If the minimal system cannot learn, debug correctness.
If it can learn but the full system cannot, restore complexity incrementally and record the first change that recreates the failure.

### 5. Separate training from evaluation

Run evaluation with a fixed protocol, fresh episodes, and exploration settings appropriate to the algorithm.
Do not infer policy quality from actor loss, critic loss, entropy, or training-time reward alone.
When stochasticity matters, compare distributions across independent seeds and preserve per-run results for [[Evaluation, benchmarks, and reproducibility in deep RL]].

## Key Principles

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

## Primary Sources

- Andy Jones, 2021, [Debugging Reinforcement Learning Systems](https://andyljones.com/posts/rl-debugging.html). A practitioner workflow centered on unit tests, toy environments, and checking the full data path. [practitioner]
- Andrej Karpathy, 2019, [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/). General neural-network debugging guidance that transfers to RL learners, including small-batch overfitting and staged complexity. [practitioner]
- Richard S. Sutton and Andrew G. Barto, 2018, [Reinforcement Learning: An Introduction, second edition](https://mitpress.mit.edu/9780262039246/reinforcement-learning/). Defines returns, value targets, bootstrapping, and core algorithmic semantics used in diagnostic calculations. [verified]
- Logan Engstrom et al., 2020, [Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO](https://arxiv.org/abs/2005.12729). Isolates code-level implementation choices that influence policy-gradient results. [evidence-based]
- Farama Foundation, [Gymnasium Env API](https://gymnasium.farama.org/api/env/) and [environment checker utilities](https://gymnasium.farama.org/api/utils/). Official contracts for observations, actions, resets, termination, truncation, and automated checks. [verified]
- Farama Foundation, [Handling Time Limits](https://gymnasium.farama.org/tutorials/gymnasium_basics/handling_time_limits/). Official explanation of termination, truncation, and bootstrapping implications. [verified]
- Stable-Baselines3 maintainers, [Reinforcement Learning Tips and Tricks](https://stable-baselines3.readthedocs.io/en/master/guide/rl_tips.html). Library guidance on evaluation, normalization, custom environments, and reproducibility. [verified]

## Evidence Caveats

- The Jones and Karpathy sources are practitioner guidance, not controlled comparisons of debugging procedures. [practitioner]
- An environment checker validates parts of an interface contract but cannot determine whether a task's reward or terminal semantics match the intended problem. [verified]
- The displayed target assumes a continuing-value interpretation after truncation; finite-horizon tasks may require remaining time in the state and different semantics. [evidence-based]
- A near-one initial importance ratio is expected only when the old and current log-probabilities use the same observations, actions, transformations, and parameters. [evidence-based]
- PPO and TRPO implementation findings do not quantify every algorithm, environment, library, or accelerator stack. [evidence-based]
- Diagnostic metric ranges depend on algorithm, task, reward scale, batch construction, and hyperparameters; universal cutoffs are not established here. [practitioner]
- Passing toy tasks is necessary evidence for many implementations but is not proof of correct scaling or strong real-task performance. [practitioner]
- A single repaired run can show that a failure disappeared under one condition, but reproducibility requires repeated evaluation. [evidence-based]

## Brain Hooks

- Folded concept: [[Debugging RL training runs in practice]]
- Evaluation discipline: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Stability risks: [[Function approximation and the deadly triad]]
- Proximal updates: [[Trust-region and proximal methods (TRPO, PPO)]]
- Policy-gradient checks: [[Policy gradient methods and REINFORCE]]
- Advantage checks: [[Actor-critic methods (A2C A3C, GAE)]]
- Value-learning checks: [[Deep Q-Networks and value-based deep RL (DQN, Rainbow)]]
- Specification checks: [[Reward design, reward hacking, and specification gaming]]
- Implementation context: [[RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF)]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]
