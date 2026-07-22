## Verified findings

- Topic 027 already covers DreamerV3 and Genie 3. The live [DreamerV3 arXiv record](https://arxiv.org/abs/2301.04104) identifies the paper and describes imagined future scenarios; the live [Genie 3 post](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) is dated 2025-08-05 and labels Genie 3 a limited research preview. Its vendor claims should therefore remain qualified.
- Topic 028 already covers [The Art of Scaling Test-Time Compute for Large Language Models](https://arxiv.org/abs/2512.02008), whose live arXiv record is dated 2025-12-01. The paper reports a protocol-bound comparison across eight open models and states that no single test-time-scaling strategy universally dominates in its study.
- The candidate set below contains six items, all fetched live on 2026-07-22: three world-model or agent-environment items and three January to May 2026 test-time-compute follow-ups. It is a candidate pack, not a claim of independent replication or state of the art.

## URL re-verification (existing sources: id, url, status)

| id | url | status |
| --- | --- | --- |
| genie-3-blog-2025 | https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/ | Resolved on 2026-07-22 after redirecting to `https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/`; fetched page is dated 2025-08-05. |
| art-of-scaling-ttc-2025 | https://arxiv.org/abs/2512.02008 | Resolved and fetched on 2026-07-22; arXiv page identifies submission date 2025-12-01. |

## Candidate ledger entries

```json
[
  {
    "id": "world-model-waymo-2026",
    "title": "The Waymo World Model: A New Frontier For Autonomous Driving Simulation",
    "url": "https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation/",
    "source_type": "vendor",
    "date": "2026-02-06",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "medium",
    "claims": [
      "waymo-world-model-autonomous-driving-simulation"
    ],
    "supports_claims": [
      "C271"
    ]
  },
  {
    "id": "dreamer-world-model-cdp-2026",
    "title": "Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction",
    "url": "https://arxiv.org/abs/2603.07083",
    "source_type": "primary-research",
    "date": "2026-03-07",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "medium",
    "claims": [
      "dreamer-cdp-reconstruction-free-latent-prediction"
    ],
    "supports_claims": [
      "C272"
    ]
  },
  {
    "id": "world-model-behavior-consistency-2026",
    "title": "Beyond State Consistency: Behavior Consistency in Text-Based World Models",
    "url": "https://arxiv.org/abs/2604.13824",
    "source_type": "primary-research",
    "date": "2026-04-15",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "medium",
    "claims": [
      "behavior-consistency-reward-for-text-agent-world-models"
    ],
    "supports_claims": [
      "C273"
    ]
  },
  {
    "id": "test-time-adaptive-allocation-2026",
    "title": "What If We Allocate Test-Time Compute Adaptively?",
    "url": "https://arxiv.org/abs/2602.01070",
    "source_type": "primary-research",
    "date": "2026-02-01",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "medium",
    "claims": [
      "prm-guided-adaptive-test-time-compute-allocation"
    ],
    "supports_claims": [
      "C274"
    ]
  },
  {
    "id": "test-time-compute-aligned-training-2026",
    "title": "Compute Aligned Training: Optimizing for Test Time Inference",
    "url": "https://arxiv.org/abs/2604.24957",
    "source_type": "primary-research",
    "date": "2026-04-27",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "medium",
    "claims": [
      "test-time-compute-aligned-sft-and-rl-training-objectives"
    ],
    "supports_claims": [
      "C275"
    ]
  },
  {
    "id": "test-time-post-training-scaling-law-2026",
    "title": "What should post-training optimize? A test-time scaling law perspective",
    "url": "https://arxiv.org/abs/2605.10716",
    "source_type": "primary-research",
    "date": "2026-05-11",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "medium",
    "claims": [
      "best-of-n-oriented-post-training-under-budget-mismatch"
    ],
    "supports_claims": [
      "C276"
    ]
  }
]
```

## Claim rows

| C??? | claim | source ids | verdict |
| --- | --- | --- | --- |
| C271 | Waymo's 2026-02-06 vendor post introduces a Genie 3-based world model for autonomous-driving simulation and says it generates camera and lidar outputs under driving-action, layout, and language controls. | world-model-waymo-2026 | Candidate only. Vendor evidence, medium confidence, and not evidence of independently established safety or training benefit. |
| C272 | Dreamer-CDP proposes a reconstruction-free, JEPA-style continuous deterministic predictor for a Dreamer-adjacent world-model setting; its authors report matching Dreamer on Crafter. | dreamer-world-model-cdp-2026 | Candidate only. Single arXiv paper and benchmark-scoped author report. |
| C273 | The behavior-consistency paper introduces Behavior Consistency Reward for text-based world models and reports results in WebShop and TextWorld, including preliminary inference-time lookahead findings. | world-model-behavior-consistency-2026 | Candidate only. Single arXiv paper; do not generalize its text-environment evidence to visual or physical environments. |
| C274 | The adaptive-allocation paper proposes iterative, process-reward-model-guided test-time allocation that jointly chooses reasoning tools and compute strategy. | test-time-adaptive-allocation-2026 | Candidate only. Its reported benchmark improvements are paper-specific and need matched-budget replication. |
| C275 | Compute Aligned Training frames common test-time strategies as operators on the base policy and instantiates aligned objectives for both supervised fine-tuning and reinforcement learning. | test-time-compute-aligned-training-2026 | Candidate only. The claimed improvement over standard training is a single-paper empirical result, not a settled TTC-versus-RL conclusion. |
| C276 | The test-time scaling-law paper studies a regime in which post-training uses far fewer per-prompt rollouts than best-of-N deployment and proposes tail-extrapolated estimators for that mismatch. | test-time-post-training-scaling-law-2026 | Candidate only. It relies on stated reward-tail assumptions and instruction-following experiments. |

## Topic patch notes

- `references/topics/027-*.md`: retain DreamerV3 and Genie 3 as the historical anchors. Add C271 as a vendor-qualified, post-Genie 3 deployment claim, not proof of safe autonomous driving. Add C272 as a Dreamer-adjacent reconstruction-free candidate, and C273 as a text-agent world-model candidate. In `Evidence Caveats`, distinguish visual interactive generation, autonomous-driving simulation, and text-agent surrogate environments; none establishes a universally reliable environment for RL or computer use.
- `references/topics/028-*.md`: retain the 2025 Art of Scaling finding that strategy selection is model-, difficulty-, and budget-dependent. Add C274 under adaptive routing, C275 under train-time objective alignment with deployment-time aggregation, and C276 under the training-rollout versus deployment-rollout budget mismatch. State that these papers offer mechanisms and bounded empirical evidence, not a universal answer to whether more test-time compute is preferable to RL training.

## Negative results

- No canonical DreamerV4 release or official Dreamer-line replacement was selected. The live survey surfaced Dreamer-adjacent 2026 papers, so C272 is a research candidate rather than a successor release claim.
- No standalone video model was selected merely because it generates video. The selected Waymo entry was included because its dated first-party post describes action-conditioned, multi-sensor driving simulation; it remains vendor evidence.
- No candidate was selected from search-result snippets, third-party summaries, or an unfetched URL.

## Flags for verification

- Before ledger promotion, obtain an independent source or an original technical report for C271. Keep `source_type: vendor` and confidence no higher than medium unless the evidence base changes.
- Treat C272 through C276 as preprint-level evidence. Verify code, evaluation protocol, compute accounting, and reproduction status before using any comparative or performance language in a canon note.
- Preserve the current Genie 3 limitation: its live vendor post calls it a limited research preview. Do not write that it is a production-grade RL training environment.
- This report intentionally does not update `references/source-ledger.json` or either topic file, per the requested single-file scope.
