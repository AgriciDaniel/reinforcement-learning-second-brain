#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any

try:
    from import_training_run import InputError as RunInputError
    from import_training_run import validate_run
except ModuleNotFoundError:
    from scripts.import_training_run import InputError as RunInputError
    from scripts.import_training_run import validate_run


MAX_BYTES = 10 * 1024 * 1024
SEVERITIES = ("critical", "warn", "info")
CONFIDENCE_TAGS = {"practitioner", "evidence-based"}
FINDING_KEYS = {"id", "severity", "metric", "evidence", "explanation", "confidence", "canon_ref"}
WINDOWS_ABSOLUTE = re.compile(r"^[A-Za-z]:[\\/]")
WINDOWS_ABSOLUTE_ANYWHERE = re.compile(r"(^|[^A-Za-z0-9])[A-Za-z]:[\\/]")
POSIX_ABSOLUTE_ANYWHERE = re.compile(r"(^|[\s=:'\"`(\[{,;])/(?!/)")
UNC_ABSOLUTE_ANYWHERE = re.compile(r"(^|[\s=:'\"`(\[{,;])(?:\\\\|//)[^/\\\s]")
URL = re.compile(r"\b[A-Za-z][A-Za-z0-9+.-]*://[^\s`<>()\[\]{}]+")


class RenderError(ValueError):
    pass


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render an RL training-run findings report.")
    parser.add_argument("--findings", required=True)
    parser.add_argument("--run", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    try:
        findings_path = Path(args.findings).expanduser().resolve()
        run_path = Path(args.run).expanduser().resolve()
        out_path = Path(args.out).expanduser().resolve()
        run = load_json_object(run_path, "normalized run")
        validate_run(run)
        findings_data = load_json_object(findings_path, "findings")
        findings = validate_findings(findings_data)
        report = render_report(run, findings)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report, encoding="utf-8")
    except (OSError, RuntimeError, UnicodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(json.dumps({"findings": len(findings), "out": str(out_path)}, sort_keys=True))
    return 0


def render_report(run: dict[str, Any], findings: list[dict[str, Any]]) -> str:
    reject_absolute_strings(run["run_id"], "run_id")
    reject_absolute_strings(run["algorithm"], "algorithm")
    counts = {severity: sum(item["severity"] == severity for item in findings) for severity in SEVERITIES}
    lines = [
        f"# Training Run Report: {inline(run['run_id'])} ({inline(run['algorithm'])})",
        "",
        "## Findings summary",
        "",
        "| Severity | Count |",
        "|---|---:|",
        f"| Critical | {counts['critical']} |",
        f"| Warn | {counts['warn']} |",
        f"| Info | {counts['info']} |",
        "",
    ]
    if not findings:
        lines.extend(["No findings were produced by the configured health checks.", ""])

    for finding in findings:
        canon_ref = validated_relative_path(finding["canon_ref"], "canon_ref")
        lines.extend(
            [
                f"## {inline(finding['id'])}",
                "",
                f"- Severity: `{finding['severity']}`",
                f"- Metric: `{inline(finding['metric'])}`",
                f"- Confidence: `{finding['confidence']}`",
                f"- Canon: [{canon_ref}]({canon_ref})",
                "",
                inline(finding["explanation"]),
                "",
                "### Evidence",
                "",
                "```json",
                json.dumps(finding["evidence"], indent=2, sort_keys=True, allow_nan=False),
                "```",
                "",
            ]
        )

    lines.extend(
        [
            "---",
            "",
            "Advisory read-only V1. This report provides diagnostic guidance and does not mutate training systems or accounts.",
            "",
            "Confidence-tag legend:",
            "",
            "- `practitioner`: an operating heuristic or threshold that requires task-specific review.",
            "- `evidence-based`: a conclusion directly supported by the cited canon evidence.",
        ]
    )
    report = "\n".join(lines).rstrip() + "\n"
    reject_absolute_strings(report, "rendered report")
    return report


def validate_findings(data: dict[str, Any]) -> list[dict[str, Any]]:
    run_id = data.get("run_id")
    findings = data.get("findings")
    if not isinstance(run_id, str):
        raise RenderError("findings run_id must be a string")
    if set(data) != {"run_id", "findings"}:
        raise RenderError("findings document must contain only run_id and findings")
    if not isinstance(findings, list):
        raise RenderError("findings must be an array")
    for index, finding in enumerate(findings, start=1):
        if not isinstance(finding, dict) or set(finding) != FINDING_KEYS:
            raise RenderError(f"finding {index} has an invalid shape")
        for key in ("id", "severity", "metric", "explanation", "confidence", "canon_ref"):
            if not isinstance(finding[key], str):
                raise RenderError(f"finding {index} {key} must be a string")
        if finding["severity"] not in SEVERITIES:
            raise RenderError(f"finding {index} has an unsupported severity")
        if finding["confidence"] not in CONFIDENCE_TAGS:
            raise RenderError(f"finding {index} has an unsupported confidence tag")
        if not isinstance(finding["evidence"], dict):
            raise RenderError(f"finding {index} evidence must be an object")
        evidence = finding["evidence"]
        if set(evidence) != {"steps", "values", "summary"}:
            raise RenderError(f"finding {index} evidence must contain steps, values, and summary")
        if not isinstance(evidence["steps"], list) or not isinstance(evidence["values"], list) or not isinstance(evidence["summary"], dict):
            raise RenderError(f"finding {index} evidence has invalid types")
        validated_relative_path(finding["canon_ref"], f"finding {index} canon_ref")
        reject_absolute_strings(finding, f"finding {index}")
    return findings


def load_json_object(path: Path, label: str) -> dict[str, Any]:
    if not path.is_file():
        raise RenderError(f"{label} file not found: {path}")
    if path.stat().st_size > MAX_BYTES:
        raise RenderError(f"{label} file exceeds 10MB: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"), parse_constant=reject_json_constant)
    except ValueError as exc:
        raise RenderError(f"invalid {label} JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise RenderError(f"{label} must be a JSON object")
    return data


def validated_relative_path(value: str, label: str) -> str:
    clean = value.strip().replace("\\", "/")
    path = PurePosixPath(clean)
    if not clean or path.is_absolute() or ".." in path.parts or WINDOWS_ABSOLUTE.match(value):
        raise RenderError(f"{label} must be a repo-relative path")
    return path.as_posix()


def reject_absolute_strings(value: object, label: str) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            reject_absolute_strings(key, label)
            reject_absolute_strings(nested, label)
    elif isinstance(value, list):
        for nested in value:
            reject_absolute_strings(nested, label)
    elif isinstance(value, str):
        without_urls = URL.sub("", value)
        if (
            POSIX_ABSOLUTE_ANYWHERE.search(without_urls)
            or WINDOWS_ABSOLUTE_ANYWHERE.search(without_urls)
            or UNC_ABSOLUTE_ANYWHERE.search(without_urls)
        ):
            raise RenderError(f"{label} contains a local absolute path")


def inline(value: object) -> str:
    return " ".join(str(value).split()).replace("|", "\\|")


def reject_json_constant(value: str) -> None:
    raise ValueError(f"non-finite number {value} is not allowed")


if __name__ == "__main__":
    raise SystemExit(main())
