## Verified findings

- The live record for the existing PRM survey is now version 3, revised on 2026-04-29. It describes PRM applications across math, code, text, multimodal reasoning, robotics, and agents, plus emerging benchmarks. [arXiv:2510.08049](https://arxiv.org/abs/2510.08049)
- The existing Qwen PRM line remains a mathematical-reasoning source. Its authors report annotation and best-of-N evaluation issues in that setting, so it does not itself establish PRM behavior in open-ended or multimodal work. [arXiv:2501.07301](https://arxiv.org/abs/2501.07301)
- Post-cutoff papers provide scoped extensions of rubric-conditioned rewards and LLM judging: RRD targets open-ended LLM judging and reward modeling, while RLR3 targets partially verifiable vision-language tasks with deterministic-extractor and LLM-judge routes. These are task-specific reports, not a general cross-domain result. [RRD](https://arxiv.org/abs/2602.05125) [RLR3](https://arxiv.org/abs/2605.30244)
- Post-cutoff generative reward-model candidates include self-training with consistency-aware answer and critique rewards, and natural-language-feedback training that scores generated critiques against human critiques. [ConsistRM](https://arxiv.org/abs/2604.07484) [RM-NLHF](https://arxiv.org/abs/2601.07349)
- The new visual PRM benchmark candidate contains 1,206 manually annotated thinking-with-images trajectories across four categories and 16 subcategories; its authors report that current LVLMs are not yet reliable PRMs in this setting. [arXiv:2602.08346](https://arxiv.org/abs/2602.08346)
- For verifier scaling, AgentV-RL reports a tool-augmented, bidirectional verifier and gains under both parallel and sequential test-time scaling. This is a single-paper result that needs protocol review before it informs a general scaling rule. [arXiv:2604.16004](https://arxiv.org/abs/2604.16004)

## Candidate ledger entries

```json
[
  {
    "id": "rubric-rrd-reward-2026",
    "title": "Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks",
    "url": "https://arxiv.org/abs/2602.05125",
    "source_type": "primary",
    "date": "2026-02-04",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based, single-source empirical claim",
    "claims": [
      "rrd-recursively-refines-rubrics-for-llm-judging-and-rft"
    ],
    "supports_claims": [
      "C001"
    ]
  },
  {
    "id": "rubric-rlr3-verifier-2026",
    "title": "Reinforcement Learning with Robust Rubric Rewards",
    "url": "https://arxiv.org/abs/2605.30244",
    "source_type": "primary",
    "date": "2026-05-28",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based, single-source empirical claim",
    "claims": [
      "rlr3-criterion-level-rubric-verification-for-vision-language-rl"
    ],
    "supports_claims": [
      "C002"
    ]
  },
  {
    "id": "reward-consistrm-2026",
    "title": "ConsistRM: Improving Generative Reward Models via Consistency-Aware Self-Training",
    "url": "https://arxiv.org/abs/2604.07484",
    "source_type": "primary",
    "date": "2026-04-08",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based, single-source empirical claim",
    "claims": [
      "consistrm-self-trains-generative-reward-models-with-consistency-aware-rewards"
    ],
    "supports_claims": [
      "C003"
    ]
  },
  {
    "id": "prm-rm-nlhf-reward-2026",
    "title": "Reward Modeling from Natural Language Human Feedback",
    "url": "https://arxiv.org/abs/2601.07349",
    "source_type": "primary",
    "date": "2026-01-12",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based, single-source empirical claim",
    "claims": [
      "rm-nlhf-uses-human-critiques-as-process-reward-for-generative-reward-models"
    ],
    "supports_claims": [
      "C004"
    ]
  },
  {
    "id": "verifier-agentv-rl-2026",
    "title": "AgentV-RL: Scaling Reward Modeling with Agentic Verifier",
    "url": "https://arxiv.org/abs/2604.16004",
    "source_type": "primary",
    "date": "2026-04-17",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based, single-source empirical claim",
    "claims": [
      "agentv-rl-scales-tool-augmented-bidirectional-verification-at-test-time"
    ],
    "supports_claims": [
      "C005"
    ]
  },
  {
    "id": "prm-thinking-images-verifier-benchmark-2026",
    "title": "What, Whether and How? Unveiling Process Reward Models for Thinking with Images Reasoning",
    "url": "https://arxiv.org/abs/2602.08346",
    "source_type": "primary",
    "date": "2026-02-09",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based, single-source empirical claim",
    "claims": [
      "thinking-images-benchmark-evaluates-prms-on-multimodal-step-errors"
    ],
    "supports_claims": [
      "C006"
    ]
  }
]
```

## Claim rows

| id | claim | source ids | verdict |
| --- | --- | --- | --- |
| C001 | RRD reports that recursively decomposing, filtering, and weighting rubrics improved its open-ended LLM-judge and RFT evaluations, including JudgeBench, PPE, WildChat, HealthBench-Hard, and BiGGen Bench. | rubric-rrd-reward-2026 | EVIDENCE-BASED, SINGLE-SOURCE, reported result |
| C002 | RLR3 uses criterion-level rubrics in vision-language RL, routing criteria either to an LLM extractor plus deterministic verifier or to an LLM judge; its authors report results on 15 benchmarks. | rubric-rlr3-verifier-2026 | EVIDENCE-BASED, SINGLE-SOURCE, reported result |
| C003 | ConsistRM trains a generative reward model without human annotations by using consistency-aware answer and critique rewards; its authors report a 1.5% average improvement over vanilla RFT across five datasets and four base models. | reward-consistrm-2026 | EVIDENCE-BASED, SINGLE-SOURCE, reported result |
| C004 | RM-NLHF uses similarity between a GRM-generated critique and a human critique as a process reward, and introduces a MetaRM intended to generalize that process reward to data without human critiques. | prm-rm-nlhf-reward-2026 | EVIDENCE-BASED, SINGLE-SOURCE, method and reported result |
| C005 | AgentV-RL frames reward modeling as a multi-turn, tool-augmented forward and backward verification process; its authors report gains under parallel and sequential test-time scaling. | verifier-agentv-rl-2026 | EVIDENCE-BASED, SINGLE-SOURCE, reported result |
| C006 | The Thinking-with-Images PRM benchmark contains 1,206 manually annotated trajectories, seven error types, four categories, and 16 subcategories; its authors report positive bias and step-position sensitivity in current LVLM PRMs. | prm-thinking-images-verifier-benchmark-2026 | EVIDENCE-BASED, SINGLE-SOURCE, reported benchmark result |
| C007 | SINGLE-SOURCE: RaR reports rubric-reward results in medical and science evaluations within one study. This supports only that study's scoped result, not the claim that rubric rewards work across domains. | rubric-rar-2025-context, https://arxiv.org/abs/2507.17746 | EVIDENCE-BASED, SINGLE-SOURCE, do not generalize |
| C008 | The PRM survey is version 3 as of 2026-04-29 and states coverage that includes text, multimodal reasoning, robotics, and agents. | prm-survey-2025, https://arxiv.org/abs/2510.08049 | EVIDENCE-BASED, SINGLE-SOURCE, literature-map update |

## Topic patch notes

- Keep the existing 2025-10-09 survey entry, but record that its live arXiv page was version 3 on 2026-04-29. Do not change its publication date to the revision date.
- Add a post-2025-10 subsection with the six candidate URLs above, separated into rubric and judge rewards, generative rewards, verifier scaling, and multimodal PRM evaluation.
- Add C001 through C006 only with their single-source scope labels. Retain the existing warning that PRM results in one task or protocol do not establish a domain-independent ranking.
- Add a benchmark-evaluation caveat from C006: test step-error localization, positive bias, and sensitivity to step position separately from final-answer selection.
- Add an operations caveat from C005: tool access and forward or backward verification paths change the reward model and test-time compute protocol, so compare them with matched tools, scorer calls, and latency.
- Add C007 as `SINGLE-SOURCE` if mentioning RaR's medical and science evidence. Do not write that rubric rewards work across domains. The currently verified material does not establish that general claim through two independent lineages.
- Preserve the Qwen PRM entry as mathematical-reasoning evidence and do not use it to support claims about open-ended, vision-language, or agentic verification.

## Negative results

- RaR is a relevant baseline but not a candidate in this post-2025-10 intake: its latest arXiv version is dated 2025-10-03, before the cutoff. [arXiv:2507.17746](https://arxiv.org/abs/2507.17746)
- Direct arXiv searches did not yield a later broad PRM survey to replace the existing 2025 survey. The existing survey's version 3 revision is a verification update, not a newly dated survey candidate. [arXiv:2510.08049](https://arxiv.org/abs/2510.08049)
- No source was promoted from a secondary paper-summary or blog result. Every candidate ledger URL is a directly fetched arXiv abstract page.

## Flags for verification

- All six candidates are single-paper claims. Before promotion to the canonical ledger, inspect the paper PDF, released code or data if any, evaluation prompts, model versions, and whether the reward, judge, or verifier was evaluated on a distribution affected by its own training data.
- Treat the numerical gains in C001, C002, C003, and C005 as author-reported results, not comparative state-of-the-art claims.
- `Rubric rewards work across domains` remains unproven here. C007 is explicitly SINGLE-SOURCE, and the text and vision-language candidates use different tasks, reward execution paths, and evaluations.
- For C004, determine whether critique similarity measures factual process quality or reward-model agreement before using it as step-supervision evidence.
- For C006, verify the annotation protocol and guided-search harness before treating the reported LVLM failure modes as a general PRM limitation.
