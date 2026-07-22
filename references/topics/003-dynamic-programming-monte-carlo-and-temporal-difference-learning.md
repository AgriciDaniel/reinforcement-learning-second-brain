---
type: "canon"
title: "003. Dynamic programming, Monte Carlo, and temporal-difference learning"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 003. Dynamic programming, Monte Carlo, and temporal-difference learning

Ledger: 003 | target: Dynamic programming, Monte Carlo, and temporal-difference learning | confidence: evidence-based | fold: [[Dynamic programming, Monte Carlo, and temporal-difference learning]] | status: active.

## Core Thesis

Dynamic programming (DP), Monte Carlo (MC), and temporal-difference (TD) learning are three complementary ways to estimate value functions and improve policies in finite Markov decision processes. DP backs up expected values using a known environment model, MC learns from complete sampled returns without a model, and TD learns from sampled transitions while bootstrapping from its own current estimates. Their differing use of models, sampling, and bootstrapping is a central design axis for reinforcement-learning algorithms.

## How It Works

Let a policy be \(\pi(a\mid s)\), the discount be \(\gamma\), and \(v_\pi(s)\) denote the expected discounted return from state \(s\).

The Bellman expectation equation states

\[
v_\pi(s)=\sum_a \pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\left[r+\gamma v_\pi(s')\right].
\]

This equation is both a fixed-point characterization and a template for backups.

### Dynamic programming

DP assumes access to the transition and reward model \(p(s',r\mid s,a)\).

Iterative policy evaluation repeatedly applies the Bellman expectation backup to every state until the value changes are sufficiently small.

Policy improvement then makes the policy greedy, or tie-aware greedy, with respect to one-step lookahead from the current value function.

Policy iteration alternates substantially complete policy evaluation with policy improvement.

Value iteration combines truncated evaluation and improvement through the Bellman optimality backup

\[
v(s) \leftarrow \max_a \sum_{s',r}p(s',r\mid s,a)\left[r+\gamma v(s')\right].
\]

Generalized policy iteration describes the broader pattern in which evaluation and improvement interact at any granularity, even before either has converged.

### Monte Carlo learning

MC methods replace model expectations with complete returns sampled from episodes.

For time \(t\), the episodic return is

\[
G_t=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots+\gamma^{T-t-1}R_T.
\]

Every-visit MC updates after every occurrence of a state or state-action pair, while first-visit MC updates only from its first occurrence in an episode.

An incremental state-value update is

\[
V(S_t) \leftarrow V(S_t)+\alpha\left[G_t-V(S_t)\right].
\]

MC control alternates action-value estimation with policy improvement, commonly using an exploratory policy so all relevant actions continue to be sampled.

Off-policy MC separates a behavior policy from a target policy and corrects the return with ordinary or weighted importance sampling ratios.

### Temporal-difference learning

One-step TD prediction updates immediately from the next reward and the next state's current estimate.

Its TD error is

\[
\delta_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t),
\]

followed by

\[
V(S_t) \leftarrow V(S_t)+\alpha\delta_t.
\]

The target \(R_{t+1}+\gamma V(S_{t+1})\) is sampled like MC but bootstrapped like DP.

The \(n\)-step return interpolates between one-step TD and full-return MC by using \(n\) sampled rewards before bootstrapping.

Eligibility traces and TD(\(\lambda\)) provide a backward-view implementation that assigns each TD error to recently visited states, with \(\lambda\) controlling the trace decay.

A common training loop initializes values, collects transitions under a behavior policy, computes the method-specific target, applies an incremental update, and periodically improves the policy from the current action values.

## Key Principles

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

## Primary Sources

- Richard S. Sutton and Andrew G. Barto (2018), *Reinforcement Learning: An Introduction*, second edition, Chapters 4 to 7, The MIT Press: https://mitpress.mit.edu/9780262039246/reinforcement-learning/
- Richard S. Sutton and Andrew G. Barto (2020), complete second-edition author-hosted text: http://incompleteideas.net/book/RLbook2020.pdf
- Richard S. Sutton (1988), “Learning to Predict by the Methods of Temporal Differences,” *Machine Learning* 3, DOI: https://doi.org/10.1007/BF00115009

## Evidence Caveats

- The textbook's tabular convergence results rely on assumptions such as finite representations, appropriate step-size schedules, adequate visitation, and stationary Markov dynamics. They do not automatically transfer to nonlinear function approximation. [evidence-based]
- DP sweeps are computational abstractions, and a known model can still be too large for exhaustive backups. [evidence-based]
- The broad bias-variance comparison between MC and TD does not determine which method learns faster on a particular task, representation, or data stream. [practitioner]
- Importance-sampled off-policy estimates can be dominated by rare trajectories, so small experiments may show severe seed and episode-length variance. [evidence-based]
- The cited sources establish algorithms and theory, not a universal hyperparameter setting, benchmark ranking, or state-of-the-art empirical claim. [evidence-based]
- Reported results should distinguish environment stochasticity, exploratory-policy randomness, initialization, and implementation details rather than attributing all variation to the algorithm family. [practitioner]

## Brain Hooks

- Folded concept: [[Dynamic programming, Monte Carlo, and temporal-difference learning]]
- Problem formalization: [[Markov decision processes and the RL problem formulation]]
- Exploration context: [[Bandits and exploration-exploitation]]
- Tabular control descendants: [[Q-learning, SARSA, and tabular methods]]
- Approximation boundary: [[Function approximation and the deadly triad]]
- Gradient-based alternative: [[Policy gradient methods and REINFORCE]]
- Planning connection: [[Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)]]
- Broader exploration methods: [[Exploration strategies and intrinsic motivation]]
- Evaluation discipline: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]
