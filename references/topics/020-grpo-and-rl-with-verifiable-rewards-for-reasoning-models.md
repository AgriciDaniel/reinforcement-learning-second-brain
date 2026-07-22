---
type: "canon"
title: "020. GRPO and RL with verifiable rewards for reasoning models"
created: "2026-07-22"
updated: "2026-07-23"
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

### 2025 GRPO refinement lineage

DAPO describes decoupled clipping and dynamic sampling policy optimization, while Dr. GRPO introduces an optimization method its authors call unbiased and describes a minimalist R1-Zero-like recipe. These are primary-source mechanism reports; implementation and performance claims remain scoped to the authors' preprints. [evidence-based]

### Ratio granularity

The baseline GRPO description here uses token-level importance ratios. GSPO instead defines an importance ratio from sequence likelihood and applies sequence-level clipping, rewarding, and optimization. GSPO's comparison with GRPO is author-reported in one preprint and remains contested pending independent evidence; sequence-level ratios are not presented as generally better. [contested]

### Entropy and credit-assignment refinements

EP-GRPO proposes entropy-gated token modulation and implicit process signals, while SD-GRPO maps verifiable segment rewards to a vector of segment-level advantages for long-form vision-language generation. The policy-gradient-foundations paper argues that output-only reward gives every token in a rollout one scalar advantage, raising a theoretical credit-assignment caveat. Each is a single-source preprint and not a new default recipe. [contested]

### Single-stream hybrid and asynchronous candidate

SKPO applies single-stream optimization to an upstream reasoning phase while retaining group-relative optimization downstream. SAO is an asynchronous agentic-RL candidate that replaces group-wise sampling with one rollout per prompt and uses strict double-sided token-level clipping. Their benchmark results are author-reported only and do not establish that either method supersedes GRPO. [contested]

With process supervision, a scorer can attach rewards to intermediate reasoning steps and each token can receive the sum of normalized future step rewards. With outcome supervision, all response tokens share the normalized final reward. [evidence-based]

A verifiable-reward function parses the model output and executes a task-specific check. Examples include exact-equivalence checks for structured mathematics and compiler or test-case feedback for code. [evidence-based]

The checker is part of the environment specification: formatting, parser behavior, test coverage, timeouts, and sandbox failures determine the reward actually optimized. [evidence-based]

DeepSeek-R1-Zero applies GRPO to a base model with rule-based accuracy and format rewards. The published DeepSeek-R1 pipeline adds cold-start supervised data, reasoning-focused RL, rejection-sampled supervised fine-tuning, and a later RL stage covering broader helpfulness and harmlessness goals. [evidence-based]

The repeated loop is generate a response group, verify or score each response, compute group-relative advantages, update against the clipped objective and KL penalty, refresh policy snapshots, and evaluate on a frozen protocol. [evidence-based]

### 2026 recipe-disclosure examples

As of the 2026-07-22 retrieval, DeepSeek's official released-model catalog does not record DeepSeek R2; treat third-party R2 delay accounts as contested. This is a catalog-absence observation, not evidence of release, cancellation, or a training fact. [evidence-based]

GLM-5.1 documents multi-turn SFT plus RL and a process-quality evaluation framework, but does not publish its RL optimizer or reward construction. MiniMax M3's associated MaxProof report documents generative-verifier RL for proof generation, verification, and critique-conditioned repair. These are high-level recipe examples with different disclosure levels and neither identifies a universally superior optimizer or reward scheme. [evidence-based]

Qwen-AgentWorld's card documents CPT, SFT, then GSPO RL, while its report describes hybrid rubric-and-rule rewards for simulation fidelity. The sources do not disclose reward weights or all training settings, so they support only the stated recipe description. [evidence-based]

Meta's RA-RFT report combines gold-relevance retriever distillation with reinforcement fine-tuning under verifiable outcome rewards. Anthropic's introspection-adapter report uses SFT followed by LLM-judge-scored DPO preference refinement; it is reward-model-relevant auditing work, not RLVR. [evidence-based]

