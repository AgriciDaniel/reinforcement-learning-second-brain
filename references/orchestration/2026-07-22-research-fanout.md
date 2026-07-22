# Orchestration Run: Research Fan-Out (2026-07-22)

Orchestrator: Claude (Fable 5) in Claude Code. Review policy: no subagent output merged without orchestrator verification.

## Task packets

| Packet | Worker | Scope | Output | Review gate |
|---|---|---|---|---|
| source-ledger | Claude general-purpose (web) | 28-35 verified primary sources | scratchpad source-ledger-candidate.json | URL spot-check, schema validation, date sanity before merge into references/source-ledger.json |
| current-requirements + market-research | Claude general-purpose (web) | verified versions, ecosystem state | scratchpad candidates | placeholder scan, date checks, merge into references/ |
| canon 001-006 | Codex (GPT-5 class) subagent | classic RL foundations | references/canon/001..006 | contract compliance, line floor, wikilink count, quote discipline, fact spot-check |
| canon 007-012 | Codex subagent | policy gradient to exploration | references/canon/007..012 | same |
| canon 013-018 | Codex subagent | offline RL to RLHF | references/canon/013..018 | same |
| canon 019-024 | Codex subagent | preference optimization to tooling | references/canon/019..024 | same |

## Contract

Shared canon note contract: frontmatter preserved, ledger line, Core Thesis, How It Works, Key Principles (confidence-tagged), Best Practices, Primary Sources (real only), Evidence Caveats, Brain Hooks; minimum 80 lines and 8 wikilinks per note; no verbatim quotes unless certain, labeled paraphrase otherwise; no fabricated citations.

## Status log

- 2026-07-22: all six packets dispatched in parallel. Canon writers run as detached Codex background jobs.
- 2026-07-22: requirements and market research reviewed and merged; orchestrator caught and corrected a TRL version error (agent reported 0.29.1, PyPI verified 1.9.0, TRL 1.0.0 shipped 2026-03-30).
- 2026-07-22: source ledger merged, 43 entries, field vocabulary mapped to auditor schema. Research audit: status researched, score 74.
- 2026-07-22: all 24 canon files passed contract checks (line floor, wikilinks, sections, tags, no seeds); all 38 cited arXiv ids verified against known papers. Canon index synced.
- 2026-07-22: canon folded into 24 wiki concept notes via deterministic scripts/fold_canon_to_concepts.py. Vault lint passed.
- 2026-07-22: claim ledger resolved with 8 evidence-backed rows; source ids cross-checked against the ledger. Adapter build dispatched to Codex under contract.
- 2026-07-22: Codex adapter build reviewed and verified end-to-end (import, synthesis, render; 8/8 tests pass; entropy_collapse and kl_spike detected on the collapse fixture; no em dashes, no leaked paths). Audit reached 100 market-ready.
- 2026-07-22: substance gates closed: scripts/render_research_pack.py renders wiki/sources/ research pack (67 URLs) and theme source notes from the ledger; sample-vault sha256 fixture written; changelog dated; third-party notices, plugin allowed-tools, and curator coverage matrices completed.
- 2026-07-22: final state: audit 100 market-ready, coach grade SSS+ score 100, tests 8/8, validation and strict vault lint pass.

## Full review pass (same day, later)

- Incident found and fixed: `scripts/synthesize_brain.py` owns `references/canon/` and regenerated it from the source ledger during the demo/test run, deleting the 24 topic dossiers. All 24 were recovered from Codex session rollouts (22 from Add File patches, 2 reconstructed from Update File context) and now live in generator-safe `references/topics/` with their own `_index.md`. Fold script repointed to `references/topics/`; concepts re-folded; ownership note recorded in the topics index.
- Dead-link scan across all roots: apparent dead targets (Dashboard, Hot, Index, Log, Overview) are case-variant links that Obsidian resolves; canvas and svg targets exist under `_attachments` and `canvases`. No true dead wikilinks in shipped vaults.
- Orphan scan: theme source notes were orphaned; research pack renderer now emits a Theme Notes wikilink section. Wiki orphans now zero.
- Sample-vault sha256 fixture regenerated after the demo rebuild.
- Coverage gap analysis: Claude web analyst delivered a ranked 10-item gap list (essential: agentic multi-turn RL, process reward models, world models, test-time compute and search); Codex second opinion pending.

## Expansion wave (025-034)

- Consensus gap set from two independent reviewers (Claude web analyst, Codex repo reviewer): agentic multi-turn RL, process reward models, world models, test-time compute and search, POMDPs, meta-RL and curricula, safe and constrained RL, distributed RL systems and self-play, sim-to-real robotics, distributional RL. RL theory folded into existing topics rather than added.
- 10 new topic dossiers written by two Codex batches under the shared contract; all passed mechanical contract checks; every new arXiv citation verified against live abs pages (export API was down; five unfamiliar IDs individually confirmed: shielding, risk-constrained RL, sim-to-real loop, unsupervised environment design, asymmetric RL under partial observability).
- Source ledger extended to 70 verified sources (wave 2: 27 entries, POMDP paper on author-hosted canonical URL after ScienceDirect bot block).
- 10 Codex quality findings adjudicated: 8 fixed (claim contradictions, RLVR origin, title truncation bug in safe_note_name, overclaims), 2 declined with rationale (generator-owned canon thinness, separate theory topic).
- Concepts folded, vault index extended, research pack re-rendered (70 sources), demo and sha256 fixture regenerated, variant wikilinks normalized.
- Final state: 34 topics, audit 100 market-ready, coach SSS+ 100, tests 8/8, validation and strict lint pass, zero orphans, zero true dead links.
