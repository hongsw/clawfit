# Research Watch: Meta Muse Code

- Repo/Link: https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2
- Source: Hacker News (145 pts, 2026-08-06)

## Why this is worth watching
Meta shipped Muse Code (public beta, August 5, 2026) — a terminal coding agent powered by their new Muse Spark 1.2 model with a 1M-token context window. This is Meta's first direct entry into the AI coding agent market, competing head-to-head with Claude Code and OpenAI Codex. Unlike LLM releases, this is a complete agentic product: it plans changes, writes code, validates results, and runs parallel worker + reviewer agents per task. Available on macOS and Linux with a single install command.

## What stands out immediately
- Persistent async background agents: multiple parallel workers + background reviewers per task
- 1M-token context window allows long-horizon tasks in a single session
- Contributor pricing tier: significantly cheaper rates in exchange for helping train the model
- Meta Superintelligence Labs (formerly FAIR) is the research org behind it
- Direct terminal CLI ergonomics — same UX niche as Claude Code
- No IDE dependency; runs as a standalone terminal agent

## Why clawfit should care
Muse Code is a direct competitor to the core tools in clawfit's coding agent registry (Claude Code, OpenCode, Aider, Cline, Goose). Its contributor pricing model is structurally novel: lower cost in exchange for training data contribution, which may suit individual developers but raises privacy considerations for enterprise users (`data_sensitivity: confidential` profiles should score this lower). The 1M-context window may affect latency scoring. Add to registry once billing/latency data becomes available.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base Coding Agent Runtime** (terminal CLI, persistent async agents, backed by proprietary model)

## Status
- Public beta, macOS + Linux. First signal.
- Registry candidate once stable pricing/latency data is available.
- Schema watch: `contributor_pricing_model: bool` (opt-in cheaper tier with training data trade-off)
