"""Build the performance-journey chart from every lesson's results/headline.json.

    uv run python -m bench.plot
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent


def collect() -> list[dict]:
    points = []
    for path in sorted(ROOT.glob("lessons/*/results/headline.json")):
        data = json.loads(path.read_text())
        for rec in data["records"]:
            points.append({"lesson": path.parent.parent.name, **rec})
    return points


def main() -> None:
    points = collect()
    if not points:
        print("no headline results yet")
        return
    labels = [p.get("label", p["lesson"]) for p in points]
    tps = [p["tokens_per_s"] for p in points]

    fig, ax = plt.subplots(figsize=(max(6, len(points) * 0.9), 4))
    ax.plot(labels, tps, marker="o", color="#2b6cb0")
    ax.set_ylabel("tokens / s")
    ax.set_title("Performance journey (canonical workload)")
    ax.grid(axis="y", alpha=0.3)
    plt.xticks(rotation=30, ha="right")
    fig.tight_layout()
    out = ROOT / "assets" / "journey.png"
    fig.savefig(out, dpi=150)
    print(f"saved {out}")


if __name__ == "__main__":
    main()
