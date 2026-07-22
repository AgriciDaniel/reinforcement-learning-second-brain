---
type: "canon"
title: "008. Actor-critic methods (A2C A3C, GAE)"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 008. Actor-critic methods (A2C A3C, GAE)

Ledger: 008 | target: Actor-critic methods (A2C A3C, GAE) | confidence: evidence-based | fold: [[Actor-critic methods (A2C A3C, GAE)]] | status: active.

## Core Thesis

Actor-critic methods couple a parameterized policy, the actor, with a learned value estimator, the critic, that supplies lower-variance credit signals.
They trade the pure Monte Carlo estimator of REINFORCE for bootstrapped targets that can reduce variance while introducing bias from value approximation.
A3C organizes many actor-learners asynchronously, A2C is the later synchronous batching convention, and generalized advantage estimation (GAE) exposes a tunable bias-variance continuum for the actor's advantage target.

## How It Works

Let the actor be \(\pi_\theta(a\mid s)\) and a state-value critic be \(V_w(s)\).
The one-step temporal-difference residual is

\[
\delta_t^V=R_{t+1}+\gamma V_w(S_{t+1})-V_w(S_t),
\]

where the next-state value is zero after a true terminal transition.
When the critic is exact, the conditional expectation of this residual given \(S_t,A_t\) is the policy advantage for the one-step formulation.
With an approximate critic, it is a bootstrapped advantage estimate.

The actor applies a score-function update such as

\[
\widehat g_t=\widehat A_t\nabla_\theta\log\pi_\theta(A_t\mid S_t),
\]

while the critic regresses toward a return target.
For an \(n\)-step rollout, that target is

\[
\widehat R_t^{(n)}
=\sum_{i=0}^{n-1}\gamma^i R_{t+i+1}
+\gamma^n V_w(S_{t+n}),
\]

with the bootstrap term omitted at a true terminal state.
The corresponding advantage target is commonly \(\widehat R_t^{(n)}-V_w(S_t)\).

GAE forms an exponentially weighted sum of temporal-difference residuals:

\[
\widehat A_t^{\mathrm{GAE}(\gamma,\lambda)}
=\sum_{l=0}^{T-t-1}(\gamma\lambda)^l\delta_{t+l}^V.
\]

At \(\lambda=0\), GAE is the one-step residual.
At \(\lambda=1\), the finite episodic sum telescopes toward the discounted Monte Carlo return minus the current value estimate when terminal handling is correct.
Intermediate \(\lambda\) values mix multi-step estimators, usually reducing variance as more bootstrapping is introduced and reducing bootstrap bias as longer returns receive more weight.

An advantage actor-critic loss is typically assembled from three terms:

\[
L=L_{\mathrm{policy}}+c_v L_{\mathrm{value}}-c_H H(\pi_\theta(\cdot\mid S)),
\]

where the policy term uses negative log probability times a detached advantage, the value term fits the critic target, and the entropy term encourages a broader action distribution.
The coefficients and even the inclusion of entropy regularization are algorithm and implementation choices.

In A3C, each worker repeatedly does the following:

1. Synchronize local parameters from shared global parameters.
2. Interact with its own environment instance for a rollout segment or until termination.
3. Bootstrap from the final state when the segment ended without true termination.
4. Compute policy, value, and optional entropy gradients locally.
5. Apply gradients asynchronously to shared parameters, then begin another segment.

The original A3C implementation used multiple asynchronous actor-learners to decorrelate experience and drive shared updates without a replay buffer.
Workers can compute gradients from parameters that are no longer current when those gradients are applied, so system-level staleness is part of the method's practical behavior.

A2C retains the same broad advantage actor-critic objective but synchronizes rollout collection.
It waits for a batch of actor environments, aggregates their rollout data, and performs one coordinated update.
The A2C name is an implementation convention popularized after A3C, not a separate theorem in the A3C paper.

## Key Principles

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

## Primary Sources

- Vijay R. Konda and John N. Tsitsiklis (2000; NeurIPS 12 conference proceedings), "Actor-Critic Algorithms": https://proceedings.neurips.cc/paper_files/paper/1999/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html
- Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, and Koray Kavukcuoglu (2016), "Asynchronous Methods for Deep Reinforcement Learning," ICML, arXiv:1602.01783: https://arxiv.org/abs/1602.01783
- John Schulman, Philipp Moritz, Sergey Levine, Michael I. Jordan, and Pieter Abbeel (2015), "High-Dimensional Continuous Control Using Generalized Advantage Estimation," arXiv:1506.02438: https://arxiv.org/abs/1506.02438
- Yuhuai Wu, Elman Mansimov, Shun Liao, Alec Radford, and John Schulman (2017), "OpenAI Baselines: ACKTR & A2C," official implementation note: https://openai.com/index/openai-baselines-acktr-a2c/
- Richard S. Sutton and Andrew G. Barto (2018), *Reinforcement Learning: An Introduction*, second edition, Chapter 13, MIT Press: https://mitpress.mit.edu/9780262039246/reinforcement-learning/

## Evidence Caveats

Konda and Tsitsiklis analyze two-time-scale actor-critic algorithms under assumptions including linear critic structure; those results do not automatically establish convergence for deep shared networks.
The A3C paper reports empirical outcomes for its tasks, architectures, preprocessing, and compute setting, not a universal benefit from asynchronous updates.
A2C's synchronous label covers implementation variants, and its performance relative to A3C depends on hardware, batch construction, policy lag, and environment cost.
GAE's bias and variance depend jointly on \(\gamma\), \(\lambda\), critic error, rollout truncation, and the objective being approximated.
Single-seed curves and aggregate means can conceal instability, while value loss alone does not establish that the critic produces useful policy-gradient directions.

## Brain Hooks

- Folded concept: [[Actor-critic methods (A2C A3C, GAE)]]
- Gradient foundation: [[Policy gradient methods and REINFORCE]]
- TD foundation: [[Dynamic programming, Monte Carlo, and temporal-difference learning]]
- Approximation risk: [[Function approximation and the deadly triad]]
- Proximal consumer of GAE: [[Trust-region and proximal methods (TRPO, PPO)]]
- Off-policy continuous actors: [[Continuous control (DDPG, TD3, SAC)]]
- Exploration mechanisms: [[Exploration strategies and intrinsic motivation]]
- On-policy evaluation: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Training diagnosis: [[Debugging RL training runs in practice]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]
