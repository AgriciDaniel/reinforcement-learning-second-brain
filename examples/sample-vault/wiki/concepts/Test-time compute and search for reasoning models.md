---
type: "concept"
title: "Test-time compute and search for reasoning models"
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
  - "https://arxiv.org/abs/2408.03314"
  - "https://arxiv.org/abs/2501.12948"
  - "https://arxiv.org/abs/2512.02008"
  - "https://arxiv.org/abs/2305.14992"
---

# Test-time compute and search for reasoning models

Confidence tag: evidence-based. Folded from canon `028-test-time-compute-and-search-for-reasoning-models.md` on the date in `updated`.

## Sourced Takeaways

Test-time compute spends additional inference on candidate generation, revision, verification, aggregation, or search without changing the deployed model's parameters for that request. [evidence-based]

Best-of-N sampling, PRM-guided beam or tree search, and Monte Carlo tree search allocate compute differently across breadth, depth, and evaluation. Their value depends jointly on the proposer, scorer, task, and budget. [evidence-based]

No cited strategy establishes a universal compute-scaling rule across model families and reasoning tasks. Broad claims that one method or longer traces always win remain contested. [contested]

- Test-time compute is a budgeted decision procedure, not a capability guarantee, and additional optimization can amplify proposer or verifier errors. [evidence-based]
- Best-of-N allocates breadth to completed solutions, while beam and tree search spend part of the budget deciding which prefixes receive more depth. [evidence-based]
- A PRM score on a prefix is not automatically a calibrated value for the search policy that generated that prefix. [evidence-based]
- MCTS is a selection, expansion, evaluation, and backup pattern whose language-specific state and action semantics must be defined explicitly. [evidence-based]
- Prompt difficulty is model-relative and must not be treated as a cost-free intrinsic label available at deployment. [evidence-based]
- Train-time RL and test-time search move computation to different stages and can complement one another. [evidence-based]
- Searching more candidates applies stronger optimization pressure to the scorer and increases the need for independent answer checks. [evidence-based]
- Claims that one strategy or reasoning length dominates across current models and tasks exceed the cited evidence. [contested]

## Best Practices

- Define the inference budget using proposer tokens, verifier tokens, model calls, latency, peak memory, and available parallelism. [practitioner]
- Compare greedy decoding, voting, best-of-N, beam search, and tree search under matched declared budgets and identical answer extraction. [practitioner]
- Freeze prompts, sampling settings, stopping rules, verifier versions, and evaluation code before confirmatory comparisons. [practitioner]
- Include the difficulty router's own calls, errors, and latency when reporting adaptive allocation. [evidence-based]
- Validate verifier calibration on candidates and prefixes produced by the actual search policy, not only its original training distribution. [evidence-based]
- Log candidates, prefix scores, pruning decisions, visit counts, verifier calls, stopping causes, and external correctness. [practitioner]
- Track answer diversity, duplicate rate, trace length, branch survival, score-correctness divergence, and results by difficulty slice. [practitioner]
- Red-team high-scoring wrong traces with an independent checker before increasing the search budget. [practitioner]
- Report the training-rollout and deployment-rollout budgets separately, including any mismatch between post-training sampling and best-of-N or search-time aggregation. [evidence-based]

## Evidence Caveats

- The compute-allocation findings in Snell et al. depend on specific models, mathematics tasks, verifiers, revision methods, and budget definitions. [contested]
- The 2025 scaling study compares a selected set of open models, datasets, strategies, and token budgets, so its rankings are protocol-dependent. [contested]
- DeepSeek-R1 combines reinforcement learning, supervised stages, reward design, rejection sampling, and distillation, limiting attribution to one component. [evidence-based]
- A verifier trained on one generator's outputs can become miscalibrated as search moves toward unusual high-score prefixes. [evidence-based]
- Selecting a maximum from more noisy scores creates more opportunity for proxy exploitation even when average verifier accuracy appears stable. [evidence-based]
- Token count alone does not capture architecture, cache reuse, batching, verifier cost, memory, or serial latency. [practitioner]
- Comparative or state-of-the-art claims remain contested without a current, contamination-audited, compute-matched protocol. [contested]
- The 2026 adaptive-allocation, compute-aligned-training, and scaling-law papers provide mechanisms and bounded empirical evidence, not a universal answer to whether additional test-time compute is preferable to RL training. [contested]
- Training and deployment rollouts can use different budgets and aggregation rules, so results must disclose the mismatch rather than comparing nominal token counts alone. [evidence-based]

## Sources

- Canon evidence file: `references/topics/028-test-time-compute-and-search-for-reasoning-models.md`
- Charlie Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar, 2024, "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters," arXiv:2408.03314, [paper](https://arxiv.org/abs/2408.03314).
- DeepSeek-AI et al., 2025, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning," arXiv:2501.12948, [paper](https://arxiv.org/abs/2501.12948).
- Aradhye Agarwal, Ayan Sengupta, and Tanmoy Chakraborty, 2025, "The Art of Scaling Test-Time Compute for Large Language Models," arXiv:2512.02008, [paper](https://arxiv.org/abs/2512.02008).
- Shibo Hao, Yi Gu, Haodi Ma, Joshua Jiahua Hong, Zhen Wang, Daisy Zhe Wang, and Zhiting Hu, 2023, "Reasoning with Language Model is Planning with World Model," arXiv:2305.14992, [paper](https://arxiv.org/abs/2305.14992).
- "What If We Allocate Test-Time Compute Adaptively?" [arXiv:2602.01070](https://arxiv.org/abs/2602.01070), 2026-02-01. SINGLE-SOURCE for reported results.
- "Compute Aligned Training: Optimizing for Test Time Inference," [arXiv:2604.24957](https://arxiv.org/abs/2604.24957), 2026-04-27. SINGLE-SOURCE for reported results.
- "What should post-training optimize? A test-time scaling law perspective," [arXiv:2605.10716](https://arxiv.org/abs/2605.10716), 2026-05-11. SINGLE-SOURCE for stated mechanism and reported results.
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]
