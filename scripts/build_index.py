#!/usr/bin/env python3
"""Regenerate data/tasks.jsonl from the task files.

The task files under tasks/ are the source of truth; the index is a derived,
machine-readable copy of the full dataset (one task per line, sorted by
task_id). Run this after any change to a task file, then run
scripts/validate.py.

Usage: python3 scripts/build_index.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

records = [
    json.loads(p.read_text()) for p in sorted(ROOT.glob("tasks/*/*/task.json"))
]
records.sort(key=lambda r: r["task_id"])
out = ROOT / "data/tasks.jsonl"
out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records))
print(f"wrote {out.relative_to(ROOT)}: {len(records)} tasks")
