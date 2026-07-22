---
type: "canon"
title: "009. Trust-region and proximal methods (TRPO, PPO)"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 009. Trust-region and proximal methods (TRPO, PPO)

Ledger: 009 | target: Trust-region and proximal methods (TRPO, PPO) | confidence: evidence-based | fold: [[Trust-region and proximal methods (TRPO, PPO)]] | status: active.

## Core Thesis

Trust-region policy optimization (TRPO) and proximal policy optimization (PPO) are on-policy policy-gradient methods that limit how aggressively a policy is changed using data collected by an older policy. TRPO expresses proximity as an average Kullback-Leibler (KL) divergence constraint and approximately solves a constrained second-order problem. PPO trades that machinery for first-order surrogate objectives that are easier to optimize, while providing no hard trust-region guarantee.

## How It Works

### Shared surrogate structure

For a stochastic policy \(\pi_\theta\), the discounted-return objective is

\[
J(\theta)=\mathbb{E}_{\tau\sim\pi_\theta}\left[\sum_{t=0}^{T-1}\gamma^t r_t\right].
\]

Both methods collect trajectories with \(\pi_{\theta_{\mathrm{old}}}\), estimate advantages \(\hat A_t\), and optimize an importance-ratio surrogate. The probability ratio is

\[
r_t(\theta)=\frac{\pi_\theta(a_t\mid s_t)}{\pi_{\theta_{\mathrm{old}}}(a_t\mid s_t)}.
\]

At the old parameters, the gradient of \(\mathbb{E}_t[r_t(\theta)\hat A_t]\) matches the sampled policy-gradient estimator. Far from the behavior policy, however, the ratio and the state distribution can change enough that the local surrogate becomes unreliable.

### TRPO constrained update

The practical TRPO problem approximately maximizes the ratio surrogate subject to an empirical average-KL constraint:

\[
\max_\theta\;\mathbb{E}_t[r_t(\theta)\hat A_t]
\quad\text{subject to}\quad
\mathbb{E}_t[D_{\mathrm{KL}}(\pi_{\theta_{\mathrm{old}}}(\cdot\mid s_t)\,\|\,\pi_\theta(\cdot\mid s_t))]\leq\delta.
\]

TRPO linearizes the surrogate and quadratically approximates the KL divergence. If \(g\) is the surrogate gradient and \(F\) is the policy KL Hessian, the natural-gradient direction solves \(Fx=g\). Conjugate gradient and Fisher-vector products avoid forming \(F\) explicitly; the step is scaled to the KL budget, then a backtracking line search checks surrogate improvement and the sampled constraint.

The monotonic-improvement argument in the paper applies to a penalized theoretical update involving a maximum statewise divergence. The implemented average-KL constraint, finite samples, approximate advantages, truncated conjugate gradient, and line search are practical approximations to that result.

### PPO proximal surrogates

PPO proposes a KL-penalty variant and the more commonly used clipped-ratio objective:

\[
L^{\mathrm{CLIP}}(\theta)=\mathbb{E}_t\left[
\min\left(r_t(\theta)\hat A_t,
\operatorname{clip}(r_t(\theta),1-\epsilon,1+\epsilon)\hat A_t\right)
\right].
\]

For positive advantages, the clipped term removes incentive to increase the sampled action probability beyond the upper ratio boundary. For negative advantages, it removes incentive to decrease that probability beyond the lower boundary. Clipping is therefore a pessimistic local surrogate, not a projection, a hard bound on every probability ratio, or a direct KL constraint.

A typical PPO implementation combines the clipped policy objective with a fitted value loss and an entropy bonus. It then performs several shuffled minibatch epochs on one rollout batch before discarding that batch. Generalized advantage estimation (GAE) is commonly used to construct \(\hat A_t\), with \(\lambda\) controlling the practical bias-variance tradeoff of the estimator.

### Training loop shape

1. Freeze the behavior-policy parameters and collect an on-policy rollout batch.
2. Compute bootstrapped returns, advantages, old log probabilities, and usually old value predictions.
3. For TRPO, solve the approximate constrained step and accept it only if line-search checks pass.
4. For PPO, take a bounded number of first-order minibatch epochs on the clipped or KL-penalized objective.
5. Fit or update the value function, record diagnostics, then collect fresh data with the new policy.

