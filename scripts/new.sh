#!/usr/bin/env bash
# Scaffold a new lesson or journal entry from templates/.
#   ./scripts/new.sh lesson 01 kv-cache
#   ./scripts/new.sh journal
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
START_DATE="2026-10-06"

case "${1:-}" in
  lesson)
    num="${2:?lesson number required}"; slug="${3:?lesson slug required}"
    dir="$ROOT/lessons/${num}-${slug}"
    [[ -e "$dir" ]] && { echo "exists: $dir"; exit 1; }
    mkdir -p "$dir/results"
    sed "s/NN/${num}/; s/<name>/${slug}/" "$ROOT/templates/brief.md" > "$dir/brief.md"
    sed "s/NN/${num}/; s/<name>/${slug}/" "$ROOT/templates/lesson-README.md" > "$dir/README.md"
    sed "s/NN/${num}/; s/<name>/${slug}/" "$ROOT/templates/debrief.md" > "$dir/debrief.md"
    sed "s/NN/${num}/; s/<name>/${slug}/" "$ROOT/templates/review.md" > "$dir/review.md"
    touch "$dir/results/.gitkeep"
    echo "created $dir"
    ;;
  journal)
    today="$(date +%F)"
    day=$(( ( $(date -d "$today" +%s) - $(date -d "$START_DATE" +%s) ) / 86400 + 1 ))
    file="$ROOT/journal/day-$(printf '%03d' "$day").md"
    [[ -e "$file" ]] && { echo "exists: $file"; exit 0; }
    sed "s/NNN/$(printf '%03d' "$day")/; s/YYYY-MM-DD/${today}/" "$ROOT/templates/journal.md" > "$file"
    echo "created $file"
    ;;
  *)
    echo "usage: $0 lesson <NN> <slug> | journal"; exit 1 ;;
esac
