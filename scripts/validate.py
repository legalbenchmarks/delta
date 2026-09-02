#!/usr/bin/env python3
"""Validate the dataset. Runs offline, no dependencies, exits non-zero on any error.

Checks, in order:
  1. Every tasks/<area>/<slug>/task.json parses and matches the schema.
  2. task_id equals its directory path.
  3. Every task has a valid task horizon and ISO legal-review cut-off date.
  4. Every title, prompt, practice area, and criterion is complete in both
     Dutch and English.
  5. Dutch pass criteria start with "PASS als"; English with "PASS if".
  6. Criterion IDs are unique within a task and use the C-/S-/F- convention
     matching their type (citation, substance, form).
  7. Substance and form criteria carry valid descriptive dimensions; citation
     criteria do not duplicate their type with dimension metadata.
  8. Every criterion carries lawyer_validated: true.
  9. data/tasks.jsonl agrees byte-for-byte with the task files (regenerate it
     with scripts/build_index.py if this fails).

Usage: python3 scripts/validate.py
"""
import json
import pathlib
import re
import sys
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent.parent
TYPES = {"substance": "S-", "citation": "C-", "form": "F-"}
DIMENSIONS = {
    "substance": {"legal_correctness", "legal_judgment"},
    "form": {"style", "usability"},
}
REQUIRED_DIMENSIONS = {
    "substance": "legal_correctness",
    "form": "usability",
}
ID_RE = re.compile(r"^[CSF]-\d{3}$")
TASK_HORIZONS = {"short", "medium", "long"}

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def check_task(path: pathlib.Path) -> dict | None:
    rel = path.relative_to(ROOT)
    try:
        t = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        err(f"{rel}: invalid JSON ({e})")
        return None

    expected_id = "/".join(path.parent.parts[-2:])
    if t.get("task_id") != expected_id:
        err(f"{rel}: task_id {t.get('task_id')!r} does not match path {expected_id!r}")

    for field in ("jurisdiction", "normative_language"):
        if not t.get(field):
            err(f"{rel}: missing {field}")
    if t.get("normative_language") != "nl":
        err(f"{rel}: normative_language must be 'nl'")

    if t.get("task_horizon") not in TASK_HORIZONS:
        err(f"{rel}: task_horizon must be one of {sorted(TASK_HORIZONS)}")
    law_as_of = t.get("law_as_of")
    try:
        date.fromisoformat(law_as_of)
    except (TypeError, ValueError):
        err(f"{rel}: law_as_of must be an ISO date in YYYY-MM-DD format")

    for field in ("title", "prompt", "practice_area"):
        block = t.get(field) or {}
        if not isinstance(block, dict):
            err(f"{rel}: {field} must be an object with 'nl' and 'en' keys")
            continue
        for lang in ("nl", "en"):
            if not (block.get(lang) or "").strip():
                err(f"{rel}: {field}.{lang} is missing or empty")

    seen_ids: set[str] = set()
    for criterion in t.get("criteria") or []:
        cid = criterion.get("id", "?")
        where = f"{rel} {cid}"
        if cid in seen_ids:
            err(f"{where}: duplicate criterion id")
        seen_ids.add(cid)
        if not ID_RE.match(cid):
            err(f"{where}: id must match C-/S-/F- followed by three digits")
        ctype = criterion.get("type")
        if ctype not in TYPES:
            err(f"{where}: type must be one of {sorted(TYPES)}")
        elif not cid.startswith(TYPES[ctype]):
            err(f"{where}: id prefix does not match type {ctype!r}")
        if ctype == "citation":
            if "dimensions" in criterion:
                err(f"{where}: citation criteria must not carry dimensions")
        elif ctype in DIMENSIONS:
            dimensions = criterion.get("dimensions")
            if not isinstance(dimensions, list) or not dimensions:
                err(f"{where}: dimensions must be a non-empty list")
            else:
                if len(dimensions) != len(set(dimensions)):
                    err(f"{where}: dimensions must not contain duplicates")
                invalid = set(dimensions) - DIMENSIONS[ctype]
                if invalid:
                    err(f"{where}: invalid dimensions for {ctype}: {sorted(invalid)}")
                required = REQUIRED_DIMENSIONS[ctype]
                if required not in dimensions:
                    err(f"{where}: {ctype} criteria must include {required!r}")
        if criterion.get("lawyer_validated") is not True:
            err(f"{where}: lawyer_validated must be true")
        crit = criterion.get("pass_criteria") or {}
        nl, en = (crit.get("nl") or "").strip(), (crit.get("en") or "").strip()
        if not nl.startswith("PASS als"):
            err(f"{where}: Dutch pass_criteria must start with 'PASS als'")
        if not en.startswith("PASS if"):
            err(f"{where}: English pass_criteria must start with 'PASS if'")
        if ctype == "citation" and not criterion.get("cited_authority"):
            warnings.append(f"{where}: citation criterion without cited_authority")
    if not t.get("criteria"):
        err(f"{rel}: no criteria")
    return t


def main() -> int:
    task_files = sorted(ROOT.glob("tasks/*/*/task.json"))
    if not task_files:
        err("no task files found under tasks/")
    records = [t for p in task_files if (t := check_task(p)) is not None]

    index_path = ROOT / "data/tasks.jsonl"
    if not index_path.exists():
        err("data/tasks.jsonl is missing")
    elif not errors:
        expected = "".join(
            json.dumps(r, ensure_ascii=False) + "\n"
            for r in sorted(records, key=lambda r: r["task_id"])
        )
        if index_path.read_text() != expected:
            err("data/tasks.jsonl is out of date; run scripts/build_index.py")

    n = sum(len(r.get("criteria") or []) for r in records)
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"{len(records)} tasks, {n} criteria, "
          f"{len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
