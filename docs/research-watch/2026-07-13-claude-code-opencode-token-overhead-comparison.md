# Research Watch: Claude Code vs OpenCode Token Overhead Analysis

- Repo/Link: https://systima.ai/blog/claude-code-vs-opencode-token-overhead
- Source: Hacker News (#7, 427 points, 238 comments — 2026-07-12)

## Why this is worth watching

Systima used a logging proxy to intercept raw API payloads and isolate token overhead by category — the most granular baseline-cost breakdown of Claude Code vs OpenCode published to date. The gap (33k vs 7k tokens before the user prompt is even read) is large enough to reorder cost-axis recommendations for any short-to-medium coding task, independent of per-token price. At 427 HN points this is the highest-signal cost methodology post since the Reflex computer-use benchmark (412 points, 2026-05-06).

## What stands out immediately

- **Measurement:** logging proxy captures raw JSON payloads; variables added progressively in isolation — more rigorous than anecdotal comparisons
- **Tool schema count is the dominant driver:** Claude Code ships 27 tools (~24k schema tokens); OpenCode ships 10 (~4.8k) — a 5× tool-count gap before any configuration
- **Instruction file multiplier:** CLAUDE.md/AGENTS.md adds ~20k tokens per request — a per-call cost, not amortized
- **MCP overhead:** ~1–1.4k tokens per connected server; five servers add 5–7k tokens above baseline
- **Subagent chaining tax:** a task costing 121k tokens direct cost 513k tokens via two subagents — each subagent pays its own full bootstrap
- **Cache invalidation gap:** Claude Code triggered 5.9×–54× more cache-prefix rewrites than OpenCode (claim to inspect: harness behavior vs. API-gateway behavior)
- **Quality parity noted** on benchmarked tasks; reasoning-heavy tasks excluded

## Why clawfit should care

Token overhead is a hidden cost multiplier that clawfit's current scoring does not model. The effective cost per task is `price/token × tokens/task`, and on short tasks the bootstrap term dominates. Three concrete gaps:

1. `monthly_budget: low` scoring uses per-token price but not per-session bootstrap cost
2. MCP server count is not tracked in the registry; each connected server inflates cost silently  
3. Subagent-capable agents carry a per-subagent bootstrap tax unmodeled in the cartesian product scorer

Claim to inspect: Systima serves regulated-industry clients and may favor leaner tooling — independent replication of the 33k/7k figures is needed before use as hard scoring parameters.

## Preliminary interpretation

Current best reading:
- **Level 2 — Meta wrappers / harnesses / orchestration layers** (overhead is a structural property of harness design: system prompt architecture, tool schema count, subagent dispatch cost)
- Secondary: **Level 5 — Memory / MCP / context layer** (MCP tool-schema and instruction-file inflation are L5-adjacent drivers)
- Architectural cost-axis signal — not a tool; do not register

## Status

- Signal logged 2026-07-13; no registry or reference-levels.md change
- Schema watch: `bootstrap_token_cost` per agent; `mcp_server_count` as cost multiplier input
- Flag for scoring analyst: `monthly_budget: low` profiles should surface bootstrap overhead warnings for high-tool-count or MCP-heavy agent configurations
