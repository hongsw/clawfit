# Research Watch: Real-SWE — AI Benchmarking on Private Enterprise Codebases

- Repo/Link: https://withspecific.com/benchmarks/real-swe
- Source: Hacker News (78 pts, 54 comments)

## Why this is worth watching
Real-SWE benchmarks AI models against real-world private enterprise codebases — not curated public repos like SWE-bench. This directly addresses the known contamination and distribution gap in public coding benchmarks. For teams evaluating which AI coding agent to deploy, this is more ecologically valid signal than SWE-bench Verified or SWE-bench Pro.

## What stands out immediately
- Runs against private, non-public enterprise codebases to avoid training-set contamination
- Positions as a more honest signal for enterprise adopters than public benchmarks
- 54 HN comments indicates active community debate about benchmark validity
- Companion to the growing "eval reliability" discourse (SWE-bench-Pro, dreadnode contamination finding)

## Why clawfit should care
Clawfit's recommendation engine currently ranks coding agents partly on baseline performance. If Real-SWE becomes a trusted evaluation standard, its scores should feed into the scoring weights alongside SWE-bench numbers. It also suggests adding an `eval_source` metadata field to agents in the registry — distinguishing between public-benchmark-only and private-codebase-validated agents. For the org-fit model, teams with `data_sensitivity: confidential` would specifically value agents with Real-SWE scores over public-benchmark agents.

## Preliminary interpretation
Current best reading:
- **Level 5 — Evaluation / Benchmark Infrastructure**

## Status
- Tracking: new signal 2026-09-13; watch for published benchmark results and model rankings
