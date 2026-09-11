# Research Watch: Dan Luu — How Well Do Coding Agents Use Testing?

- Repo/Link: https://danluu.com/agentic-testing/
- Source: GeekNews (2026-09-11)

## Why this is worth watching
Dan Luu is a high-signal technical blogger whose empirical analyses have historically preceded mainstream acknowledgment of engineering problems. His investigation of whether coding agents actually apply test and verification techniques — not whether they can, but whether they do — fills a gap that benchmarks like SWE-Bench don't address: task completion vs. engineering discipline.

## What stands out immediately
- Framed around concrete implementation tasks (e.g., a Rust project), not toy problems
- Asks whether agents proactively write tests, use property-based testing, add assertions, verify intermediate states
- Complements SWE-Bench Pro Verified (tracked 2026-09-10) — both expose evaluation blind spots
- No GitHub repo; the artifact is the analysis itself

## Why clawfit should care
clawfit scores tools on task fit (code-gen, qa) but does not currently model "engineering discipline" as a scoring dimension. If leading coding agents routinely skip testing practices even when capable, the `qa` task label in org_fit may be overstated for several registry entries. This is an evaluation signal that could inform a future `code_quality_discipline` dimension.

## Preliminary interpretation
Current best reading:
- **Level 5 — Evaluation / Benchmarks** (empirical analysis of agent behavior quality)

## Status
- Read and assess; if findings align with registry entries for top coding agents, consider whether `tasks: ["qa"]` claims need annotation
