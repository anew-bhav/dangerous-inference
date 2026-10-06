"""Write results as small JSON files with env metadata attached."""

import json
from datetime import datetime, timezone
from pathlib import Path

from bench.env import collect_env


def save(lesson_dir: str | Path, name: str, records: list[dict], **meta) -> Path:
    """Save to <lesson_dir>/results/<name>.json.

    Name a file `headline` to feed the cross-lesson journey chart (bench.plot).
    A headline record must be measured on the canonical workload (bench.workload)
    and include a `label` field for the x-axis.
    """
    out_dir = Path(lesson_dir) / "results"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{name}.json"
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "env": collect_env(),
        "meta": meta,
        "records": records,
    }
    path.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"saved {path}")
    return path
