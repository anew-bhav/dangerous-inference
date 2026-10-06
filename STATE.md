# STATE

> Both Claude Code sessions (teacher in `teacher/`, executor at root) read this first.
> Trust this file over either session's memory. Update "Turn" + "Next action" on every handoff.

- **Turn:** teacher
- **Day:** 1
- **Date started:** 2026-10-06
- **Current lesson:** none yet
- **Next action:** teacher drafts lesson 00 from what's already been covered (user brings a summary from the old session), picks the canonical workload

## Done
- Repo scaffolded

## Canonical benchmark workload
_Not decided yet._ Teacher picks it; it gets fixed in `bench/workload.py` and must not change after that, or the journey chart stops being comparable.
- Model:
- GPU:
- Prompt tokens / new tokens / batch:

## Open questions
<!-- Things teacher said vs things we measured that disagree, unexplained results, etc. -->
-

## Decisions log
- 2026-10-06: Stack = PyTorch + HF transformers, uv, RunPod for GPU.