## Key Principles

- The policy ratio corrects action probabilities under the old policy, but it does not correct the rollout state distribution after a large update. [evidence-based]
- TRPO's practical trust region is an average sampled KL constraint, while its strongest theoretical bound uses a stricter divergence quantity. [evidence-based]
- PPO clipping changes the optimization objective but does not guarantee that realized KL divergence or all probability ratios remain small. [evidence-based]
- Reusing a rollout for multiple PPO epochs improves data use relative to a single policy-gradient step, but the batch becomes progressively less on-policy as optimization proceeds. [evidence-based]
- Advantage quality matters because sign errors determine which side of the PPO clipping rule is active and can misdirect either algorithm. [evidence-based]
- The critic is a variance-reduction device for the policy update, so value loss is a diagnostic rather than the task objective itself. [evidence-based]
- TRPO and PPO optimize local surrogates and do not remove nonconvexity, partial observability, reward misspecification, or exploration failure. [evidence-based]

## Best Practices

- Log approximate KL, clip fraction, policy entropy, value error, explained variance, episodic return, and the number of accepted or rejected updates. [practitioner]
- For PPO, stop minibatch epochs early when measured KL materially exceeds a chosen target, since clipping alone does not enforce proximity. [practitioner]
- Treat the clip range, learning rate, rollout length, number of epochs, minibatch size, discount, and GAE \(\lambda\) as coupled controls rather than independent defaults. [practitioner]
- Preserve old log probabilities exactly for the sampled actions and test ratio computation, masking, termination handling, and advantage construction before tuning. [practitioner]
- Normalize advantages per training batch only as an implementation choice, and document it because it changes gradient scale and interactions with optimization. [practitioner]
- Keep policy and value losses separately observable, and consider separate optimizers or capacity when a shared network creates destructive interference. [practitioner]
- Compare algorithms across multiple seeds with identical environment steps, preprocessing, evaluation policy, and termination semantics. [evidence-based]

## Primary Sources

- John Schulman, Sergey Levine, Pieter Abbeel, Michael I. Jordan, and Philipp Moritz (2015), [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html), ICML, PMLR 37, arXiv:1502.05477.
- John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov (2017), [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347), arXiv:1707.06347.
- John Schulman, Philipp Moritz, Sergey Levine, Michael I. Jordan, and Pieter Abbeel (2015), [High-Dimensional Continuous Control Using Generalized Advantage Estimation](https://arxiv.org/abs/1506.02438), arXiv:1506.02438.
- Richard S. Sutton and Andrew G. Barto (2018), [Reinforcement Learning: An Introduction, second edition](http://incompleteideas.net/book/the-book-2nd.html), Chapter 13 on policy-gradient methods.

## Evidence Caveats

TRPO's theorem does not prove monotonic improvement for the exact neural-network implementation under finite sampling. The practical algorithm substitutes an average KL, approximate curvature, estimated advantages, and an acceptance heuristic for quantities in the bound.

The PPO paper reports favorable benchmark evidence for the tested objectives and settings, but it does not establish that clipping dominates TRPO, the KL-penalty form, or other policy optimizers across tasks. The clip range is not a universal safe step size, and implementation details can materially alter results.

Results from a small number of simulated-control or Atari seeds should not be treated as a universal ranking. Environment versions, time-limit handling, observation and reward normalization, network initialization, evaluation stochasticity, and total interaction budget can all change a comparison.

## Brain Hooks

- Folded concept: [[Trust-region and proximal methods (TRPO, PPO)]]
- Foundation: [[Policy gradient methods and REINFORCE]]
- Advantage estimation: [[Actor-critic methods (A2C A3C, GAE)]]
- Continuous-action context: [[Continuous control (DDPG, TD3, SAC)]]
- Post-training application: [[RLHF reward models and PPO post-training (InstructGPT lineage)]]
- Evaluation discipline: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Operational diagnostics: [[Debugging RL training runs in practice]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]
