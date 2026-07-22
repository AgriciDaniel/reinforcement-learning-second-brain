---
type: "canon"
title: "010. Continuous control (DDPG, TD3, SAC)"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 010. Continuous control (DDPG, TD3, SAC)

Ledger: 010 | target: Continuous control (DDPG, TD3, SAC) | confidence: evidence-based | fold: [[Continuous control (DDPG, TD3, SAC)]] | status: active.

## Core Thesis

DDPG, TD3, and SAC are model-free, off-policy actor-critic algorithms designed for continuous action spaces, where enumerating actions for a greedy value update is impractical. DDPG learns a deterministic actor, TD3 adds mechanisms that reduce exploitation of critic error, and SAC learns a stochastic policy under a maximum-entropy objective. Their replay-based data reuse can improve interaction efficiency, but their bootstrapped critics still make optimization sensitive to data coverage, reward scale, and function-approximation error.

## How It Works

### Shared off-policy backbone

An actor proposes a bounded continuous action and a critic estimates its long-run value. Each transition \((s_t,a_t,r_t,s_{t+1},d_t)\) enters a replay buffer, where \(d_t\) indicates a true terminal transition. Minibatches sampled from replay train Bellman targets, while slowly updated target networks reduce rapid movement of those targets.

For a generic target parameter vector \(\bar\theta\), Polyak averaging has the form

\[
\bar\theta\leftarrow\rho\bar\theta+(1-\rho)\theta,
\]

with \(\rho\) close to one in this notation. This convention is equivalent to using a small interpolation coefficient on the online parameters.

### DDPG

DDPG uses a deterministic actor \(\mu_\phi(s)\), critic \(Q_\theta(s,a)\), replay buffer, and target copies of both networks. Its one-step target is

\[
y=r+\gamma(1-d)Q_{\bar\theta}(s',\mu_{\bar\phi}(s')).
\]

The critic minimizes \(\mathbb{E}[(Q_\theta(s,a)-y)^2]\). The deterministic policy gradient updates the actor through the critic:

\[
\nabla_\phi J\approx
\mathbb{E}_{s\sim\mathcal D}\left[
\nabla_a Q_\theta(s,a)|_{a=\mu_\phi(s)}\nabla_\phi\mu_\phi(s)
\right].
\]

Because the target actor is deterministic, exploration comes from a separate behavior process, commonly action noise added during data collection. Replay makes learning off-policy, while target networks and normalization choices were important stabilizers in the original deep implementation.

### TD3

TD3 retains DDPG's deterministic actor but changes three coupled parts of the update. It learns two critics and uses the smaller target estimate, adds clipped noise to the target action, and updates the actor and target networks less frequently than the critics.

With \(\varepsilon\sim\operatorname{clip}(\mathcal N(0,\sigma),-c,c)\) and the noisy target action clipped to the valid action range, the critic target is

\[
y=r+\gamma(1-d)\min_{i\in\{1,2\}}
Q_{\bar\theta_i}(s',\operatorname{clip}(\mu_{\bar\phi}(s')+\varepsilon)).
\]

The minimum reduces the actor's opportunity to exploit a spuriously high target from either critic. Target-policy smoothing trains values for a neighborhood of actions rather than a single sharp target action. Delayed policy updates give the critics additional optimization steps before their current estimates steer the actor, and the actor is conventionally optimized against the first critic.

### SAC

SAC optimizes a maximum-entropy return, which rewards task performance and policy entropy:

\[
J(\pi)=\mathbb{E}\left[\sum_t\gamma^t
(r_t+\alpha\mathcal H(\pi(\cdot\mid s_t)))\right].
\]

In the widely used later 2018 formulation, the actor is typically a reparameterized, tanh-squashed Gaussian. Given \(a'\sim\pi_\phi(\cdot\mid s')\), two target critics define

\[
y=r+\gamma(1-d)\left[
\min_i Q_{\bar\theta_i}(s',a')-\alpha\log\pi_\phi(a'\mid s')
\right].
\]

The actor minimizes

