## Verified findings

Repo audit: topic 025 currently centers Search-R1's retrieval trajectory, MUA-RL's simulated-user loop, and the 2025 landscape survey. The live landscape survey is now at arXiv v5, revised 2026-04-17. Its scope is broad, so it does not replace a task- and environment-specific dossier. [agentic-landscape-survey-v5-2026]

Three independently authored Apr-Jul 2026 primary papers make a focused computer-use and tool-use topic evidence-backed: autonomous terminal evaluation for GUI agents, learned context compaction for SWE and terminal agents, and reward-swap optimization for stateful multi-turn agents. Their reported gains are paper- and benchmark-specific, not cross-paper evidence of a general best method. [agentic-cua-autonomous-evaluation-2026; agentic-compactionrl-swe-terminal-2026; agentic-rspo-multiturn-2026]

TRL v1.6.0 documents stateful environment training through `environment_factory`: its GRPO trainer performs the multi-turn tool-call loop and its documented meta-environment pattern routes one training run across Wordle and Catch. This is concrete trainer capability, not an empirical claim that multi-environment training improves every agent. [agentic-trl-openenv-multienv-grpo-2026]

veRL's live Agentic RL document confirms asynchronous rollouts, multi-turn conversations and tool calls, and a LangGraph-based agent, but the document itself says it was last updated 2025-07-15. It is verified baseline support, not an Apr-Jul 2026 development or a go signal. URL fetched: https://github.com/verl-project/verl/blob/main/docs/start/agentic_rl.rst

The April 2026 review and the April 2026 revision of the landscape survey are useful taxonomy checks, but neither supplies independent validation of the new papers' results. [agentic-rl-review-2026; agentic-landscape-survey-v5-2026]

## Candidate ledger entries

```json
[
  {
    "id": "agentic-cua-autonomous-evaluation-2026",
    "title": "Reinforcement Learning for Computer-Use Agents with Autonomous Evaluation",
    "url": "https://arxiv.org/abs/2606.24515",
    "source_type": "primary-research",
    "date": "2026-06-23",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "c201-cua-autonomous-terminal-evaluation"
    ],
    "supports_claims": [
      "c201-cua-autonomous-terminal-evaluation"
    ]
  },
  {
    "id": "agentic-compactionrl-swe-terminal-2026",
    "title": "CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents",
    "url": "https://arxiv.org/abs/2607.05378",
    "source_type": "primary-research",
    "date": "2026-07-06",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "c202-long-horizon-swe-terminal-context-compaction"
    ],
    "supports_claims": [
      "c202-long-horizon-swe-terminal-context-compaction"
    ]
  },
  {
    "id": "agentic-rspo-multiturn-2026",
    "title": "RSPO: Reward-Swap Policy Optimization for Multi-Turn LLM Agents",
    "url": "https://arxiv.org/abs/2607.04713",
    "source_type": "primary-research",
    "date": "2026-07-06",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "c203-multiturn-process-outcome-reward-swap"
    ],
    "supports_claims": [
      "c203-multiturn-process-outcome-reward-swap"
    ]
  },
  {
    "id": "agentic-trl-openenv-multienv-grpo-2026",
    "title": "TRL v1.6.0 OpenEnv Integration for Training LLMs with Environments",
    "url": "https://huggingface.co/docs/trl/v1.6.0/en/openenv",
    "source_type": "official-doc",
    "date": "2026-06-11",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "evidence-based",
    "claims": [
      "c204-trl-stateful-multiturn-and-multienvironment-grpo"
    ],
    "supports_claims": [
      "c204-trl-stateful-multiturn-and-multienvironment-grpo"
    ]
  },
  {
    "id": "agentic-rl-review-2026",
    "title": "Rethinking Agentic Reinforcement Learning In Large Language Models",
    "url": "https://arxiv.org/abs/2604.27859",
    "source_type": "primary-research",
    "date": "2026-04-30",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "practitioner",
    "claims": [
      "c205-agentic-rl-review-scope-check"
    ],
    "supports_claims": [
      "c205-agentic-rl-review-scope-check"
    ]
  },
  {
    "id": "agentic-landscape-survey-v5-2026",
    "title": "The Landscape of Agentic Reinforcement Learning for LLMs: A Survey, arXiv v5",
    "url": "https://arxiv.org/abs/2509.02547",
    "source_type": "primary-research",
    "date": "2026-04-17",
    "retrieved": "2026-07-22",
    "last_verified": "2026-07-22",
    "confidence": "practitioner",
    "claims": [
      "c206-agentic-rl-landscape-survey-refresh"
    ],
    "supports_claims": [
      "c206-agentic-rl-landscape-survey-refresh"
    ]
  }
]
```

## Claim rows

