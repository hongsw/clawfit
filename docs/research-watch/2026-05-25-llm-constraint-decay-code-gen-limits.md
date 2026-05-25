# Research Watch: LLM Constraint Decay in Code Generation

- Repo/Link: https://arxiv.org/abs/2605.06445
- Source: Hacker News front page (156 points)

## Why this is worth watching
Empirical evidence of a specific failure mode in LLM code generation: "constraint decay" — as structural requirements accumulate, agent pass rates drop ~30 points from baseline on average, with weaker configurations approaching near-zero. 80 greenfield + 20 feature-implementation tasks across 8 web frameworks. This is directly relevant to clawfit's `task: code-gen` scoring dimension.

## What stands out immediately
- **Constraint decay**: performance drops ~30 assertion pass-rate points when moving from baseline to fully-specified tasks
- **Framework sensitivity**: agents succeed with minimal-convention frameworks (Flask) but fail substantially in convention-heavy environments (FastAPI, Django)
- **Root cause**: data-layer defects dominate — incorrect query composition and ORM runtime violations
- 100 benchmark tasks total; 8 web frameworks covered; both behavioral and static verification
- HN 156 points; peer-reviewed arxiv preprint

## Why clawfit should care
The scoring model currently treats `task: code-gen` as a monolithic category. This paper shows that code-gen performance is highly heterogeneous by framework complexity and constraint count. Implications: (1) tools scoring well on simple code-gen (solo_dev_codegen profile) may not score well on production backend generation; (2) the `setup_complexity` and `min_maturity` fields in the registry indirectly capture this — high setup_complexity tools may actually be better suited for constraint-heavy scenarios; (3) a `task: backend-codegen` or `task: constrained-codegen` sub-type is worth considering.

## Preliminary interpretation
Current best reading:
- **Level 5 — Evaluation/benchmark signal** (empirical benchmark revealing a structural limitation in L1/L2 coding agents across all frameworks tested)

Not a tool — this is a research paper. Relevant to the scoring-analyst role: the `task: code-gen` category may need sub-typing before the next major scoring revision.

## Status
- No registry entry (paper, not a tool)
- Flag for scoring-analyst: constraint decay evidence suggests `task: code-gen` is too coarse; a `task: backend-codegen` sub-type would better surface tools optimized for production-scale constraint satisfaction
- Promotion threshold for schema change: a second independent paper or benchmark corroborating the framework-sensitivity dimension, or a production incident report from a major coding agent
