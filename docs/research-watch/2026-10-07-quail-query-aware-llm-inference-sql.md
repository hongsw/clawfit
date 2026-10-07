# Research Watch: Quail — Query-Aware LLM Inference for AI-SQL

- Repo/Link: https://github.com/fsdatalab/quail
- Blog: https://fsdatalab.github.io/blog/introducing-quail/
- Source: GeekNews front page

## Why this is worth watching
Quail jointly optimizes SQL query planning and open-weight LLM inference to minimize redundant KV cache computation across large document batches. It achieves 1.84× average speedup vs. tuned vLLM baselines (up to 14× on specific workloads), which signals that the query-planning and inference layers are not yet efficiently co-designed in mainstream stacks.

## What stands out immediately
- Joint optimizer: treats SQL operator ordering and KV-cache scheduling as one problem, not two
- KV regret metric: formalizes the cost of cache misses across document batches (a new vocabulary for optimization)
- 29 benchmark queries across classification and relationship-detection tasks
- MIT license, academic research origin (fsdatalab), designed for open-weight models only
- No proprietary API — runs on local GPU infrastructure

## Why clawfit should care
This is infrastructure that lives one layer below the harness (L7), between the agent and the inference runtime. If adopted, it would change cost and latency profiles for batch-heavy coding agents running document classification or codebase analysis. Relevant to `clawfit`'s `latency` and `budget` dimension calibration: batch workloads on local hardware may be faster and cheaper than current registry assumptions suggest.

## Preliminary interpretation
Current best reading:
- **Level 7 — Inference / Execution Infrastructure** (primary)
- **Level 4 — Tool/Capability Layer** (secondary: touches KV cache management, a capability concern)

## Status
- First signal for "query-aware joint optimization of SQL query planning and LLM inference"
- Monitoring: star count not yet confirmed; academic origin suggests slow but sustained adoption trajectory
- Registry entry: not warranted yet (no billable service, no deployable agent entry; academic stage)
