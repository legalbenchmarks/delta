# Judge

A judge grades each answer against the task's criteria. This document follows the same principles as Legal Benchmarks' [public methodology](https://www.legalbenchmarks.ai/methodology).

## Two axes, never blended

Quality is reported on two independent axes, substance and form, kept separate rather than blended into a single score. An output can be polished but legally unreliable, or substantively strong but poorly presented; reporting the axes separately preserves that distinction.

In this dataset:

- **Substance axis**: the substance criteria (is the work correct, complete, and responsive) and the citation criteria (does it cite the controlling statute or case).
- **Form axis**: the form criteria (could a practitioner use the answer as delivered).

Substance includes legal judgment: selecting and applying the relevant law, handling uncertainty, and reaching a professionally defensible conclusion. Form assesses the observable delivery of that judgment, including prioritisation, proportionality, appropriate qualification, structure, and placement of authority.

The optional second level is recorded in each non-citation criterion's `dimensions` field: `legal_correctness` and `legal_judgment` for substance, and `style` and `usability` for form. These are descriptive labels for analysis and reporting. They are not separate requirements: do not include them in the judge prompt; judges grade only the written criterion.

Grade the axes independently: a judge grading substance should not see form verdicts, and vice versa.

## Grading

Every criterion is a fixed binary pass/fail question:

1. **Apply the criteria as written.** The judge answers one question per criterion: does this answer satisfy this criterion, PASS or FAIL. An explicit professional preference in a form criterion is part of the grading standard and must be applied. Do not add a preference that the criterion does not state.
2. **The Dutch text controls.** Grade against `pass_criteria.nl`. The English text is a reference translation for human reviewers, not the standard.
3. **Grade the submission, blind.** Judges grade the final answer, blind to the reasoning that produced it and without knowing which system produced it.
4. **The criteria accommodate defensible approaches.** Legal work does not always have a single acceptable answer. Where several approaches are professionally defensible, the criteria are written to accommodate them while identifying the specific omissions and errors that should fail. Grade what the criterion says, not your own taste.

If an answer takes a potentially defensible approach that a criterion does not clearly address, log the issue for qualified human review rather than treating novelty alone as a failure. If the approach is accepted, revise the criterion in the next dataset version.

## Judge setup

LLM judges work well on this format if the setup keeps them honest:

- **Use more than one judge, from more than one model family.** A single judge inherits a single model's blind spots. Cross-family judges, grading independently and blind, are the floor for publishable results; neither judge should see the other's scores or comments.
- **Log disagreements.** Any disagreement that could change whether a task passes should be escalated to a qualified lawyer for a final, binding determination. The lawyer reviews the output blind, and the human determination takes precedence and is preserved for audit.
- **Spot-check with humans.** Have practitioners spot-check judge verdicts on a sample of every run, and carry confirmed corrections into the published scores.
- **Watch for favoritism.** If a judge model grades answers produced by its own maker's models, check whether it scores them higher.

## Metrics

Two metrics, always reported per axis and together with the dataset version and run count:

- **Criteria met**: the percentage of criteria satisfied.
- **Task pass rate**: the percentage of tasks for which every criterion was satisfied. A task passes only when all criteria are met, so this is a deliberately hard metric; report both so readers see the difference between mostly right and right.

Do not blend the axes into a single total. Publish the per-axis numbers, the version, the run count, and a description of your judge setup, so others can reproduce and challenge your findings.

## Disputes

If grading exposes a criterion you believe is legally wrong, that is a contribution: open a dispute issue with your authorities. See [CONTRIBUTING.md](../CONTRIBUTING.md).
