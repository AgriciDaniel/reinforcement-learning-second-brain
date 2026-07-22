---
type: "canon"
title: "020. GRPO and RL with verifiable rewards for reasoning models"
created: "2026-07-22"
updated: "2026-07-22"
status: "active"
---

# 020. GRPO and RL with verifiable rewards for reasoning models

Ledger: 020 | target: GRPO and RL with verifiable rewards for reasoning models | confidence: evidence-based | fold: [[GRPO and RL with verifiable rewards for reasoning models]] | status: active.

## Core Thesis

Group Relative Policy Optimization, or GRPO, is a PPO-family policy-gradient method that estimates advantages by comparing multiple responses to the same prompt instead of training a separate critic. [evidence-based]
When task outcomes can be checked by an exact answer parser, compiler, test suite, or formal verifier, reinforcement learning can obtain a relatively low-ambiguity reward without a general-purpose learned judge. [evidence-based]
The DeepSeekMath and DeepSeek-R1 results are important demonstrations, but they do not prove that GRPO, long reasoning traces, or rule-based rewards dominate other post-training designs across domains. [contested]

## How It Works

For each prompt `x`, an old policy samples a group of `G` candidate responses, and a reward function assigns each complete response a score. [evidence-based]

For outcome supervision, GRPO standardizes each response reward within its prompt group: the group mean is subtracted and the result is divided by the group standard deviation. The normalized response score is then used as the advantage for its generated tokens. [evidence-based]

The policy objective uses a token-level importance ratio between the current and old policies. Like PPO, it maximizes the smaller of the unclipped ratio-times-advantage term and its clipped counterpart, limiting each update relative to the sampling policy. [evidence-based]

GRPO adds a weighted KL-divergence penalty between the current policy and a reference policy directly to the objective. It omits PPO's separately trained value model, which changes the baseline estimator and reduces the set of large models held for actor-critic training. [evidence-based]

With process supervision, a scorer can attach rewards to intermediate reasoning steps and each token can receive the sum of normalized future step rewards. With outcome supervision, all response tokens share the normalized final reward. [evidence-based]

A verifiable-reward function parses the model output and executes a task-specific check. Examples include exact-equivalence checks for structured mathematics and compiler or test-case feedback for code. [evidence-based]

The checker is part of the environment specification: formatting, parser behavior, test coverage, timeouts, and sandbox failures determine the reward actually optimized. [evidence-based]

DeepSeek-R1-Zero applies GRPO to a base model with rule-based accuracy and format rewards. The published DeepSeek-R1 pipeline adds cold-start supervised data, reasoning-focused RL, rejection-sampled supervised fine-tuning, and a later RL stage covering broader helpfulness and harmlessness goals. [evidence-based]

The repeated loop is generate a response group, verify or score each response, compute group-relative advantages, update against the clipped objective and KL penalty, refresh policy snapshots, and evaluate on a frozen protocol. [evidence-based]

## Key Principles

- GRPO replaces a learned critic with a within-prompt group baseline, but still pays for multiple sampled completions and reward evaluation. [evidence-based]
- Group normalization supplies relative signal within a prompt, so it does not make reward scales or task difficulty directly comparable across prompts. [evidence-based]
- A group whose candidates receive identical rewards provides no useful relative ranking signal under the basic normalized estimator. [evidence-based]
- Verifiable rewards are strongest when correctness can be checked independently of surface style, but they are only as sound and complete as the checker. [evidence-based]
- Separate accuracy and format rewards expose different objectives, and a model can optimize formatting without improving semantic correctness. [evidence-based]
- Outcome rewards credit an entire trajectory from its final result, while process rewards require more granular labels or a process scorer. [evidence-based]
- DeepSeek-R1 is a multi-stage data and optimization pipeline, so attributing its reported behavior to GRPO alone is not supported by the paper. [contested]
- Claims that longer visible reasoning universally causes better reasoning, or that RL reliably creates a general reasoning strategy, exceed the cited evidence. [contested]

## Best Practices

- Unit-test every parser, equivalence rule, compiler wrapper, timeout, and sandbox result on correct, incorrect, malformed, and adversarial outputs before RL. [practitioner]
- Log accuracy, formatting, safety, and auxiliary reward components separately so one component cannot silently dominate the scalar reward. [practitioner]
- Keep hidden verification cases and contamination checks, because optimizing against a fixed public test set can reward memorization or test-specific shortcuts. [practitioner]
- Define stable behavior for zero-variance groups, numerical epsilon, invalid generations, and verifier failures, and include these rates in run reports. [practitioner]
- Monitor reward distribution, group variance, response length, policy entropy, KL, clipping fraction, duplicate rate, and pass rate by task slice. [practitioner]
- Sweep group size, sampling temperature, KL coefficient, clipping range, and learning rate under a fixed evaluation budget rather than copying one recipe. [practitioner]
- Begin with a small model and short generation cap, inspect raw trajectories, then scale only after the reward and update loop pass controlled tests. [practitioner]
- Evaluate with held-out tasks, fresh seeds, fixed decoding rules, and non-rewarded quality or safety checks before making comparative claims. [evidence-based]

## Primary Sources

- Zhihong Shao et al., 2024, "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models," arXiv:2402.03300, [paper](https://arxiv.org/abs/2402.03300).
- DeepSeek-AI et al., 2025, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning," Nature 645, arXiv:2501.12948, [paper](https://arxiv.org/abs/2501.12948), [journal record](https://doi.org/10.1038/s41586-025-09422-z).
- Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe, 2023, "Let's Verify Step by Step," arXiv:2305.20050, [paper](https://arxiv.org/abs/2305.20050).

## Evidence Caveats

- DeepSeekMath and DeepSeek-R1 report results from specific model families, data mixtures, reward implementations, and evaluation harnesses, not controlled evidence for every reasoning model. [contested]
- The R1 paper combines RL, supervised stages, rejection sampling, reward design, and distillation, which limits causal attribution to any one component. [evidence-based]
- Exact-answer and code checks can miss equivalent answers, accept unintended shortcuts, contain weak tests, or expose exploitable parser behavior. [evidence-based]
- Group-relative estimation can be noisy when groups are small or rewards are sparse, and sampling more candidates increases generation cost. [evidence-based]
- Process-supervision findings from a particular mathematics benchmark do not establish a universal advantage over outcome supervision. [contested]
- Observed self-correction, reflection, or longer traces do not by themselves identify the learned internal mechanism or guarantee faithful reasoning. [contested]
- SOTA comparisons in reasoning post-training age quickly and should be treated as contested unless reproduced under a named, current, contamination-audited protocol. [contested]

## Brain Hooks

- Folded concept: [[GRPO and RL with verifiable rewards for reasoning models]]
- Related canon: [[Trust-region and proximal methods (TRPO, PPO)]]
- Related canon: [[RLHF reward models and PPO post-training (InstructGPT lineage)]]
- Related canon: [[Direct preference optimization family (DPO, IPO, KTO, ORPO)]]
- Related canon: [[Reward design, reward hacking, and specification gaming]]
- Related canon: [[Evaluation, benchmarks, and reproducibility in deep RL]]
- Related canon: [[Debugging RL training runs in practice]]
- Related canon: [[RL tooling landscape (Gymnasium, SB3, CleanRL, RLlib, TRL, veRL, OpenRLHF)]]
- Related canon: [[Policy gradient methods and REINFORCE]]
- Source intake path: [[Source Intake Workflow]]
- Verification path: [[Claim Verification Flow]]
