# Product Boundaries

Reinforcement Learning Brain is an advisory, read-only Obsidian brain for reinforcement learning, covering fundamentals, deep RL, RLHF/RLAIF and preference optimization, evaluation, tooling, and applied best practices.

## It Does

- Preserve raw sources under `.raw/`.
- Synthesize source-cited notes and deliverables.
- Maintain action queues, reports, and next actions.
- Keep decisions auditable through source links and rollback notes.
- Gate maturity through `references/source-ledger.json`,
  `references/adapter-manifest.json`, and `scripts/audit_brain.py`.

## It Does Not

- No unsourced claims about algorithm performance, benchmarks, or state of the art
- No credentials, tokens, API keys, or private training data in repo artifacts
- No claims of a universal best algorithm; recommendations must state task assumptions
- No presenting contested or folklore practices as evidence-based without labeling

## Safety Risks

- Stale state-of-the-art claims in a fast-moving field
- Reward hacking and specification gaming presented without caveats
- Overconfident synthesis from single papers or unreproduced results
- Benchmark numbers quoted without seed variance and evaluation-protocol context

## Maturity Boundary

This repo starts as `scaffolded`. Market-ready quality requires current
research, domain adapters, deterministic demo verification, source citations,
Obsidian graph hygiene, and release scans. The audit score is capped below 90
until those stages are complete.
