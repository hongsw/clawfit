# Research Watch: Parsimony — Code Volume Benchmark for AI Models

- Repo/Link: https://parsimony.lasu.dev/
- Source: Hacker News

## Why this is worth watching
Parsimony measures how much extra code AI models add when completing a task — a dimension absent from capability benchmarks like SWE-bench. As agentic coding tools mature, code bloat and over-generation are real operational costs; a benchmark that quantifies this fills a genuine gap. It surfaced on HN with 33 points and generated immediate practitioner discussion.

## What stands out immediately
- Open-source benchmark; measures code _volume_ added per solved task, not just pass/fail
- Targets the "AI writes more code but not more software" problem documented in concurrent research
- Provides per-model comparisons — useful for picking leaner agents for cost-sensitive orgs
- Complements SWE-bench (correctness) with an efficiency axis

## Why clawfit should care
clawfit scores agents on latency, cost, and LLM preference but has no "output leanness" dimension. Parsimony's methodology could inform a new scoring axis for organizations where codebase maintainability matters. Results also provide evidence for adjusting `org_fit` weights for tools that tend to over-generate.

## Preliminary interpretation
Current best reading:
- **Level 2 — Evaluation / Benchmark Layer**: a measurement instrument for coding agents, not an agent itself.

## Status
- Tracking; evaluate for a future `code_leanness` scoring dimension
