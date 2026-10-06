"""Capture hardware + software metadata. A benchmark number without this is meaningless."""

import platform
import subprocess


def _run(cmd: list[str]) -> str | None:
    try:
        return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def collect_env() -> dict:
    env = {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "git_commit": _run(["git", "rev-parse", "--short", "HEAD"]),
        "git_dirty": bool(_run(["git", "status", "--porcelain"])),
    }
    try:
        import torch

        env["torch"] = torch.__version__
        env["cuda"] = torch.version.cuda
        if torch.cuda.is_available():
            props = torch.cuda.get_device_properties(0)
            env["gpu"] = props.name
            env["gpu_count"] = torch.cuda.device_count()
            env["gpu_mem_gb"] = round(props.total_memory / 1e9, 1)
    except ImportError:
        pass
    try:
        import transformers

        env["transformers"] = transformers.__version__
    except ImportError:
        pass
    env["driver"] = _run(["nvidia-smi", "--query-gpu=driver_version", "--format=csv,noheader"])
    return env
