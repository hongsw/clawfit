# Research Watch: FrontierHarness Eval — 9-Harness Comparative Benchmark

- Repo/Link: https://frontierharness.org
- Source: Hacker News (36 points, 2026-09-02): "Show HN: FrontierHarness Eval – 9 harness, same model, cost per pass varies 17x"

## Why this is worth watching

FrontierHarness Eval is the first published benchmark that holds model, infrastructure, and task set constant while varying only the harness layer — and measures pass rate, cost per task, and execution speed across all three dimensions simultaneously. The headline finding ("cost per pass varies 17x across harnesses") directly challenges the common assumption that harness choice is an ergonomics decision rather than an economic one. For any tool — clawfit included — that helps users select an agent stack, a dataset showing 17x cost variation at constant quality is primary evidence that the selection layer matters.

## What stands out immediately

- **Controlled experiment methodology**: all 360 trials start from identical fresh checkpoint restores on fixed vCPU/memory/disk allocations via Runta's infrastructure — warm-cache bias and resource variation are explicitly eliminated, which is harder to achieve than it sounds in distributed execution environments
- **9 harnesses across 12 configurations** tested: Codex leads on quality (66.7% pass rate), Exo Harness leads on cost ($1.05/task), DSH Minimal leads on speed (5m 41s median runtime) — no single winner across all three dimensions
- **17x cost range**: the spread implies that harness selection is a first-order economic decision, not a second-order optimization; this is not driven by model differences
- **Same model across all runs**: Kimi K3 was used as the fixed model — isolating harness contribution to cost and quality from model contribution; choice of Kimi K3 (not GPT-5 or Claude Opus 5) may affect generalizability
- **Terminal/coding task focus**: evaluation is limited to "software engineering contexts and terminal-based tasks" — the authors explicitly acknowledge this scope limit, unlike most benchmark papers that bury caveats
- **No provider neutrality claim**: Runta (the infrastructure provider) ran the evaluation; potential conflict of interest is not disclosed in the methodology section
- **Top cost leader ($1.05/task)**: if confirmed at production load, this is a specific, falsifiable number that clawfit's `budget` filter could reference once the harness is mappable to a registry entry

## Why clawfit should care

clawfit's scoring weights latency at 0.5 and cost at 0.25, but both weights were calibrated on model-level data — not harness-level variation. FrontierHarness Eval is direct empirical evidence that harness choice affects cost as much or more than model choice in comparable task contexts. A 17x cost spread across harnesses, on the same model, means the current scoring model underweights harness selection.

The benchmark also surfaces a practical tension: the quality leader (Codex, 66.7%) and the cost leader (Exo Harness, $1.05/task) are not the same system. clawfit's recommendation output should ideally surface this tradeoff explicitly rather than collapsing quality and cost into a single fit score.

The controlled methodology (identical checkpoint restores, fixed resource allocation, same model) is the kind of evidence clawfit's scoring calibration should eventually rely on, not self-reported latency from vendor documentation. This is the first signal in this research-watch log from an independent third-party benchmarking effort at the harness layer.

## Preliminary interpretation

Current best reading:
- **Level 5 — Memory/Observability/Evaluation** (primary): this is an evaluation contribution, measuring observable outcomes across harness configurations; it is not a harness, model, or capability itself
- Secondary signal for **Level 2** (the harnesses being evaluated are L2 systems): the benchmark characterizes the L2 layer empirically

## Claims to verify

- Whether the Runta infrastructure provider introduces any systematic advantage for harnesses that are Runta-native or Runta-optimized — the methodology section does not address this
- Whether the 17x cost ratio holds across other model choices (Kimi K3 may have unusual caching or tokenization behavior that amplifies harness cost differences vs. other models)
- Whether "cost per task" includes model inference cost, infrastructure cost, or both — this distinction determines whether the numbers are comparable across deployments
- Whether the quality measure (pass rate) uses the same test cases and grader for all 9 harnesses, or whether some harnesses were evaluated on easier task subsets
- Whether the 360-trial sample size (roughly 40 trials per harness) is sufficient to distinguish genuine differences from statistical noise, particularly for the lower-performing harnesses
- Whether the speed comparison is wall-clock or CPU-time — harnesses that parallelize heavily may show misleadingly low wall-clock times on high-core-count infrastructure

## Status

- Research signal only; no registry entry (benchmarking project, not a harness/agent/LLM)
- First published multi-harness comparative benchmark with controlled infrastructure methodology
- Directly relevant to clawfit scoring calibration: if the 17x cost finding is independently replicated, the `cost` weight (currently 0.25) should reflect harness-level variation, not only model-level variation
- Watch: whether methodology and raw data are published; whether independent replication confirms the 17x cost range; whether Runta conflict-of-interest is addressed in a follow-up
