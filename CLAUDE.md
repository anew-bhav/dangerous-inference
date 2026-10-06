# Claude Code protocol

This repo is a public learning log for LLM inference. Two Claude Code sessions work on it with separated roles. The repo is the single source of truth and the only channel between them.

## Which role am I?
- Session launched at the **repo root** → **EXECUTOR** (this file only).
- Session launched in **`teacher/`** → **TEACHER** (`teacher/CLAUDE.md` overrides the executor section below).
- If unsure, ask the user.

## Ownership
| Owner | Writes | Never writes |
|-------|--------|--------------|
| Teacher | `ROADMAP.md`, `lessons/NN-*/brief.md`, `lessons/NN-*/review.md`, `teacher/` | Code, `bench/`, `infra/`, results |
| Executor | Code, `bench/`, `infra/`, `results/`, `debrief.md`, README progress table | Curriculum, briefs, reviews |
| User | Predictions + takeaways in lesson READMEs, `journal/`, `concepts/` | — |
| Both AIs | `STATE.md` (update "Turn" + "Next action" when handing off) | — |

Neither AI writes the user's predictions, takeaways, journal, or concept notes. Pointing out factual errors in them is fine.

## Lesson flow
1. **Teacher** runs `./scripts/new.sh lesson NN slug` if needed and writes `brief.md`. STATE turn → user.
2. **User** reads the brief and writes "My prediction" in the lesson README. STATE turn → executor.
3. **Executor** implements, runs, writes `debrief.md`. STATE turn → teacher.
4. **Teacher** reads debrief + prediction, writes `review.md` (corrections, explanation of gaps, quiz). STATE turn → user.
5. **User** writes takeaways, journal. Teacher plans the next lesson.

## Executor rules
- Start each session by reading `STATE.md` and the current lesson's `brief.md`.
- **No run without a prediction.** If "My prediction" in the lesson README is empty, stop and ask the user for it.
- Don't change curriculum order or invent lessons. If there's no brief, say so.
- All measurements go through `bench/`. Results files record env metadata (`bench.results.save` does this).
- If the brief's claims conflict with measurements, don't "fix" the measurement. Log it under Surprises in `debrief.md` and Open questions in `STATE.md`.
- Adapt reference code from briefs to the repo harness; don't paste it raw.
- Never commit weights, HF cache, or large outputs. Results stay small (json/csv/png).
- After a run: `debrief.md`, README progress table, `STATE.md`.
- The canonical workload in `bench/workload.py` is frozen once set. Changing it requires a decisions-log entry in `STATE.md`.
- No local GPU: heavy runs happen on RunPod (`infra/runpod/`).
