"""Fold canon evidence files into wiki concept notes.

Reads each references/topics/NNN-*.md file, extracts its sourced sections,
and rewrites the matching assets/template-brain/wiki/concepts/<fold>.md
note so the vault carries canon substance instead of seed language.
Deterministic: content comes only from canon files, never generated.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANON = ROOT / "references" / "topics"
CONCEPTS = ROOT / "assets" / "template-brain" / "wiki" / "concepts"

SECTION_RE = re.compile(r"^## (.+?)\n(.*?)(?=^## |\Z)", re.M | re.S)
LEDGER_RE = re.compile(
    r"Ledger: (\d+) \| target: (.+?) \| confidence: ([a-z-]+) \| fold: \[\[(.+?)\]\]"
)
URL_RE = re.compile(r"https?://[^\s)\]]+")


def norm(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", name.lower())


def concept_path(fold: str) -> Path | None:
    index = {norm(p.stem): p for p in CONCEPTS.glob("*.md") if p.stem != "_index"}
    return index.get(norm(fold))


def fold_one(canon_file: Path) -> str:
    text = canon_file.read_text()
    ledger = LEDGER_RE.search(text)
    if not ledger:
        return f"SKIP {canon_file.name}: no ledger line"
    num, _target, confidence, fold = ledger.groups()
    sections = {title.strip(): body.strip() for title, body in SECTION_RE.findall(text)}
    required = ["Core Thesis", "Key Principles", "Best Practices", "Primary Sources", "Evidence Caveats"]
    missing = [s for s in required if s not in sections]
    if missing:
        return f"SKIP {canon_file.name}: missing sections {missing}"

    target = concept_path(fold)
    if target is None:
        return f"SKIP {canon_file.name}: no concept note for fold '{fold}'"

    old = target.read_text()
    fm_match = re.match(r"^---\n(.*?)\n---\n", old, re.S)
    if not fm_match:
        return f"SKIP {canon_file.name}: concept note has no frontmatter"
    fm = fm_match.group(1)
    fm = re.sub(r'^status: ".*?"', 'status: "active"', fm, flags=re.M)
    fm = re.sub(r'^confidence: ".*?"', f'confidence: "{confidence}"', fm, flags=re.M)
    fm = re.sub(r'#confidence/[a-z-]+', f"#confidence/{confidence}", fm)
    urls = URL_RE.findall(sections["Primary Sources"])
    url_block = "source_urls:\n" + "".join(f'  - "{u}"\n' for u in urls) if urls else "source_urls: []\n"
    fm = re.sub(r"^source_urls: \[\]$", url_block.rstrip("\n"), fm, flags=re.M)

    body = f"""# {fold}

Confidence tag: {confidence}. Folded from canon `{canon_file.name}` on the date in `updated`.

## Sourced Takeaways

{sections["Core Thesis"]}

{sections["Key Principles"]}

## Best Practices

{sections["Best Practices"]}

## Evidence Caveats

{sections["Evidence Caveats"]}

## Sources

- Canon evidence file: `references/topics/{canon_file.name}`
{sections["Primary Sources"]}
- [[Source Manifest Guide]]
- [[Claim Verification Flow]]

## Related

- [[wiki/concepts/_index|Concepts Hub]]
- [[Best Practices Kernel]]
- [[Source Intake Workflow]]
- [[Research Refresh Workflow]]
- [[Claim Verification Flow]]
- [[Dashboard]]
"""
    target.write_text(f"---\n{fm}\n---\n\n{body}")
    return f"FOLDED {num} -> {target.name} ({confidence}, {len(urls)} urls)"


def main() -> int:
    results = [fold_one(f) for f in sorted(CANON.glob("0*.md"))]
    for line in results:
        print(line)
    skipped = [r for r in results if r.startswith("SKIP")]
    return 1 if skipped else 0


if __name__ == "__main__":
    sys.exit(main())
