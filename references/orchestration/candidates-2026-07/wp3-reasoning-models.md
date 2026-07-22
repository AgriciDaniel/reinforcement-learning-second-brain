## Verified findings

- **DeepSeek R2 status, 2026-07-22:** still unreleased in the only status that can be confirmed from a primary release record. DeepSeek's Transparency Center says it lists released models with their release dates, reports, and model cards; the retrieved catalog lists V3.2 and V4, but not R2. This establishes that no official R2 release is recorded there. It does not establish that R2 was cancelled. [deepseek-transparency-center]
- **Rumor separation:** Tom's Hardware reported an account of alleged R2 training delays, attributed to Financial Times reporting and unnamed sources. It is a rumor, not confirmation by DeepSeek, and is retained only as a contested claim. [tomshardware-r2-delay-rumor]
- **Open-weight model candidates that meet the evidence threshold:**
  - **GLM-5.1, 2026-04-07.** Z.ai's release notes say it used multi-turn SFT, RL, and a process-quality evaluation framework; the official model card provides MIT-licensed weights. The public material does not name the RL optimizer or reward construction. [zai-glm-5-1-release-notes, zai-glm-5-1-model-card]
  - **MiniMax M3, 2026-06-01.** MiniMax calls M3 an officially released open-weight model; the associated MaxProof report says the M3 series trains proof generation, verification, and critique-conditioned repair with generative-verifier RL, using a defense-in-depth verifier engineered for a low false-positive rate. The abstract does not name a policy optimizer. [minimax-m3-release, minimax-maxproof]
  - **Qwen-AgentWorld-35B-A3B, 2026-06-23 report/model-announcement date.** The official card provides Apache-2.0 weights and documents CPT, SFT, then GSPO RL; its technical report says the RL framework uses hybrid rubric-and-rule rewards to sharpen simulation fidelity. June 23 is the technical report date, not an independently retrieved weight-upload timestamp. [qwen-agentworld-model-card, qwen-agentworld-report]
- **Frontier-lab reports, April through July 2026:** Meta's RA-RFT report uses gold-relevance distillation for retrieval and reinforcement fine-tuning with retrieved analogous demonstrations under verifiable outcome rewards. Anthropic's robotics report evaluates language models that train controllers from scratch with RL, alongside other robot-control interfaces. Anthropic's introspection-adapter report is reward-model-relevant auditing work: it uses SFT and a DPO refinement whose preference pairs are scored for accuracy by an LLM judge. [meta-ra-rft, anthropic-claude-plays-robotics, anthropic-introspection-adapters]

## Candidate ledger entries

