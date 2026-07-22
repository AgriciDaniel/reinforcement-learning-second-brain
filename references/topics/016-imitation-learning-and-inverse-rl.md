---
type: "canon"
title: "016. Imitation learning and inverse RL"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 016. Imitation learning and inverse RL

Ledger: 016 | target: Imitation learning and inverse RL | confidence: evidence-based | fold: [[Imitation learning and inverse RL]] | status: active.

## Core Thesis

Imitation learning uses demonstrations to learn behavior, while inverse reinforcement learning asks which reward could make demonstrated behavior optimal. Behavioral cloning learns actions directly by supervised learning, classical inverse RL searches over rewards, and GAIL learns a policy by adversarially matching the expert's discounted state-action occupancy. These objectives are related but not interchangeable, especially when the desired artifact is a transferable reward rather than a policy for the demonstrated environment.

## How It Works

Given demonstration trajectories \(\mathcal D_E=\{\tau_i\}\), behavioral cloning treats the expert state-action pairs as supervised examples and minimizes negative log likelihood:

\[
\mathcal L_{\mathrm{BC}}(\theta)
=-\mathbb E_{(s,a)\sim\mathcal D_E}
\left[\log \pi_\theta(a\mid s)\right].
\]

The learner is trained only on states visited by the demonstrator. When its own prediction error leads to a different state, the next decision may be out of the training distribution, so one-step supervised accuracy does not directly control closed-loop trajectory error.

Classical inverse RL assumes an MDP model, a discount, and observed expert behavior. It seeks a reward \(r\) for which the expert policy \(\pi_E\) satisfies the optimality inequalities

\[
Q_r^{\pi_E}(s,\pi_E(s))
\ge Q_r^{\pi_E}(s,a)
\quad\text{for all relevant }s,a.
\]

The zero reward satisfies these inequalities for every policy, and many nonzero rewards can rationalize the same behavior. Ng and Russell therefore formulate linear programs that prefer a margin between the expert action and alternatives while constraining or penalizing reward magnitude. A schematic finite-state form introduces margins \(\xi_s\):

\[
\max_{r,\xi}\ \sum_s \xi_s-\lambda\lVert r\rVert_1
\]

subject to

\[
Q_r^{\pi_E}(s,\pi_E(s))-Q_r^{\pi_E}(s,a)\ge\xi_s,
\]

plus reward bounds and the policy-optimality constraints. Their paper develops cases for a known policy in a finite MDP, sampled transition estimates in large state spaces, and finite observed trajectories.

GAIL starts from the discounted state-action occupancy measure

\[
\rho_\pi(s,a)
=\sum_{t=0}^{\infty}\gamma^t
\Pr_\pi(S_t=s,A_t=a).
\]

Matching \(\rho_\pi\) to \(\rho_{\pi_E}\) matches how often the policy visits state-action pairs under the paper's MDP and initial-state assumptions. Ho and Ermon connect regularized IRL followed by RL to a primal occupancy-matching problem, then use an adversarial discriminator to obtain the saddle objective

\[
\min_\pi\max_D\
\mathbb E_{(s,a)\sim\rho_\pi}[\log D(s,a)]
+\mathbb E_{(s,a)\sim\rho_{\pi_E}}[\log(1-D(s,a))]
-\lambda H(\pi).
\]

Here \(H(\pi)\) is discounted causal entropy. This label convention assigns \(D=1\) to learner samples and \(D=0\) to expert samples; swapping labels gives an equivalent classifier with the corresponding policy loss.

The GAIL training loop alternates:

1. Roll out the current policy in the environment to collect learner state-action pairs.
2. Update the discriminator to distinguish learner pairs from expert pairs.
3. Treat the discriminator output as a local learned cost.
4. Update the policy with a KL-constrained TRPO step and causal-entropy regularization.
5. Repeat with the new learner occupancy.

With the discriminator optimized in the theoretical objective, the policy term corresponds, up to constants and conventions, to minimizing Jensen-Shannon divergence between learner and expert occupancy measures. The practical neural algorithm approximates this alternating game and directly returns a policy, not an identified ground-truth reward.

## Key Principles

