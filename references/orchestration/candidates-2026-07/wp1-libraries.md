## Verified findings

- Gymnasium's current PyPI release is `1.3.0`, uploaded on 2026-04-22, and GitHub marks `v1.3.0` as the latest release; source URLs: https://pypi.org/pypi/gymnasium/json, https://pypi.org/project/gymnasium/, https://github.com/Farama-Foundation/Gymnasium/releases/tag/v1.3.0; date seen on page: 2026-04-22; evidence: PyPI labels 1.3.0 as the latest release and gives the upload date, while GitHub labels the matching tag Latest.
- Gymnasium is assessed **active** from release recency; source URL: https://pypi.org/project/gymnasium/; date seen on page: 2026-04-22; evidence: its latest release is less than three months old as of 2026-07-22. This is a release-recency assessment, not a maintainer declaration.
- Stable-Baselines3's current PyPI release is `2.9.0`, uploaded on 2026-06-15, and GitHub marks `v2.9.0` as the latest release; source URLs: https://pypi.org/pypi/stable-baselines3/json, https://pypi.org/project/stable-baselines3/, https://github.com/DLR-RM/stable-baselines3/releases/tag/v2.9.0; date seen on page: 2026-06-15; evidence: PyPI labels 2.9.0 as latest and GitHub labels the matching tag Latest.
- Stable-Baselines3 is assessed **active** from release recency; source URL: https://pypi.org/project/stable-baselines3/; date seen on page: 2026-06-15; evidence: the latest release is about five weeks old as of 2026-07-22. This is a release-recency assessment, not a maintainer declaration.
- CleanRL's current PyPI release is `1.2.0`, uploaded on 2023-05-22; source URL: https://pypi.org/project/cleanrl/; date seen on page: 2023-05-22; evidence: PyPI labels 1.2.0 as the latest release.
- CleanRL's GitHub releases page instead marks `v1.0.0` as its latest GitHub release, dated 2022-11-14; source URLs: https://github.com/vwxyzjn/cleanrl/releases/tag/v1.0.0, https://github.com/vwxyzjn/cleanrl; date seen on page: 2022-11-14; evidence: the GitHub repository renders `v1.0.0 CleanRL Release` as Latest with that date.
- CleanRL is assessed **slow** from release recency; source URLs: https://pypi.org/project/cleanrl/, https://github.com/vwxyzjn/cleanrl/releases; date seen on page: 2023-05-22 and 2022-11-14; evidence: neither the latest PyPI distribution nor the latest GitHub release is recent. This does not establish that the repository is archived.
- Ray, which contains RLlib, has current PyPI and GitHub release `2.56.1`, uploaded/released on 2026-07-17; source URLs: https://pypi.org/pypi/ray/json, https://pypi.org/project/ray/, https://github.com/ray-project/ray/releases/tag/ray-2.56.1; date seen on page: 2026-07-17; evidence: PyPI labels 2.56.1 as latest and GitHub labels `ray-2.56.1` Latest.
- Ray/RLlib is assessed **active** from release recency; source URL: https://pypi.org/project/ray/; date seen on page: 2026-07-17; evidence: the latest release is five days old as of 2026-07-22. This is a release-recency assessment, not a maintainer declaration.
- TRL's current PyPI and GitHub release is `1.9.0`, uploaded/released on 2026-07-21; source URLs: https://pypi.org/pypi/trl/json, https://pypi.org/project/trl/, https://github.com/huggingface/trl/releases; date seen on page: 2026-07-21; evidence: PyPI labels 1.9.0 latest and GitHub labels `v1.9.0` Latest.
- TRL is assessed **active** from release recency; source URL: https://pypi.org/project/trl/; date seen on page: 2026-07-21; evidence: the latest release is one day old as of 2026-07-22. This is a release-recency assessment, not a maintainer declaration.
- veRL's current PyPI and GitHub release is `0.8.0`, uploaded/released on 2026-06-01; source URLs: https://pypi.org/project/verl/, https://github.com/verl-project/verl/releases/tag/v0.8.0; date seen on page: 2026-06-01; evidence: PyPI labels 0.8.0 latest and GitHub labels `v0.8.0` Latest. The previously recorded `volcengine/verl` release URL redirects to `verl-project/verl`.
- veRL is assessed **active** from release recency; source URL: https://pypi.org/project/verl/; date seen on page: 2026-06-01; evidence: the latest release is about seven weeks old as of 2026-07-22. This is a release-recency assessment, not a maintainer declaration.
- OpenRLHF's current PyPI and GitHub release is `0.10.4`, uploaded/released on 2026-06-08; source URLs: https://pypi.org/project/openrlhf/, https://github.com/OpenRLHF/OpenRLHF/releases/tag/v0.10.4; date seen on page: 2026-06-08; evidence: PyPI labels 0.10.4 latest and GitHub labels `v0.10.4` Latest.
- OpenRLHF is assessed **active** from release recency; source URL: https://pypi.org/project/openrlhf/; date seen on page: 2026-06-08; evidence: the latest release is about six weeks old as of 2026-07-22. This is a release-recency assessment, not a maintainer declaration.
- The required JSON endpoint returned application JSON for Gymnasium, Stable-Baselines3, Ray, and TRL; source URLs: https://pypi.org/pypi/gymnasium/json, https://pypi.org/pypi/stable-baselines3/json, https://pypi.org/pypi/ray/json, https://pypi.org/pypi/trl/json; date seen on page: 2026-07-22; evidence: each fetch returned a PyPI JSON response. The human-readable PyPI project pages above were used to capture the rendered version and date fields.
- The required CleanRL JSON endpoint failed twice in this browser with `Cache miss`; source URL: https://pypi.org/pypi/cleanrl/json; date seen on page: 2026-07-22; evidence: the endpoint fetch returned an error even though the official project page was available.
- The required veRL JSON endpoint failed twice in this browser, first with `Cache miss` and then with `(400) OK`; source URL: https://pypi.org/pypi/verl/json; date seen on page: 2026-07-22; evidence: the endpoint fetch returned errors even though the official project page was available.
- The required OpenRLHF JSON endpoint failed twice in this browser, first with an internal error and then with `Unknown error fetching`; source URL: https://pypi.org/pypi/openrlhf/json; date seen on page: 2026-07-22; evidence: the endpoint fetch returned errors even though the official project page was available.
- In current TRL `1.9.0` documentation, `GRPOTrainer` is categorized as an online method and `DPOTrainer` as an offline method; source URL: https://huggingface.co/docs/trl/index; date seen on page: no publication date displayed, version selector shows 1.9.0; evidence: the taxonomy explicitly lists GRPO under Online methods and DPO under Offline methods.
- Current DPO guidance requires offline rows with `prompt`, preferred `chosen`, and dispreferred `rejected` completions; source URL: https://huggingface.co/docs/trl/dpo_trainer; date seen on page: no publication date displayed; evidence: the DPO trainer documentation states that each example is expected to contain those three elements.
- TRL `v1.0.0`, released on 2026-03-31, introduced `AsyncGRPOTrainer` from `trl.experimental.async_grpo` and a `GRPOConfig(loss_type="vespo")` option; source URL: https://github.com/huggingface/trl/releases/tag/v1.0.0; date seen on page: 2026-03-31; evidence: the release notes show both imports/configuration paths. Guidance should therefore describe Async GRPO as an explicitly versioned experimental path rather than as the default GRPO recipe.
- TRL `v1.0.0` added `max_length` support for DPO VLM training, and current DPO documentation says to use `DPOConfig(max_length=None)` when truncation could remove image tokens; source URLs: https://github.com/huggingface/trl/releases/tag/v1.0.0, https://huggingface.co/docs/trl/dpo_trainer; date seen on page: 2026-03-31 and no publication date displayed; evidence: the release note announces the option and the current trainer page gives the VLM safeguard.
- TRL `v1.9.0` added iterable or streaming dataset support to GRPO and RLOO, with `max_steps` required for iterable datasets and `dispatch_batches=False` enforced; source URL: https://github.com/huggingface/trl/releases; date seen on page: 2026-07-21; evidence: the release notes say the new generator preserves grouped prompts and state both constraints.
- TRL `v1.9.0` added `DPOConfig(loss_type="sigmoid_norm")`, a length-normalized DPO sigmoid loss; source URL: https://github.com/huggingface/trl/releases; date seen on page: 2026-07-21; evidence: the release notes name the option and state that it is intended to mitigate length bias.

