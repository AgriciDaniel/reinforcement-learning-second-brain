# Market Research

## Who Needs an RL Brain

- ML engineers doing LLM post-training: the largest and fastest-growing segment. They need current, correct answers about GRPO variants, RLVR, reward hacking, and which framework (TRL vs veRL vs OpenRLHF) fits their scale. Their pain is that the field moves monthly and most written guidance is already stale.
- Robotics and control engineers: need classical and deep RL (PPO, SAC, TD3, offline RL, sim-to-real) with trustworthy library guidance (Gymnasium, SB3, RLlib, Isaac-style simulators). Their pain is that tutorials still target dead APIs (old Gym, old RLlib stack).
- Researchers and graduate students: need canonical theory (Sutton and Barto, Silver lectures) plus an accurate map of the 2025-2026 literature, with provenance so they can cite primary sources rather than blog summaries.
- Students and career-switchers: need a curated path through free resources, plus honest labels about which famous resources are now low-maintenance (Spinning Up, HF Deep RL course) so they do not burn weeks on broken code.
- Secondary: engineering managers and technical writers who need a defensible, source-cited picture of the RL ecosystem for planning and content.

## Existing Resources and Gaps

- OpenAI Spinning Up: still the best-written conceptual introduction, but officially in maintenance mode (README: bug fixes and minor updates only) and the repo's last push was August 2024. Code predates Gymnasium. Gap: no current-ecosystem coverage, no LLM post-training.
- Hugging Face Deep RL Course: broad, practical, free; the course page itself states it is in a low-maintenance state with last major updates around mid-2024. Gap: does not cover the RLVR/GRPO era that now dominates industry demand.
- Awesome lists (for example aikorea/awesome-rl, about 9.9k stars): last pushed May 2023. Link dumps with no provenance, no freshness dates, many dead or stale entries.
- Textbooks: Sutton and Barto (2018) is canonical for foundations and will stay so, but by design says nothing about the 2024-2026 LLM post-training wave.
- Library docs (TRL, veRL, OpenRLHF, RLlib): accurate for their own APIs but siloed; none compares alternatives honestly or tracks the algorithm literature.
- Newsletters and blog surveys (Turing Post, individual practitioner blogs): timely but secondary, uneven quality, and rarely cite primary evidence per claim.

Gaps a curated, source-cited brain fills: (1) fragmentation, one place linking foundations, libraries, and the LLM post-training frontier; (2) stale SOTA claims, explicit retrieval dates and a refresh cadence instead of undated assertions; (3) no provenance, every claim carries a URL and a confidence tag; (4) missing deprecation guidance, explicit Gym-to-Gymnasium, RLlib API-stack, and TRL trainer-churn migration notes that no single existing resource maintains.

## Competing and Adjacent Products

- Direct free competitors: Spinning Up, HF Deep RL course, library documentation, awesome lists. All are either low-maintenance, siloed, or provenance-free; none is refreshed on a stated cadence.
- Nathan Lambert's RLHF Book (rlhfbook.com) and associated writing: the closest adjacent product for the LLM post-training slice; strong on RLHF/RLVR narrative, but it is a book plus blog, not a versioned, source-logged knowledge base, and it does not cover classical RL or robotics (practitioner judgment; maintenance cadence not re-verified this cycle).
- Paid courses and bootcamps (Coursera RL specializations, DeepLearning.AI short courses): structured but slow to update and not citation-driven.
- General AI assistants and LLM chat: the default alternative for most practitioners. Fast but prone to stale or fabricated version claims, which is exactly the failure mode a source-logged brain is built to avoid.
- Internal company wikis at labs: high quality but private; no public equivalent exists.

## Positioning

A source-cited, confidence-tagged, advisory knowledge base for reinforcement learning, refreshed monthly. Differentiators: every claim has a URL, a retrieval date, and an evidence-based or practitioner tag; deprecations and migrations are first-class content, not footnotes; the scope deliberately spans classical RL through LLM post-training, the join that no existing free resource maintains; and it is advisory, it recommends and explains tradeoffs rather than prescribing a single stack. The refresh cadence is itself a stated, auditable commitment, which directly answers the biggest weakness of every incumbent resource: silent staleness.

## Evidence

URLs consulted, all retrieved 2026-07-22:

- https://pypi.org/pypi/gymnasium/json (Gymnasium 1.3.0)
- https://pypi.org/pypi/stable-baselines3/json and https://github.com/DLR-RM/stable-baselines3/releases (SB3 2.9.0)
- https://pypi.org/pypi/trl/json (TRL 0.29.1)
- https://pypi.org/pypi/ray/json and https://docs.ray.io/en/latest/rllib/index.html (Ray 2.56.1, docs at 2.56.0)
- https://pypi.org/pypi/cleanrl/json and https://api.github.com/repos/vwxyzjn/cleanrl (PyPI stale at 1.2.0; repo active, last push 2026-04-20, ~10.1k stars)
- https://pypi.org/pypi/verl/json and https://api.github.com/repos/volcengine/verl (veRL 0.8.0; repo last push 2026-07-22, ~22.6k stars)
- https://pypi.org/pypi/openrlhf/json (OpenRLHF 0.10.4)
- https://github.com/openai/spinningup and https://spinningup.openai.com/en/latest/ (maintenance mode; last push 2024-08-05, ~11.9k stars)
- https://huggingface.co/learn/deep-rl-course/en/unit0/introduction and https://github.com/huggingface/deep-rl-class (low-maintenance state)
- https://api.github.com/repos/aikorea/awesome-rl (last push 2023-05-25, ~9.9k stars)
- https://www.turingpost.com/p/reasoning-rl-in-2026 and https://llm-stats.com/blog/research/post-training-techniques-2026 (2026 post-training practice surveys, secondary)
- https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond (DeepSeek lineage overview, secondary; R2 unreleased as of June 2026 reporting)
- http://incompleteideas.net/book/the-book-2nd.html (Sutton and Barto, canonical, not re-fetched this cycle: practitioner-stable URL)
