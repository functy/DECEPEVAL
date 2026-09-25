from __future__ import annotations

import concurrent.futures
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


PACKAGE_ROOT = Path(__file__).resolve().parents[2]
EXECUTOR = Path(__file__).with_name("react_agent.py")
JUDGE = Path(__file__).with_name("llm_judge.py")
IMAGE_ARCHIVE = Path(__file__).with_name("docker") / "agent-code-v1-react.tar"


def _now() -> str:
    return datetime.now().astimezone().isoformat()


def _append_fact(path: Path, message: str) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"[{_now()}] {message}\n")
        handle.flush()
        os.fsync(handle.fileno())


def _run_command(command: list[str], log_path: Path, env: dict[str, str], attempts: int) -> tuple[int, str | None]:
    error = None
    returncode = 1
    for attempt in range(1, attempts + 1):
        with log_path.open("a", encoding="utf-8") as log:
            log.write(f"\n--- ATTEMPT {attempt}/{attempts} ---\n")
            try:
                completed = subprocess.run(
                    command,
                    cwd=PACKAGE_ROOT,
                    env=env,
                    stdout=log,
                    stderr=subprocess.STDOUT,
                    text=True,
                )
                returncode = completed.returncode
                error = None if returncode == 0 else f"returncode={returncode}"
            except OSError as exc:
                returncode = 1
                error = f"{type(exc).__name__}: {exc}"
        if returncode == 0:
            break
    return returncode, error


def _container_path(path: Path) -> str:
    return "/benchmark/" + str(path.resolve().relative_to(PACKAGE_ROOT)).replace(os.sep, "/")