## Candidate ledger entries

```json
[
  {
    "id": "vime-vllm",
    "title": "vime: A Simple, Stable, and Efficient RL Framework for LLMs",
    "url": "https://vllm-project.github.io/2026/06/09/announcing-vime.html",
    "source_type": "official",
    "date": "2026-06-09",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "medium",
    "claims": [
      "vime-vllm-megatron-rl-pipeline",
      "vime-grpo-ppo-example-coverage"
    ],
    "supports_claims": [
      "vime-vllm-megatron-rl-pipeline",
      "vime-grpo-ppo-example-coverage"
    ]
  },
  {
    "id": "miles-radixark",
    "title": "Miles: A PyTorch-Native Stack for Large-Scale LLM RL Post-Training",
    "url": "https://pytorch.org/blog/miles-a-pytorch-native-stack-for-large-scale-llm-rl-post-training/",
    "source_type": "vendor",
    "date": "2026-06-30",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "medium",
    "claims": [
      "miles-llm-rl-post-training-framework",
      "miles-sglang-megatron-ray-stack"
    ],
    "supports_claims": [
      "miles-llm-rl-post-training-framework",
      "miles-sglang-megatron-ray-stack"
    ]
  }
]
```

### Updates to existing sources

- `gymnasium-docs`: set the current package/release snapshot to `1.3.0`, 2026-04-22, active; sources: https://pypi.org/project/gymnasium/ and https://github.com/Farama-Foundation/Gymnasium/releases/tag/v1.3.0.
- `stable-baselines3-docs`: set the current package/release snapshot to `2.9.0`, 2026-06-15, active; sources: https://pypi.org/project/stable-baselines3/ and https://github.com/DLR-RM/stable-baselines3/releases/tag/v2.9.0.
- `cleanrl-docs`: record the release-channel divergence: PyPI `1.2.0`, 2023-05-22, while GitHub's latest release is `v1.0.0`, 2022-11-14; classify release activity as slow and do not infer repository archival; sources: https://pypi.org/project/cleanrl/ and https://github.com/vwxyzjn/cleanrl/releases/tag/v1.0.0.
- `rllib-docs`: record Ray package/release `2.56.1`, 2026-07-17, active, and retain the note that RLlib ships in Ray rather than as a separately versioned PyPI package; sources: https://pypi.org/project/ray/ and https://github.com/ray-project/ray/releases/tag/ray-2.56.1.
- `trl-docs`: set the current package/release snapshot to `1.9.0`, 2026-07-21, active; correct the v1.0.0 release date to 2026-03-31; add the current online-GRPO versus offline-DPO taxonomy and the v1.9 streaming-GRPO and `sigmoid_norm` DPO changes; sources: https://pypi.org/project/trl/, https://huggingface.co/docs/trl/index, and https://github.com/huggingface/trl/releases.
- `verl-docs`: set the current package/release snapshot to `0.8.0`, 2026-06-01, active; change the canonical GitHub release URL from the redirected `volcengine/verl` path to https://github.com/verl-project/verl/releases/tag/v0.8.0; source: https://pypi.org/project/verl/.
- `openrlhf-repo`: set the current package/release snapshot to `0.10.4`, 2026-06-08, active; sources: https://pypi.org/project/openrlhf/ and https://github.com/OpenRLHF/OpenRLHF/releases/tag/v0.10.4.

