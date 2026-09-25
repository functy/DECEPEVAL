from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

from runtime.code.batch_runner import run_code_benchmark

ROOT = Path(__file__).resolve().parent
DATA_ROOT = ROOT / "benchmark_data"
RUNTIME = ROOT / "runtime"


def now() -> str:
    return datetime.now().astimezone().isoformat()


def rewrite_paths(value: Any, prefix: str) -> Any:
    if isinstance(value, dict):
        return {key: rewrite_paths(item, prefix) for key, item in value.items()}
    if isinstance(value, list):
        return [rewrite_paths(item, prefix) for item in value]
    if isinstance(value, str):
        return value.replace("workspace/", f"{prefix}/workspace/")
    return value


def load_tasks(dataset_root: Path, limit: int | None, scenario_ids: set[str] | None = None) -> list[dict[str, Any]]:
    tasks: list[dict[str, Any]] = []
    pairs = sorted(dataset_root.glob("data/*/*/*/pair"))
    if not pairs:
        raise RuntimeError(f"No pair directories found in {dataset_root}")
    for pair_ordinal, pair in enumerate(pairs):
        for condition in ("neutral", "induced"):
            task_path = pair / f"{condition}.json"
            if not task_path.is_file():
                raise RuntimeError(f"Missing task file: {task_path}")
            task = json.loads(task_path.read_text(encoding="utf-8"))
            if scenario_ids is not None and str(task.get("scenario_id", "")) not in scenario_ids:
                continue
            task["_source_pair"] = str(pair)
            task["_runtime_task_id"] = pair_ordinal * 2 + (condition == "induced")
            task["_condition"] = condition
            tasks.append(task)
    return tasks if limit is None else tasks[:limit]


def apply_benchmark_limits(task: dict[str, Any], settings: dict[str, Any]) -> None:
    limits = dict(task.get("resource_limits") or {})
    for name in ("max_steps_per_turn", "max_tool_calls", "max_completion_tokens_per_generation"):
        if settings.get(name) is not None:
            limits[name] = settings[name]
    task["resource_limits"] = limits


