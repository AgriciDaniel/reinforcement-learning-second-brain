## Verified findings

- DAPO is arXiv:2503.14476, titled "DAPO: An Open-Source LLM Reinforcement Learning System at Scale"; https://arxiv.org/abs/2503.14476; 2025-03-18; the abstract names Decoupled Clip and Dynamic Sampling Policy Optimization and says the system is open sourced.
- Dr. GRPO appears in arXiv:2503.20783, titled "Understanding R1-Zero-Like Training: A Critical Perspective"; https://arxiv.org/abs/2503.20783; 2025-03-26; the abstract introduces Dr. GRPO as an unbiased optimization method and describes a minimalist R1-Zero recipe.
- GSPO is arXiv:2507.18071, titled "Group Sequence Policy Optimization"; https://arxiv.org/abs/2507.18071; 2025-07-24; the abstract defines its importance ratio from sequence likelihood and applies sequence-level clipping, rewarding, and optimization rather than token-level ratios.
- SKPO is arXiv:2604.08690, titled "Skip-Connected Policy Optimization for Implicit Advantage"; https://arxiv.org/abs/2604.08690; 2026-04-09; its abstract uses single-stream optimization for an upstream reasoning phase and group-relative optimization for a downstream phase.
- EP-GRPO is arXiv:2605.04960, titled "EP-GRPO: Entropy-Progress Aligned Group Relative Policy Optimization with Implicit Process Guidance"; https://arxiv.org/abs/2605.04960; 2026-05-06; its abstract proposes entropy-gated token modulation and a zero-variance-gradient mitigation without external reward models.
- SD-GRPO is arXiv:2606.09871, titled "SD-GRPO: Verifiable Segment Decomposition for Long-Form Vision-Language Generation"; https://arxiv.org/abs/2606.09871; 2026-06-02; the paper replaces one scalar rollout advantage with a vector of per-segment advantages from verifiable segment rewards.
- "On the Policy Gradient Foundations of Group Relative Policy Optimization: Credit Assignment, Gradient Sparsity, and Rank Collapse" is arXiv:2606.29238; https://arxiv.org/abs/2606.29238; 2026-06-28; its abstract argues that output-only reward gives every token in a rollout the same advantage, yielding a single-scalar form of token credit.
- "GRPO, Dr. GRPO, and DAPO Are Three Operations on One Number: The Group-Standard-Deviation Identity" is arXiv:2607.00152; https://arxiv.org/abs/2607.00152; 2026-06-30; its abstract characterizes the three methods through different treatments of group reward standard deviation.
- SAO is arXiv:2607.07508, titled "Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning"; https://arxiv.org/abs/2607.07508; 2026-07-08; the abstract replaces group-wise sampling with one rollout per prompt and introduces double-sided token-level clipping for asynchronous training.

## Candidate ledger entries

