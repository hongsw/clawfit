# Research Watch: OpenMausBot — Multi-Model Agent Harness with Per-Bot VM Isolation

- Repo: https://github.com/milind-soni/OpenMausBot (⭐16.7k)
- Source: GitHub Trending (all languages), daily

## Why this is worth watching
OpenMausBot is a self-hosted multi-model agent harness where each AI "bot" runs via a locally installed CLI agent (Claude Code, Codex, Grok CLI). The architectural claim is per-bot VM isolation: each bot gets its own cloud computer and connected apps, so compromised tool access or runaway tool calls are contained to that VM. This is architecturally distinct from multi-agent orchestrators like LangGraph or Bee Agent, which run models as library calls inside a shared process. The isolation model is structural, not advisory.

## What stands out immediately
- Each bot maps to a specific installed CLI agent (Claude Code, Codex, Grok) — the harness composes existing runtimes rather than reimplementing one
- Per-bot VM boundary: compromised MCP server or runaway tool call is contained by OS-level isolation, not soft guardrails
- Apache 2.0 license — commercially usable without restrictions
- 16.7k stars; not affiliated with xAI or Manus despite naming similarity to "Manus" bot class
- Integrates "connected apps" per bot — implies per-VM MCP or OAuth scoping, not global credential store
- Explicit self-hosted posture — no cloud gateway required, comparable to Open Duet in deployment model
- README describes it as an alternative to Grok Bot (xAI's commercial offering) — positions it in the multi-model consumer-harness market

## Why clawfit should care
clawfit scores tools on `network: local | cloud` and `statefulness` but has no axis for *isolation model* — whether agent tool access is OS-isolated per agent or shared across all agents in a session. OpenMausBot is the first signal for per-bot VM isolation as a first-class design choice in a consumer-grade multi-model harness (as opposed to enterprise CUA frameworks like AutoCua). If this pattern propagates to other harnesses, a `isolation: shared | process | vm` scoring dimension becomes defensible. Also relevant: existing clawfit registry entries (Claude Code, Codex, Goose) would score differently when run inside a VM-isolated harness like OpenMausBot vs. their standalone configurations.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / Orchestration Layer** (multi-model CLI composition sub-type)
- Secondary: L7 (infrastructure) — per-bot VM provisioning is non-trivial infra

## Claims to verify
- Actual VM isolation mechanism: container, full VM, or marketing language for process isolation?
- "Connected apps" scope: is MCP credential isolation enforced at the VM boundary or at the app level?
- Star velocity: 16.7k total or just today? If total, adoption is significant; if today, may reflect trending burst
- Self-reported as "not affiliated with xAI" — worth confirming the project is genuinely independent

## Status
- First signal for per-bot VM isolation in a consumer-grade multi-model agent harness
- Registry action: candidate pending star count and isolation mechanism verification; meets star threshold (>5k if total); cost/latency data unavailable (self-hosted, variable)