```json
[
  {
    "id": "deepseek-transparency-center",
    "title": "Transparency Center",
    "url": "https://www.deepseek.com/en/transparency/",
    "source_type": "official",
    "date": "2026-04-24",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": ["DeepSeek describes this as its catalog of released models, release dates, technical reports, and model cards; its retrieved list contains V3.2 and V4, not R2."],
    "supports_claims": ["C009"]
  },
  {
    "id": "tomshardware-r2-delay-rumor",
    "title": "DeepSeek reportedly urged by Chinese authorities to train new model on Huawei hardware after multiple failures",
    "url": "https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseek-reportedly-urged-by-chinese-authorities-to-train-new-model-on-huawei-hardware-after-multiple-failures-r2-training-to-switch-back-to-nvidia-hardware-while-ascend-gpus-handle-inference",
    "source_type": "practitioner",
    "date": "2025-08-14",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "contested",
    "claims": ["Tom's Hardware relayed an alleged R2 training-delay account attributed to Financial Times reporting and unnamed sources; DeepSeek confirmation was not retrieved."],
    "supports_claims": ["C016"]
  },
  {
    "id": "zai-glm-5-1-release-notes",
    "title": "New Released - GLM-5.1",
    "url": "https://docs.z.ai/release-notes/new-released",
    "source_type": "official",
    "date": "2026-04-07",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": ["Z.ai dates GLM-5.1 to 2026-04-07 and describes multi-turn SFT, RL, and a process-quality evaluation framework."],
    "supports_claims": ["C010"]
  },
  {
    "id": "zai-glm-5-1-model-card",
    "title": "zai-org/GLM-5.1 model card",
    "url": "https://huggingface.co/zai-org/GLM-5.1",
    "source_type": "official",
    "date": "2026-04-07",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": ["The Z.ai-hosted model card exposes GLM-5.1 files and states the MIT license."],
    "supports_claims": ["C010"]
  },
  {
    "id": "minimax-m3-release",
    "title": "MiniMax M3: Frontier Coding, 1M Context, Native Multimodality",
    "url": "https://www.minimax.io/blog/minimax-m3",
    "source_type": "official",
    "date": "2026-06-01",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": ["MiniMax says M3 was officially released on 2026-06-01 and describes it as an open-weight model."],
    "supports_claims": ["C011"]
  },
  {
    "id": "minimax-maxproof",
    "title": "MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level Test-Time Scaling",
    "url": "https://arxiv.org/abs/2606.13473",
    "source_type": "primary",
    "date": "2026-06-11",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": ["The report states that the MiniMax-M3 series trains proof generation, verification, and critique-conditioned repair with a low-false-positive generative verifier, then merges them into a released M3 model."],
    "supports_claims": ["C011"]
  },
  {
    "id": "qwen-agentworld-model-card",
    "title": "Qwen/Qwen-AgentWorld-35B-A3B model card",
    "url": "https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B",
    "source_type": "official",
    "date": "2026-06-23",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": ["The Qwen card provides Apache-2.0 model artifacts and specifies CPT, SFT, and RL using GSPO."],
    "supports_claims": ["C012"]
  },
  {
    "id": "qwen-agentworld-report",
    "title": "Qwen-AgentWorld: Language World Models for General Agents",
    "url": "https://arxiv.org/abs/2606.24597",
    "source_type": "primary",
    "date": "2026-06-23",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": ["The technical report's first arXiv version is dated 2026-06-23, introduces Qwen-AgentWorld, and describes a tailored RL framework with hybrid rubric-and-rule rewards for simulation fidelity."],
    "supports_claims": ["C012"]
  },
  {
    "id": "meta-ra-rft",
    "title": "Learning to Reason by Analogy via Retrieval-Augmented Reinforcement Fine-Tuning",
    "url": "https://ai.meta.com/research/publications/learning-to-reason-by-analogy-via-retrieval-augmented-reinforcement-fine-tuning/",
    "source_type": "vendor",
    "date": "2026-07-17",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": ["Meta describes RA-RFT as gold-relevance distillation for retrieval followed by reinforcement fine-tuning of a policy with retrieved analogous demonstrations under verifiable outcome rewards."],
    "supports_claims": ["C013"]
  },
  {
    "id": "anthropic-claude-plays-robotics",
    "title": "Claude plays robotics",
    "url": "https://www.anthropic.com/research/claude-plays-robotics",
    "source_type": "vendor",
    "date": "2026-07-09",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": ["Anthropic evaluates language models across robot-control interfaces, including one in which the model trains a controller from scratch with reinforcement learning."],
    "supports_claims": ["C014"]
  },
  {
    "id": "anthropic-introspection-adapters",
    "title": "Introspection Adapters: Training LLMs to Report Their Learned Behaviors",
    "url": "https://alignment.anthropic.com/2026/introspection-adapters/",
    "source_type": "vendor",
    "date": "2026-04-28",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": ["Anthropic describes introspection-adapter training with SFT followed by DPO refinement using LLM-judge accuracy scores to create preference pairs; it evaluates a reward-model-sycophant case among its audit settings."],
    "supports_claims": ["C015"]
  }
]
```

## Claim rows

| C009 | As of 2026-07-22, DeepSeek's official released-model catalog records no DeepSeek R2 release. | deepseek-transparency-center | verified |
| C010 | GLM-5.1 was released on 2026-04-07 with publicly available MIT-licensed weights; the disclosed recipe is multi-turn SFT plus RL and a process-quality evaluation framework, without a named optimizer or reward construction. | zai-glm-5-1-release-notes, zai-glm-5-1-model-card | verified |
| C011 | MiniMax M3 was released open-weight on 2026-06-01; the associated M3-series report documents generative-verifier RL for proof generation, verification, and repair, with a verifier engineered for low false-positive rate. | minimax-m3-release, minimax-maxproof | verified |
| C012 | Qwen-AgentWorld's official weights use Apache-2.0 and the card documents CPT, SFT, then GSPO RL; the report describes hybrid rubric-and-rule rewards for simulation fidelity and is dated 2026-06-23, while an independently dated weight-upload event was not retrieved. | qwen-agentworld-model-card, qwen-agentworld-report | single-source |
| C013 | Meta's July 17 RA-RFT report combines gold-relevance retriever distillation with reinforcement fine-tuning under verifiable outcome rewards. | meta-ra-rft | single-source |
| C014 | Anthropic's July 9 robotics report includes evaluation of language models supervising the training of RL controllers from scratch. | anthropic-claude-plays-robotics | single-source |
| C015 | Anthropic's April 28 introspection-adapter report is reward-model-relevant auditing work that uses LLM-judge-scored DPO refinement. | anthropic-introspection-adapters | single-source |
| C016 | The claimed DeepSeek R2 training delays are unconfirmed reporting, not a verified release or training fact. | tomshardware-r2-delay-rumor | contested |

