# Research Watch: DeepSWE — Contamination-Free Benchmark for Long-Horizon Coding Agents

- Repo/Link: https://datacurve.ai/blog/deepswe
- Source: Hacker News front page (2026-05-27)

## Why this is worth watching
SWE-bench has become the standard for coding agent evaluation but suffers from training-data contamination — models may have memorized issue resolutions during pre-training. DeepSWE proposes a contamination-free alternative targeting "long-horizon" tasks, which implies multi-step, stateful execution rather than single-pass code edits. This is the first high-signal benchmark explicitly framing agent evaluation around task horizon rather than just pass rate.

## What stands out immediately
- Contamination-free design: test cases are provably unseen by current frontier models
- "Long-horizon" framing: distinguishes from SWE-bench's patch-level tasks; implies multi-turn, multi-file, possibly multi-session execution
- Published by datacurve.ai (inference and data labeling tooling company)
- HN front page placement — visible to the practitioner community building and evaluating agents

## Why clawfit should care
- **L5 evaluation signal**: clawfit currently has no registry entries for agent benchmarks; DeepSWE's "long-horizon" framing maps directly onto clawfit's `statefulness` filter — a benchmark that penalizes stateless-only approaches could shift which agents score highest in clawfit recommendations
- **Task granularity signal**: "long-horizon coding" is a distinct task profile from one-shot `code-gen`; if this benchmark gains adoption it may support a future `task: backend-codegen` or `task: long-horizon-codegen` sub-type in clawfit schema (see also `2026-05-25-llm-constraint-decay-code-gen-limits.md`)
- **Scoring calibration input**: if agents like OpenHands or Goose are independently benchmarked on DeepSWE, those results should inform `baseline_score` values in `llms.json` and registry `comparison_priority` rankings

## Preliminary interpretation
Current best reading:
- **Level 5 — Agent evaluation / benchmarking**

Adjacent signal: `2026-05-25-llm-constraint-decay-code-gen-limits.md` (also from HN, also frames code-gen task as too coarse a category). Two independent benchmark signals in 2 days pointing at the same gap strengthens the case for a `backend-codegen` or `long-horizon-codegen` task sub-type at the next schema revision.

## Status
- Held: not a registry candidate by type (benchmark, not an agent/harness/hardware)
- Map mutation deferred: single signal for contamination-free long-horizon benchmark; need independent reproduction or star count before adding to L5 section of reference-levels.md
- Flag: if a second independent contamination-free coding agent benchmark appears (≥500 HN pts or ≥2k★), consider adding a named L5 sub-type note for "contamination-free long-horizon eval"