- Behavioral cloning is supervised policy estimation and does not require environment interaction during fitting. [evidence-based]
- One-step imitation loss is measured on the expert's state distribution, while deployment decisions are made on the learner's induced state distribution, allowing errors to compound through covariate shift. [evidence-based]
- Inverse RL is underdetermined without extra assumptions because multiple rewards, including a trivial constant reward, can make the same policy optimal. [evidence-based]
- Any recovered reward is conditional on the modeled dynamics, discount, observation representation, reward class, and assumptions about demonstrator optimality. [evidence-based]
- GAIL bypasses an explicit intermediate reward-recovery stage and learns a policy by adversarial occupancy matching. [evidence-based]
- The GAIL derivation links a regularized IRL-plus-RL construction to occupancy matching, but it does not make the discriminator a uniquely identified human objective. [evidence-based]
- Model-free GAIL still needs learner rollouts from the environment, so expert-data efficiency and environment-interaction efficiency are separate quantities. [evidence-based]
- Policy imitation, behavior prediction, and transferable reward inference are distinct deliverables and should be evaluated against different success criteria. [practitioner]

## Best Practices

- Decide first whether the required output is an action policy, a reward for downstream planning, or an explanation of behavior; this choice determines whether cloning, direct imitation, or IRL fits the use case. [practitioner]
- Train behavioral cloning as a transparent baseline and evaluate it with closed-loop rollouts from deployment-relevant initial states, not only held-out action accuracy. [practitioner]
- Split validation data by complete trajectories or demonstrators when possible so adjacent state-action pairs from one rollout do not leak across evaluation partitions. [practitioner]
- For inverse RL, document the transition model, discount, reward feature class, optimality model, and regularization, then test how the inferred reward changes under plausible alternatives. [practitioner]
- For GAIL, track discriminator accuracy and loss together with policy return, occupancy summaries, entropy, KL movement, and environment steps; classifier saturation alone is not evidence of successful imitation. [practitioner]
- Balance discriminator and policy updates empirically, and rerun multiple seeds, because the cited paper does not establish a universal update ratio or architecture. [practitioner]
- Consider behavioral-cloning initialization when environment interaction is costly, while treating its benefit as task-dependent rather than guaranteed. [practitioner]
- Evaluate safety-relevant and task-relevant state visitation, not only aggregate return, because two policies can receive similar evaluation scores while differing on rare states. [practitioner]

## Primary Sources

- Andrew Y. Ng and Stuart Russell (2000), "Algorithms for Inverse Reinforcement Learning," Proceedings of the Seventeenth International Conference on Machine Learning (ICML 2000). [Author-hosted primary paper PDF](https://ai.stanford.edu/~ang/papers/icml00-irl.pdf)
- Jonathan Ho and Stefano Ermon (2016), "Generative Adversarial Imitation Learning," Advances in Neural Information Processing Systems 29, arXiv:1606.03476. [Official NeurIPS proceedings](https://proceedings.neurips.cc/paper/2016/hash/cc7e2b878868cbae992d1fb743995d8f-Abstract.html) and [arXiv record](https://arxiv.org/abs/1606.03476)

## Evidence Caveats

- Ng and Russell's formal algorithms depend on known or estimated MDP structure and an optimality interpretation of behavior; they do not identify a unique true reward from demonstrations alone.
- Margin and norm choices resolve an optimization ambiguity by preference, not by proving that the selected reward is the demonstrator's internal objective.
- GAIL's occupancy and divergence characterization is exact for the stated mathematical setup. Finite trajectories, restricted networks, approximate discriminator updates, and approximate policy optimization introduce gaps.
- The GAIL experiments use simulated control tasks and generated expert policies. They do not establish reliability for human demonstrations, partial observability, real-world safety constraints, or severe dynamics mismatch.
- The GAIL paper reports strong results in its tested suite but also a task where behavioral cloning was more sample efficient, so it does not support universal superiority over cloning.
- Ho and Ermon explicitly note that their model-free method is not especially efficient in environment interaction, despite using expert demonstrations efficiently in their experiments.
- Neither source proves robustness to imperfect, heterogeneous, strategically misleading, or out-of-distribution demonstrations.
- Matching demonstrated occupancy can reproduce behavior without recovering intent, causal preferences, or a reward that transfers when dynamics or available actions change.
- Adversarial training and policy optimization can introduce seed sensitivity and optimization failures that the underlying occupancy objective does not eliminate.

## Brain Hooks

- Folded concept: [[Imitation learning and inverse RL]]
- Formal environment model: [[Markov decision processes and the RL problem formulation]]
- Policy optimization mechanics: [[Policy gradient methods and REINFORCE]]
- Critic-based optimization: [[Actor-critic methods (A2C A3C, GAE)]]
- GAIL policy step lineage: [[Trust-region and proximal methods (TRPO, PPO)]]
- Fixed-data boundary: [[Offline batch RL and conservatism]]
- Reward ambiguity and misuse: [[Reward design, reward hacking, and specification gaming]]
- Evaluation discipline: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Run diagnosis: [[Debugging RL training runs in practice]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]
const result = await tools.apply_patch(patch);
text(result);
