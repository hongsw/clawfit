# Research Watch: Taskhand — Local AI Windows Task Automation

- Repo/Link: https://news.hada.io/topic?id=37312
- Source: GeekNews

## Why this is worth watching
Taskhand is a free Windows automation tool that learns repetitive web and file tasks from a single user demonstration, using built-in local AI to generalize and replay them. This is the "low-code RPA" pattern applied to AI — no cloud dependency, no data leaving the device, one-shot learning from demonstration.

## What stands out immediately
- Learns from a single demonstration (record-and-replay with local AI generalization)
- Local AI inference only — no cloud, no network required for execution
- Targets web + file task automation on Windows desktops
- Free tier with no signup, targeting solo developers and power users

## Why clawfit should care
This is a signal for the growing `offline` / `confidential` local agent tier. Taskhand fills a gap between full coding agents (Goose, Aider) and no-code RPA tools (Power Automate) — it's aimed at developers who want automation without writing agent harness code. If added to registry, it would fit the `offline_mid_codegen`/`process-automation` task type. The `network: offline` and `setup_complexity: low` profile makes it relevant for the enterprise confidential-data segment clawfit currently underserves.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness/Wrapper (local execution, desktop automation)**

## Status
- Tracking; early signal from GeekNews — no GitHub link found yet, checking adoption trajectory
