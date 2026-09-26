# Research Watch: Ollaya — Local Decision Model Runtime

- Repo/Link: https://ollaya.dev
- Source: Hacker News front page (300 points)

## Why this is worth watching
Ollaya positions itself as "Ollama for open-source, Jev-style decision models" — a locally-run inference daemon that manages download, versioning, and serving of structured-output decision models. This is the first tracked tool that explicitly targets Jev-class typed decision models as a first-class runtime primitive rather than wrapping a general LLM. If the Jev pattern produces a standard inference protocol, Ollaya is the closest thing to a reference implementation of that protocol's server side.

## What stands out immediately
- Explicitly Jev-positioned: no free-text generation, only ranked probability outputs and typed decisions
- Ollama-style UX: pull model → serve → call; no Python environment required
- 300 HN points on front page indicates practitioner curiosity at meaningful scale
- Self-hosted, local-first, no cloud dependency; same governance posture as Ollama
- Decision model served as a local API endpoint — drop-in for coding agent tool-selection or routing

## Why clawfit should care
This is the **seventh cross-date signal** for the Jev/typed-decision-model pattern (TypeSafe Jev 2026-09-16, OpenJev 2026-09-19, ConvAI RL-NAR 2026-09-20, Kev 2026-09-22, JevBench 2026-09-23, agent-jev 2026-09-23, Ollaya today). It is also the **first signal for a dedicated local serving runtime for decision models** — structurally distinct from model weights or benchmarks. If this category grows, clawfit's hardware.json may need a `local-decision-runtime` deployment mode, and the org_fit scoring could surface Ollaya-compatible stacks for offline + confidential + governance-hard profiles.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base Agent Runtime** (decision model inference substrate)
- Secondary: **Level 4** (structured tool-call capability provider)

## Status
- Monitoring: no GitHub repo URL confirmed yet; tracking at ecosystem level
- Below 5k★ registry threshold; deferred pending confirmed repo and star count
- Jev pattern now at 7 signals from 6 organizations; canonical promotion assessment warranted
