"""Render the wiki research pack from the source ledger.

Generates wiki/sources/research-pack-<date>.md plus one source note per
curator theme, all derived deterministically from
references/source-ledger.json and references/claim-ledger.md.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "references" / "source-ledger.json"
CLAIMS = ROOT / "references" / "claim-ledger.md"
OUT_DIR = ROOT / "wiki" / "sources"

THEMES: dict[str, tuple[str, ...]] = {
    "Classic RL Foundations": (
        "sutton", "silver", "cs285", "spinning", "hf-deep-rl", "dqn", "rainbow",
        "policy-gradient", "a3c", "gae", "trpo", "q-learning",
    ),
    "Deep RL Algorithms": (
        "ppo", "ddpg", "td3", "sac", "alphazero", "muzero", "mbpo", "dyna",
        "rnd", "icm", "cql", "bcq", "maddpg", "qmix", "gail", "options",
        "world-model", "dreamer", "genie", "pomdp", "drqn", "meta-rl", "rl2",
        "c51", "qr-dqn", "distributional", "cpo", "safety-gym", "omnisafe",
        "impala", "ape-x", "seed-rl", "domain-random", "sim-to-real",
        "vla", "reality-gap", "kaelbling", "shield", "risk", "robotics",
    ),
    "LLM Post-Training and Preference Optimization": (
        "instructgpt", "dpo", "ipo", "kto", "orpo", "grpo", "deepseek", "rlaif",
        "constitutional", "rlvr", "tulu", "preference", "summarize", "spurious",
        "agentic", "search-r1", "mua-rl", "prm", "process-reward",
        "test-time", "verify-step", "glm", "minimax", "qwen", "rft",
        "introspection", "rubric", "consistrm",
    ),
    "Evaluation and Reproducibility": (
        "matters", "precipice", "rliable", "atari-eval", "reproducib",
        "procgen", "memorization", "contamination",
    ),
    "Tooling and Engineering Practice": (
        "gymnasium", "stable-baselines", "cleanrl", "rllib", "trl", "verl",
        "openrlhf", "reward-hacking", "specification-gaming", "vime", "miles",
        "alignment", "specbench", "ai-control",
    ),
}

RELATED = [
    "[[wiki/sources/_index|Sources Hub]]",
    "[[Source Manifest Guide]]",
    "[[Source Intake Workflow]]",
    "[[Research Refresh Workflow]]",
    "[[Claim Verification Flow]]",
    "[[Best Practices Kernel]]",
    "[[dashboard|Dashboard]]",
    "[[wiki/concepts/_index|Concepts Hub]]",
]


def frontmatter(title: str, date: str) -> str:
    tags = "\n".join(f'  - "{t}"' for t in ("#type/source", "#confidence/evidence-based"))
    related = "\n".join(f'  - "{r}"' for r in RELATED)
    return (
        f'---\ntype: "source"\ntitle: "{title}"\ncreated: "{date}"\n'
        f'updated: "{date}"\nstatus: "active"\ntags:\n{tags}\nrelated:\n{related}\n---\n'
    )


def entry_lines(src: dict) -> list[str]:
    claims = ", ".join(src.get("claims") or []) or "unassigned"
    return [
        f"### {src['title']}",
        "",
        f"- URL: {src['url']}",
        f"- Published: {src['date']} | Retrieved: {src['retrieved']} | Refresh due: {src['refresh_due']}",
        f"- Type: {src['source_type']} | Confidence: {src.get('confidence', 'evidence-based')}",
        f"- Supports claims: {claims}",
        "",
    ]


def theme_of(src: dict) -> str:
    key = (src["id"] + " " + src["title"]).lower()
    for theme, needles in THEMES.items():
        if any(n in key for n in needles):
            return theme
    return "Classic RL Foundations"


def main() -> int:
    parser = argparse.ArgumentParser(description="Render research pack from the source ledger.")
    parser.add_argument("--date", default=None, help="Pack date (defaults to ledger last_research_pass)")
    args = parser.parse_args()

    data = json.loads(LEDGER.read_text())
    sources = data["sources"]
    date = args.date or data.get("last_research_pass") or "undated"
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    by_theme: dict[str, list[dict]] = {t: [] for t in THEMES}
    for src in sources:
        by_theme[theme_of(src)].append(src)

    claim_rows = [
        line for line in CLAIMS.read_text().splitlines()
        if line.startswith("| C") and line.count("|") >= 6
    ]

    pack = [frontmatter(f"Research Pack {date}", date), f"# Research Pack {date}", ""]
    pack += [
        f"Master source pack for the Reinforcement Learning Brain, rendered from "
        f"`references/source-ledger.json` ({len(sources)} sources, research pass {date}). "
        "Every entry carries a publication date, retrieval date, refresh-due date, and claim links. "
        "Regenerate with `python3 scripts/render_research_pack.py` after each research pass.",
        "",
    ]
    pack += ["## Theme Notes", ""]
    for theme in THEMES:
        name = re.sub(r"[^A-Za-z0-9 -]", "", f"{theme} Sources")
        pack += [f"- [[{name}|{theme}]]"]
    pack += [""]
    for theme, entries in by_theme.items():
        pack += [f"## {theme}", ""]
        for src in sorted(entries, key=lambda s: s["id"]):
            pack += entry_lines(src)
    pack += ["## Ecosystem Snapshot", ""]
    pack += [
        "Version and maintenance evidence from `references/current-requirements.md` and "
        "`references/market-research.md`, retrieved on the pack date:",
        "",
    ]
    url_re = re.compile(r"https?://[^\s|)\]]+")
    seen = {s["url"] for s in sources}
    for rel in ("current-requirements.md", "market-research.md"):
        text = (ROOT / "references" / rel).read_text()
        for url in url_re.findall(text):
            url = url.rstrip(".,")
            if url not in seen:
                seen.add(url)
                pack += [f"- {url} (retrieved {date}, see references/{rel})"]
    pack += [""]
    pack += ["## Claim Coverage", ""]
    pack += ["Claims resolved this pass (see `references/claim-ledger.md`):", ""]
    for row in claim_rows:
        cid = row.split("|")[1].strip()
        claim = row.split("|")[3].strip()
        pack += [f"- {cid}: {claim}"]
    pack += ["", "## Related", ""] + [f"- {r}" for r in RELATED] + [""]
    (OUT_DIR / f"research-pack-{date}.md").write_text("\n".join(pack))
    print(f"research-pack-{date}.md: {len(pack)} lines, {len(sources)} sources")

    for theme, entries in by_theme.items():
        title = f"{theme} Sources"
        note = [frontmatter(title, date), f"# {title}", ""]
        note += [
            f"Theme slice of the {date} research pack: {len(entries)} sources supporting the "
            f"{theme.lower()} canon files and concept notes. The master list lives in "
            f"[[research-pack-{date}|Research Pack {date}]].",
            "",
        ]
        for src in sorted(entries, key=lambda s: s["id"]):
            note += entry_lines(src)
        note += ["## Related", ""] + [f"- {r}" for r in RELATED]
        note += [f"- [[research-pack-{date}|Research Pack {date}]]", ""]
        name = re.sub(r"[^A-Za-z0-9 -]", "", title)
        (OUT_DIR / f"{name}.md").write_text("\n".join(note))
        print(f"{name}.md: {len(note)} lines, {len(entries)} sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
