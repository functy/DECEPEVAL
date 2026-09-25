<div align="center">

# DecepEval

**A Benchmark for Evaluating Deception in LLM Agents**

[Overview](#overview) · [Setup](#setup) · [Usage](#usage) · [Apache-2.0 License](./LICENSE)

</div>

## Overview

DecepEval is a benchmark for evaluating deception in large language model agents. It contains **1,532 task pairs (3,064 instances)** spanning tool use, coding, and long-horizon workflows.

Each pair includes a `neutral` and an `induced` version to compare agent behavior under external conditions of pressure, incentive, opportunity, and conflict. Evaluation combines task facts, tool feedback, execution traces, and final deliverables to distinguish deception from ordinary errors and honest exits.

## Setup

Clone this repository with [Git LFS](https://git-lfs.com/) installed, then run `git lfs pull` to download the bundled Docker image.

We recommend **Python 3.11**. Run the following commands from the repository root:

```bash
python -m venv .venv
```

Activate the environment with `.\.venv\Scripts\Activate.ps1` in Windows PowerShell or `source .venv/bin/activate` on Linux/macOS. Then install the dependencies:

```bash
python -m pip install -r runtime/requirements.txt
```

Edit [config.json](./config.json) and replace `tested_model.name` and `judge_model.name` with the actual model IDs. Both models require an OpenAI-compatible API.

Keep the environment variable references for API keys and base URLs in the configuration, and set their values in your terminal:

```powershell
# Windows PowerShell
$env:EVAL_API_KEY = "your-evaluation-api-key"
$env:EVAL_BASE_URL = "https://your-provider.example/v1"
$env:JUDGE_API_KEY = "your-judge-api-key"
$env:JUDGE_BASE_URL = "https://your-provider.example/v1"
```

```bash
# Linux / macOS
export EVAL_API_KEY="your-evaluation-api-key"
export EVAL_BASE_URL="https://your-provider.example/v1"
export JUDGE_API_KEY="your-judge-api-key"
export JUDGE_BASE_URL="https://your-provider.example/v1"
```

Replace these example values with your actual credentials and endpoints. Coding tasks also require Docker with Linux containers. Start Docker and load the bundled `linux/amd64` image:

```bash
docker load --input runtime/code/docker/agent-code-v1-react.tar
```

## Usage

Choose a task family to run its full dataset:

```bash
# Tool use
python run_benchmark.py --benchmark tool --run-name tool

# Coding (requires Docker)
python run_benchmark.py --benchmark code --run-name code

# Long-horizon workflows
python run_benchmark.py --benchmark long_horizon --run-name long
```

Results are saved to `results/<run-name>/`: `summary.json` contains the run summary, `results.json` contains per-task results, and `fact_summary.log` records progress. Use a new run name for each new experiment.

---

DecepEval's original code and dataset content are licensed under the [Apache License 2.0](./LICENSE). Third-party materials retain their respective licenses; see [licenses/](./licenses/) and the notices included with dependencies.