| C??? | claim | source ids | verdict |
|---|---|---|---|
| C201 | The CUA paper uses a vision-language evaluator on the final screenshot and instruction as a noisy terminal reward, with a correction for evaluator noise; it reports results in macOSWorld, Windows Agent Arena, and OSWorld. | agentic-cua-autonomous-evaluation-2026 | SUPPORTED, SINGLE-SOURCE, paper-reported |
| C202 | CompactionRL jointly optimizes task execution and summary generation for long trajectories and reports SWE-bench Verified and Terminal-Bench 2.0 results. | agentic-compactionrl-swe-terminal-2026 | SUPPORTED, SINGLE-SOURCE, paper-reported |
| C203 | RSPO is presented as a way to use dense process-reward information while retaining an outcome-reward objective, with experiments on WebShop and ALFWorld. | agentic-rspo-multiturn-2026 | SUPPORTED, SINGLE-SOURCE, paper-reported |
| C204 | TRL v1.6.0 documents stateful multi-turn environment training through `environment_factory` and a multi-environment GRPO pattern that routes dataset rows to a selected environment. | agentic-trl-openenv-multienv-grpo-2026 | SUPPORTED AS OFFICIAL IMPLEMENTATION DOCUMENTATION |
| C205 | The April 2026 review frames agentic RL around multi-step decision making and identifies design and evaluation challenges; it is a scope reference, not comparative empirical evidence. | agentic-rl-review-2026 | SUPPORTED AS SCOPE MAP, SINGLE-SOURCE |
| C206 | The existing landscape survey's live arXiv record was revised on 2026-04-17 and describes a compendium of agentic environments, benchmarks, and frameworks. | agentic-landscape-survey-v5-2026 | SUPPORTED AS SURVEY UPDATE, SINGLE-SOURCE |

## Topic patch notes

- Keep `references/topics/025-agentic-multi-turn-rl-for-llm-agents.md` as the abstraction dossier for POMDP framing, action and token boundaries, trajectory masking, dynamic users, and rollout staleness.
- Correct its landscape-survey freshness note to arXiv v5, revised 2026-04-17. [agentic-landscape-survey-v5-2026]
- Add a scope boundary that computer-use, browser, terminal, and SWE environments are concrete task domains with distinct action spaces, side effects, success checkers, and reset semantics. Link to the proposed new dossier rather than expanding 025 into a task-suite catalogue. [agentic-cua-autonomous-evaluation-2026; agentic-compactionrl-swe-terminal-2026; agentic-trl-openenv-multienv-grpo-2026]
- Retain Search-R1 and MUA-RL as the existing retrieval and simulated-user anchors. A live fetch reconfirmed Search-R1's multi-turn retrieval and retrieved-token masking, and MUA-RL's simulated-user training loop. Do not label the 2026 candidates as direct lineage successors without an explicit author claim. URLs fetched: https://arxiv.org/abs/2503.09516 and https://arxiv.org/abs/2508.18669
- Add a cross-link for reward design: RSPO is an example of the dense-process versus outcome-reward tension, not a settled solution to reward alignment. [agentic-rspo-multiturn-2026]
- Add a tooling cross-link for TRL's stateful `environment_factory`, multi-turn tool-call orchestration, and multi-environment pattern. Keep this as versioned implementation documentation, not a capability comparison with veRL. [agentic-trl-openenv-multienv-grpo-2026]
- Do not transfer any paper-reported benchmark number across OSWorld, SWE-bench, Terminal-Bench, WebShop, or ALFWorld. Record the harness, action interface, verifier, budget, and version with every future comparison. [agentic-cua-autonomous-evaluation-2026; agentic-compactionrl-swe-terminal-2026; agentic-rspo-multiturn-2026]

## New topic recommendation

GO. A new dossier, **RL for computer-use and tool-use agents**, is warranted. The threshold is exceeded by three fetched Apr-Jul 2026 primary sources that cover distinct training settings: GUI computer use, SWE and terminal agents, and stateful tool-use agents. [agentic-cua-autonomous-evaluation-2026; agentic-compactionrl-swe-terminal-2026; agentic-rspo-multiturn-2026]

Proposed 8-point outline:

- Scope, non-goals, and relationship to topic 025
- Agent-environment contracts for GUI, browser, terminal, SWE, and API tool actions
- Episode state, memory, context windows, and learnable context compaction
- Reward and verifier taxonomy: executable tests, final-state checks, vision-language judges, process signals, and outcome rewards
- RL objectives and credit assignment across turns, including the process-versus-outcome tension
- Environment suites and training infrastructure: reset isolation, sandboxing, side effects, timeouts, tracing, and multi-environment routing
- Framework implementation patterns: TRL `environment_factory`, GRPO rollout limits, and version-pinned agent loops
- Evaluation protocol and safety: held-out tasks, independent verifiers, cost and latency, action validity, side-effect audit, and non-comparable benchmark caveats

## Negative results

- No fetched Apr-Jul 2026 primary source was found that explicitly presents itself as a direct successor to MUA-RL's simulated-user loop. Do not claim a direct successor relationship from topical similarity alone.
- veRL's official Agentic RL page fetched successfully, but its declared last-update date is 2025-07-15. It was excluded from the six 2026 candidate entries despite confirming existing multi-turn trainer support.
- ProRL Agent and RLAnything appeared in discovery results but have March and February 2026 submission dates, respectively, so they were excluded from this Apr-Jul candidate set.
- No fetch failed for the six ledger entries. The candidate papers are still preprints or reviews unless their source record states otherwise.

## Flags for verification

- Treat C201 through C203 as single-source, paper-reported evidence until an independent reproduction or a matched second primary source is logged.
- Before a source-ledger promotion, fetch and record each paper's code or artifact URL, pinned commit, model checkpoint, harness version, sampling budget, timeout policy, and evaluator configuration.
- The CUA paper's evaluator is explicitly modeled as noisy. A future dossier must distinguish evaluator agreement from task completion and track false positive and false negative error by environment. [agentic-cua-autonomous-evaluation-2026]
- The TRL capability claim is version-specific to v1.6.0. Re-check the official documentation and release notes before adopting it, because a later release may alter the environment contract. [agentic-trl-openenv-multienv-grpo-2026]
- veRL needs a release-tag or commit-level verification before it is used as an implementation recommendation, because its fetched Agentic RL guide predates this survey window.
