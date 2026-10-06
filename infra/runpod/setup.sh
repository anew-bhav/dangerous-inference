#!/usr/bin/env bash
# One-shot setup on a fresh RunPod pod (PyTorch template).
#   curl -fsSL <raw-url-of-this-file> | bash        or        bash infra/runpod/setup.sh
# Everything persistent lives under /workspace (the network volume).
set -euo pipefail

REPO_URL="${REPO_URL:-https://github.com/<you>/learning_inference.git}"
WORKDIR=/workspace/learning_inference

export HF_HOME=/workspace/hf_cache
export UV_CACHE_DIR=/workspace/.uv_cache
grep -q HF_HOME ~/.bashrc 2>/dev/null || cat >> ~/.bashrc <<EOF
export HF_HOME=$HF_HOME
export UV_CACHE_DIR=$UV_CACHE_DIR
export PATH=\$HOME/.local/bin:\$PATH
EOF

command -v uv >/dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

[[ -d "$WORKDIR/.git" ]] || git clone "$REPO_URL" "$WORKDIR"
cd "$WORKDIR"
uv sync

nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv
uv run python -c "from bench import collect_env; import json; print(json.dumps(collect_env(), indent=2))"
echo "ready: cd $WORKDIR"
