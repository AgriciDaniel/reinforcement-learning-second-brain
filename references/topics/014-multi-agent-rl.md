---
type: "canon"
title: "014. Multi-agent RL"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 014. Multi-agent RL

Ledger: 014 | target: Multi-agent RL | confidence: evidence-based | fold: [[Multi-agent RL]] | status: active.

## Core Thesis

Multi-agent reinforcement learning studies sequential decisions when several adaptive agents jointly affect transitions and rewards. Each learner faces strategic dependence, partial information, and moving co-learners, so a process that appears stationary in the joint state can be nonstationary from one agent's local perspective. Centralized training with decentralized execution uses joint information to improve learning while preserving the information and action constraints imposed at execution.

## How It Works

A Markov game has state `s`, agents `i = 1,...,n`, joint action `a = (a_1,...,a_n)`, transition kernel `P(s'|s,a)`, and agent-specific rewards `r_i(s,a)`. Under partial observability, agent `i` acts from a local observation or action-observation history `tau_i` using `pi_i(a_i|tau_i)`. Shared rewards define a fully cooperative objective, while distinct rewards permit mixed cooperative-competitive or general-sum interactions.

Independent learning treats other agents as part of the environment. Because their policies change during training, the transition and reward distribution induced for any one learner also changes. Replay data can therefore become stale in a way that is not explained by the learner's own current policy, and credit assignment must separate the effect of one action from the joint behavior.

Multi-Agent Deep Deterministic Policy Gradient, or MADDPG, gives each agent a decentralized actor `mu_i(o_i)` and a centralized action-value critic `Q_i(x,a_1,...,a_n)` during training. Here `x` denotes the joint observations or other centralized information available only to the trainer. Each agent may optimize its own reward, so centralized critics do not require identical objectives or a shared actor.

The MADDPG critic target is `y_i = r_i + gamma Q_i'(x', mu_1'(o_1'),...,mu_n'(o_n'))`, using target actors and a target critic. Its deterministic policy-gradient estimate is `E[grad_theta_i mu_i(o_i) grad_a_i Q_i(x,a_1,...,a_n)]`, evaluated at the actors' current joint actions. Joint transitions enter replay, critics regress toward their targets, actors ascend their centralized-critic objectives, and target networks update slowly.

MADDPG also studies policy ensembles, sampling a policy from each agent's ensemble for an episode so that training encounters a wider distribution of counterpart behavior. This is an empirical robustness device from the paper, not a guarantee against all unseen partners or adversaries.

QMIX addresses fully cooperative, decentralized discrete control through value factorization. Each agent learns a recurrent utility `Q_i(tau_i,a_i)`, while a mixing network combines those utilities with global state into `Q_tot(tau,a,s)`. Hypernetworks conditioned on state produce nonnegative mixing weights, structurally enforcing `partial Q_tot / partial Q_i >= 0`.

The monotonicity constraint makes decentralized greedy action selection consistent with maximizing the centralized value: each agent can choose `argmax_a_i Q_i(tau_i,a_i)` without enumerating the joint action space. QMIX minimizes a joint temporal-difference loss such as `(y_tot - Q_tot)^2`, with `y_tot = r + gamma max_a' Q_tot_target(tau',a',s')`; target networks and replay support off-policy training. At execution, only the per-agent recurrent utilities and local histories are needed.

## Key Principles

- The relevant formal object is a joint policy in a Markov game or partially observable stochastic game, even when learning code exposes one agent at a time. [evidence-based]
- Simultaneously changing policies create nonstationarity for local learners and complicate replay, exploration, and attribution of reward. [evidence-based]
- Centralized training may use joint observations, actions, or global state, but decentralized execution must not depend on information unavailable to an acting agent. [evidence-based]
- MADDPG conditions each agent's critic on joint actions while keeping its actor local, which supports cooperative, competitive, and mixed reward structures considered in the paper. [evidence-based]
- QMIX makes joint greedy maximization tractable by monotonic value factorization, but this restriction excludes some joint value functions. [evidence-based]
- Parameter sharing, a centralized critic, and a shared team reward are separate design choices and should not be conflated. [practitioner]
- Training against a narrow population can produce coordination conventions or exploits that fail with new partners, opponents, or population sizes. [practitioner]