\[
J_\pi(\phi)=\mathbb{E}_{s\sim\mathcal D,a\sim\pi_\phi}
[\alpha\log\pi_\phi(a\mid s)-\min_i Q_{\theta_i}(s,a)].
\]

The temperature \(\alpha\) sets the reward-entropy tradeoff. The follow-up formulation can optimize \(\alpha\) against a target entropy through a dual objective. The ICML 2018 SAC algorithm instead presents a separate soft value network and a fixed temperature or reward scale, so these variants should not be described as one unchanged algorithm.

### Training loop shape

1. Scale the actor output into the environment's legal action range and collect a transition with an exploratory deterministic policy or SAC's stochastic policy.
2. Store the transition in replay, preserving whether episode end was a true terminal state or an external time limit.
3. Sample a minibatch and update the critic or critics toward target-network Bellman backups.
4. Update the actor through the critic, on every scheduled step for DDPG or SAC and on delayed steps for TD3.
5. Update target networks, and for automatic-temperature SAC also update \(\alpha\).
6. Evaluate with a separately defined policy, usually noise-free for DDPG and TD3 and explicitly deterministic or stochastic for SAC.

## Key Principles

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

## Primary Sources

- David Silver, Guy Lever, Nicolas Heess, Thomas Degris, Daan Wierstra, and Martin Riedmiller (2014), [Deterministic Policy Gradient Algorithms](https://proceedings.mlr.press/v32/silver14.html), ICML, PMLR 32.
- Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, and Daan Wierstra (2015), [Continuous Control with Deep Reinforcement Learning](https://arxiv.org/abs/1509.02971), arXiv:1509.02971, presented at ICLR 2016.
- Scott Fujimoto, Herke van Hoof, and David Meger (2018), [Addressing Function Approximation Error in Actor-Critic Methods](https://proceedings.mlr.press/v80/fujimoto18a.html), ICML, PMLR 80, arXiv:1802.09477.
- Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine (2018), [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html), ICML, PMLR 80, arXiv:1801.01290.
- Tuomas Haarnoja et al. (2018), [Soft Actor-Critic Algorithms and Applications](https://arxiv.org/abs/1812.05905), arXiv:1812.05905, including the automatic-temperature formulation.
- Richard S. Sutton and Andrew G. Barto (2018), [Reinforcement Learning: An Introduction, second edition](http://incompleteideas.net/book/the-book-2nd.html), Chapter 13 on policy-gradient methods.

## Evidence Caveats

The original papers evaluate particular simulated-control tasks, architectures, environment versions, and tuning protocols. Their reported comparisons do not prove a universal ordering among DDPG, TD3, SAC, on-policy methods, or model-based control.

DDPG can be especially sensitive to critic error and exploration, while TD3 mitigates rather than eliminates those failures. Taking a minimum over two learned critics can trade overestimation for pessimism, and target smoothing can blur genuinely narrow optima.

SAC's entropy can aid exploration and robustness in the tested settings, but a target-entropy heuristic is not a task-independent optimum. Fixed-temperature SAC, automatic-temperature SAC, the original value-network architecture, and later no-value-network implementations are materially different experimental specifications.

Seed variance, simulator determinism, action scaling, time-limit bootstrapping, replay initialization, update-to-data ratio, and evaluation mode can change conclusions. None of these sources establishes safety, real-world transfer, or reliable learning from a fixed dataset without additional assumptions.

## Brain Hooks

- Folded concept: [[Continuous control (DDPG, TD3, SAC)]]
- Policy-gradient foundation: [[Policy gradient methods and REINFORCE]]
- Critic foundation: [[Actor-critic methods (A2C A3C, GAE)]]
- Stability context: [[Function approximation and the deadly triad]]
- Proximal comparison: [[Trust-region and proximal methods (TRPO, PPO)]]
- Dynamics-aware alternative: [[Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)]]
- Data-coverage boundary: [[Offline batch RL and conservatism]]
- Exploration context: [[Exploration strategies and intrinsic motivation]]
- Reproducibility: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Operational diagnostics: [[Debugging RL training runs in practice]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]
