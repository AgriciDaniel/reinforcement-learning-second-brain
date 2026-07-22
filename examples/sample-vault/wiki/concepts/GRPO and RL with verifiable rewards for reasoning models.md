---
type: "concept"
title: "GRPO and RL with verifiable rewards for reasoning models"
domain: "reinforcement learning"
status: "active"
created: "2026-07-22"
updated: "2026-07-22"
tags:
  - "#domain/reinforcement-learning"
  - "#type/concept"
  - "#confidence/evidence-based"
confidence: "evidence-based"
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
  - "https://arxiv.org/abs/2402.03300"
  - "https://arxiv.org/abs/2501.12948"
  - "https://doi.org/10.1038/s41586-025-09422-z"
  - "https://arxiv.org/abs/2305.20050"
---

# GRPO and RL with verifiable rewards for reasoning models

Confidence tag: evidence-based. Folded from canon `020-grpo-and-rl-with-verifiable-rewards-for-reasoning-models.md` on the date in `updated`.

## Sourced Takeaways

Group Relative Policy Optimization, or GRPO, is a PPO-family policy-gradient method that estimates advantages by comparing multiple responses to the same prompt instead of training a separate critic. [evidence-based]
When task outcomes can be checked by an exact answer parser, compiler, test suite, or formal verifier, reinforcement learning can obtain a relatively low-ambiguity reward without a general-purpose learned judge. [evidence-based]
The DeepSeekMath and DeepSeek-R1 results are important demonstrations, but they do not prove that GRPO, long reasoning traces, or rule-based rewards dominate other post-training designs across domains. [contested]

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

## Sources

- Canon evidence file: `references/topics/020-grpo-and-rl-with-verifiable-rewards-for-reasoning-models.md`
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
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]
