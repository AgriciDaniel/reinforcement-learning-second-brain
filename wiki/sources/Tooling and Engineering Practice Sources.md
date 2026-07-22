---
type: "source"
title: "Tooling and Engineering Practice Sources"
created: "2026-07-23"
updated: "2026-07-23"
status: "active"
tags:
  - "#type/source"
  - "#confidence/evidence-based"
related:
  - "[[wiki/sources/_index|Sources Hub]]"
  - "[[Source Manifest Guide]]"
  - "[[Source Intake Workflow]]"
  - "[[Research Refresh Workflow]]"
  - "[[Claim Verification Flow]]"
  - "[[Best Practices Kernel]]"
  - "[[dashboard|Dashboard]]"
  - "[[wiki/concepts/_index|Concepts Hub]]"
---

# Tooling and Engineering Practice Sources

Theme slice of the 2026-07-23 research pack: 15 sources supporting the tooling and engineering practice canon files and concept notes. The master list lives in [[research-pack-2026-07-23|Research Pack 2026-07-23]].

### Automated Alignment Researchers: Using large language models to scale scalable oversight

- URL: https://www.anthropic.com/research/automated-alignment-researchers
- Published: 2026-04-14 | Retrieved: 2026-07-22 | Refresh due: 2026-10-20
- Type: vendor | Confidence: practitioner
- Supports claims: automated-alignment-researchers-can-reward-hack-a-weak-to-strong-evaluation-harness, human-review-and-untamperable-evaluations-are-needed-for-automated-research

### Natural emergent misalignment from reward hacking in production RL (Anthropic)

- URL: https://www.anthropic.com/research/emergent-misalignment-reward-hacking
- Published: 2025-11-21 | Retrieved: 2026-07-22 | Refresh due: 2026-10-23
- Type: vendor | Confidence: evidence-based
- Supports claims: reward-hacking-generalizes-to-misalignment, inoculation-prompting-mitigation

### CleanRL Documentation

- URL: https://docs.cleanrl.dev/
- Published: 2022-01-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-21
- Type: official | Confidence: evidence-based
- Supports claims: single-file-rl-implementations, implementation-detail-transparency

### Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers

- URL: https://arxiv.org/abs/2604.25891
- Published: 2026-04-28 | Retrieved: 2026-07-22 | Refresh due: 2027-01-26
- Type: primary | Confidence: evidence-based
- Supports claims: inoculation-prompting-can-leave-conditional-misalignment, standard-safety-evaluations-can-miss-context-triggered-misalignment

### Securing the future of AI agents

- URL: https://deepmind.google/blog/securing-the-future-of-ai-agents/
- Published: 2026-06-18 | Retrieved: 2026-07-22 | Refresh due: 2026-10-25
- Type: vendor | Confidence: practitioner
- Supports claims: ai-control-roadmap-treats-agents-as-potentially-misaligned, agent-control-uses-monitoring-prevention-response-and-measurable-coverage-recall-time-to-response

### Specification gaming: the flip side of AI ingenuity (DeepMind blog)

- URL: https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/
- Published: 2020-04-21 | Retrieved: 2026-07-22 | Refresh due: 2027-07-31
- Type: vendor | Confidence: evidence-based
- Supports claims: specification-gaming-examples, reward-misspecification-failure-modes

### Gymnasium Documentation (Farama Foundation)

- URL: https://gymnasium.farama.org/
- Published: 2022-10-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-22
- Type: official | Confidence: evidence-based
- Supports claims: gymnasium-env-api-standard, gym-to-gymnasium-migration

### Miles: A PyTorch-Native Stack for Large-Scale LLM RL Post-Training

- URL: https://pytorch.org/blog/miles-a-pytorch-native-stack-for-large-scale-llm-rl-post-training/
- Published: 2026-06-30 | Retrieved: 2026-07-22 | Refresh due: 2026-10-29
- Type: vendor | Confidence: practitioner
- Supports claims: miles-llm-rl-post-training-framework, miles-sglang-megatron-ray-stack

### OpenRLHF GitHub Repository

- URL: https://github.com/OpenRLHF/OpenRLHF
- Published: 2024-05-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-23
- Type: vendor | Confidence: evidence-based
- Supports claims: openrlhf-ray-vllm-distributed-rlhf, ppo-reinforce-plus-plus-grpo-support

### RLlib Documentation (Ray)

- URL: https://docs.ray.io/en/latest/rllib/index.html
- Published: 2018-07-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-24
- Type: official | Confidence: evidence-based
- Supports claims: rllib-scalable-distributed-rl, production-rl-workloads

### SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents

- URL: https://arxiv.org/abs/2605.21384
- Published: 2026-05-20 | Retrieved: 2026-07-22 | Refresh due: 2027-01-22
- Type: primary | Confidence: evidence-based
- Supports claims: visible-to-held-out-test-gap-measures-coding-agent-reward-hacking, specbench-long-horizon-coding-agent-evaluation

### Stable-Baselines3 Documentation

- URL: https://stable-baselines3.readthedocs.io/en/master/
- Published: 2021-01-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-25
- Type: official | Confidence: evidence-based
- Supports claims: sb3-reliable-algorithm-implementations, sb3-supported-algorithm-matrix

### TRL Documentation (Hugging Face Transformer Reinforcement Learning)

- URL: https://huggingface.co/docs/trl/index
- Published: 2026-03-27 | Retrieved: 2026-07-22 | Refresh due: 2026-08-26
- Type: official | Confidence: evidence-based
- Supports claims: trl-trainer-taxonomy, grpo-dpo-kto-trainer-availability

### verl Documentation (HybridFlow RL training framework for LLMs)

- URL: https://verl.readthedocs.io/en/latest/
- Published: 2024-09-01 | Retrieved: 2026-07-22 | Refresh due: 2026-08-27
- Type: official | Confidence: evidence-based
- Supports claims: verl-hybrid-controller-programming-model, llm-rl-post-training-infra

### vime: A Simple, Stable, and Efficient RL Framework for LLMs

- URL: https://vllm-project.github.io/2026/06/09/announcing-vime.html
- Published: 2026-06-09 | Retrieved: 2026-07-22 | Refresh due: 2027-01-29
- Type: official | Confidence: evidence-based
- Supports claims: vime-vllm-megatron-rl-pipeline, vime-grpo-ppo-example-coverage

## Related

- [[wiki/sources/_index|Sources Hub]]
- [[Source Manifest Guide]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Best Practices Kernel]]
- [[dashboard|Dashboard]]
- [[wiki/concepts/_index|Concepts Hub]]
- [[research-pack-2026-07-23|Research Pack 2026-07-23]]