## Key Principles

- GRPO replaces a learned critic with a within-prompt group baseline, but still pays for multiple sampled completions and reward evaluation. [evidence-based]
- Group normalization supplies relative signal within a prompt, so it does not make reward scales or task difficulty directly comparable across prompts. [evidence-based]
- A group whose candidates receive identical rewards provides no useful relative ranking signal under the basic normalized estimator. [evidence-based]
- Verifiable rewards are strongest when correctness can be checked independently of surface style, but they are only as sound and complete as the checker. [evidence-based]
- Separate accuracy and format rewards expose different objectives, and a model can optimize formatting without improving semantic correctness. [evidence-based]
- Outcome rewards credit an entire trajectory from its final result, while process rewards require more granular labels or a process scorer. [evidence-based]
- DeepSeek-R1 is a multi-stage data and optimization pipeline, so attributing its reported behavior to GRPO alone is not supported by the paper. [contested]
- Claims that longer visible reasoning universally causes better reasoning, or that RL reliably creates a general reasoning strategy, exceed the cited evidence. [contested]
- DAPO, Dr. GRPO, GSPO, EP-GRPO, SKPO, SD-GRPO, and SAO describe differing mechanisms, but no single-source paper establishes that its variant supersedes GRPO across workloads. [contested]
- A disclosed algorithm name without reward semantics, training-stack provenance, or a complete protocol cannot establish a reproducible post-training recipe. [evidence-based]

## Best Practices

- Unit-test every parser, equivalence rule, compiler wrapper, timeout, and sandbox result on correct, incorrect, malformed, and adversarial outputs before RL. [practitioner]
- Log accuracy, formatting, safety, and auxiliary reward components separately so one component cannot silently dominate the scalar reward. [practitioner]
- Keep hidden verification cases and contamination checks, because optimizing against a fixed public test set can reward memorization or test-specific shortcuts. [practitioner]
- Define stable behavior for zero-variance groups, numerical epsilon, invalid generations, and verifier failures, and include these rates in run reports. [practitioner]
- Monitor reward distribution, group variance, response length, policy entropy, KL, clipping fraction, duplicate rate, and pass rate by task slice. [practitioner]
- Sweep group size, sampling temperature, KL coefficient, clipping range, and learning rate under a fixed evaluation budget rather than copying one recipe. [practitioner]
- Begin with a small model and short generation cap, inspect raw trajectories, then scale only after the reward and update loop pass controlled tests. [practitioner]
- Evaluate with held-out tasks, fresh seeds, fixed decoding rules, and non-rewarded quality or safety checks before making comparative claims. [evidence-based]
- Treat every new GRPO variant as a versioned experimental branch: reproduce the stated objective, evaluate under matched compute and verifier budgets, and keep author-reported comparisons separate from independent evidence. [practitioner]
- Keep model-recipe examples at their published level of disclosure and do not infer optimizer details, reward weights, or framework implementation from a model card alone. [practitioner]

## Primary Sources

