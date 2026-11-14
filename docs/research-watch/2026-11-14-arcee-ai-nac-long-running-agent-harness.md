# Research Watch: nac — Long-Running Agent Goal-Alignment Harness

- Repo/Link: https://github.com/arcee-ai/nac
- Source: GeekNews

## Why this is worth watching
Most agent harnesses focus on short-horizon task execution, but nac (by Arcee AI) targets the other end: experiments, training runs, and other work that spans hours or days. It introduces a central orchestrator that continuously re-checks whether ongoing work is still aligned with the original goal — essentially a steering layer above the execution layer. This is a meaningfully different architectural concern from tool-calling orchestration.

## What stands out immediately
- Applies to long-running background jobs (training, experiments, batch pipelines), not just interactive sessions
- Central orchestrator pattern: single component responsible for goal-drift detection
- Open-source from Arcee AI, a team known for fine-tuning and instruction-following models
- Surfaced on GeekNews as a "Show GN" — practical adoption interest, not purely research

## Why clawfit should care
clawfit currently models agent harnesses primarily as interactive coding orchestrators (Level 2). nac expands the category to include long-horizon autonomy — a distinct statefulness/execution-mode axis. The `statefulness` field in clawfit's recommendation model (session vs stateless) doesn't yet capture "persistent background worker with drift correction"; nac is evidence that this axis matters. Also relevant to the `org_fit.tasks` taxonomy: "orchestration" may need a sub-dimension distinguishing short-session from long-horizon execution.

## Preliminary interpretation
Current best reading:
- **Level 2 — Agent Harness / Wrapper Layer** (long-horizon variant)

## Status
- Tracking: new signal 2026-11-14; watch for adoption reports and harness comparisons
