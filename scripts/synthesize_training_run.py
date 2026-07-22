#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
import statistics
import sys
from pathlib import Path
from typing import Any, Callable

try:
    from import_training_run import InputError as RunInputError
    from import_training_run import validate_run
except ModuleNotFoundError:
    from scripts.import_training_run import InputError as RunInputError
    from scripts.import_training_run import validate_run


MAX_BYTES = 10 * 1024 * 1024
CANON_REF = "references/canon/023-debugging-rl-training-runs-in-practice.md"
EPSILON = 1e-12
ALIASES = {
    "return": ("episodic_return", "ep_rew_mean", "reward"),
    "entropy": ("entropy",),
    "kl": ("approx_kl", "kl"),
    "value_loss": ("value_loss", "vf_loss", "critic_loss"),
}
Point = tuple[int, int, float]
Detector = Callable[[list[Point]], dict[str, Any] | None]


class SynthesisError(ValueError):
    pass


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Analyze a normalized RL training run.")
    parser.add_argument("--run", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    try:
        run_path = Path(args.run).expanduser().resolve()
        out_path = Path(args.out).expanduser().resolve()
        run = load_json_object(run_path, "normalized run")
        validate_run(run)
        result = analyze_run(run)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(
            json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n",
            encoding="utf-8",
        )
    except (OSError, RuntimeError, UnicodeError, ValueError, ArithmeticError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(json.dumps({"findings": len(result["findings"]), "run_id": result["run_id"]}, sort_keys=True))
    return 0


def analyze_run(run: dict[str, Any]) -> dict[str, Any]:
    series = metric_series(run["metrics"])
    return_series = matching_series(series, ALIASES["return"])
    findings: list[dict[str, Any]] = []

    add_detected(
        findings,
        "reward_collapse",
        "critical",
        return_series,
        detect_reward_collapse,
        "Episodic return fell more than 50% from its running peak throughout the final 20% of training.",
    )
    add_detected(
        findings,
        "reward_plateau",
        "warn",
        return_series,
        detect_reward_plateau,
        "Episodic return had a relative range below 5% over the final 50% of training.",
    )
    add_detected(
        findings,
        "entropy_collapse",
        "critical",
        matching_series(series, ALIASES["entropy"]),
        detect_entropy_collapse,
        "Policy entropy fell below 5% of its initial value before 50% of training was complete.",
    )
    add_detected(
        findings,
        "kl_spike",
        "warn",
        matching_series(series, ALIASES["kl"]),
        detect_kl_spike,
        "A KL metric exceeded 10 times its median value.",
    )
    add_detected(
        findings,
        "value_loss_explosion",
        "critical",
        matching_series(series, ALIASES["value_loss"]),
        detect_value_loss_explosion,
        "Value or critic loss grew monotonically over the final 30% of training and finished above 10 times its median.",
    )
    if not return_series:
        findings.append(
            make_finding(
                "missing_core_metrics",
                "info",
                "return-like",
                {
                    "steps": [],
                    "values": [],
                    "summary": {"available_metrics": sorted(series, key=str.casefold)},
                },
                "No return-like metric was found, so reward health could not be assessed.",
            )
        )
    return {"run_id": run["run_id"], "findings": findings}


def metric_series(metrics: list[dict[str, Any]]) -> dict[str, list[Point]]:
    series: dict[str, list[Point]] = {}
    for index, metric in enumerate(metrics):
        series.setdefault(metric["name"], []).append((metric["step"], index, float(metric["value"])))
    for points in series.values():
        points.sort(key=lambda point: (point[0], point[1]))
    return series


def matching_series(series: dict[str, list[Point]], aliases: tuple[str, ...]) -> list[tuple[str, list[Point]]]:
    matched = []
    for name, points in series.items():
        rank = alias_rank(name, aliases)
        if rank is not None:
            matched.append((rank, normalize_name(name), name.casefold(), name, points))
    matched.sort(key=lambda item: item[:3])
    return [(item[3], item[4]) for item in matched]


def alias_rank(name: str, aliases: tuple[str, ...]) -> int | None:
    normalized = normalize_name(name)
    compact = normalized.replace("_", "")
    tokens = normalized.split("_")
    for index, alias in enumerate(aliases):
        alias_compact = alias.replace("_", "")
        if alias == "kl":
            if "kl" in tokens or "kl" in compact:
                return index
        elif alias in normalized or alias_compact in compact:
            return index
    return None


def normalize_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.casefold()).strip("_")


def add_detected(
    findings: list[dict[str, Any]],
    finding_id: str,
    severity: str,
    candidates: list[tuple[str, list[Point]]],
    detector: Detector,
    explanation: str,
) -> None:
    for name, points in candidates:
        evidence = detector(points)
        if evidence is not None:
            findings.append(make_finding(finding_id, severity, name, evidence, explanation))
            return


def detect_reward_collapse(points: list[Point]) -> dict[str, Any] | None:
    tail = final_window(points, 0.20)
    if not tail:
        return None
    start = len(points) - len(tail)
    ratios = []
    for offset, point in enumerate(tail):
        running_peak = max(item[2] for item in points[: start + offset + 1])
        ratios.append((running_peak - point[2]) / max(abs(running_peak), EPSILON))
    if not all(ratio > 0.50 for ratio in ratios):
        return None
    return evidence(
        tail,
        {
            "running_peak": max(point[2] for point in points),
            "minimum_drop_ratio": min(ratios),
            "threshold_ratio": 0.50,
        },
    )


def detect_reward_plateau(points: list[Point]) -> dict[str, Any] | None:
    tail = final_window(points, 0.50)
    if len(tail) < 2:
        return None
    values = [point[2] for point in tail]
    relative_range = (max(values) - min(values)) / max(max(abs(value) for value in values), EPSILON)
    if relative_range >= 0.05:
        return None
    return evidence(
        tail,
        {
            "minimum": min(values),
            "maximum": max(values),
            "relative_range": relative_range,
            "threshold_ratio": 0.05,
        },
    )


def detect_entropy_collapse(points: list[Point]) -> dict[str, Any] | None:
    if len(points) < 2 or points[0][2] <= 0:
        return None
    initial = points[0][2]
    first_step = points[0][0]
    last_step = points[-1][0]
    for index, point in enumerate(points[1:], start=1):
        if last_step == first_step:
            progress = index / (len(points) - 1)
        else:
            progress = (point[0] - first_step) / (last_step - first_step)
        if progress < 0.50 and point[2] < 0.05 * initial:
            return evidence(
                [points[0], point],
                {
                    "initial": initial,
                    "collapsed": point[2],
                    "value_ratio": point[2] / initial,
                    "training_progress": progress,
                    "threshold_ratio": 0.05,
                },
            )
    return None


def detect_kl_spike(points: list[Point]) -> dict[str, Any] | None:
    if not points:
        return None
    median = statistics.median(point[2] for point in points)
    spike = max(points, key=lambda point: point[2])
    if median < 0 or spike[2] <= 10 * median:
        return None
    ratio = spike[2] / median if median != 0 else None
    return evidence(
        [spike],
        {
            "median": median,
            "maximum": spike[2],
            "maximum_to_median_ratio": ratio,
            "threshold_multiplier": 10,
        },
    )


def detect_value_loss_explosion(points: list[Point]) -> dict[str, Any] | None:
    tail = final_window(points, 0.30)
    if len(tail) < 2:
        return None
    values = [point[2] for point in tail]
    nondecreasing = all(current <= following for current, following in zip(values, values[1:]))
    increased = any(current < following for current, following in zip(values, values[1:]))
    median = statistics.median(point[2] for point in points)
    if median < 0 or not nondecreasing or not increased or values[-1] <= 10 * median:
        return None
    ratio = values[-1] / median if median != 0 else None
    return evidence(
        tail,
        {
            "median": median,
            "tail_initial": values[0],
            "final": values[-1],
            "final_to_median_ratio": ratio,
            "threshold_multiplier": 10,
        },
    )


def final_window(points: list[Point], fraction: float) -> list[Point]:
    if not points:
        return []
    first_step = points[0][0]
    last_step = points[-1][0]
    if last_step == first_step:
        count = max(1, math.ceil(len(points) * fraction))
        return points[-count:]
    cutoff = first_step + (last_step - first_step) * (1 - fraction)
    return [point for point in points if point[0] >= cutoff]


def evidence(points: list[Point], summary: dict[str, Any]) -> dict[str, Any]:
    return {
        "steps": [point[0] for point in points],
        "values": [point[2] for point in points],
        "summary": summary,
    }


def make_finding(
    finding_id: str,
    severity: str,
    metric: str,
    evidence_: dict[str, Any],
    explanation: str,
) -> dict[str, Any]:
    return {
        "id": finding_id,
        "severity": severity,
        "metric": metric,
        "evidence": evidence_,
        "explanation": explanation,
        "confidence": "practitioner",
        "canon_ref": CANON_REF,
    }


def load_json_object(path: Path, label: str) -> dict[str, Any]:
    if not path.is_file():
        raise SynthesisError(f"{label} file not found: {path}")
    if path.stat().st_size > MAX_BYTES:
        raise SynthesisError(f"{label} file exceeds 10MB: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"), parse_constant=reject_json_constant)
    except ValueError as exc:
        raise SynthesisError(f"invalid {label} JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise SynthesisError(f"{label} must be a JSON object")
    return data


def reject_json_constant(value: str) -> None:
    raise ValueError(f"non-finite number {value} is not allowed")


if __name__ == "__main__":
    raise SystemExit(main())
