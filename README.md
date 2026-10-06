# dangerous-inference

Learning LLM inference until I know enough to be dangerous.
Predict, measure, explain: from HF `generate` to my own engine vs vLLM.

Every lesson follows the same loop: **brief → predict → run → compare → reflect**.
Predictions are written *before* running, so the gaps between what I expected and what I measured are part of the record.

<!-- Once there's data: ![Performance journey](assets/journey.png) -->

## Progress

| # | Lesson | Key result | Status |
|---|--------|-----------|--------|
| 00 | _TBD_ | | ⏳ |

Status: ✅ done · 🔄 in progress · ⏳ planned

## Repo map

| Path | What lives there |
|------|------------------|
| [`lessons/`](lessons/) | One folder per experiment: brief, code, results, write-up |
| [`journal/`](journal/) | Daily log: raw, honest, dated |
| [`concepts/`](concepts/) | Evergreen notes in my own words, refined over time |
| [`bench/`](bench/) | Shared benchmark harness, so every lesson measures the same way |
| [`infra/runpod/`](infra/runpod/) | Reproducible GPU pod setup |
| [`teacher/`](teacher/) | Teacher session's home: role rules + lesson-planning notes |
| [`templates/`](templates/) | Templates for briefs, debriefs, reviews, lessons, journal entries |
| [`STATE.md`](STATE.md) | Where I am right now |
| [`ROADMAP.md`](ROADMAP.md) | The planned arc |

## How this is made

I learn with two [Claude Code](https://claude.com/claude-code) sessions that have strictly separated roles ([protocol](CLAUDE.md)):

- **Teacher** (runs in [`teacher/`](teacher/)): sets the curriculum, explains concepts, writes each lesson's `brief.md` and `review.md`.
- **Executor** (runs at repo root): writes the code, runs experiments, produces benchmarks and `debrief.md`.
- **Me**: predictions (written before every run), takeaways, journal, and concept notes, all in my own words.

They never talk directly. The repo is the only channel, so every handoff is visible in git history.

## Running

```bash
uv sync                                  # install deps (GPU box; see infra/runpod)
uv run python lessons/NN-name/run.py     # run a lesson
uv run python -m bench.plot              # regenerate the journey chart
./scripts/new.sh lesson 01 kv-cache      # scaffold a new lesson
./scripts/new.sh journal                 # today's journal entry
```
