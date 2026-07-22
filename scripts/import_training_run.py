#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
from decimal import Decimal, InvalidOperation
from datetime import date
from pathlib import Path
from typing import Any


MAX_BYTES = 10 * 1024 * 1024
STEP_COLUMNS = ("step", "global_step", "time/total_timesteps")
RUN_KEYS = {"run_id", "algorithm", "library", "created", "hyperparameters", "metrics"}
METRIC_KEYS = {"step", "name", "value"}
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}\Z")


class InputError(ValueError):
    pass


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Normalize an exported RL training run.", allow_abbrev=False)
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--run-id")
    parser.add_argument("--algorithm")
    parser.add_argument("--library")
    parser.add_argument("--from-wandb-api", action="store_true")
    raw_args = list(argv) if argv is not None else sys.argv[1:]
    if any(arg == "--from-wandb-api" or arg.startswith("--from-wandb-api=") for arg in raw_args):
        print(
            "ERROR: live W&B API import and WANDB_API_KEY use are out of scope for advisory V1; use an exported JSON file",
            file=sys.stderr,
        )
        return 2
    args = parser.parse_args(raw_args)
    try:
        if args.from_wandb_api:
            raise InputError("live W&B API import is out of scope for advisory V1")
        source = Path(args.input).expanduser().resolve()
        destination = Path(args.out).expanduser().resolve()
        run = import_run(
            source,
            run_id=args.run_id,
            algorithm=args.algorithm,
            library=args.library,
        )
        validate_run(run)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            json.dumps(run, indent=2, sort_keys=True, allow_nan=False) + "\n",
            encoding="utf-8",
        )
    except (InputError, OSError, RuntimeError, UnicodeError, csv.Error, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(json.dumps({"run_id": run["run_id"], "out": str(destination)}, sort_keys=True))
    return 0


def import_run(
    source: Path,
    *,
    run_id: str | None = None,
    algorithm: str | None = None,
    library: str | None = None,
) -> dict[str, Any]:
    if not source.is_file():
        raise InputError(f"input file not found: {source}")
    if source.stat().st_size > MAX_BYTES:
        raise InputError(f"input file exceeds 10MB: {source}")

    suffix = source.suffix.lower()
    if suffix == ".csv":
        normalized = import_csv(source)
    elif suffix == ".json":
        normalized = import_wandb_json(source)
    else:
        raise InputError(f"unsupported input extension: {source.suffix or '<none>'}")

    if run_id is not None:
        normalized["run_id"] = run_id
    if algorithm is not None:
        normalized["algorithm"] = algorithm
    if library is not None:
        normalized["library"] = library
    if not normalized["metrics"]:
        raise InputError("input contains no numeric metrics")
    return normalized


def import_csv(source: Path) -> dict[str, Any]:
    with source.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        raw_headers = reader.fieldnames
        if not raw_headers or any(header is None for header in raw_headers):
            raise InputError("CSV is missing a header row")
        headers = [str(header).strip() for header in raw_headers]
        folded_headers = [header.casefold() for header in headers]
        if any(not header for header in headers):
            raise InputError("CSV contains an empty column name")
        if len(set(folded_headers)) != len(folded_headers):
            raise InputError("CSV contains duplicate column names")

        step_column = next(
            (headers[folded_headers.index(candidate)] for candidate in STEP_COLUMNS if candidate in folded_headers),
            None,
        )
        if step_column is None:
            expected = ", ".join(STEP_COLUMNS)
            raise InputError(f"CSV is missing a step column; expected one of: {expected}")

        rows: list[dict[str, str]] = []
        for raw_row in reader:
            if None in raw_row:
                raise InputError("CSV row has more fields than the header")
            rows.append({headers[index]: str(raw_row.get(raw_headers[index], "") or "").strip() for index in range(len(headers))})

    steps = [parse_step(row[step_column], f"CSV row {index + 2}") for index, row in enumerate(rows)]
    metric_columns: dict[str, dict[int, float]] = {}
    for header in headers:
        if header == step_column:
            continue
        parsed: dict[int, float] = {}
        numeric_column = True
        for index, row in enumerate(rows):
            raw_value = row[header]
            if not raw_value:
                continue
            try:
                parsed[index] = parse_number(raw_value)
            except InputError:
                numeric_column = False
                break
        if numeric_column and parsed:
            metric_columns[header] = parsed

    metrics = []
    for index, step in enumerate(steps):
        for name in headers:
            if name in metric_columns and index in metric_columns[name]:
                metrics.append({"step": step, "name": name, "value": metric_columns[name][index]})

    return {
        "run_id": source.stem,
        "algorithm": "unknown",
        "library": "unknown",
        "created": date.today().isoformat(),
        "hyperparameters": {},
        "metrics": metrics,
    }


def import_wandb_json(source: Path) -> dict[str, Any]:
    text = source.read_text(encoding="utf-8")
    try:
        payload = json.loads(text, parse_constant=reject_json_constant)
    except ValueError as exc:
        raise InputError(f"invalid JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise InputError("W&B export must be a JSON object")
    config = payload.get("config", {})
    history = payload.get("history")
    if not isinstance(config, dict):
        raise InputError("W&B export config must be an object")
    if not isinstance(history, list):
        raise InputError("W&B export history must be an array")

    metrics: list[dict[str, Any]] = []
    for index, row in enumerate(history):
        if not isinstance(row, dict):
            raise InputError(f"W&B history row {index + 1} must be an object")
        if "_step" not in row:
            raise InputError(f"W&B history row {index + 1} is missing _step")
        step = parse_step(row["_step"], f"W&B history row {index + 1}")
        for name, value in row.items():
            if not isinstance(name, str) or name.startswith("_"):
                continue
            if is_number(value):
                metrics.append({"step": step, "name": name, "value": value})

    name = payload.get("name")
    created = normalized_created(payload.get("created") or payload.get("created_at"))
    return {
        "run_id": name if isinstance(name, str) and name else source.stem,
        "algorithm": config_string(config, "algorithm", "algo", fallback="unknown"),
        "library": config_string(config, "library", "framework", fallback="unknown"),
        "created": created,
        "hyperparameters": config,
        "metrics": metrics,
    }


def validate_run(run: object) -> None:
    if not isinstance(run, dict):
        raise InputError("normalized run must be an object")
    if any(not isinstance(key, str) for key in run):
        raise InputError("normalized run keys must be strings")
    missing = sorted(RUN_KEYS - set(run))
    extra = sorted(set(run) - RUN_KEYS)
    if missing:
        raise InputError(f"normalized run is missing required keys: {', '.join(missing)}")
    if extra:
        raise InputError(f"normalized run has unsupported keys: {', '.join(extra)}")
    for key in ("run_id", "algorithm", "library", "created"):
        if not isinstance(run[key], str):
            raise InputError(f"normalized run {key} must be a string")
    if not ISO_DATE.fullmatch(run["created"]):
        raise InputError("normalized run created must be an ISO date")
    try:
        date.fromisoformat(run["created"])
    except ValueError as exc:
        raise InputError("normalized run created must be an ISO date") from exc
    if not isinstance(run["hyperparameters"], dict):
        raise InputError("normalized run hyperparameters must be an object")
    metrics = run["metrics"]
    if not isinstance(metrics, list):
        raise InputError("normalized run metrics must be an array")
    if not metrics:
        raise InputError("normalized run metrics must not be empty")
    for index, metric in enumerate(metrics, start=1):
        if not isinstance(metric, dict):
            raise InputError(f"metric {index} must be an object")
        if set(metric) != METRIC_KEYS:
            raise InputError(f"metric {index} must contain only step, name, and value")
        if isinstance(metric["step"], bool) or not isinstance(metric["step"], int):
            raise InputError(f"metric {index} step must be an integer")
        if not isinstance(metric["name"], str):
            raise InputError(f"metric {index} name must be a string")
        if not is_number(metric["value"]):
            raise InputError(f"metric {index} value must be a finite number")


def parse_step(value: object, context: str) -> int:
    if isinstance(value, bool):
        raise InputError(f"{context} step must be an integer")
    if isinstance(value, int):
        return value
    try:
        numeric = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise InputError(f"{context} step must be an integer") from exc
    if not numeric.is_finite() or numeric != numeric.to_integral_value():
        raise InputError(f"{context} step must be an integer")
    return int(numeric)


def parse_number(value: object) -> float:
    if isinstance(value, bool):
        raise InputError("metric value must be numeric")
    try:
        numeric = float(value)
    except (OverflowError, TypeError, ValueError) as exc:
        raise InputError("metric value must be numeric") from exc
    if not math.isfinite(numeric):
        raise InputError("metric value must be finite")
    return numeric


def is_number(value: object) -> bool:
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return True
    return isinstance(value, float) and math.isfinite(value)


def config_string(config: dict[str, Any], *keys: str, fallback: str) -> str:
    for key in keys:
        value = config.get(key)
        if isinstance(value, str) and value:
            return value
    return fallback


def normalized_created(value: object) -> str:
    if isinstance(value, str):
        candidate = value[:10]
        if ISO_DATE.fullmatch(candidate):
            try:
                date.fromisoformat(candidate)
            except ValueError:
                pass
            else:
                return candidate
    return date.today().isoformat()


def reject_json_constant(value: str) -> None:
    raise ValueError(f"non-finite number {value} is not allowed")


if __name__ == "__main__":
    raise SystemExit(main())
