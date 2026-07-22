# Current Requirements

## Refresh Cadence

Monthly for fast-moving sources: LLM post-training practice (GRPO variants, RLVR results, new open reasoning models) and library releases (TRL, veRL, OpenRLHF, Ray). Before every release of this brain, re-verify all canonical claims (versions, maintenance statuses, URLs) against primary sources, even if the monthly pass already ran.

## Required Source Standard

Every factual claim in this brain must trace to a primary source: PyPI or GitHub releases for versions, official documentation for API behavior, arXiv or publisher pages for papers, and the maintainer's own repository or site for maintenance status. Secondary sources (blog posts, newsletters, surveys) may be cited only as practitioner context and must be tagged as such. Each source carries a retrieval date and a confidence tag: evidence-based (verified against a primary source on the retrieval date) or practitioner (informed judgment or secondary reporting, to be upgraded or removed at next refresh). Claims that cannot be re-verified at refresh time are demoted or deleted, never silently kept.

## Source Log

| Source | URL | Retrieved | Version | Confidence | Notes |
|---|---|---|---|---|---|
| Gymnasium (PyPI) | https://pypi.org/project/gymnasium/ | 2026-07-22 | 1.3.0 | evidence-based | Uploaded 2026-04-22. Requires Python 3.10+. Canonical environment API, successor to OpenAI Gym. |
| Stable-Baselines3 (PyPI/GitHub) | https://github.com/DLR-RM/stable-baselines3/releases | 2026-07-22 | 2.9.0 | evidence-based | Latest stable on PyPI and GitHub releases. PyTorch implementations of classic deep RL algorithms. |
| TRL (PyPI) | https://pypi.org/project/trl/ | 2026-07-22 | 1.9.0 | evidence-based | Uploaded 2026-07-21. TRL 1.0.0 shipped 2026-03-30. Hugging Face library for LLM post-training (SFT, DPO, GRPO, RLOO, Online DPO trainers; PPO marked experimental in 1.0). |
| Ray / RLlib (PyPI, docs) | https://docs.ray.io/en/latest/rllib/index.html | 2026-07-22 | 2.56.1 | evidence-based | PyPI latest 2.56.1; docs current at 2.56.0. RLlib ships inside Ray, no separate versioning. |
| CleanRL (PyPI) | https://pypi.org/project/cleanrl/ | 2026-07-22 | 1.2.0 | evidence-based | PyPI package stale (uploaded 2023-05-22), but the GitHub repo is active: last push 2026-04-20, about 10.1k stars. Use the repo, not the PyPI package. |
| veRL (PyPI/GitHub) | https://github.com/volcengine/verl | 2026-07-22 | 0.8.0 | evidence-based | PyPI 0.8.0 uploaded 2026-06-01. Repo very active (last push 2026-07-22, about 22.6k stars). ByteDance/Volcano Engine RL post-training framework (HybridFlow). |
| OpenRLHF (PyPI) | https://pypi.org/project/openrlhf/ | 2026-07-22 | 0.10.4 | evidence-based | Uploaded 2026-06-08. Release notes highlight multi-turn VLM RL. Ray plus vLLM based RLHF framework. |
| Sutton and Barto, Reinforcement Learning: An Introduction (2nd ed.) | http://incompleteideas.net/book/the-book-2nd.html | 2026-07-22 | 2nd edition (2018) | evidence-based | Canonical textbook, free official HTML/PDF from the authors. Stable URL, unchanged content. |
| OpenAI Spinning Up in Deep RL | https://spinningup.openai.com/en/latest/ | 2026-07-22 | n/a | evidence-based | Repo README declares maintenance mode (bug fixes only). Last push to openai/spinningup was 2024-08-05, about 11.9k stars. Still valuable for theory, code predates Gymnasium. |
| Hugging Face Deep RL Course | https://huggingface.co/learn/deep-rl-course/en/unit0/introduction | 2026-07-22 | n/a | evidence-based | Course page states it is in a low-maintenance state; last major content updates mid-2024. Exercises use SB3, CleanRL, Sample Factory. |
| DeepMind x UCL RL Lecture Series (David Silver lineage) | https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021 | 2026-07-22 | 2021 series | practitioner | Canonical free video course for classical RL theory. URL stability not re-verified this cycle, confirm before release. |
| DeepSeek-R1 paper | https://arxiv.org/abs/2501.12948 | 2026-07-22 | R1 (Jan 2025) | evidence-based | Catalyst for mass adoption of the RLVR plus GRPO reasoning recipe; GRPO itself originates in DeepSeekMath (2024) and the RLVR framing predates R1 (Tulu 3, 2024). Later published in Nature (Sept 2025). As of June 2026 reporting, no official R2 release; treat R2 claims as rumor. |
| DAPO paper (GRPO variant) | https://arxiv.org/abs/2503.14476 | 2026-07-22 | DAPO (2025) | evidence-based | Decoupled clip and dynamic sampling; mitigates entropy collapse in long chain-of-thought RL in the reported setting. One of the main GRPO refinements alongside Dr. GRPO and GSPO (GSPO is sequence-level, from the Qwen team). |
| Post-training practice surveys 2025-2026 | https://www.turingpost.com/p/reasoning-rl-in-2026 | 2026-07-22 | n/a | practitioner | Secondary survey. Consensus picture: RLVR is the dominant paradigm for reasoning models; GRPO-family critic-free methods dominate open-source post-training; agentic and multi-turn RL is the active frontier. |