## Topic patch notes

- `references/topics/020-grpo-and-rl-with-verifiable-rewards-for-reasoning-models.md`: add C011 as a concrete generative-verifier-RL example and C013 as a retrieval-augmented RFT example with verifiable outcome rewards. State that neither source identifies a universally superior optimizer or reward scheme. Add C010 only as a high-level multi-turn-SFT-plus-RL example because its optimizer and reward construction are not published. Add C012 in a separate language-world-model subsection, noting its GSPO and hybrid rubric-and-rule reward description but not inferring undisclosed reward weights or training settings. Add C015 under reward-model auditing and preference-refinement caveats, not as RLVR.
- `references/topics/020-grpo-and-rl-with-verifiable-rewards-for-reasoning-models.md`: replace the existing informal R2 wording with: "As of the 2026-07-22 retrieval, DeepSeek's official released-model catalog does not record DeepSeek R2; treat third-party R2 delay accounts as contested." Cite `deepseek-transparency-center` and keep the rumor source clearly separated.
- `references/topics/024-rl-tooling-landscape-gymnasium-sb3-cleanrl-rllib-trl-verl-openrl.md`: add a short integration note that model cards may expose a named post-training algorithm, such as GSPO, while omitting reward semantics and training-stack provenance. Link readers to topic 020 for recipe and verifier analysis; do not infer that any existing tool implements the cited vendor recipes without a pinned implementation source.
- No repository topic file was changed in this task, per scope.

## Negative results

- **Kimi K2.6:** the official Kimi timeline dates its open-source release to 2026-04-20 and the official card supplies weights, but the retrieved K2.6 card does not document a K2.6-specific RL post-training recipe. It says K2.6 has K2.5's architecture and links the K2.5 report, which is insufficient to transfer the older recipe. Excluded from the 2 to 5 candidate set. Sources: https://www.kimi.com/help/agent/agent-overview and https://huggingface.co/moonshotai/Kimi-K2.6.
- **Kimi K3:** Kimi's official timeline says K3 launched through product surfaces on 2026-07-16 but that full weights arrive on 2026-07-27. That date is after this snapshot, so K3 is not an open-weight candidate as of 2026-07-22. Source: https://www.kimi.com/help/agent/agent-overview.
- **Qwen3.6:** I retrieved first-party release material but not a Qwen3.6-specific RL post-training recipe with an algorithm and reward type. It is excluded rather than inheriting a recipe from another Qwen generation. Source checked: https://qwen.ai/blog?id=qwen3.6-35b-a3b.
- **GLM-5.2:** Z.ai's release notes date it to 2026-06-16, but the retrieved entry does not state a GLM-5.2-specific RL recipe. It is excluded instead of projecting GLM-5.1 or GLM-5 training details forward. Source checked: https://docs.z.ai/release-notes/new-released.
- **Llama lineage and Mistral:** no April through July 2026 open-weight reasoning-model release with a qualifying, fetched first-party RL recipe was added.
- **OpenAI and Google DeepMind:** no qualifying April through July first-party report on RL post-training, reward modeling, or RLVR was retrieved for inclusion. This is a search result for this run, not a claim that no such work exists.
- **Anthropic's "Abstractive Red-Teaming"** was not included because the retrieved publication is dated March 2026, outside the requested window.

## Flags for verification

- C009 is an official-catalog absence result. For a stronger claim than "no official release is recorded," obtain an explicit current DeepSeek statement about R2's status.
- C012 uses the report's 2026-06-23 date as a model-announcement proxy. Before entering a release chronology, verify the weight repository's first commit or a dated Qwen release post.
- C010, C011, and C012 document different levels of recipe detail. Do not normalize their reward types, policy objectives, reward weights, or claimed capability gains without full technical reports and reproducible implementations.
- All vendor reports are primary for what their organizations say they did, but their performance and comparative claims remain vendor-reported unless independently reproduced.
- Recheck the Kimi K3 weights after 2026-07-27. Its availability status is time-sensitive.
