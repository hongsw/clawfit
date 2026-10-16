# Research Watch: ARTEMIS — Android Automation Agent with MCP Integration

- Repo: https://github.com/google/artemis (⭐12,021)
- Source: GitHub Trending Python (221 stars today)

## Why this is worth watching
ARTEMIS is Google's open-source tool for driving Android phones and emulators from natural-language instructions, with a native Model Context Protocol (MCP) server that makes Android automation callable from AI coding agents (Claude Code, Windsurf, and similar tools). The MCP integration is the key signal: Android automation moves from a standalone test-automation tool to a live capability any agent runtime can invoke. At 12k stars and trending on GitHub Python, this has reached a traction level that warrants ecosystem tracking.

## What stands out immediately
- Native MCP server exposes Android device control as an agent-callable tool surface — any agent with MCP support gains access to Android automation without custom integration
- Two execution profiles: "Flash" (3–5s per step, reactive tasks) and "Pro" (15–40s per step, multi-agent planning with Planner/Operator/Checker architecture) — the architecture directly mirrors general agent patterns now applied to mobile UIs
- Vendor-reported 99%+ task completion on Google Research's AndroidWorld benchmark (unverified independently)
- Multimodal targeting: element indices + coordinate fallback + visual fallback; the layered fallback is notable because Android UI layouts are inconsistent across devices and app versions
- Action bursts: chaining transient UI actions without an additional model turn reduces per-action latency for sequences like scroll-tap-type
- Multi-model support: Gemini, Claude, Qwen — model-agnostic at the driver layer
- Compressed, searchable session history for long-running automations, which addresses context window pressure for multi-step flows

## Why clawfit should care
This is the first tracked signal for "Android automation as a native agent capability layer." The MCP integration pattern is architecturally different from prior mobile automation tools: rather than a standalone agent for mobile, it is a capability surface that any agent runtime can consume via MCP. This is consistent with the L4c pattern (capability/tool surface), not L1 (base runtime).

For clawfit's recommendation engine: `primary_task: mobile-dev` is already a known gap in org_questions.json (flagged 2026-10-10). ARTEMIS adds a second dimension: not just "building mobile apps" but "operating mobile interfaces as part of agentic workflows" — QA automation, device testing, mobile UI interaction as a task step. These are related but distinct task types that share the `mobile-dev` gap.

The Google provenance is relevant: unlike community mobile automation projects, ARTEMIS has enterprise-grade test infrastructure investment (AndroidWorld benchmark, Logcat integration, accessibility tree reading with UIAutomator2 fallback). This reduces the risk of early abandonment.

## Preliminary interpretation
Current best reading:
- **Level 4c primary — Tool-use / MCP / capability surface**: ARTEMIS exposes Android device control as an MCP-callable tool; any agent runtime gains mobile automation capability by connecting to it
- **Level 1 secondary** — the "Pro" execution profile includes its own Planner/Operator/Checker multi-agent architecture, which is a lightweight agent runtime for mobile task decomposition

## Claims to verify
- 99%+ AndroidWorld benchmark claim (vendor-reported; independent reproductions not found at time of tracking)
- Production stability on physical devices vs. emulators (page describes both but reliability at scale is unconfirmed)
- MCP server stability for long-running sessions (Flash vs Pro profile behavior under session interruption)
- Whether the "Google" repo namespace implies ongoing engineering commitment or a research release without production support

## Status
- 12,021 stars, growing; Google Apache 2.0 license
- Registry entry: candidate if `primary_task: mobile-automation` or an expanded `mobile-dev` task type is added to schema; org_fit mapping not clear under current fields
- 📡 note: second signal for `mobile-dev` task gap; ARTEMIS is specifically about operating mobile interfaces, not building apps — the task type distinction matters for org_questions.json