## Deprecations and Migrations

- OpenAI Gym to Gymnasium: `gym` is unmaintained; Gymnasium (Farama Foundation) is the maintained successor and the environment API targeted by the mainstream open-source RL libraries tracked here (SB3, CleanRL, RLlib). Gymnasium 1.x changed the vector environment API and the plugin/registration system relative to 0.29, so pre-1.0 tutorials need adaptation. Current stable is 1.3.0.
- TRL trainer churn: TRL added `GRPOTrainer` in v0.14 (January 2025), shipped v1.0.0 on 2026-03-30, and is at 1.9.0 as of 2026-07-21. The 1.0 taxonomy stabilizes GRPO (with multi-environment agentic RL), RLOO, Online DPO, Nash-MD, XPO, and KTO, while PPO is marked experimental. Legacy trainer APIs from 0.x era tutorials no longer match 1.x. Pin the TRL version in any recipe and re-check trainer signatures each monthly refresh.
- RLlib API stacks: RLlib's new API stack (RLModule, ConnectorV2) is the default; the old ModelV2/Policy stack is deprecated. Any RLlib guidance must state which stack it targets. Ray also deprecated Pydantic v1 support around 2.56.
- CleanRL via PyPI: do not install CleanRL from PyPI (frozen at 1.2.0, 2023); clone the repository, which is the actual maintained artifact.
- Spinning Up code: educational text remains sound, but the code targets old Gym and TensorFlow/older PyTorch; treat it as theory reference, not runnable baseline.

## Fast-Moving Areas

- LLM post-training algorithms: GRPO variants (DAPO, Dr. GRPO, GSPO, agentic policy optimization) iterate monthly; any "current best practice" claim expires fast.
- RLVR scope: what counts as a verifiable reward (unit tests, checkers, rubric-based verifiers) keeps expanding; re-verify claims about where RLVR does and does not work.
- Open reasoning model releases: DeepSeek lineage (R2 still unreleased as of this retrieval), Qwen, Kimi, and Llama-family reasoning models change the reference implementations people copy.
- Framework versions: veRL, OpenRLHF, and TRL each release multiple times per quarter; version-pinned recipes go stale within one to two months.
- Ray/RLlib: fast release train (roughly monthly minors); API-stack migration details shift between releases.
- Maintenance statuses: Spinning Up and the HF Deep RL course are both in low-maintenance mode; re-check whether either is revived, archived, or superseded.