- Zhihong Shao et al., 2024, "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models," arXiv:2402.03300, [paper](https://arxiv.org/abs/2402.03300).
- DeepSeek-AI et al., 2025, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning," Nature 645, arXiv:2501.12948, [paper](https://arxiv.org/abs/2501.12948), [journal record](https://doi.org/10.1038/s41586-025-09422-z).
- Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe, 2023, "Let's Verify Step by Step," arXiv:2305.20050, [paper](https://arxiv.org/abs/2305.20050).
- "DAPO: An Open-Source LLM Reinforcement Learning System at Scale," [arXiv:2503.14476](https://arxiv.org/abs/2503.14476), 2025-03-18; and "Understanding R1-Zero-Like Training: A Critical Perspective," [arXiv:2503.20783](https://arxiv.org/abs/2503.20783), 2025-03-26.
- "Group Sequence Policy Optimization," [arXiv:2507.18071](https://arxiv.org/abs/2507.18071), 2025-07-24; and "Skip-Connected Policy Optimization for Implicit Advantage," [arXiv:2604.08690](https://arxiv.org/abs/2604.08690), 2026-04-09.
- "EP-GRPO: Entropy-Progress Aligned Group Relative Policy Optimization with Implicit Process Guidance," [arXiv:2605.04960](https://arxiv.org/abs/2605.04960), 2026-05-06; "SD-GRPO: Verifiable Segment Decomposition for Long-Form Vision-Language Generation," [arXiv:2606.09871](https://arxiv.org/abs/2606.09871), 2026-06-02; and "On the Policy Gradient Foundations of Group Relative Policy Optimization," [arXiv:2606.29238](https://arxiv.org/abs/2606.29238), 2026-06-28.
- "GRPO, Dr. GRPO, and DAPO Are Three Operations on One Number: The Group-Standard-Deviation Identity," [arXiv:2607.00152](https://arxiv.org/abs/2607.00152), 2026-06-30; and "Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning," [arXiv:2607.07508](https://arxiv.org/abs/2607.07508), 2026-07-08.
- DeepSeek, [Transparency Center](https://www.deepseek.com/en/transparency/), 2026-04-24; Z.ai, [GLM-5.1 release notes](https://docs.z.ai/release-notes/new-released), 2026-04-07; and [GLM-5.1 model card](https://huggingface.co/zai-org/GLM-5.1), 2026-04-07.
- MiniMax, [M3 release](https://www.minimax.io/blog/minimax-m3), 2026-06-01; "MaxProof: Scaling Mathematical Proof with Generative-Verifier RL," [arXiv:2606.13473](https://arxiv.org/abs/2606.13473), 2026-06-11; [Qwen-AgentWorld model card](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B), 2026-06-23; and "Qwen-AgentWorld," [arXiv:2606.24597](https://arxiv.org/abs/2606.24597), 2026-06-23.
- Meta, [Learning to Reason by Analogy via Retrieval-Augmented Reinforcement Fine-Tuning](https://ai.meta.com/research/publications/learning-to-reason-by-analogy-via-retrieval-augmented-reinforcement-fine-tuning/), 2026-07-17; and Anthropic, [Introspection Adapters](https://alignment.anthropic.com/2026/introspection-adapters/), 2026-04-28.

## Evidence Caveats

- DeepSeekMath and DeepSeek-R1 report results from specific model families, data mixtures, reward implementations, and evaluation harnesses, not controlled evidence for every reasoning model. [contested]
- The R1 paper combines RL, supervised stages, rejection sampling, reward design, and distillation, which limits causal attribution to any one component. [evidence-based]
- Exact-answer and code checks can miss equivalent answers, accept unintended shortcuts, contain weak tests, or expose exploitable parser behavior. [evidence-based]
- Group-relative estimation can be noisy when groups are small or rewards are sparse, and sampling more candidates increases generation cost. [evidence-based]
- Process-supervision findings from a particular mathematics benchmark do not establish a universal advantage over outcome supervision. [contested]
- Observed self-correction, reflection, or longer traces do not by themselves identify the learned internal mechanism or guarantee faithful reasoning. [contested]
- SOTA comparisons in reasoning post-training age quickly and should be treated as contested unless reproduced under a named, current, contamination-audited protocol. [contested]
- DAPO, Dr. GRPO, and GSPO are connected by the group-standard-deviation identity analysis, but that mechanism note is not independent validation that any variant supersedes another. [evidence-based]
- EP-GRPO, SKPO, SD-GRPO, SAO, and the credit-assignment analysis are recent single-source preprints. Their mechanisms are recorded, while every superiority or default-recipe claim remains contested. [contested]
- DeepSeek R2 is an official-catalog absence observation only. Third-party delay accounts are unconfirmed rumor and establish neither release nor cancellation. [evidence-based]
- GLM-5.1, MiniMax M3, Qwen-AgentWorld, RA-RFT, and introspection-adapter descriptions come from their authors or vendors at differing levels of detail; they do not support inferred reward semantics, unreported parameters, or cross-model comparisons. [evidence-based]

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
