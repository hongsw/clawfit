# Research Watch: Apache Maka — Local-First AI Agent Workspace

- Repo/Link: https://github.com/apache/maka
- Source: GitHub Trending

## Why this is worth watching
Maka is an Apache-incubated local-first AI agent workspace that treats an append-only event log as the authoritative runtime state — not just a history. This "log as runtime" architecture separates execution evidence from model context, enabling verifiable audit trails, session branching, and context compaction without discarding facts. Apache incubation gives it institutional credibility despite its early star count.

## What stands out immediately
- **Append-only runtime event log** records every model message, tool call, result, permission grant, and event — SQLite-backed, permanent
- **Context compaction without data loss**: LLM context can be pruned/compacted, but the underlying log is never modified
- **Session branching and recovery**: execution can fork from any point in the log
- **Built-in evaluation framework** for reproducible benchmarks against the log
- **Multiple interfaces**: desktop Electron app, terminal UI, CLI — all backed by the same log
- **Local-first by default**: sessions, records, and artifacts stored on-machine; cloud APIs optional
- TypeScript, ~2,000★, 240 forks, Apache Incubating

## Why clawfit should care
The "log as runtime" pattern is architecturally distinct from existing harnesses (Claude Code, Cursor, Goose) which treat the conversation as ephemeral context. If this pattern gains adoption, clawfit's scoring may need a `audit_trail` or `execution_log` dimension — especially relevant for governance-heavy org profiles (`governance_need: hard`) where verifiable agent execution is required. The built-in evaluation framework also aligns with clawfit's upcoming benchmark-aware scoring roadmap.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness/Agent Workspace** (primary)
- **Level 5 — Evaluation** (secondary — built-in benchmark/reproducibility layer)

## Status
- Tracking: first signal 2026-08-22
- Stars below 5k registry threshold — hold registry entry
- Watch: Apache incubation momentum, adoption among governance-sensitive teams
- Schema signal: `execution_log_mode: [ephemeral | append-only | ...]; has_eval_framework: bool`
