# Research Watch: Empirical Study on Coding Agent Harness Design

- Repo/Link: https://arxiv.org/abs/2609.20804
- Source: GeekNews (front page, item #1 — 2026-09-20)

## Why this is worth watching
A formal empirical study testing 176 harness configurations across 4 models and 2 coding benchmarks — varying planning strategies, tool composition, and context management. It directly probes the question HarnessTax (2026-09-19) raised informally: does harness design matter independently of model choice? An academic paper with this scope is a methodological anchor for clawfit's harness cost and fit scoring.

## What stands out immediately
- 176 configurations evaluated (planning, tool composition, context management as independent axes)
- 4 models tested, 2 benchmarks — suggests cross-model validity claims
- Specifically isolates harness configuration as the variable, not model capability
- Appeared as GeekNews #1 on 2026-09-20; no star count (preprint, no code repo confirmed)

## Why clawfit should care
- **Second signal** for "harness design overhead independent of model" (HarnessTax 2026-09-19 was first signal, empirical site; this is a peer-reviewed-track empirical study)
- Both signals confirm the same hypothesis: harness configuration choices carry significant cost/performance trade-offs independent of LLM pricing
- Validates `harness_overhead: [low | medium | high]` axis candidate raised by HarnessTax
- If planning strategy and context management are major variables, clawfit's current scoring treats them as fixed per tool — a gap this paper quantifies
- Direct relevance to scoring dimension weighting (latency, cost, fit score)

## Preliminary interpretation
Current best reading:
- **Level 5 — Evaluation / Benchmark infrastructure** (primary)
- L2 secondary: findings feed directly back into harness/SDK design choices

## Status
- Monitoring; arxiv preprint (no confirmed code repo or tool release)
- Cross-date two-signal pattern confirmed for "harness-layer cost/performance variability": HarnessTax (2026-09-19) + this study (2026-09-20)
- Axis candidate `harness_overhead` now has two independent signals; not yet at three-signal canonical promotion threshold
