#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
PY = sys.executable
FIXTURES = REPO / "tests" / "fixtures"
CANON_REF = "references/canon/023-debugging-rl-training-runs-in-practice.md"


def run(args: list[str], *, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [PY, *args],
        cwd=REPO,
        text=True,
        capture_output=True,
        env=env or os.environ.copy(),
        check=False,
    )


def assert_success(proc: subprocess.CompletedProcess[str]) -> None:
    assert proc.returncode == 0, f"stdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"


def test_csv_import_happy_path() -> None:
    with tempfile.TemporaryDirectory(prefix="rl-adapter-csv-") as tmp:
        output = Path(tmp) / "normalized.json"
        proc = run(
            [
                "scripts/import_training_run.py",
                "--input",
                str(FIXTURES / "sample-progress.csv"),
                "--out",
                str(output),
                "--run-id",
                "healthy-ppo",
                "--algorithm",
                "PPO",
                "--library",
                "Stable-Baselines3",
            ]
        )
        assert_success(proc)
        data = json.loads(output.read_text(encoding="utf-8"))
        assert data["run_id"] == "healthy-ppo"
        assert data["algorithm"] == "PPO"
        assert data["library"] == "Stable-Baselines3"
        assert data["hyperparameters"] == {}
        assert len(data["metrics"]) == 120
        assert {item["name"] for item in data["metrics"]} == {
            "episodic_return",
            "entropy",
            "approx_kl",
            "value_loss",
        }
        assert all(isinstance(item["step"], int) for item in data["metrics"])


def test_json_import_happy_path() -> None:
    with tempfile.TemporaryDirectory(prefix="rl-adapter-json-") as tmp:
        output = Path(tmp) / "normalized.json"
        proc = run(
            [
                "scripts/import_training_run.py",
                "--input",
                str(FIXTURES / "sample-run-wandb.json"),
                "--out",
                str(output),
            ]
        )
        assert_success(proc)
        data = json.loads(output.read_text(encoding="utf-8"))
        assert data["run_id"] == "wandb-ppo-collapse"
        assert data["algorithm"] == "PPO"
        assert data["library"] == "CleanRL"
        assert data["hyperparameters"]["learning_rate"] == 0.0003
        assert len(data["metrics"]) == 48
        assert all(not item["name"].startswith("_") for item in data["metrics"])


def test_malformed_csv_rejected() -> None:
    with tempfile.TemporaryDirectory(prefix="rl-adapter-bad-csv-") as tmp:
        output = Path(tmp) / "normalized.json"
        proc = run(
            [
                "scripts/import_training_run.py",
                "--input",
                str(FIXTURES / "malformed-progress.csv"),
                "--out",
                str(output),
            ]
        )
        assert proc.returncode == 2
        assert "ERROR" in proc.stderr
        assert not output.exists()


def test_malformed_json_rejected() -> None:
    with tempfile.TemporaryDirectory(prefix="rl-adapter-bad-json-") as tmp:
        output = Path(tmp) / "normalized.json"
        proc = run(
            [
                "scripts/import_training_run.py",
                "--input",
                str(FIXTURES / "malformed-run.json"),
                "--out",
                str(output),
            ]
        )
        assert proc.returncode == 2
        assert "ERROR" in proc.stderr
        assert not output.exists()


def test_wandb_api_refused_without_credentials() -> None:
    env = os.environ.copy()
    env.pop("WANDB_API_KEY", None)
    proc = run(["scripts/import_training_run.py", "--from-wandb-api"], env=env)
    assert proc.returncode == 2
    assert "ERROR" in proc.stderr
    assert "out of scope for advisory V1" in proc.stderr

    env["WANDB_API_KEY"] = "adapter-test-secret"
    proc_with_key = run(["scripts/import_training_run.py", "--from-wandb-api"], env=env)
    assert proc_with_key.returncode == 2
    assert "adapter-test-secret" not in proc_with_key.stdout + proc_with_key.stderr

    with tempfile.TemporaryDirectory(prefix="rl-adapter-api-abbrev-") as tmp:
        output = Path(tmp) / "normalized.json"
        abbreviated = run(
            [
                "scripts/import_training_run.py",
                "--input",
                str(FIXTURES / "sample-run-wandb.json"),
                "--out",
                str(output),
                "--from-wandb-a",
            ],
            env=env,
        )
        assert abbreviated.returncode == 2
        assert not output.exists()


