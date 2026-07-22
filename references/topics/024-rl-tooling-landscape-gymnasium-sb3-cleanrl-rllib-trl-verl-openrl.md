---
type: "canon"
title: "024. RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF)"
created: "2026-07-22"
updated: "2026-07-23"
status: "active"
---

# 024. RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF)

Ledger: 024 | target: RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF) | confidence: practitioner | fold: [[RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF)]] | status: active.

## Core Thesis

An RL framework is part of the experimental method because its environment contract, data path, defaults, parallelism, and logging shape what is actually trained and measured. [evidence-based]
Gymnasium, Stable-Baselines3, CleanRL, RLlib, TRL, veRL, and OpenRLHF cover overlapping but distinct layers, so tool selection should begin with the workload and the evidence required. [verified]
There is no evidence here that one framework is universally best across classic control, distributed RL, and language-model post-training. [contested]

## How It Works

### 1. Map the workload before choosing a framework

Classic online RL repeatedly obtains an observation, samples an action, receives a reward and next state, stores transition data, and updates a policy or value function.
A common one-step target is

\[
y_t = r_t + \gamma\left(1 - \mathbb{1}[\mathrm{terminated}_t]\right)V(s_{t+1}).
\]

Language-model post-training instead begins with prompts, generates token sequences, scores whole or partial responses, and updates a policy under memory and throughput constraints.
Offline preference optimization begins with logged preference or feedback records rather than live environment steps.
These data paths share optimization concepts but impose different contracts on tooling.

### 2. Use Gymnasium as an environment contract

Gymnasium defines an `Env` interface around `reset()` and `step()` plus observation and action spaces.
Its step result distinguishes `terminated` from `truncated`, which affects bootstrapping and reset logic.
Wrappers, vector environments, registration, and checker utilities help compose tasks, but custom semantic tests remain necessary.
Gymnasium supplies the task-facing layer rather than a complete learning algorithm.

### 3. Choose an inspectable or packaged classic-RL learner

Stable-Baselines3 provides documented PyTorch implementations, policy interfaces, callbacks, evaluation helpers, and vectorized-environment integration.
It is useful when a compact high-level training API and maintained algorithm implementations fit the experiment.

CleanRL presents single-file implementations with research-friendly details exposed in the training script.
Its small surface can make algorithm study and differential debugging convenient, while extension and production lifecycle concerns remain the operator's responsibility.

### 4. Add distributed orchestration when the workload requires it

RLlib organizes RL workloads around environment runners, learner processes, replay or sampling components, and configurable scaling.
That architecture can separate sampling and learning resources across processes or nodes.
Distribution also introduces policy-version lag, serialization, fault handling, resource scheduling, and reproducibility concerns that must be measured rather than assumed away.

### 5. Treat language-model post-training as a systems workload

TRL provides trainers and utilities for supervised fine-tuning, reward modeling, preference optimization, and RL-style post-training in the Hugging Face ecosystem.
veRL focuses on flexible RL training for large language models with distributed execution and configurable worker roles.
OpenRLHF provides a distributed RLHF training stack with multiple training stages and serving or generation integrations.

In TRL 1.9.0, GRPO is documented as online generated-rollout training, while DPO is documented as offline preference-pair training. The corresponding data contracts differ: GRPO needs generated completions plus rewards or environments, while DPO needs `prompt`, preferred `chosen`, and dispreferred `rejected` records. [verified]

The 2026-07-22 release snapshot is Gymnasium 1.3.0 (2026-04-22), Stable-Baselines3 2.9.0 (2026-06-15), CleanRL PyPI 1.2.0 (2023-05-22) with GitHub release v1.0.0 (2022-11-14), Ray/RLlib 2.56.1 (2026-07-17), TRL 1.9.0 (2026-07-21), veRL 0.8.0 (2026-06-01), and OpenRLHF 0.10.4 (2026-06-08). Release recency supports an active label for every listed project except CleanRL, whose release activity is slow; this is not a declaration about repository archival. [verified]

TRL v1.0.0, released 2026-03-31, introduced experimental Async GRPO and `GRPOConfig(loss_type="vespo")`. TRL v1.9.0 adds iterable or streaming GRPO and RLOO support with `max_steps` required and `dispatch_batches=False` enforced for iterable datasets, plus `DPOConfig(loss_type="sigmoid_norm")` for a length-normalized DPO sigmoid loss. Pin a TRL minor version before applying a recipe. [verified]