```json
[
  {
    "id": "dapo-grpo-2025",
    "arxiv_id": "2503.14476",
    "title": "DAPO: An Open-Source LLM Reinforcement Learning System at Scale",
    "url": "https://arxiv.org/abs/2503.14476",
    "source_type": "primary",
    "date": "2025-03-18",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "dapo-decoupled-clip-dynamic-sampling"
    ],
    "supports_claims": [
      "dapo-decoupled-clip-dynamic-sampling"
    ]
  },
  {
    "id": "dr-grpo-2025",
    "arxiv_id": "2503.20783",
    "title": "Understanding R1-Zero-Like Training: A Critical Perspective",
    "url": "https://arxiv.org/abs/2503.20783",
    "source_type": "primary",
    "date": "2025-03-26",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "dr-grpo-unbiased-optimization-claim",
      "minimalist-rlvr-recipe-report"
    ],
    "supports_claims": [
      "dr-grpo-unbiased-optimization-claim",
      "minimalist-rlvr-recipe-report"
    ]
  },
  {
    "id": "gspo-grpo-2025",
    "arxiv_id": "2507.18071",
    "title": "Group Sequence Policy Optimization",
    "url": "https://arxiv.org/abs/2507.18071",
    "source_type": "primary",
    "date": "2025-07-24",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "gspo-sequence-level-importance-ratio"
    ],
    "supports_claims": [
      "gspo-sequence-level-importance-ratio"
    ]
  },
  {
    "id": "ep-grpo-2026",
    "arxiv_id": "2605.04960",
    "title": "EP-GRPO: Entropy-Progress Aligned Group Relative Policy Optimization with Implicit Process Guidance",
    "url": "https://arxiv.org/abs/2605.04960",
    "source_type": "primary",
    "date": "2026-05-06",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "ep-grpo-entropy-guided-token-feedback",
      "ep-grpo-zero-variance-gradient-mitigation"
    ],
    "supports_claims": [
      "ep-grpo-entropy-guided-token-feedback",
      "ep-grpo-zero-variance-gradient-mitigation"
    ]
  },
  {
    "id": "skpo-grpo-single-stream-2026",
    "arxiv_id": "2604.08690",
    "title": "Skip-Connected Policy Optimization for Implicit Advantage",
    "url": "https://arxiv.org/abs/2604.08690",
    "source_type": "primary",
    "date": "2026-04-09",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "skpo-single-stream-upstream-grpo-downstream"
    ],
    "supports_claims": [
      "skpo-single-stream-upstream-grpo-downstream"
    ]
  },
  {
    "id": "sd-grpo-2026",
    "arxiv_id": "2606.09871",
    "title": "SD-GRPO: Verifiable Segment Decomposition for Long-Form Vision-Language Generation",
    "url": "https://arxiv.org/abs/2606.09871",
    "source_type": "primary",
    "date": "2026-06-02",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "sd-grpo-segment-level-verifiable-credit"
    ],
    "supports_claims": [
      "sd-grpo-segment-level-verifiable-credit"
    ]
  },
  {
    "id": "grpo-policy-gradient-foundations-2026",
    "arxiv_id": "2606.29238",
    "title": "On the Policy Gradient Foundations of Group Relative Policy Optimization: Credit Assignment, Gradient Sparsity, and Rank Collapse",
    "url": "https://arxiv.org/abs/2606.29238",
    "source_type": "primary",
    "date": "2026-06-28",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "grpo-output-reward-token-credit-assignment"
    ],
    "supports_claims": [
      "grpo-output-reward-token-credit-assignment"
    ]
  },
  {
    "id": "grpo-group-standard-deviation-identity-2026",
    "arxiv_id": "2607.00152",
    "title": "GRPO, Dr. GRPO, and DAPO Are Three Operations on One Number: The Group-Standard-Deviation Identity",
    "url": "https://arxiv.org/abs/2607.00152",
    "source_type": "primary",
    "date": "2026-06-30",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "grpo-drgrpo-dapo-standard-deviation-identity"
    ],
    "supports_claims": [
      "grpo-drgrpo-dapo-standard-deviation-identity"
    ]
  },
  {
    "id": "sao-grpo-async-2026",
    "arxiv_id": "2607.07508",
    "title": "Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning",
    "url": "https://arxiv.org/abs/2607.07508",
    "source_type": "primary",
    "date": "2026-07-08",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "sao-single-rollout-asynchronous-off-policy-grpo"
    ],
    "supports_claims": [
      "sao-single-rollout-asynchronous-off-policy-grpo"
    ]
  }
]
```

## Claim rows

| C001 | DAPO names a decoupled-clipping and dynamic-sampling policy-optimization algorithm. | dapo-grpo-2025 | evidence-based |
| C002 | The Dr. GRPO paper introduces Dr. GRPO and describes its recipe as minimalist. | dr-grpo-2025 | evidence-based |
| C003 | GSPO uses sequence-likelihood importance ratios and sequence-level clipping, rewarding, and optimization. | gspo-grpo-2025 | evidence-based |
| C004 | GSPO outperforms GRPO. | gspo-grpo-2025 | contested: the only checked support is the GSPO authors' preprint abstract, not two independent sources. |
| C005 | EP-GRPO proposes entropy-gated modulation and implicit process signals for directional token-level feedback. | ep-grpo-2026 | evidence-based |
| C006 | EP-GRPO achieves superior accuracy and efficiency to GRPO variants. | ep-grpo-2026 | contested: comparative result appears only in the authors' preprint abstract. |
| C007 | SKPO uses single-stream optimization upstream and group-relative optimization downstream. | skpo-grpo-single-stream-2026 | evidence-based |
| C008 | SKPO improves on the strongest baselines. | skpo-grpo-single-stream-2026 | contested: comparative result appears only in the authors' preprint abstract. |
| C009 | SD-GRPO turns verifiable segment rewards into a vector of segment-level advantages. | sd-grpo-2026 | evidence-based |
| C010 | SD-GRPO improves on GRPO in long-form vision-language generation. | sd-grpo-2026 | contested: comparative result appears only in the authors' preprint abstract. |
| C011 | Under output-only reward, the policy-gradient-foundations paper assigns one scalar advantage to all tokens in a rollout. | grpo-policy-gradient-foundations-2026 | evidence-based |
| C012 | The group-standard-deviation-identity paper relates GRPO, Dr. GRPO, and DAPO to three treatments of group reward standard deviation. | grpo-group-standard-deviation-identity-2026 | evidence-based |
| C013 | SAO replaces group-wise sampling with one rollout per prompt and uses strict double-sided token-level clipping. | sao-grpo-async-2026 | evidence-based |
| C014 | SAO outperforms GRPO and its variants on agentic coding and reasoning benchmarks. | sao-grpo-async-2026 | contested: comparative result appears only in the authors' preprint abstract. |