def test_synthesis_detects_entropy_collapse_and_kl_spike() -> None:
    with tempfile.TemporaryDirectory(prefix="rl-adapter-findings-") as tmp:
        normalized = Path(tmp) / "normalized.json"
        findings_path = Path(tmp) / "findings.json"
        assert_success(
            run(
                [
                    "scripts/import_training_run.py",
                    "--input",
                    str(FIXTURES / "sample-run-wandb.json"),
                    "--out",
                    str(normalized),
                ]
            )
        )
        assert_success(
            run(
                [
                    "scripts/synthesize_training_run.py",
                    "--run",
                    str(normalized),
                    "--out",
                    str(findings_path),
                ]
            )
        )
        findings = json.loads(findings_path.read_text(encoding="utf-8"))["findings"]
        assert [item["id"] for item in findings] == ["entropy_collapse", "kl_spike"]
        assert all(item["confidence"] == "practitioner" for item in findings)
        assert all(item["canon_ref"] == CANON_REF for item in findings)
        assert all(set(item["evidence"]) == {"steps", "values", "summary"} for item in findings)


def test_synthesis_clean_on_healthy_fixture() -> None:
    with tempfile.TemporaryDirectory(prefix="rl-adapter-clean-") as tmp:
        normalized = Path(tmp) / "normalized.json"
        findings_path = Path(tmp) / "findings.json"
        assert_success(
            run(
                [
                    "scripts/import_training_run.py",
                    "--input",
                    str(FIXTURES / "sample-progress.csv"),
                    "--out",
                    str(normalized),
                    "--algorithm",
                    "PPO",
                    "--library",
                    "CleanRL",
                ]
            )
        )
        assert_success(
            run(
                [
                    "scripts/synthesize_training_run.py",
                    "--run",
                    str(normalized),
                    "--out",
                    str(findings_path),
                ]
            )
        )
        assert json.loads(findings_path.read_text(encoding="utf-8"))["findings"] == []


def test_renderer_cites_canon_without_absolute_paths() -> None:
    with tempfile.TemporaryDirectory(prefix="rl-adapter-report-") as tmp:
        normalized = Path(tmp) / "normalized.json"
        findings_path = Path(tmp) / "findings.json"
        report_path = Path(tmp) / "report.md"
        assert_success(
            run(
                [
                    "scripts/import_training_run.py",
                    "--input",
                    str(FIXTURES / "sample-run-wandb.json"),
                    "--out",
                    str(normalized),
                ]
            )
        )
        assert_success(
            run(
                [
                    "scripts/synthesize_training_run.py",
                    "--run",
                    str(normalized),
                    "--out",
                    str(findings_path),
                ]
            )
        )
        assert_success(
            run(
                [
                    "scripts/render_training_run_report.py",
                    "--findings",
                    str(findings_path),
                    "--run",
                    str(normalized),
                    "--out",
                    str(report_path),
                ]
            )
        )
        report = report_path.read_text(encoding="utf-8")
        assert report.startswith("# Training Run Report: wandb-ppo-collapse (PPO)\n")
        assert "| Critical | 1 |" in report
        assert "| Warn | 1 |" in report
        assert CANON_REF in report
        assert "Advisory read-only V1" in report
        assert "Confidence-tag legend" in report
        assert str(REPO) not in report
        assert tmp not in report
        assert "/home/" not in report
        assert "/Users/" not in report

        unsafe = json.loads(findings_path.read_text(encoding="utf-8"))
        unsafe["findings"][0]["evidence"]["summary"]["source"] = "source=/tmp/private/run.csv"
        unsafe_path = Path(tmp) / "unsafe-findings.json"
        unsafe_report = Path(tmp) / "unsafe-report.md"
        unsafe_path.write_text(json.dumps(unsafe), encoding="utf-8")
        rejected = run(
            [
                "scripts/render_training_run_report.py",
                "--findings",
                str(unsafe_path),
                "--run",
                str(normalized),
                "--out",
                str(unsafe_report),
            ]
        )
        assert rejected.returncode == 2
        assert "ERROR" in rejected.stderr
        assert not unsafe_report.exists()


def main() -> int:
    tests = [
        test_csv_import_happy_path,
        test_json_import_happy_path,
        test_malformed_csv_rejected,
        test_malformed_json_rejected,
        test_wandb_api_refused_without_credentials,
        test_synthesis_detects_entropy_collapse_and_kl_spike,
        test_synthesis_clean_on_healthy_fixture,
        test_renderer_cites_canon_without_absolute_paths,
    ]
    for test in tests:
        test()
    print(f"Adapter tests passed: {len(tests)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