Model cards may name a post-training algorithm, such as GSPO, while omitting reward semantics and training-stack provenance. Treat that disclosure as a pointer to [[GRPO and RL with verifiable rewards for reasoning models]], not evidence that a listed framework implements the vendor recipe without a pinned implementation source. [evidence-based]

### 2026 watchlist

vime and Miles are 2026 watchlist entries rather than core-comparison tools. vime's maintainers describe a vLLM and Megatron-oriented LLM RL framework, and a PyTorch-hosted vendor article describes Miles as composing SGLang, Megatron-LM, Ray, and PyTorch. Their framework and performance descriptions presently rest on maintainer or vendor material only. [practitioner]

Feature sets and supported algorithms change quickly.
Pin the version, read the matching documentation, and verify that the implemented objective, tokenizer behavior, generation settings, KL treatment, reward aggregation, and checkpoint semantics match the experiment.

### 6. Validate the selected stack end to end

Start from an official minimal example at the pinned release.
Replace its task with a deterministic probe, inspect one trajectory and one update, then restore the real workload one component at a time.
Measure correctness, sample throughput, learner throughput, accelerator utilization, communication overhead, checkpoint behavior, and evaluation reproducibility separately.
Use [[Debugging RL training runs in practice]] when an abstraction boundary hides the source of a failure.

## Key Principles

- Gymnasium primarily standardizes environment interaction; it does not provide the policy-learning stack described by the other tools. [verified]
- Termination semantics, wrappers, vectorization, normalization, and autoreset behavior are algorithmically relevant interface details. [evidence-based]
- Stable-Baselines3 favors a packaged API while CleanRL exposes compact training scripts, but which tradeoff is preferable depends on the experiment. [practitioner]
- RLlib exposes distributed sampling and learning controls, yet distribution alone does not establish faster convergence or better final policy quality. [evidence-based]
- In language-model RL, generation, sharding, placement, tokenizer, and reward-pipeline settings can alter the effective training procedure. [evidence-based]
- Official feature lists establish supported interfaces at a particular version, not independent comparative performance. [verified]
- Claims that any listed framework is the universal state of the art or best default remain unsupported across all workload classes. [contested]

## Best Practices

- Write a requirements matrix covering task type, algorithm, model scale, hardware, distribution, observability, extensibility, and reproducibility before selecting tools. [practitioner]
- Pin library, framework, driver, and accelerator versions, and archive the resolved configuration with every run. [evidence-based]
- Run the framework's environment checker and add independent tests for reward timing, observation bounds, reset behavior, termination, and truncation. [evidence-based]
- Reproduce an official minimal example, then validate a deterministic probe task before porting a full experiment. [practitioner]
- Keep training and evaluation processes distinct, preserve raw per-episode results, and version checkpoints with their exact preprocessing and generation settings. [practitioner]
- Scale one axis at a time and log sample throughput, learner throughput, utilization, communication time, queue depth, and policy lag where applicable. [practitioner]
- Review release notes and migration guides before an upgrade, then rerun correctness and reproducibility checks under the new version. [evidence-based]
- Treat Async GRPO and VESPO as explicitly versioned experimental TRL paths, and rerun objective and data-pipeline tests when moving between TRL minor releases. [practitioner]
- For TRL 1.9 iterable GRPO or RLOO inputs, set and record `max_steps`, preserve grouped prompts, and confirm the enforced `dispatch_batches=False` path before scaling. [practitioner]
- Keep vime and Miles in an evaluated watchlist until independent reproducibility, systems, and performance evidence is available. [practitioner]

## Primary Sources