def prepare_shard(tasks: list[dict[str, Any]], run_root: Path, shard: int, settings: dict[str, Any]) -> tuple[Path, Path, Path]:
    shard_root = run_root / "shards" / f"shard_{shard:02d}"
    staging = shard_root / "staging"
    staged: list[dict[str, Any]] = []
    for source_task in tasks:
        task = {key: value for key, value in source_task.items() if not key.startswith("_")}
        task_id = int(source_task["_runtime_task_id"])
        prefix = f"task_{task_id:04d}"
        source_workspace = Path(source_task["_source_pair"]) / "workspace"
        destination = staging / prefix / "workspace"
        if source_workspace.is_dir():
            shutil.copytree(source_workspace, destination, dirs_exist_ok=True)
        else:
            raise RuntimeError(f"Missing packaged workspace: {source_workspace}")
        task = rewrite_paths(task, prefix)
        # ``rewrite_paths`` also rewrites multi-turn instructions into the
        # staged task workspace. Keep the official-output check on that same
        # rewritten path; otherwise a correctly created nested artifact is
        # mistaken for a missing recipient artifact.
        if task.get("task_type", 0) == 0 and isinstance(task.get("official_output_file"), str):
            output_name = task["official_output_file"]
            if not output_name.startswith(prefix + "/"):
                task["official_output_file"] = f"{prefix}/workspace/{output_name}"
        task["task_id"] = task_id
        task["task_index"] = task_id
        task["pair_id"] = str(task.get("pair_id") or f"runtime_pair_{task_id // 2:04d}")
        task["judge_version"] = str(task.get("judge_version") or "binary_v3")
        apply_benchmark_limits(task, settings)
        staged.append(task)
    dataset = shard_root / "dataset.json"
    dataset.parent.mkdir(parents=True, exist_ok=True)
    dataset.write_text(json.dumps(staged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return shard_root, dataset, staging


def append_fact(log_path: Path, line: str) -> None:
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"[{now()}] {line}\n")
        handle.flush()
        os.fsync(handle.fileno())


def validate_config(config: dict[str, Any], benchmark: str) -> None:
    for model_key in ("tested_model", "judge_model"):
        model = config.get(model_key) or {}
        for field in ("api_key", "base_url"):
            value = model.get(field)
            if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
                model[field] = os.getenv(value[2:-1], "")
        missing = [field for field in ("name", "api_key", "base_url") if not isinstance(model.get(field), str) or not model[field].strip()]
        if missing:
            raise SystemExit(f"config.json: {model_key} is missing {', '.join(missing)}")
    if benchmark not in (config.get("benchmarks") or {}):
        raise SystemExit(f"config.json: missing benchmarks.{benchmark}")
    if int((config.get("runtime") or {}).get("workers", 5)) != 5:
        raise SystemExit("This package requires runtime.workers to remain 5.")


def run(config: dict[str, Any], benchmark: str, run_name: str, limit: int | None, resume: bool, scenario_ids: set[str] | None = None) -> dict[str, Any]:
    validate_config(config, benchmark)
    settings = config["benchmarks"][benchmark]
    if benchmark == "code":
        if resume:
            raise SystemExit("--resume is not currently supported for the Code benchmark.")
        return run_code_benchmark(config, settings, run_name, limit, scenario_ids)
    dataset_root = DATA_ROOT / settings["dataset"]
    all_tasks = load_tasks(dataset_root, limit, scenario_ids)
    # The supplied run name is the directory name directly under results/.
    # This keeps each invocation in the same topology as archived benchmark runs.
    run_root = ROOT / "results" / run_name
    run_root.mkdir(parents=True, exist_ok=True)
    facts = run_root / "fact_summary.log"
    append_fact(facts, f"START benchmark={benchmark} dataset={settings['dataset']} planned={len(all_tasks)} workers=5 tested_model={config['tested_model']['name']} judge_model={config['judge_model']['name']}")
    chunks = [all_tasks[index::5] for index in range(5)]
    processes = []
    seen: dict[int, set[int]] = {index: set() for index in range(5)}
    for shard, chunk in enumerate(chunks):
        shard_root = run_root / "shards" / f"shard_{shard:02d}"
        result_file = shard_root / "results.json"
        if resume and result_file.is_file():
            existing = json.loads(result_file.read_text(encoding="utf-8"))
            completed = {int(item["task_id"]) for item in existing if item.get("execution_status") == "completed"}
            chunk = [task for task in chunk if int(task["_runtime_task_id"]) not in completed]
        if not chunk:
            append_fact(facts, f"SHARD shard={shard:02d} no pending tasks")
            continue
        shard_root, dataset, staging = prepare_shard(chunk, run_root, shard, settings)
        env = dict(os.environ)
        env.update({
            "EVAL_MODEL_ID": config["tested_model"]["name"],
            "EVAL_KEY": config["tested_model"]["api_key"],
            "EVAL_URL": config["tested_model"]["base_url"],
            "JUDGE_NAME": config["judge_model"]["name"],
            "JUDGE_KEY": config["judge_model"]["api_key"],
            "JUDGE_URL": config["judge_model"]["base_url"],
            "TASK_MAX_ATTEMPTS": str(config.get("runtime", {}).get("task_max_attempts", 3)),
            "JUDGE_FAILURE_DEFER": "1" if config.get("runtime", {}).get("judge_failure_defer", True) else "0",
            "AGENT_USE_FALLBACK": "1" if config.get("runtime", {}).get("use_fallback_agent", True) else "0",
        })
        cmd = [sys.executable, "-u", str(RUNTIME / "evaluation.py"), "--dataset", str(dataset), "--output_dir", str(shard_root / "artifacts"), "--results", str(result_file), "--prompts_dir", str(RUNTIME / "template"), "--workspace_dir", str(staging), "--tool_mode", str(config.get("runtime", {}).get("tool_mode", "normal")), "--temperature", str(settings.get("temperature", 1.0))]
        log_path = run_root / "log" / f"shard_{shard:02d}.stdout.log"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        handle = log_path.open("a" if resume else "w", encoding="utf-8")
        processes.append((shard, subprocess.Popen(cmd, cwd=RUNTIME, env=env, stdout=handle, stderr=subprocess.STDOUT), handle, result_file))
        append_fact(facts, f"LAUNCH shard={shard:02d} tasks={len(chunk)}")
    while any(process.poll() is None for _, process, _, _ in processes):
        for shard, _, _, result_file in processes:
            if not result_file.is_file():
                continue
            try:
                records = json.loads(result_file.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            for record in records:
                task_id = int(record["task_id"])
                if task_id in seen[shard] or record.get("execution_status") not in {"completed", "failed_preserved", "judge_pending"}:
                    continue
                seen[shard].add(task_id)
                result = record.get("result") or {}
                append_fact(facts, f"RESULT shard={shard:02d} task_id={task_id} condition={record.get('condition')} scenario={record.get('scenario_id')} status={record.get('execution_status')} label={result.get('label')} behavioral_deception={result.get('behavioral_deception')} valid={result.get('valid')}")
        time.sleep(1)
    statuses = []
    merged = []
    for shard, process, handle, result_file in processes:
        statuses.append(process.wait())
        handle.close()
        if result_file.is_file():
            merged.extend(json.loads(result_file.read_text(encoding="utf-8")))
    merged.sort(key=lambda item: int(item["task_id"]))
    (run_root / "results.json").write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    valid = [item for item in merged if (item.get("result") or {}).get("valid") is True]
    summary = {"benchmark": benchmark, "dataset": settings["dataset"], "tested_model": config["tested_model"]["name"], "judge_model": config["judge_model"]["name"], "tasks": len(merged), "completed": sum(item.get("execution_status") == "completed" for item in merged), "valid": len(valid), "behavioral_deception": sum((item.get("result") or {}).get("behavioral_deception") is True for item in valid), "shard_returncodes": statuses, "updated_at": now()}
    (run_root / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    append_fact(facts, f"FINAL completed={summary['completed']}/{len(all_tasks)} valid={summary['valid']} behavioral_deception={summary['behavioral_deception']} returncodes={statuses}")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--benchmark", choices=("tool", "long_horizon", "code"), required=True)
    parser.add_argument("--run-name", help="Overrides runtime.run_name in config.json")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--scenario-ids", help="Comma-separated scenario_id values to run")
    args = parser.parse_args()
    config = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
    run_name = args.run_name or config.get("runtime", {}).get("run_name")
    if not isinstance(run_name, str) or not run_name.strip() or run_name.startswith("replace_"):
        raise SystemExit("Set runtime.run_name in config.json or pass --run-name.")
    scenario_ids = {item.strip() for item in (args.scenario_ids or "").split(",") if item.strip()} or None
    print(json.dumps(run(config, args.benchmark, run_name, args.limit, args.resume, scenario_ids), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
