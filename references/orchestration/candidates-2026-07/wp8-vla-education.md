## Verified findings

Research snapshot: 2026-07-22. I read the topic 033 dossier before researching and re-fetched both ledger anchors. [SimpleVLA-RL](https://arxiv.org/abs/2509.09674) resolves to its arXiv record, submitted 2025-09-11. [The Reality Gap in Robotics](https://arxiv.org/abs/2510.20808) resolves to its arXiv record, submitted 2025-10-23; the fetched record says it was accepted for the 2026 *Annual Review of Control, Robotics, and Autonomous Systems*.

Four Apr-Jun 2026 results merit candidate status. They represent distinct ways to improve or adapt VLA policies with RL: residual policy learning and subsequent distillation (PLD), online on-robot RL fine-tuning (EXPO-FT), paired visual invariance and sensitivity objectives during PPO fine-tuning (PAIR-VLA), and GRPO post-training in RoboCasa (Z-1). Their performance numbers are each author-reported, single-source results, not an independently replicated ranking. [PLD](https://rpl.cs.utexas.edu/publications/2026/04/01/xiao-iclr26-pld/) was listed by UT Austin for ICLR 2026 on 2026-04-01, [EXPO-FT](https://arxiv.org/abs/2605.25477) was submitted 2026-05-25, [PAIR-VLA](https://arxiv.org/abs/2605.13105) was submitted 2026-05-13, and [Z-1](https://arxiv.org/abs/2606.31846) was submitted 2026-06-30.

Lab check: Physical Intelligence's [pi-star 0.6](https://arxiv.org/abs/2511.14759) is a directly relevant real-world VLA RL report, but its arXiv v1 date is 2025-11-18, so it is context rather than an Apr-Jul 2026 candidate. NVIDIA's [Alpamayo post-training guide](https://developer.nvidia.com/blog/how-to-post-train-autonomous-vehicle-models-in-closed-loop-with-nvidia-alpamayo/) is a 2026-05-31 official VLA closed-loop RL workflow, but the fetched page is a guide, not a manipulation result with a comparable experimental claim. NVIDIA's [SPARR project page](https://research.nvidia.com/labs/srl/projects/sparr/) is an ICRA 2026 real-robot residual-RL assembly result, but it is not a VLA paper. I did not add any Google DeepMind result to the candidate ledger because this run did not verify an Apr-Jul 2026 DeepMind technical report specifically about RL fine-tuning a VLA.

Education status: the [CS 185/285 page](https://rail.eecs.berkeley.edu/deeprlcourse/) currently shows a Spring 2026 staff address, January through April weekly material, and calls Fall 2023 recordings a past offering. Its fetched text contains no "Fall 2026" announcement, so the correct status is that a Fall 2026 offering is not shown on that page, not that no such offering exists. The [Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course/unit0/introduction) is live, free, and open-source, and currently exposes the listed introductory through PPO, robotics, multi-agent, and bonus units; the fetched page has no displayed last-updated field. The specified [Spinning Up landing page](https://spinningup.openai.com/en/latest/) is indexed live and lists documentation, algorithms, resources, exercises, and benchmark material. Its official [GitHub README](https://github.com/openai/spinningup) says "Maintenance (expect bug fixes and minor updates)" and the documentation introduction says no major updates are planned.

## URL re-verification

| id | url | status | what the page shows |
| --- | --- | --- | --- |
| simplevla-rl | https://arxiv.org/abs/2509.09674 | fetched, resolves to arXiv | *SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning*; v1 submitted 2025-09-11; the abstract describes VLA-specific trajectory sampling, parallelization, and comparisons. |
| reality-gap | https://arxiv.org/abs/2510.20808 | fetched, resolves to arXiv | *The Reality Gap in Robotics: Challenges, Solutions, and Best Practices*; v1 submitted 2025-10-23; the record says accepted for the 2026 *Annual Review of Control, Robotics, and Autonomous Systems*. |
| cs285 | https://rail.eecs.berkeley.edu/deeprlcourse/ | fetched, resolves to the Berkeley course page | CS 185/285 with `cs285-staff-sp2026`, a 2026 Jan-Apr schedule, and a link to Fall 2023 recordings as a past offering. No Fall 2026 text was found in the fetched page. |
| hf-course | https://huggingface.co/learn/deep-rl-course/unit0/introduction | fetched, resolves to the Hugging Face learning page | A free, open-source Deep RL Course with units covering Q-learning, Atari, policy gradients, Unity ML-Agents, robotics actor-critic methods, multi-agent RL, PPO, and bonus material. No last-updated field was displayed in the fetched page. |
| spinning-up | https://spinningup.openai.com/en/latest/ | fetched through live search index; direct page-open parser returned an internal error | The live indexed landing page lists documentation, RL introduction, resources, exercises, benchmarks, and algorithm documentation. The official GitHub README reports maintenance mode with bug fixes and minor updates; the indexed introduction says no major updates are planned. |

## Candidate ledger entries

```json
[
  {
    "id": "pld-vla-residual-rl-2026",
    "title": "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL",
    "url": "https://rpl.cs.utexas.edu/publications/2026/04/01/xiao-iclr26-pld/",
    "source_type": "official-lab-publication",
    "date": "2026-04-01",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "PLD uses residual RL probing, a hybrid rollout scheme, and distillation into a VLA generalist."
    ],
    "supports_claims": [
      "C331"
    ]
  },
  {
    "id": "expo-ft-vla-rl-2026",
    "title": "EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models",
    "url": "https://arxiv.org/abs/2605.25477",
    "source_type": "primary-research",
    "date": "2026-05-25",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "EXPO-FT reports online RL fine-tuning of pretrained VLA policies on real manipulation tasks."
    ],
    "supports_claims": [
      "C332"
    ]
  },
  {
    "id": "pair-vla-rl-finetuning-2026",
    "title": "What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models",
    "url": "https://arxiv.org/abs/2605.13105",
    "source_type": "primary-research",
    "date": "2026-05-13",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "PAIR-VLA adds paired visual invariance and sensitivity objectives during PPO RL fine-tuning."
    ],
    "supports_claims": [
      "C333"
    ]
  },
  {
    "id": "z1-vla-rl-2026",
    "title": "Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models",
    "url": "https://arxiv.org/abs/2606.31846",
    "source_type": "primary-research",
    "date": "2026-06-30",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "Z-1 applies task-wise GRPO post-training to a pi-0.5-based flow VLA on 24 RoboCasa tasks."
    ],
    "supports_claims": [
      "C334"
    ]
  }
]
```

## Claim rows

| id | claim | source ids | verdict |
| --- | --- | --- | --- |
| C331 | PLD's official lab page describes residual RL probing, distribution-aware hybrid rollout collection, and SFT distillation back into the VLA generalist. | pld-vla-residual-rl-2026 | verified source description; reported result only |
| C332 | EXPO-FT reports stable, sample-efficient online RL fine-tuning of pretrained VLA policies and reports 30/30 evaluated-task success within an average 19.1 minutes of online robot data. | expo-ft-vla-rl-2026 | verified author report; single-source performance claim |
| C333 | PAIR-VLA reports PPO fine-tuning with paired visual invariance and sensitivity objectives for visual shifts. | pair-vla-rl-finetuning-2026 | verified source description; comparative gains remain author-reported |
| C334 | Z-1 reports task-wise GRPO post-training of a pi-0.5-based flow VLA across 24 RoboCasa tasks and an 80.6% mean success rate. | z1-vla-rl-2026 | verified author report; single-source benchmark result |
| C335 | The fetched CS 185/285 page shows Spring 2026 material but no Fall 2026 offering text. | berkeley-cs285 | verified page-state observation; does not establish university-wide non-offering |
| C336 | The fetched Hugging Face page offers a free, open-source Deep RL Course and displays its units, but no visible update date. | hf-deep-rl-course | verified page-state observation |
| C337 | Spinning Up is in maintenance mode, with bug fixes and minor updates expected, and its documentation says no major updates are planned. | openai-spinning-up | verified against the official GitHub README and live indexed documentation |

## Topic patch notes

- Topic 033: add the four candidate records as an Apr-Jun 2026 subsection. Keep their reported benchmark or real-robot outcomes explicitly single-source and protocol-specific. Separate four adaptation patterns: residual-RL data generation and distillation, real-robot online VLA fine-tuning, visual-robustness PPO objectives, and simulator-based GRPO post-training.
- Topic 033: retain SimpleVLA-RL as the existing 2025 anchor. Add a dated context note for Physical Intelligence pi-star 0.6, but do not misdate it as a 2026 release. Add NVIDIA's Alpamayo guide as a workflow source only, and SPARR as adjacent non-VLA sim-to-real residual RL evidence.
- Education-source notes: update CS285 to "Spring 2026 page live; Fall 2026 not shown on fetched landing page". Keep Hugging Face as live course material with no page-visible update date. Mark Spinning Up as maintenance-only and retain it for fundamentals, not current-library or current-benchmark guidance.

## Negative results

- No Fall 2026 CS285 offering was found on the fetched course landing page. This is a page-level result, not evidence that Berkeley will not offer the course.
- Physical Intelligence's directly relevant pi-star 0.6 paper was outside the requested Apr-Jul 2026 window because its arXiv v1 is dated 2025-11-18.
- NVIDIA's Alpamayo release is related VLA closed-loop RL infrastructure, but the fetched guide does not provide a directly comparable experimental manipulation result. NVIDIA SPARR is a real-robot RL result, but not a VLA result.
- This run did not verify an Apr-Jul 2026 Google DeepMind technical report that specifically presents RL fine-tuning of a VLA. No candidate was inferred from the absence of a fetched report.

## Flags for verification

- Obtain a second, independent source or reproduction before using C332 or C334 as a comparative performance claim. The present claims are paper-author reports.
- Confirm PLD's canonical publication metadata before adding it to the permanent ledger: the UT Austin page is dated 2026-04-01, while its arXiv preprint date is 2025-10-30.
- Recheck CS285 near Berkeley's Fall 2026 schedule publication. The present page only confirms what was displayed on 2026-07-22.
- Recheck the Hugging Face course repository or revision history if a maintenance cadence is needed; the fetched course page has no visible last-updated field.
- Direct parsing of the specified Spinning Up URL failed in the browser tool even though live indexed documentation and the official GitHub README were retrievable. Re-fetch the page directly before asserting an HTTP-level availability status.