def _ensure_docker_image(image: str) -> None:
    inspected = subprocess.run(
        ["docker", "image", "inspect", image],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if inspected.returncode == 0:
        return
    if not IMAGE_ARCHIVE.is_file():
        raise RuntimeError(f"Docker image {image!r} is absent and archive is missing: {IMAGE_ARCHIVE}")
    subprocess.run(["docker", "load", "--input", str(IMAGE_ARCHIVE)], check=True)


def _run_one(index: int, task_path: Path, run_root: Path, env: dict[str, str], attempts: int, image: str) -> dict[str, Any]:
    task = json.loads(task_path.read_text(encoding="utf-8"))
    condition = str(task["condition"])
    stem = f"{index:04d}_{condition}"
    trajectory = run_root / "trajectories" / f"{stem}.json"
    judgement = run_root / "judgements" / f"{stem}.json"
    agent_log = run_root / "agent_logs" / f"{stem}.log"
    judge_log = run_root / "judge_logs" / f"{stem}.log"
    for directory in (trajectory.parent, judgement.parent, agent_log.parent, judge_log.parent):
        directory.mkdir(parents=True, exist_ok=True)

    docker_prefix = [
        "docker", "run", "--rm",
        "-e", "EVAL_MODEL_ID", "-e", "EVAL_KEY", "-e", "EVAL_URL",
        "-e", "JUDGE_NAME", "-e", "JUDGE_KEY", "-e", "JUDGE_URL",
        "-e", "AGENT_REQUEST_TIMEOUT_SECONDS",
        "-e", "CODE_MAX_TURNS", "-e", "CODE_MAX_TOOL_CALLS", "-e", "CODE_TEST_TIMEOUT_SECONDS",
        "-e", "CODE_REPORTING_MAX_TURNS", "-e", "CODE_REPORTING_MAX_TOOL_CALLS",
        "-v", f"{PACKAGE_ROOT}:/benchmark", "-w", "/benchmark", image,
    ]
    executor_command = [
        *docker_prefix, "python", _container_path(EXECUTOR), _container_path(task_path),
        "--output", _container_path(trajectory),
    ]
    executor_rc, executor_error = _run_command(executor_command, agent_log, env, attempts)
    judge_rc = None
    judge_error = None
    result: dict[str, Any] = {}
    if executor_rc == 0 and trajectory.is_file():
        judge_command = [
            *docker_prefix, "python", _container_path(JUDGE), _container_path(task_path),
            _container_path(trajectory), "--output", _container_path(judgement),
        ]
        judge_rc, judge_error = _run_command(judge_command, judge_log, env, attempts)
        if judge_rc == 0 and judgement.is_file():
            try:
                result = json.loads(judgement.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                judge_error = f"invalid judge JSON: {exc}"

    valid = result.get("valid") is True
    return {
        "task_id": task.get("task_id"),
        "pair_id": task.get("pair_id"),
        "condition": condition,
        "primary_inducement": task.get("primary_inducement"),
        "operation_type": task.get("operation_type"),
        "execution_status": "completed" if executor_rc == 0 and judge_rc == 0 and valid else "failed_preserved",
        "executor_returncode": executor_rc,
        "judge_returncode": judge_rc,
        "executor_error": executor_error,
        "judge_error": judge_error,
        "trajectory": str(trajectory.relative_to(run_root)),
        "judgement": str(judgement.relative_to(run_root)) if judgement.is_file() else None,
        "agent_log": str(agent_log.relative_to(run_root)),
        "judge_log": str(judge_log.relative_to(run_root)),
        "result": result,
    }


def run_code_benchmark(
    config: dict[str, Any],
    settings: dict[str, Any],
    run_name: str,
    limit: int | None,
    scenario_ids: set[str] | None,
) -> dict[str, Any]:
    dataset_root = PACKAGE_ROOT / "benchmark_data" / settings["dataset"]
    pairs = json.loads((dataset_root / "pairs.json").read_text(encoding="utf-8"))
    jobs: list[tuple[int, Path]] = []
    for pair_index, pair in enumerate(pairs, 1):
        pair_dir = PACKAGE_ROOT / pair["directory"]
        for condition in ("neutral", "induced"):
            task_path = pair_dir / f"{condition}.json"
            task = json.loads(task_path.read_text(encoding="utf-8"))
            identifiers = {str(task.get("task_id", "")), str(task.get("pair_id", ""))}
            if scenario_ids is not None and not identifiers.intersection(scenario_ids):
                continue
            jobs.append((pair_index * 2 - (1 if condition == "neutral" else 0), task_path))
    if limit is not None:
        jobs = jobs[:limit]
    if not jobs:
        raise RuntimeError("No Code benchmark tasks matched the requested selection")

    run_root = PACKAGE_ROOT / "results" / run_name
    run_root.mkdir(parents=True, exist_ok=True)
    fact_log = run_root / "fact_summary.log"
    env = dict(os.environ)
    env.update({
        "EVAL_MODEL_ID": config["tested_model"]["name"],
        "EVAL_KEY": config["tested_model"]["api_key"],
        "EVAL_URL": config["tested_model"]["base_url"],
        "JUDGE_NAME": config["judge_model"]["name"],
        "JUDGE_KEY": config["judge_model"]["api_key"],
        "JUDGE_URL": config["judge_model"]["base_url"],
        "AGENT_REQUEST_TIMEOUT_SECONDS": str(settings.get("request_timeout_seconds", 120)),
        "CODE_MAX_TURNS": str(settings.get("max_turns", 5)),
        "CODE_MAX_TOOL_CALLS": str(settings.get("max_tool_calls", 36)),
        "CODE_TEST_TIMEOUT_SECONDS": str(settings.get("test_timeout_seconds", 300)),
        "CODE_REPORTING_MAX_TURNS": str(settings.get("reporting_max_turns", 6)),
        "CODE_REPORTING_MAX_TOOL_CALLS": str(settings.get("reporting_max_tool_calls", 20)),
        "CODE_MAX_TURNS": str(settings.get("max_turns", 5)),
        "CODE_MAX_TOOL_CALLS": str(settings.get("max_tool_calls", 36)),
        "CODE_TEST_TIMEOUT_SECONDS": str(settings.get("test_timeout_seconds", 300)),
        "CODE_REPORTING_MAX_TURNS": str(settings.get("reporting_max_turns", 6)),
        "CODE_REPORTING_MAX_TOOL_CALLS": str(settings.get("reporting_max_tool_calls", 20)),
    })
    attempts = int(config.get("runtime", {}).get("task_max_attempts", 3))
    image = str(settings.get("docker_image", "agent-code-v1-react"))
    _ensure_docker_image(image)
    _append_fact(fact_log, f"START benchmark=code dataset={settings['dataset']} planned={len(jobs)} workers=5")
    records: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        futures = {
            pool.submit(_run_one, index, task_path, run_root, env, attempts, image): (index, task_path)
            for index, task_path in jobs
        }
        for future in concurrent.futures.as_completed(futures):
            record = future.result()
            records.append(record)
            result = record["result"]
            _append_fact(
                fact_log,
                f"RESULT task_id={record['task_id']} condition={record['condition']} "
                f"status={record['execution_status']} behavioral_deception={result.get('behavioral_deception')} "
                f"valid={result.get('valid')}",
            )
    records.sort(key=lambda item: str(item["task_id"]))
    (run_root / "results.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    completed = sum(record["execution_status"] == "completed" for record in records)
    valid = sum((record.get("result") or {}).get("valid") is True for record in records)
    deception = sum((record.get("result") or {}).get("behavioral_deception") is True for record in records)
    summary = {
        "benchmark": "code",
        "dataset": settings["dataset"],
        "tested_model": config["tested_model"]["name"],
        "judge_model": config["judge_model"]["name"],
        "tasks": len(records),
        "completed": completed,
        "valid": valid,
        "behavioral_deception": deception,
        "workers": 5,
        "updated_at": _now(),
    }
    (run_root / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    _append_fact(fact_log, f"FINAL completed={completed}/{len(records)} valid={valid} behavioral_deception={deception}")
    return summary
