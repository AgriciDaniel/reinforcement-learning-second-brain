---
name: reinforcement-learning-brain
description: >-
  Scaffold and operate Reinforcement Learning Brain, a source-cited Obsidian brain for
  reinforcement learning, covering fundamentals, deep RL, RLHF/RLAIF and preference
  optimization, evaluation, tooling, and applied best practices.
  Use when the user says "reinforcement-learning-brain", "Reinforcement Learning Brain", "create a reinforcement learning brain",
  "import sources", "synthesize plan", "render report", or wants a persistent vault-backed
  operating system for reinforcement learning work.
argument-hint: "new | ingest | synthesize | report | visuals | lint | next"
license: Custom license
---

# Reinforcement Learning Brain

Operate the deployed vault first. Treat `CODEX.md`, `wiki/hot.md`, and
`wiki/index.md` as vault-root-relative paths, where the vault root is the
directory passed to `--vault` or opened in Obsidian. In this repo, the template
vault root is `assets/template-brain/` and the demo vault root is
`examples/sample-vault/`.

Secretary: use `agents/reinforcement-learning-secretary.md` for grounded answers, claim review,
and vault maintenance. That secretary reads the brain first, cites a vault note
and an official URL, and stays advisory and read-only.

## Commands

```bash
/reinforcement-learning-brain new <client-slug> --owner <name>
/reinforcement-learning-brain ingest --vault <path> --file <source>
/reinforcement-learning-brain synthesize --vault <path>
/reinforcement-learning-brain report --vault <path>
/reinforcement-learning-brain visuals --vault <path>
/reinforcement-learning-brain lint --vault <path>
/reinforcement-learning-brain next --vault <path>
```

Source checkout equivalent:

```bash
reinforcement-learning-brain new <client-slug> --owner <name>
reinforcement-learning-brain ingest --vault <path> --file <source>
reinforcement-learning-brain synthesize --vault <path>
reinforcement-learning-brain report --vault <path> --html-only
```

## Required Operating Rules

1. Read `<vault>/CODEX.md`.
2. Read `<vault>/wiki/hot.md`.
3. Read `<vault>/wiki/index.md`.
4. Preserve `.raw/` as immutable source material.
5. Never store credentials in the vault.
6. Never make domain-specific claims without dated trustworthy sources.
7. Keep `hot`, `index`, `overview`, and `log` current.
8. Record research evidence in `references/source-ledger.json`.
9. Record domain adapter completion in `references/adapter-manifest.json`.

## Script Mapping

- `new` -> `python scripts/scaffold_vault.py`
- `ingest` -> `python scripts/ingest_source.py`
- `synthesize` -> `python scripts/synthesize_brain.py`
- `report` -> `python scripts/render_brain_report.py`
- `visuals` -> `python scripts/generate_vault_visuals.py`
- `lint` -> `python scripts/lint_vault.py`
- `next` -> `python scripts/guide_next_action.py`

## Quality Gates

- No unsourced claims about algorithm performance, benchmarks, or state of the art
- No credentials, tokens, API keys, or private training data in repo artifacts
- No claims of a universal best algorithm; recommendations must state task assumptions
- No presenting contested or folklore practices as evidence-based without labeling

Do not call this brain market-ready unless `scripts/audit_brain.py --require
market-ready` passes. A scaffold is not a finished brain.

## Research Refresh

monthly for fast-moving sources (LLM post-training, libraries); before every release for canonical claims
