---
type: "canon"
title: "007. Policy gradient methods and REINFORCE"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 007. Policy gradient methods and REINFORCE

Ledger: 007 | target: Policy gradient methods and REINFORCE | confidence: evidence-based | fold: [[Policy gradient methods and REINFORCE]] | status: active.

## Core Thesis

Policy gradient methods directly adjust a differentiable policy to increase an expected-return objective, rather than deriving the policy only by maximizing an estimated value function.
REINFORCE applies the likelihood-ratio, or score-function, identity to sampled actions and weights their log-probability gradients by observed returns.
This gives a broadly applicable, model-free gradient estimator, but its Monte Carlo targets can have high variance and its optimization problem is generally nonconvex.

## How It Works

Let a stochastic policy be \(\pi_\theta(a\mid s)\), and let a trajectory \(\tau\) have return \(G(\tau)\).
For an episodic objective,

\[
J(\theta)=\mathbb{E}_{\tau\sim p_\theta}[G(\tau)].
\]

The likelihood-ratio identity rewrites its gradient as

\[
\nabla_\theta J(\theta)
=\mathbb{E}_{\tau\sim p_\theta}
\left[G(\tau)\nabla_\theta\log p_\theta(\tau)\right].
\]

When environment initial-state and transition probabilities do not depend on \(\theta\), only the policy terms remain:

\[
\nabla_\theta\log p_\theta(\tau)
=\sum_t \nabla_\theta\log\pi_\theta(A_t\mid S_t).
\]

Causality permits replacing total trajectory return with reward-to-go from each action.
With \(G_t=\sum_{k=0}^{T-t-1}\gamma^k R_{t+k+1}\), a sampled REINFORCE contribution is

\[
\widehat g_t=G_t\nabla_\theta\log\pi_\theta(A_t\mid S_t).
\]

Some discounted start-state objective conventions add a \(\gamma^t\) factor outside \(G_t\).
The objective definition and estimator convention must therefore be stated together.

The policy gradient theorem gives the equivalent state-action form

\[
\nabla_\theta J(\theta)
\propto
\mathbb{E}_{S\sim d^{\pi},A\sim\pi_\theta}
\left[q_\pi(S,A)\nabla_\theta\log\pi_\theta(A\mid S)\right],
\]

with the exact proportionality or normalization determined by the episodic, discounted, or average-reward formulation.
Crucially, the theorem does not require differentiating the policy-induced state distribution in the estimator.

An action-independent baseline \(b(S_t)\) can replace \(G_t\) with \(G_t-b(S_t)\):

\[
\mathbb{E}_{A\sim\pi_\theta}
\left[b(S)\nabla_\theta\log\pi_\theta(A\mid S)\right]=0.
\]

The baseline therefore preserves the expected policy gradient while often reducing variance.
A learned state-value baseline makes the weight an estimated advantage and leads directly toward actor-critic methods.

A basic training loop has the following shape:

1. Sample one or more complete episodes from the current policy.
2. Compute each timestep's reward-to-go, respecting discounting and termination semantics.
3. Optionally subtract an action-independent baseline.
4. Accumulate log-probability times return or advantage terms.
5. Apply gradient ascent, or minimize the corresponding negative surrogate loss.
6. Discard the on-policy batch before collecting data under the updated policy.

## Key Principles

- The score-function identity estimates a distribution gradient without differentiating rewards or environment dynamics. [evidence-based]
- Reward-to-go removes rewards that occurred before an action from that action's credit signal and preserves the on-policy expectation. [evidence-based]
- The policy gradient theorem expresses the gradient using policy derivatives and action values under the policy's own occupancy distribution. [evidence-based]
- Any baseline that depends on state but not on the sampled action has zero expected score-function contribution. [evidence-based]
- REINFORCE uses sampled Monte Carlo returns, so correct on-policy sampling can yield an unbiased estimator for the chosen finite-horizon objective while still producing high variance. [evidence-based]
- Direct policy parameterization naturally represents stochastic policies and common continuous-action distributions. [evidence-based]
- A valid gradient direction does not imply monotonic improvement after a finite optimizer step or convergence to a global optimum. [evidence-based]

## Best Practices

- Define the return objective, discount convention, horizon, and treatment of truncation before implementing the loss. [evidence-based]
- Compute reward-to-go backward through each trajectory and mask only true environmental terminations when deciding whether bootstrapping is valid. [practitioner]
- Use a learned value baseline or another demonstrably action-independent control variate, and keep its regression target separate from the actor objective. [evidence-based]
- Detach sampled return or advantage targets from the actor loss unless a separately derived differentiable objective requires otherwise. [practitioner]
- Check that stored log probabilities correspond to the policy that generated each action; stale or replayed samples require an explicit off-policy correction. [evidence-based]
- Track gradient norms, policy entropy, approximate policy change, episodic return distributions, and multiple random seeds rather than trusting one learning curve. [practitioner]
- Treat advantage normalization, entropy bonuses, gradient clipping, and optimizer settings as implementation choices to ablate, not as consequences of the REINFORCE theorem. [practitioner]

## Primary Sources

- Ronald J. Williams (1992), "Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning," *Machine Learning* 8, 229-256, DOI: https://doi.org/10.1007/BF00992696
- Richard S. Sutton, David A. McAllester, Satinder P. Singh, and Yishay Mansour (2000; NeurIPS 12 conference proceedings), "Policy Gradient Methods for Reinforcement Learning with Function Approximation": https://proceedings.neurips.cc/paper_files/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
- Richard S. Sutton and Andrew G. Barto (2018), *Reinforcement Learning: An Introduction*, second edition, Chapter 13, MIT Press: https://mitpress.mit.edu/9780262039246/reinforcement-learning/

## Evidence Caveats

Williams establishes a family of stochastic gradient-following rules under stated formulations; it does not show that modern neural REINFORCE is sample-efficient or stable across deep-RL benchmarks.
The Sutton et al. convergence result uses specific assumptions and compatible function-approximation structure, so it is not a blanket convergence guarantee for arbitrary nonlinear policy networks.
Unbiasedness claims depend on the precise objective, on-policy data, horizon handling, and baseline construction.
Finite batches, reward scaling, optimizer state, shared representations, and advantage normalization can materially alter empirical behavior.
Reported success on one task or seed does not establish superiority over value-based, actor-critic, or proximal alternatives.

## Brain Hooks

- Folded concept: [[Policy gradient methods and REINFORCE]]
- Problem formulation: [[Markov decision processes and the RL problem formulation]]
- Return estimators: [[Dynamic programming, Monte Carlo, and temporal-difference learning]]
- Approximation risks: [[Function approximation and the deadly triad]]
- Learned baseline extension: [[Actor-critic methods (A2C A3C, GAE)]]
- Constrained-update extension: [[Trust-region and proximal methods (TRPO, PPO)]]
- Continuous-action relatives: [[Continuous control (DDPG, TD3, SAC)]]
- Exploration context: [[Exploration strategies and intrinsic motivation]]
- Evaluation discipline: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]
