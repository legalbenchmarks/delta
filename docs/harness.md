# Harness

A harness runs each task against the system you are testing and records the answers. It can be twenty lines of Python or a full platform. What matters is that results are **attributable** (differences come from the system, not your setup), **auditable** (every step is recorded), and **reproducible** (someone else can run the same thing).

The system under test can be anything that answers a legal research question in writing: a model, a legal AI product with its own retrieval, or a human baseline. If the system uses retrieval or web search, leave it on; measure the system as it would actually be used.

## Rules

1. **Use the fixed system prompt below.** The prompt is two messages: the fixed system prompt, identical for every system and every task, plus `prompt.nl` verbatim as the user message. The Dutch text is the task; `prompt.en` is a reference translation, not an alternative input.
2. **Never include the criteria.** Grading happens outside the harness. A system that saw the criteria would be answering a different question than one that did not.
3. **No substitution.** An answer attributed to system A must come from system A. If a run fails, record the failure with its reason; do not silently retry with a different model or downgraded settings.
4. **Every attempt starts fresh**, with no memory of other tasks or attempts.
5. **Same limits for everyone.** Whatever time or token limits you set, apply them identically to every system. Report a limit-stopped or truncated answer with its stop reason; never pass it off as an ordinary answer.
6. **Record everything, overwrite nothing.** Keep the verbatim answer, the parameters you requested and the parameters actually applied, timestamps, and the sources the system saw. Every attempt gets its own record.
7. **Run the whole set, twice.** Results over a subset are not comparable with results over the set. Run the complete task set twice, collect each run independently, and average the two. Always record the dataset version (see [CHANGELOG.md](../CHANGELOG.md)).

## Fixed system prompt

Send this text verbatim as the system message:

> You are an experienced legal practitioner producing the deliverable named in the user's instructions. Return the deliverable as the body of your reply in plain text or markdown (do NOT base64-encode or attach a file). Aim for the quality and detail expected of a senior associate.

The task-specific criteria remain hidden from the system under test and are applied only during grading. The form criteria publish the professional delivery preferences against which the answer is reviewed; the harness does not coach a system criterion by criterion.

## Suggested record

One answer per line, with enough metadata to reproduce the run:

```jsonc
{
  "task_id": "tort-law/duty-to-warn",
  "dataset_version": "1.1.0",
  "system": "my-product-2026-08",
  "run": 1,
  "answer": "…full verbatim output…"
}
```

## A minimal harness pattern

```python
import json

FIXED_SYSTEM_PROMPT = """You are an experienced legal practitioner producing the deliverable named in the user's instructions. Return the deliverable as the body of your reply in plain text or markdown (do NOT base64-encode or attach a file). Aim for the quality and detail expected of a senior associate."""

tasks = [json.loads(line) for line in open("data/tasks.jsonl")]
with open("answers.jsonl", "w") as out:
    for run in (1, 2):
        for task in tasks:
            answer = my_system(
                system=FIXED_SYSTEM_PROMPT,
                user=task["prompt"]["nl"],
            )
            out.write(json.dumps({
                "task_id": task["task_id"],
                "dataset_version": "1.1.0",
                "system": "my-system",
                "run": run,
                "answer": answer,
            }, ensure_ascii=False) + "\n")
```

Grading the answers is the second half of the job: see [judge.md](judge.md).
