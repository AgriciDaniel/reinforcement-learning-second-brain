---
type: "concept"
title: "RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF)"
domain: "reinforcement learning: fundamentals, deep RL, RLHF/RLAIF and preference optimization, evaluation, tooling, and applied best practices"
status: "active"
created: "2026-07-22"
updated: "2026-07-22"
tags:
  - "#domain/reinforcement-learning-fundamentals-deep-rl-rlhf-rlaif-and-prefe"
  - "#type/concept"
  - "#confidence/practitioner"
confidence: "practitioner"
related:
  - "[[Index]]"
  - "[[CONVENTIONS]]"
  - "[[Best Practices Kernel]]"
  - "[[Source Intake Workflow]]"
  - "[[Research Refresh Workflow]]"
  - "[[Synthesis Workflow]]"
  - "[[wiki/concepts/_index|Concepts Hub]]"
  - "[[Dashboard]]"
  - "[[Tag Taxonomy]]"
  - "[[Claim Verification Flow]]"
  - "[[Reporting Workflow]]"
  - "[[Source Manifest Guide]]"
  - "[[Health Scorecard]]"
  - "[[Action Roadmap]]"
  - "[[Weekly Report]]"
  - "[[Approval Queue]]"
  - "[[wiki/flows/_index|Flows Hub]]"
  - "[[wiki/sources/_index|Sources Hub]]"
  - "[[wiki/decisions/_index|Decisions Hub]]"
  - "[[wiki/deliverables/_index|Deliverables Hub]]"
  - "[[wiki/reports/_index|Reports Hub]]"
  - "[[wiki/questions/_index|Questions Hub]]"
  - "[[wiki/gaps/_index|Gaps Hub]]"
  - "[[wiki/experiments/_index|Experiments Hub]]"
source_urls:
  - "https://gymnasium.farama.org/api/env/"
  - "https://stable-baselines3.readthedocs.io/en/master/"
  - "https://www.jmlr.org/papers/v23/21-1342.html"
  - "https://docs.cleanrl.dev/"
  - "https://docs.ray.io/en/latest/rllib/index.html"
  - "https://huggingface.co/docs/trl/index"
  - "https://verl.readthedocs.io/en/latest/"
  - "https://openrlhf.readthedocs.io/en/latest/"
  - "https://arxiv.org/abs/2405.11143"
---

# RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF)

Confidence tag: practitioner. Folded from canon `024-rl-tooling-landscape-gymnasium-sb3-cleanrl-rllib-trl-verl-openrl.md` on the date in `updated`.

## Sourced Takeaways

An RL framework is part of the experimental method because its environment contract, data path, defaults, parallelism, and logging shape what is actually trained and measured. [evidence-based]
Gymnasium, Stable-Baselines3, CleanRL, RLlib, TRL, veRL, and OpenRLHF cover overlapping but distinct layers, so tool selection should begin with the workload and the evidence required. [verified]
There is no evidence here that one framework is universally best across classic control, distributed RL, and language-model post-training. [contested]

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

## Evidence Caveats

- Documentation reflects particular releases and may change after 2026-07-22; a reproducible run must record the version actually used. [verified]
- Project-maintainer documentation is authoritative for interfaces but is not independent evidence for comparative speed, scalability, stability, or policy quality. [verified]
- The OpenRLHF paper reports results for its tested configurations and does not establish superiority for untested models, clusters, objectives, or framework versions. [evidence-based]
- Stable-Baselines3 and CleanRL cover selected algorithms and environments; neither source proves suitability for every RL problem. [verified]
- RLlib's configurable distributed architecture exposes scaling mechanisms, but realized scaling depends on workload balance, communication, hardware, and configuration. [evidence-based]
- TRL, veRL, and OpenRLHF evolve rapidly, so named trainer and backend support should be checked against the pinned release. [verified]
- Similar algorithm labels can conceal different loss normalization, KL estimation, clipping, batching, reward, and generation semantics. [evidence-based]
- Framework choice cannot compensate for an invalid environment, misspecified reward, weak evaluation protocol, or inadequate statistical reporting. [evidence-based]

## Sources

- Canon evidence file: `references/topics/024-rl-tooling-landscape-gymnasium-sb3-cleanrl-rllib-trl-verl-openrl.md`
- Farama Foundation, [Gymnasium Env API](https://gymnasium.farama.org/api/env/). Official environment interface, including reset, step, spaces, termination, and truncation. [verified]
- Stable-Baselines3 maintainers, [Stable-Baselines3 documentation](https://stable-baselines3.readthedocs.io/en/master/). Official algorithms, policies, callbacks, evaluation utilities, and usage guidance. [verified]
- Shengyi Huang et al., 2022, [CleanRL: High-quality Single-file Implementations of Deep Reinforcement Learning Algorithms](https://www.jmlr.org/papers/v23/21-1342.html), with [official documentation](https://docs.cleanrl.dev/). Primary paper and project documentation for CleanRL's design and implementations. [verified]
- Ray Project, [RLlib documentation](https://docs.ray.io/en/latest/rllib/index.html). Official architecture, algorithm, environment, and scaling documentation. [verified]
- Hugging Face, [TRL documentation](https://huggingface.co/docs/trl/index). Official trainer and method documentation for transformer post-training. [verified]
- veRL maintainers, [veRL documentation](https://verl.readthedocs.io/en/latest/). Official documentation for the distributed reinforcement-learning training framework. [verified]
- OpenRLHF maintainers, [OpenRLHF documentation](https://openrlhf.readthedocs.io/en/latest/). Official installation, training, and distributed-system documentation. [verified]
- Jian Hu et al., 2024, [OpenRLHF: An Easy-to-use, Scalable and High-performance RLHF Framework](https://arxiv.org/abs/2405.11143). Project paper describing the framework's architecture and reported experiments. [evidence-based]
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]
