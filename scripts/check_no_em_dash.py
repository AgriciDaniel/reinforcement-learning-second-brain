#!/usr/bin/env python3
"""PostToolUse hook: block em dashes in markdown files edited by agents.

House style for this brain forbids em dashes in all content. Exit code 2
surfaces the violation to the editing agent so it corrects the file.
"""
from __future__ import annotations

import json
import sys

EM_DASH = "—"


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    tool_input = payload.get("tool_input", {})
    path = tool_input.get("file_path", "")
    if not path.endswith(".md"):
        return 0
    try:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
    except OSError:
        return 0
    if EM_DASH not in text:
        return 0
    lines = [str(i + 1) for i, line in enumerate(text.splitlines()) if EM_DASH in line]
    shown = ", ".join(lines[:5])
    print(
        f"Em dash found in {path} at line(s) {shown}. House style forbids em"
        " dashes; use a comma, colon, parentheses, or a conjunction instead.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
