# Research Watch: ModelsThatRun — Open Model Hardware Benchmark Site

- Repo/Link: https://modelsthatrun.dev
- Source: GeekNews (Show GN)

## Why this is worth watching
ModelsThatRun publishes measured inference speed, VRAM use, accuracy, and license data for open models on a single RTX 4090, making hardware-model fit comparisons concrete and reproducible. The "Show GN" framing confirms community interest in this exact problem. It directly addresses the same decision clawfit is trying to automate: given my hardware constraints, which open model is worth running?

## What stands out immediately
- Single consistent hardware baseline (RTX 4090) makes cross-model comparison meaningful
- Covers VRAM, tokens/sec, and accuracy — three of the four axes clawfit uses for LLM hardware matching
- Includes license data — governance-relevant for enterprise and confidential workloads
- Not a leaderboard focused on frontier models; explicitly open-weights focus

## Why clawfit should care
clawfit's hardware scoring currently relies on registry-specified constraints (min_vram, etc.), but ModelsThatRun provides empirical throughput data that could validate or update those entries. It is also a potential reference source for `hardware.json` and `llms.json` accuracy baselines. More broadly, if this site achieves adoption, users may reference it when asking clawfit questions — aligning clawfit's data to it reduces friction.

## Preliminary interpretation
Current best reading:
- **Reference data source** — not a Level 1–7 tool itself, but feeds the registry evidence layer documented in `docs/reference-notes/evidence-schema.md`

## Status
- Tracking: new signal 2026-11-14; evaluate for data import into hardware/llm registry entries