## Best Practices

- Specify observations, action timing, rewards, communication, agent identities, termination semantics, and which information exists only during training before choosing an algorithm. [practitioner]
- Match the method to the game: MADDPG is naturally aligned with the paper's continuous-action mixed settings, while QMIX assumes a cooperative objective and decentralized discrete greedy actions. [evidence-based]
- Store synchronized joint transitions for centralized critics or mixers, and mask unavailable actions plus terminated agents consistently in both online and target calculations. [practitioner]
- Test execution code with privileged state removed; a centralized-training feature leak can create an apparently strong policy that is not deployable. [practitioner]
- Use target networks, controlled replay age, gradient diagnostics per agent, and explicit checks for one learner dominating the joint loss. [practitioner]
- Evaluate independent seeds and held-out partner or opponent populations, including cross-play rather than only self-play with the final training cohort. [practitioner]
- Report per-agent returns, team return where applicable, success criteria, and dispersion across runs; a single aggregate can hide asymmetric failure. [practitioner]

## Primary Sources

- Ryan Lowe, Yi Wu, Aviv Tamar, Jean Harb, Pieter Abbeel, and Igor Mordatch (2017), *Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments*, Advances in Neural Information Processing Systems 30, arXiv:1706.02275. https://proceedings.neurips.cc/paper_files/paper/2017/hash/68a9750337a418a86fe06c1991a1d64c-Abstract.html
- Tabish Rashid, Mikayel Samvelyan, Christian Schroeder de Witt, Gregory Farquhar, Jakob Foerster, and Shimon Whiteson (2018), *QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning*, Proceedings of the 35th International Conference on Machine Learning, PMLR 80, arXiv:1803.11485. https://proceedings.mlr.press/v80/rashid18a.html

## Evidence Caveats

- MADDPG's experiments use a limited collection of particle-world cooperative and competitive tasks. They do not establish universal scaling, robustness, or superiority over later methods.
- The policy-ensemble results in MADDPG are empirical and environment-specific; ensemble training does not prove generalization to arbitrary strategic behavior.
- QMIX's original evidence comes from cooperative StarCraft II micromanagement tasks and contemporaneous baselines under the paper's protocol. Reported comparisons should remain scoped to that setup.
- QMIX's monotonic mixing is sufficient for decentralized argmax consistency, but some coordination problems require action rankings that depend non-monotonically on other agents' actions.
- Centralized training assumes privileged joint information and a training infrastructure that can align experience across agents. Those assumptions may fail in distributed or privacy-constrained systems.
- Neither source resolves equilibrium selection, opponent adaptation, communication learning, open populations, or reliable generalization across numbers and types of agents.
- Apparent nonstationarity does not by itself identify the root cause of a failed run; representation, exploration, reward design, and implementation errors remain competing explanations.
- Results can vary with seeds, teammate populations, evaluation opponents, environment versions, and tie-breaking, so single-seed win rates are weak evidence.

## Brain Hooks

- Folded concept: [[Multi-agent RL]]
- Formal foundation: [[Markov decision processes and the RL problem formulation]]
- Gradient foundation: [[Policy gradient methods and REINFORCE]]
- Centralized-critic context: [[Actor-critic methods (A2C A3C, GAE)]]
- Continuous-control context: [[Continuous control (DDPG, TD3, SAC)]]
- Value-learning context: [[Deep Q-Networks and value-based deep RL (DQN, Rainbow)]]
- Coordination exploration: [[Exploration strategies and intrinsic motivation]]
- Evaluation discipline: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Run diagnosis: [[Debugging RL training runs in practice]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]