## Claim rows

| Claim ID | Claim text | Source ids | Verdict |
|---|---|---|---|
| C??? | Gymnasium's current package and GitHub release is 1.3.0, released on 2026-04-22. | gymnasium-docs | verified |
| C??? | Stable-Baselines3's current package and GitHub release is 2.9.0, released on 2026-06-15. | stable-baselines3-docs | verified |
| C??? | CleanRL has divergent latest release labels: PyPI 1.2.0 from 2023-05-22 and GitHub v1.0.0 from 2022-11-14. | cleanrl-docs | verified |
| C??? | Ray 2.56.1 is current as of 2026-07-17, and RLlib remains distributed as part of Ray. | rllib-docs | verified |
| C??? | TRL 1.9.0 is current as of 2026-07-21. | trl-docs | verified |
| C??? | veRL 0.8.0 is current as of 2026-06-01. | verl-docs | verified |
| C??? | OpenRLHF 0.10.4 is current as of 2026-06-08. | openrlhf-repo | verified |
| C??? | In current TRL documentation, GRPO is an online trainer and DPO is an offline trainer. | trl-docs | single-source |
| C??? | TRL 1.9 supports streaming datasets for GRPO and RLOO, requiring max_steps for iterable datasets. | trl-docs | single-source |
| C??? | TRL 1.9 adds DPOConfig loss_type sigmoid_norm for length-normalized DPO. | trl-docs | single-source |
| C??? | vime is a vLLM-ecosystem LLM post-training framework joining Megatron training with vLLM rollout. | vime-vllm | single-source |
| C??? | Miles is a RadixArk LLM RL post-training framework that composes SGLang, Megatron-LM, Ray, and PyTorch. | miles-radixark | single-source |

## Topic patch notes

