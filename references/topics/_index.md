---
type: "reference"
title: "Topic Dossier Layer"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# Topic Dossier Layer

Purpose: hold the 24 distilled topic dossiers for reinforcement learning, one per canon target, with thesis, mechanics, principles, best practices, primary sources, caveats, and brain hooks.

Ownership note: `references/canon/` is generator-owned; `scripts/synthesize_brain.py` deletes and regenerates it from `references/source-ledger.json` on every pipeline run. Topic dossiers therefore live here, in `references/topics/`, which no generator script touches. The wiki concept notes under `assets/template-brain/wiki/concepts/` are folded from these dossiers by `scripts/fold_canon_to_concepts.py`.

## Dossier Ledger

| # | Target | Confidence | Fold | Status |
|---|---|---|---|---|
| 001 | [Markov decision processes and the RL problem formulation](001-markov-decision-processes-and-the-rl-problem-formulation.md) | evidence-based | [[Markov decision processes and the RL problem formulation]] | active |
| 002 | [Bandits and exploration-exploitation](002-bandits-and-exploration-exploitation.md) | evidence-based | [[Bandits and exploration-exploitation]] | active |
| 003 | [Dynamic programming, Monte Carlo, and temporal-difference learning](003-dynamic-programming-monte-carlo-and-temporal-difference-learning.md) | evidence-based | [[Dynamic programming, Monte Carlo, and temporal-difference learning]] | active |
| 004 | [Q-learning, SARSA, and tabular methods](004-q-learning-sarsa-and-tabular-methods.md) | evidence-based | [[Q-learning, SARSA, and tabular methods]] | active |
| 005 | [Function approximation and the deadly triad](005-function-approximation-and-the-deadly-triad.md) | practitioner | [[Function approximation and the deadly triad]] | active |
| 006 | [Deep Q-Networks and value-based deep RL (DQN, Rainbow)](006-deep-q-networks-and-value-based-deep-rl-dqn-rainbow.md) | practitioner | [[Deep Q-Networks and value-based deep RL (DQN, Rainbow)]] | active |
| 007 | [Policy gradient methods and REINFORCE](007-policy-gradient-methods-and-reinforce.md) | evidence-based | [[Policy gradient methods and REINFORCE]] | active |
| 008 | [Actor-critic methods (A2C A3C, GAE)](008-actor-critic-methods-a2c-a3c-gae.md) | evidence-based | [[Actor-critic methods (A2C A3C, GAE)]] | active |
| 009 | [Trust-region and proximal methods (TRPO, PPO)](009-trust-region-and-proximal-methods-trpo-ppo.md) | evidence-based | [[Trust-region and proximal methods (TRPO, PPO)]] | active |
| 010 | [Continuous control (DDPG, TD3, SAC)](010-continuous-control-ddpg-td3-sac.md) | evidence-based | [[Continuous control (DDPG, TD3, SAC)]] | active |
| 011 | [Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)](011-model-based-rl-and-planning-dyna-mbpo-alphazero-muzero.md) | evidence-based | [[Model-based RL and planning (Dyna, MBPO, AlphaZero, MuZero)]] | active |
| 012 | [Exploration strategies and intrinsic motivation](012-exploration-strategies-and-intrinsic-motivation.md) | evidence-based | [[Exploration strategies and intrinsic motivation]] | active |
| 013 | [Offline batch RL and conservatism](013-offline-batch-rl-and-conservatism.md) | evidence-based | [[Offline batch RL and conservatism]] | active |
| 014 | [Multi-agent RL](014-multi-agent-rl.md) | evidence-based | [[Multi-agent RL]] | active |
| 015 | [Hierarchical RL and options](015-hierarchical-rl-and-options.md) | evidence-based | [[Hierarchical RL and options]] | active |
| 016 | [Imitation learning and inverse RL](016-imitation-learning-and-inverse-rl.md) | evidence-based | [[Imitation learning and inverse RL]] | active |
| 017 | [Reward design, reward hacking, and specification gaming](017-reward-design-reward-hacking-and-specification-gaming.md) | evidence-based | [[Reward design, reward hacking, and specification gaming]] | active |
| 018 | [RLHF reward models and PPO post-training (InstructGPT lineage)](018-rlhf-reward-models-and-ppo-post-training-instructgpt-lineage.md) | evidence-based | [[RLHF reward models and PPO post-training (InstructGPT lineage)]] | active |
| 019 | [Direct preference optimization family (DPO, IPO, KTO, ORPO)](019-direct-preference-optimization-family-dpo-ipo-kto-orpo.md) | evidence-based | [[Direct preference optimization family (DPO, IPO, KTO, ORPO)]] | active |
| 020 | [GRPO and RL with verifiable rewards for reasoning models](020-grpo-and-rl-with-verifiable-rewards-for-reasoning-models.md) | evidence-based | [[GRPO and RL with verifiable rewards for reasoning models]] | active |
| 021 | [RLAIF and Constitutional AI](021-rlaif-and-constitutional-ai.md) | evidence-based | [[RLAIF and Constitutional AI]] | active |
| 022 | [Evaluation, benchmarks, and reproducibility in deep RL](022-evaluation-benchmarks-and-reproducibility-in-deep-rl.md) | evidence-based | [[Evaluation, benchmarks, and reproducibility in deep RL]] | active |
| 023 | [Debugging RL training runs in practice](023-debugging-rl-training-runs-in-practice.md) | practitioner | [[Debugging RL training runs in practice]] | active |
| 024 | [RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF)](024-rl-tooling-landscape-gymnasium-sb3-cleanrl-rllib-trl-verl-openrl.md) | practitioner | [[RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF)]] | active |
| 025 | [Agentic multi-turn RL for LLM agents](025-agentic-multi-turn-rl-for-llm-agents.md) | evidence-based | [[Agentic multi-turn RL for LLM agents]] | active |
| 026 | [Process reward models and step-level supervision](026-process-reward-models-and-step-level-supervision.md) | evidence-based | [[Process reward models and step-level supervision]] | active |
| 027 | [World models and latent imagination (Dreamer, Genie)](027-world-models-and-latent-imagination-dreamer-genie.md) | evidence-based | [[World models and latent imagination (Dreamer, Genie)]] | active |
| 028 | [Test-time compute and search for reasoning models](028-test-time-compute-and-search-for-reasoning-models.md) | evidence-based | [[Test-time compute and search for reasoning models]] | active |
| 029 | [POMDPs and partial observability](029-pomdps-and-partial-observability.md) | evidence-based | [[POMDPs and partial observability]] | active |
| 030 | [Meta-RL, generalization, and curricula](030-meta-rl-generalization-and-curricula.md) | evidence-based | [[Meta-RL, generalization, and curricula]] | active |
| 031 | [Safe and constrained RL](031-safe-and-constrained-rl.md) | evidence-based | [[Safe and constrained RL]] | active |
| 032 | [Distributed RL systems and self-play (IMPALA, Ape-X, league training)](032-distributed-rl-systems-and-self-play-impala-ape-x-league-training.md) | practitioner | [[Distributed RL systems and self-play (IMPALA, Ape-X, league training)]] | active |
| 033 | [Sim-to-real and robotics RL](033-sim-to-real-and-robotics-rl.md) | evidence-based | [[Sim-to-real and robotics RL]] | active |
| 034 | [Distributional RL](034-distributional-rl.md) | evidence-based | [[Distributional RL]] | active |
