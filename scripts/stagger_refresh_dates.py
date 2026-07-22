#!/usr/bin/env python3
"""Stagger source-ledger refresh_due dates by volatility tier.

Replaces the single refresh cliff (every source due on the same day) with a
rolling window: each source gets refresh_due = last_verified + tier cadence
+ a deterministic per-tier offset (index within tier, mod 14 days), so at
most a handful of sources come due on any given day.

Tiers:
  T1 30d  live library and framework docs
  T2 90d  churn-prone official pages, vendor blogs, frontier lab reports
  T3 180d fast-moving primary papers (2024 and newer)
  T4 365d settled primary papers and older vendor pages
  T5 365d canonical statics (books, classic courses, pre-2000 papers)

Usage: python3 scripts/stagger_refresh_dates.py [--ledger PATH] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
from datetime import date, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LEDGER = REPO / "references" / "source-ledger.json"

T1_IDS = {
    "gymnasium-docs",
    "stable-baselines3-docs",
    "cleanrl-docs",
    "rllib-docs",
    "trl-docs",
    "verl-docs",
    "openrlhf-repo",
}
T2_IDS = {
    "berkeley-cs285",
    "hf-deep-rl-course",
    "openai-spinning-up",
    "genie-3-blog-2025",
    "anthropic-reward-hacking-misalignment-2025",
}
T5_IDS = {
    "sutton-barto-rl-book-2e",
    "david-silver-ucl-rl-course",
    "kaelbling-pomdp-1998",
    "policy-gradient-theorem-1999",
}
TIER_DAYS = {"T1": 30, "T2": 90, "T3": 180, "T4": 365, "T5": 365}
OFFSET_SPREAD = 14

CADENCE_NOTE = (
    "tiered: 30d live library docs, 90d churn-prone official and vendor"
    " pages, 180d fast-moving primary papers (2024+), 365d settled and"
    " canonical sources; due dates staggered inside each tier"
)


def tier_for(source: dict) -> str:
    sid = source.get("id", "")
    if sid in T1_IDS:
        return "T1"
    if sid in T2_IDS:
        return "T2"
    if sid in T5_IDS:
        return "T5"
    pub = str(source.get("date", "") or "1900-01-01")
    if source.get("source_type") == "vendor" and pub >= "2025-01-01":
        return "T2"
    if pub >= "2024-01-01":
        return "T3"
    return "T4"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=LEDGER)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    data = json.loads(args.ledger.read_text(encoding="utf-8"))
    sources = data["sources"]

    tiers: dict[str, list[dict]] = {}
    for source in sources:
        tiers.setdefault(tier_for(source), []).append(source)

    for tier, members in sorted(tiers.items()):
        members_sorted = sorted(members, key=lambda s: s.get("id", ""))
        for index, source in enumerate(members_sorted):
            base_str = source.get("last_verified") or source.get("retrieved")
            base = date.fromisoformat(base_str)
            offset = index % OFFSET_SPREAD
            due = base + timedelta(days=TIER_DAYS[tier] + offset)
            source["refresh_due"] = due.isoformat()

    data["refresh_cadence"] = CADENCE_NOTE

    if args.dry_run:
        for tier, members in sorted(tiers.items()):
            ids = sorted(s.get("id", "") for s in members)
            dues = sorted(s["refresh_due"] for s in members)
            print(f"{tier}: {len(ids)} sources, due {dues[0]} .. {dues[-1]}")
        return 0

    args.ledger.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Staggered refresh_due for {len(sources)} sources in {args.ledger}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