## Topic patch notes

- In `references/topics/020-grpo-and-rl-with-verifiable-rewards-for-reasoning-models.md`, add a dated 2025 refinement paragraph after the GRPO objective: DAPO is `arXiv:2503.14476` and Dr. GRPO is introduced in `arXiv:2503.20783`. Cite each paper's abstract, and preserve their implementation and performance results as scoped author reports.
- Add a "ratio granularity" subsection: the current GRPO description uses token-level importance ratios, while GSPO (`arXiv:2507.18071`) defines a sequence-likelihood ratio with sequence-level clipping, rewarding, and optimization. Do not write that sequence level is generally better; mark the paper's GRPO comparison contested pending independent evidence.
- Add an "entropy and credit assignment refinements" subsection: EP-GRPO (`arXiv:2605.04960`) supplies entropy-gated and implicit process signals; SD-GRPO (`arXiv:2606.09871`) uses verifiable segment rewards for segment-level advantages; and the policy-gradient-foundations paper (`arXiv:2606.29238`) is a candidate theoretical caveat on scalar output-reward credit assignment.
- Add a "single-stream hybrid" subsection: SKPO (`arXiv:2604.08690`) applies single-stream optimization to an upstream phase and retains group-relative optimization downstream. Keep its result claims contested until independently checked.
- Add an "asynchronous and single-rollout" subsection: SAO (`arXiv:2607.07508`) is a candidate for asynchronous agentic RL, replaces group sampling with one rollout per prompt, and uses strict double-sided token clipping. Keep its benchmark claims contested until independently checked.
- Add an evidence caveat that `arXiv:2607.00152` analyzes the group-standard-deviation connection among GRPO, Dr. GRPO, and DAPO. It is a useful mechanism note, not independent validation that any variant supersedes another.

## Negative results

- Direct broad arXiv search pages for `GRPO` and `RLVR` returned `Cache miss` in this run: https://arxiv.org/search/?query=GRPO&searchtype=all&abstracts=show&order=-announced_date_first&size=200 and https://arxiv.org/search/?query=RLVR&searchtype=all&abstracts=show&order=-announced_date_first&size=200. Candidate discovery therefore used web search, followed by individual arXiv abstract-page fetches.
- No comparative claim in this report has two independent sources. The GSPO, EP-GRPO, SKPO, SD-GRPO, and SAO comparative rows are consequently marked contested.
- No same-lab blog or vendor write-up was used as an additional lineage. Every candidate ledger entry is the fetched primary arXiv record.

## Flags for verification

- Before promoting any candidate into `references/source-ledger.json`, obtain a second independent source for C004, C006, C008, C010, and C014, such as a reproduction, a separately authored evaluation, or a primary benchmark record. Until then, do not state that any method supersedes or outperforms GRPO.
- Recheck all nine arXiv records on the next monthly refresh for revisions, code availability, corrected abstracts, and independent evaluations. The Apr-Jul 2026 candidates are recent preprints.
- Keep SAO scoped to asynchronous agentic RL and SD-GRPO scoped to long-form vision-language generation. Neither abstract establishes a universal RLVR recipe.
- This file is a candidate intake only. Per WP2 scope, it does not alter the existing ledger or topic dossier.
