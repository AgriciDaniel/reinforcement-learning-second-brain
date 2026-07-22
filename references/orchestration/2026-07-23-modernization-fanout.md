# Orchestration Run: Fable 5 Modernization and Research Refresh (2026-07-22 to 2026-07-23)

Orchestrator: Claude (Fable 5) in Claude Code. Executors: Codex subagents (gpt-5.6-terra, effort xhigh) through the codex-companion runtime. Review policy: no executor output merged without orchestrator verification; every research candidate spot-checked against live URLs before ledger merge.

## Phase A: repo and harness modernization

| Packet | Executor | Scope | Review gate |
|---|---|---|---|
| domain-fix | Codex A | canonical domain "reinforcement learning" and slug in spec, generator constants, references frontmatter | grep sweeps, compileall, JSON validity |
| template-cleanup | Codex B | truncated tag and {{date}} literals across 87 template files | template lint, grep sweeps, graph.json validity |
| demo-determinism | Codex C | DEMO_DATE pin and normalization in build_demo_vault.py, demo rebuild, sha256 fixture | double-rebuild clean diff, lint |
| skill-agents | Codex D | SKILL.md description, model/tools frontmatter on six agents, hero SVG tagline | YAML/XML validity, audit keyword preservation |
| version-reconcile | Codex E | 1.1.0 across plugin metadata, CI, package, tests, docs; changelog entry | JSON validity, version greps, changelog heading regex |

Orchestrator additions: canon normalization extended in build_demo_vault.py, em-dash PostToolUse hook (scripts/check_no_em_dash.py) with project settings, scripts/stagger_refresh_dates.py for tiered refresh dates.

## Phase B: research refresh (WP1-WP10)

| Packet | Executor | Scope | Output |
|---|---|---|---|
| WP1 libraries | Codex (web) | 7 tooling sources re-verified via PyPI/GitHub; vime and Miles watchlist | .research-candidates/wp1 |
| WP2 RLVR/GRPO | Codex (web) | DAPO, Dr. GRPO, GSPO backfill; Apr-Jul 2026 variant wave | .research-candidates/wp2 |
| WP3 reasoning models | Codex (web) | R2 catalog-absence evidence; GLM-5.1, MiniMax M3, Qwen-AgentWorld; frontier reports | .research-candidates/wp3 |
| WP4 agentic RL | Codex (web) | computer-use, SWE, terminal RL; TRL environment_factory; new topic go/no-go | .research-candidates/wp4 |
| WP5 verifiers/PRMs | Codex (web) | rubric and generative reward models, verifier scaling, multimodal PRM benchmark | .research-candidates/wp5 |
| WP6 world models + TTC | Codex (web) | post-Genie-3, Dreamer-line, TTC follow-ups; URL re-verification | .research-candidates/wp6 |
| WP7 safety/eval | Codex (web) | inoculation-prompting independent evidence, AAAI contamination replication, SpecBench, oversight | .research-candidates/wp7 |
| WP8 VLA + education | Codex (web) | PLD, EXPO-FT, PAIR-VLA, Z-1; CS285, HF course, Spinning Up statuses | .research-candidates/wp8 |
| WP9 merge | Orchestrator | normalize, dedup, curate, append 50 sources; stagger; claim ledger C009-C019 | references/ updates |
| WP10 integration | Codex F + orchestrator | ten dossier patches, topic 035, concept stub, fold, hubs | references/topics, template wiki |

## Shared research contract

Fetch-or-do-not-claim: no version, date, paper, or release enters a candidate file without a live URL fetched during the run; failures recorded honestly. Single-source claims marked; comparative and superiority claims contested pending independent lineages; same-lab pairs count as one lineage. Candidates quarantined in .research-candidates/, never written to references/ by executors.

## Status log

- 2026-07-22: Phase A packets dispatched (A+B parallel, then C+D+E parallel). All five verified by the orchestrator with independent greps, lint, and rebuild checks. Latent day-dependent demo drift bug found and fixed in build_demo_vault.py.
- 2026-07-22: one orphaned Codex job record (first attempt of Codex A) cancelled after verifying its work was completed by the retry; WP5 spawn silently died and was relaunched successfully.
- 2026-07-22: eight research packets dispatched as parallel Codex background jobs with live web access.
- 2026-07-23: all eight candidate files reviewed. Schema violations caught and normalized at merge: invalid source_type values (primary-research, official-doc, official-lab-publication), sentence-form claims, pre-assigned claim numbers, inconsistent confidence vocabulary.
- 2026-07-23: orchestrator spot-checked eight load-bearing URLs (arXiv 2607.00152, 2604.25891, 2606.24515, 2602.08346, 2606.31846, 2507.17746, AAAI 40687, Qwen-AgentWorld model card): eight of eight exact matches.
- 2026-07-23: curation: 50 candidates accepted, Tom's Hardware R2 rumor rejected as a ledger source (claim recorded against the DeepSeek Transparency Center catalog instead); RaR promoted to a full entry to repair a dangling reference.
- 2026-07-23: ledger merged append-only to 120 sources; refresh dates staggered into tiers T1-T5 (next window opens 2026-08-21, no cliff); verl-docs and genie-3 URLs updated to canonical redirect targets; one source id renamed (grpo-credit-assignment-foundations-2026) to fix research-pack theme routing.
- 2026-07-23: claim ledger extended to C019; C006 upgraded (independent AAAI 2026 replication), C007 split-revised (mitigation clause multi-lineage, production-RL clause still single-lineage). current-requirements.md corrected (TRL 1.0.0 date 2026-03-31, veRL org move, R2 catalog wording) and extended.
- 2026-07-23: research pack rendered at 120 sources; theme needles extended; dossier integration dispatched to Codex F.
- 2026-07-23: raw candidate files archived as provenance under references/orchestration/candidates-2026-07/ (the quarantine directory .research-candidates/ is removed before packaging).