- Farama Foundation, [Gymnasium Env API](https://gymnasium.farama.org/api/env/). Official environment interface, including reset, step, spaces, termination, and truncation. [verified]
- Stable-Baselines3 maintainers, [Stable-Baselines3 documentation](https://stable-baselines3.readthedocs.io/en/master/). Official algorithms, policies, callbacks, evaluation utilities, and usage guidance. [verified]
- Shengyi Huang et al., 2022, [CleanRL: High-quality Single-file Implementations of Deep Reinforcement Learning Algorithms](https://www.jmlr.org/papers/v23/21-1342.html), with [official documentation](https://docs.cleanrl.dev/). Primary paper and project documentation for CleanRL's design and implementations. [verified]
- Ray Project, [RLlib documentation](https://docs.ray.io/en/latest/rllib/index.html). Official architecture, algorithm, environment, and scaling documentation. [verified]
- Hugging Face, [TRL documentation](https://huggingface.co/docs/trl/index). Official trainer and method documentation for transformer post-training. [verified]
- veRL maintainers, [veRL documentation](https://verl.readthedocs.io/en/latest/). Official documentation for the distributed reinforcement-learning training framework. [verified]
- OpenRLHF maintainers, [OpenRLHF documentation](https://openrlhf.readthedocs.io/en/latest/). Official installation, training, and distributed-system documentation. [verified]
- Jian Hu et al., 2024, [OpenRLHF: An Easy-to-use, Scalable and High-performance RLHF Framework](https://arxiv.org/abs/2405.11143). Project paper describing the framework's architecture and reported experiments. [evidence-based]
- Tooling release snapshot, [Gymnasium 1.3.0](https://github.com/Farama-Foundation/Gymnasium/releases/tag/v1.3.0), 2026-04-22; [Stable-Baselines3 2.9.0](https://github.com/DLR-RM/stable-baselines3/releases/tag/v2.9.0), 2026-06-15; [Ray 2.56.1](https://github.com/ray-project/ray/releases/tag/ray-2.56.1), 2026-07-17; [TRL 1.9.0 release notes](https://github.com/huggingface/trl/releases), 2026-07-21; [veRL 0.8.0](https://github.com/verl-project/verl/releases/tag/v0.8.0), 2026-06-01; [OpenRLHF 0.10.4](https://github.com/OpenRLHF/OpenRLHF/releases/tag/v0.10.4), 2026-06-08. [verified]
- Hugging Face, [TRL v1.0.0 release notes](https://github.com/huggingface/trl/releases/tag/v1.0.0), 2026-03-31; and [DPO trainer documentation](https://huggingface.co/docs/trl/dpo_trainer), version 1.9.0. [verified]
- vLLM Project, [vime announcement](https://vllm-project.github.io/2026/06/09/announcing-vime.html), 2026-06-09; and PyTorch, [Miles announcement](https://pytorch.org/blog/miles-a-pytorch-native-stack-for-large-scale-llm-rl-post-training/), 2026-06-30. [practitioner]

## Evidence Caveats

- Documentation reflects particular releases and may change after 2026-07-22; a reproducible run must record the version actually used. [verified]
- Project-maintainer documentation is authoritative for interfaces but is not independent evidence for comparative speed, scalability, stability, or policy quality. [verified]
- The OpenRLHF paper reports results for its tested configurations and does not establish superiority for untested models, clusters, objectives, or framework versions. [evidence-based]
- Stable-Baselines3 and CleanRL cover selected algorithms and environments; neither source proves suitability for every RL problem. [verified]
- RLlib's configurable distributed architecture exposes scaling mechanisms, but realized scaling depends on workload balance, communication, hardware, and configuration. [evidence-based]
- TRL, veRL, and OpenRLHF evolve rapidly, so named trainer and backend support should be checked against the pinned release. [verified]
- Similar algorithm labels can conceal different loss normalization, KL estimation, clipping, batching, reward, and generation semantics. [evidence-based]
- Framework choice cannot compensate for an invalid environment, misspecified reward, weak evaluation protocol, or inadequate statistical reporting. [evidence-based]
- The release snapshot is date-bound. CleanRL's divergent PyPI and GitHub release labels support only a slow release-activity description, not a conclusion that its repository is archived or unusable. [verified]
- TRL versioned documentation establishes interface and configuration availability, not that Async GRPO, VESPO, streaming GRPO, or `sigmoid_norm` is a best recipe for a particular workload. [verified]
- vime and Miles remain maintainer or vendor descriptions without an independent benchmark, scalability, stability, or training-quality comparison. [practitioner]

## Brain Hooks

- Folded concept: [[RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF)]]
- Evaluation discipline: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Debugging workflow: [[Debugging RL training runs in practice]]
- Value-based baseline: [[Deep Q-Networks and value-based deep RL (DQN, Rainbow)]]
- Proximal baseline: [[Trust-region and proximal methods (TRPO, PPO)]]
- Continuous control: [[Continuous control (DDPG, TD3, SAC)]]
- Distributed agents: [[Multi-agent RL]]
- Human-feedback pipeline: [[RLHF reward models and PPO post-training (InstructGPT lineage)]]
- Offline preferences: [[Direct preference optimization family (DPO, IPO, KTO, ORPO)]]
- Verifiable-reward training: [[GRPO and RL with verifiable rewards for reasoning models]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]
