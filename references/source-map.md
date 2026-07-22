# Source Map

## Raw Sources

- Papers (arXiv PDFs), official library docs, course notes, experiment logs, training configs, and TensorBoard/W&B exports supplied by the operator

## Enrichment Sources

- Sutton & Barto, Reinforcement Learning: An Introduction (2nd ed.)
- OpenAI Spinning Up in Deep RL
- Hugging Face Deep RL Course and TRL documentation
- Original algorithm papers: DQN, PPO, SAC, TD3, A3C, AlphaZero, MuZero, InstructGPT, DPO, GRPO
- Official library documentation: Gymnasium, Stable-Baselines3, RLlib, CleanRL, TRL, veRL/OpenRLHF
- Anthropic, OpenAI, and DeepMind research publications on RLHF, RLAIF, and Constitutional AI

## Import Strategy

- Copy raw source files into `.raw/sources/`.
- Record path, hash, retrieval date, owner, and source type.
- Record external research sources in `references/source-ledger.json`.
- Record implemented schemas and adapters in `references/adapter-manifest.json`.
- Create a source note under `wiki/sources/`.
- Link affected entities, workflows, and deliverables.