- `references/topics/024-rl-tooling-landscape-gymnasium-sb3-cleanrl-rllib-trl-verl-openrl.md`: add a dated release snapshot near the tooling comparison: Gymnasium 1.3.0 (2026-04-22), SB3 2.9.0 (2026-06-15), CleanRL PyPI 1.2.0 (2023-05-22) with GitHub release 1.0.0 (2022-11-14), Ray/RLlib 2.56.1 (2026-07-17), TRL 1.9.0 (2026-07-21), veRL 0.8.0 (2026-06-01), and OpenRLHF 0.10.4 (2026-06-08). Mark all active by release recency except CleanRL as slow.
- `references/topics/024-rl-tooling-landscape-gymnasium-sb3-cleanrl-rllib-trl-verl-openrl.md`: replace the generic TRL sentence in "Treat language-model post-training as a systems workload" with version-pinned taxonomy: TRL 1.9 treats GRPO as online generated-rollout training and DPO as offline preference-pair training. State their respective data contracts: GRPO needs generated completions plus rewards or environments; DPO needs prompt/chosen/rejected records.
- `references/topics/024-rl-tooling-landscape-gymnasium-sb3-cleanrl-rllib-trl-verl-openrl.md`: add an upgrade warning for TRL: v1.0.0 was released 2026-03-31, introduced experimental Async GRPO and VESPO configuration, and v1.9 adds streaming GRPO constraints plus `sigmoid_norm` DPO. Pin a TRL minor version before applying a recipe.
- `references/topics/024-rl-tooling-landscape-gymnasium-sb3-cleanrl-rllib-trl-verl-openrl.md`: change veRL's GitHub reference from `volcengine/verl` to the canonical redirected repository `verl-project/verl`.
- `references/topics/024-rl-tooling-landscape-gymnasium-sb3-cleanrl-rllib-trl-verl-openrl.md`: add `vime` and `Miles` to a clearly labeled 2026 watchlist, not to the core comparison. Their framework and performance descriptions currently rest on maintainer or vendor material only.
- `references/current-requirements.md` Source Log: replace the seven existing tooling rows with the exact dated snapshots in the update list above. For CleanRL, remove the unverified statement that the repository is active at a named push date and replace it with the release-channel divergence and a slow release-activity label.
- `references/current-requirements.md` Deprecations and Migrations: correct the stated TRL v1.0.0 release date from 2026-03-30 to 2026-03-31. Add that current TRL guidance must separate online GRPO from offline DPO, and that streaming GRPO recipes require the v1.9 iterable-dataset constraints.

## Negative results

- Google Open Source announced OpenRL on 2026-06-11 and its repository was fetched, but the announcement explicitly says OpenRL is not an RL framework. It is excluded from candidate ledger entries; sources: https://opensource.googleblog.com/2026/06/introducing-openrl-a-self-hosted-post-training-api-for-fine-tuning-llms.html and https://github.com/gke-labs/open-rl.
- rLLM's official repository documents 2026 work, but its cited framework source is dated 2025 and the attempted official 2026 blog fetch rendered only a loading shell. It is not added without a fetchable dated first-party source; sources: https://github.com/rllm-org/rllm and https://rllm-project.com/post.html?post=rllm_ui.md.
- No PyPI JSON body could be fetched for CleanRL, veRL, or OpenRLHF in this environment despite retries. Their accessible official PyPI project pages supplied the package version and date, but the failed JSON endpoints should be retried in the next refresh.
- No independent benchmark, scalability, stability, or training-quality comparison was sought or found for the candidate frameworks. Maintainer and vendor performance claims are intentionally not promoted to verified comparative guidance.

## Flags for verification

- Verify any vime throughput, reward, or train-inference-alignment statement against an independent reproduction or benchmark before it appears outside a source note. Current evidence is the vLLM project's own announcement: https://vllm-project.github.io/2026/06/09/announcing-vime.html.
- Verify Miles scale, fault-tolerance, low-precision, and model-support claims against an independent source before treating them as operationally established. Current evidence is a PyTorch-hosted vendor article plus the maintainer repository: https://pytorch.org/blog/miles-a-pytorch-native-stack-for-large-scale-llm-rl-post-training/ and https://github.com/radixark/miles.
- Verify CleanRL's present code-maintenance activity independently before saying that the repository is active. The release evidence only supports a slow release-activity classification.
- Verify whether TRL's `sigmoid_norm` DPO setting is fully documented in the version-pinned API reference before including parameter-level recommendations. The current evidence is the 1.9.0 GitHub release note: https://github.com/huggingface/trl/releases.
