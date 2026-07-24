# Research Watch: claude-thermos — Prompt Cache Warming Proxy for Multi-Agent Sessions

- Repo/Link: https://github.com/izeigerman/claude-thermos
- Source: Hacker News front page (57pts, Show HN, 2026-07-24)

## Why this is worth watching
Claude's prompt cache has a 5-minute TTL. In multi-agent sessions where a main agent waits on a long-running subagent, the cache expires silently — causing the entire conversation prefix to re-encode at 1.25× write cost instead of 0.1× read cost. claude-thermos inserts a transparent reverse proxy that detects this idle/active pattern and sends minimal "warm requests" (same cacheable prefix, `max_tokens: 1`) on sub-5-minute intervals to keep the prefix alive. Reported ~20% API cost savings.

## What stands out immediately
- **Local reverse proxy model**: sits between the agent CLI and Anthropic API, zero code changes required
- **Lineage tracking**: groups requests by model + tool-set + system prompt to identify distinct cacheable sessions
- **Idle detection**: only warms during the danger window (main agent idle, subagent active) — not continuously
- **Cost logging**: structured logs report saved token counts per session
- **No external dependencies**: lightweight Go/Python proxy; no cloud component

## Why clawfit should care
This is infrastructure-layer cost optimization specifically for the multi-agent harness use case. For teams running Claude Code Routines or DureClaw-style multi-agent workflows, cache warming could meaningfully reduce per-task costs. It represents an emerging "meta-infrastructure" category: tooling that optimizes the agent runtime itself rather than extending agent capability. clawfit currently has no way to represent "reduces operating cost of another tool" in org_fit metadata.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / Meta-Infrastructure** (proxy that optimizes multi-agent session cost)

Could also classify as Level 7 (interface utility) but the mechanism is harness-layer: it intercepts and modifies API traffic between agent runtime and LLM provider.

## Status
- First signal. 57 HN points; no GitHub star count available at time of writing.
- "When in doubt" rule applied — first signal, no canonical section change.
- Cost savings claim (~20%) requires independent verification across different session profiles.
- Represents a new sub-pattern: **cache-warming infrastructure** for idle-heavy multi-agent loops.
- Monitor for: adoption by Claude Code Routines users; integration into harness frameworks (DureClaw, CCPM, SuperClaude).
