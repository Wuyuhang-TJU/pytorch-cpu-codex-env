#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

if command -v python3.12 >/dev/null 2>&1; then
    python_cmd=python3.12
else
    python_cmd=python3
fi

"$python_cmd" -c 'import sys; assert (3, 10) <= sys.version_info[:2] < (3, 14), "Use Python 3.10-3.13; Python 3.12 is recommended."'
"$python_cmd" -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements-torch-cpu.txt
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip check
MPLBACKEND=Agg .venv/bin/python scripts/check_environment.py
MPLBACKEND=Agg .venv/bin/python examples/train_cpu.py
