# Research Watch: uber/ADR — Enterprise AI Agent Detection and Response

- Repo: https://github.com/uber/ADR (⭐605)
- Source: GitHub Trending Python #1 (140 stars/day, 2026-08-04); MLSys 2026 accepted paper

## Why this is worth watching

ADR is Uber's production security system for AI coding agents, open-sourced with an accompanying MLSys 2026 paper. It addresses a gap that existing registry entries do not: most security tooling for AI agents targets prompt injection defense or sandboxing at the input layer. ADR operates at a different level — monitoring what agents actually *do* across their full execution lifecycle (tool calls, file writes, network requests, process spawns) and flagging behavioral anomalies against a threat baseline.

The fact that Uber ships this internally against their own use of Claude Code and Cursor is a meaningful signal. It is not a research prototype claiming agent security; it is a production system that secured employee-facing agents before it was open-sourced.

## What stands out immediately

- **Four-layer architecture:** observability (telemetry collection across 7+ AI coding tools on macOS, Linux, Windows), benchmarking (300+ adversarial tasks covering 17 attack techniques across 133 MCP servers), threat detection (two-tier: high-recall screener + deep-reasoning classifier), and prevention (not yet open-sourced)
- **ADR-Bench:** 300+ security tasks and 133 MCP server configurations form the most comprehensive public benchmark for AI agent attack surface evaluation seen in the corpus so far
- **Platform breadth:** sensor captures activity from Claude Code, Cursor, Codex, and 4+ additional tools — not tied to a single agent vendor
- **MLSys 2026 acceptance:** peer-reviewed, not just a blog post; methodology reproducibility is claimed in the repo
- **Production provenance:** deployed by Uber before open-source release; not a greenfield research demo
- **Apache 2.0 license:** commercially deployable without license friction

## Why clawfit should care

No existing registry entry captures agent security observability as a capability layer. The closest signals are MAI-Cyber-1/MDASH (Microsoft, 2026-07-27 — model + harness for vulnerability identification) and T3MP3ST (2026-07-29 — red-team meta-harness). ADR is structurally different: it is not an offensive security tool and is not a vulnerability scanner; it is a defensive monitoring and response layer for organizations that run coding agents internally.

For clawfit's `governance_need: hard` persona, ADR answers the question "once I deploy Claude Code for my engineers, how do I detect if it does something it shouldn't?" The 133 MCP server coverage in ADR-Bench also provides indirect evidence that the MCP tool saturation risk (flagged by graph-tool-call 2026-08-03) is a verified production attack surface — 133 is not a research abstraction, it is the number of servers Uber's benchmark treats as a threat surface.

Schema gap: `defensive_security_layer: bool` — no current mechanism to distinguish tools that protect agents from tools that enable agents. Also: `security_benchmark: str` (e.g., `ADR-Bench: 300 tasks / 17 attack techniques`).

## Preliminary interpretation

- **Level 5 — Observability / evaluation layer** (primary: ADR-Sensor captures full agent execution telemetry)
- Secondary: **Level 2 — Harness** (ADR-Bench evaluates harness-level attack surface; prevention layer integrates into the agent execution path)
- Cross-cutting: security governance signal — first open-source "defensive monitoring for enterprise AI coding agents" entry in the corpus

## Claims to verify

- **300 tasks / 133 MCP servers / 17 attack techniques:** check ADR-Bench folder for actual counts; these are specific and verifiable from the repo
- **MLSys 2026 paper:** verify acceptance — not yet confirmed via official MLSys program
- **Prevention layer:** only mentioned, not open-sourced — verify whether the detection layer alone is useful without it
- **7+ coding tools supported:** verify full list; Claude Code and Cursor are named, others need confirmation
- **Reproducibility claim:** paper claims reproducible; check if benchmarks can be run without Uber infrastructure

## Status

- First signal for "defensive enterprise AI agent observability" sub-type
- 605 stars meets threshold; credible org (Uber) and MLSys 2026 paper strengthen it
- No registry entry: no deterministic cost/latency data; `task: security-monitoring` dimension absent
- Schema watch: `defensive_security_layer: bool`; `security_benchmark: str`; `agent_telemetry_platforms: [list]`
- Cross-watch: ADR-Bench's 133-MCP-server coverage pairs with graph-tool-call (2026-08-03) MCP tool saturation signal — two independent confirmations that 100+ MCP configurations is a realistic production threat surface
