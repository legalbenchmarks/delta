# Contributing

Contributions are open to everyone: lawyers, engineers, researchers, students. You do not need permission to start, and no contribution is too small.

## Ways to contribute

### 1. Dispute a criterion

If you believe a criterion misstates Dutch law, is ambiguous, or is unfair to grade against, open an issue using the **Criterion dispute** template. Include:

- the `task_id` and criterion `id`;
- what you believe is wrong;
- the authorities that support your position (statute articles, ECLI numbers).

Disputes are the most valuable form of quality control this set can get.

### 2. Improve wording or translations

Typos, clearer phrasing, better English reference translations: open a PR directly. The Dutch text is normative, so a change to `pass_criteria.nl` is a substantive change (see versioning below), while a change to `pass_criteria.en` is not.

### 3. Add a task

New Dutch legal research tasks grow the set for everyone. A good task is:

- a research question a Dutch lawyer would field in practice;
- grounded in authoritative legal sources and capable of fair binary grading, including where more than one professionally defensible conclusion exists;
- self-contained: the prompt alone is enough to answer, no attachments needed;
- coverable by binary criteria: each one a single verifiable criterion.

Create `tasks/<practice-area>/<short-descriptive-slug>/task.json`:

```jsonc
{
  "task_id": "<practice-area>/<short-descriptive-slug>",
  "jurisdiction": "NL",
  "normative_language": "nl",
  "task_horizon": "short",
  "law_as_of": "YYYY-MM-DD",
  "practice_area": { "nl": "…", "en": "…" },
  "title":  { "nl": "…", "en": "…" },
  "prompt": { "nl": "…", "en": "…" },
  "criteria": [
    {
      "id": "S-001",                    // C- citation, S- substance, F- form
      "type": "substance",              // must match the id prefix
      "dimensions": ["legal_correctness", "legal_judgment"],
      "pass_criteria": {
        "nl": "PASS als …",             // must start with "PASS als"
        "en": "PASS if …"               // must start with "PASS if"
      },
      "lawyer_validated": true,
      "cited_authority": "…"            // for citation criteria
    }
  ]
}
```

Rules for good criteria:

- **One PASS or FAIL question per criterion.** A criterion may have several elements when the legal test itself is cumulative, but it must stay a single yes-or-no question. If it tests two independent things, split it into two criteria.
- **Accommodate defensible approaches.** Where multiple approaches are professionally defensible, state the common minimum requirements and the accepted alternatives.
- **Keep substance and form separate.** Substance criteria must not penalise harmless stylistic variation. Form criteria may codify an explicit practitioner preference about presentation, such as putting the answer first, when it is observable and published. They must not assess substantive legal correctness or permit a judge to add an unstated personal preference.
- **Use dimensions descriptively.** Every substance criterion includes `legal_correctness` and may also include `legal_judgment`; every form criterion includes `usability` and may also include `style`. Citation criteria omit `dimensions` because their `citation` type already states what they measure. Dimensions do not add a grading requirement beyond the written criterion.
- **Verifiable from the answer text alone.** A judge must be able to point to the passage that satisfies it.
- **Cite the controlling authority** for citation criteria: ECLI, reporter reference, or statute article.
- **No real client material.** Tasks must be based on public law, not confidential matters.

Set `task_horizon` to `short`, `medium`, or `long` to describe the scope of the assignment rather than its difficulty. Record the legal-research and review cut-off in `law_as_of` using `YYYY-MM-DD`. For historical fact patterns, the legally relevant date may be earlier than this research cut-off.

## Before you open a PR

```bash
python3 scripts/build_index.py   # regenerate data/tasks.jsonl from the task files
python3 scripts/validate.py      # must print 0 errors
```

CI runs the same validator on every PR.

## Review and versioning

Task and criterion content is legal content, so PRs that touch it are reviewed for legal accuracy as well as format, with input from practising Dutch lawyers where needed. This can take longer than ordinary code review.

Every accepted change to task content bumps the dataset version and gets a [CHANGELOG.md](CHANGELOG.md) entry:

- **Major**: tasks added or removed;
- **Minor**: criteria added, removed, or substantively revised (including changes to `pass_criteria.nl`);
- **Patch**: wording, translation, or metadata fixes that do not change what any criterion tests.

This way, any published result can always name the exact version it was measured on.
