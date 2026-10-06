# RunPod setup

Goal: go from a fresh pod to a working environment with one command.

## Pod config
- **Template:** RunPod PyTorch (any recent CUDA 12.x)
- **GPU:** _TBD (record the choice in STATE.md, it's part of the canonical workload)_
- **Network volume:** mounted at `/workspace`. Repo, HF cache, and uv cache live there so they survive pod restarts.
- **SSH:** add your public key in RunPod settings; enable "SSH over exposed TCP".

## First boot
```bash
REPO_URL=https://github.com/anew-bhav/dangerous-inference.git bash -c "$(curl -fsSL <raw-url>/infra/runpod/setup.sh)"
```
or, after cloning: `bash infra/runpod/setup.sh`

## Workflow
1. Edit locally → `git push`
2. On pod: `git pull && uv run python lessons/NN-name/run.py`
3. Pod commits `results/` → `git push` → pull locally

(Alternatively, Claude Code drives the pod over `ssh` directly.)

## Cost log
| Date | GPU | Hours | $ | Lesson |
|------|-----|-------|---|--------|
| | | | | |

## Gotchas
<!-- Things that bit me. -->
