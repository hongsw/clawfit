# Research Watch: Mancode — Anti-Over-Engineering Coding Agent Harness

- Repo: https://github.com/whitelonng/mancode (⭐363)
- Source: GitHub search (agent harness, created 2026-06-27)

## Why this is worth watching
Most coding agent harnesses compete on capability surface area. Mancode takes the opposite position: its explicit design goal is preventing AI coding agents from over-engineering. Before executing any implementation task, agents must answer six constraint questions (what problem is being solved, can existing code be reused, what is the minimum viable change, can a new abstraction be avoided, what is the minimal verification path, what is unknown). This is a deliberate inversion of the "more tools, more autonomy" default — and it targets a documented failure mode (LLM bloat and unnecessary abstraction) that several enterprise teams have publicly flagged.

## What stands out immediately
- **Six-question anti-overengineering gate**: agents must answer: what problem, reuse existing?, minimum viable change, avoid new abstraction?, minimal verification, unknowns? — hardcoded constraint filter before code generation starts
- **Five-tier intensity modes**: `solo` (default, zero ceremony) → `/manba` (mid-intensity) → `/man` (full discipline: research, requirements clarification, approved plan, implementation, evidence-backed review, completion gates) → `/mansolo` (single-agent execution of a `/man`-approved plan) → `/manteam` (multi-agent team coordination via typed entity store); `/manps` for project health scans
- **Cross-session Continuity runtime**: persists TaskRefs, Context Packs, workflow artifacts, and team decisions across sessions to `.mancode/<namespace>/workflows/<ULID>/` — addresses context window loss without requiring a dedicated memory service
- **Built-in credential and PII scrubbing**: identifies credentials in logs/configs and generates redacted copies before sharing with models; local-only, no telemetry
- **Platform-agnostic overlay**: supports Claude Code, Cursor, Codex (ChatGPT Desktop), GitHub Copilot, ZCode, Kimi Code, Qoder, DeepSeek Harness — sits on top, does not replace
- **AGPL-3.0 license**: viral; enterprise deployment requires attention to license obligations
- 363 stars, TypeScript, npm-distributed; active as of 2026-10-07

## Why clawfit should care
Mancode represents an emerging sub-pattern within L2: harnesses that enforce *discipline constraints* rather than expanding agent capabilities. clawfit's current scoring model rewards capability breadth (`task` coverage, `hardware` support) but does not model the risk dimension of over-autonomy or over-engineering. The AGPL license also creates a deployment blocker for commercial contexts not present in the more common MIT/Apache harness licenses — a variable clawfit should track if it adds a `license_type` axis. The five-tier intensity model (solo → team) also parallels the `min_maturity` axis in clawfit's `recommend` output and could inform how harness recommendations change across maturity stages.

## Preliminary interpretation
- **L2 — Harness / Wrapper** (primary): discipline-enforcing overlay that structures agent behavior across coding agent runtimes
- **L3 — Team / SSOT Generator** (secondary): `/manteam` mode coordinates multi-agent decisions via a shared typed entity store

## Claims to verify
- Anti-overengineering gate effectiveness: anecdotal claim that the six-question pre-check reduces LLM bloat; no published benchmark comparing output quality or code diff size with/without the gate
- Cross-agent compatibility: claims support for 8 different coding agents (Claude Code, Cursor, Codex, etc.); compatibility is likely shallow (prompt-level, not API-level) — verify actual integration depth per agent
- AGPL-3.0 scope: because Mancode is a CLI tool that wraps other agents, the copyleft implications depend on whether it is classified as a library vs. an independent program; enterprise legal review needed

## Status
- 363 stars, 3.5 months old (created 2026-06-27)
- No registry entry warranted: harness tool, not an LLM or hardware entry; AGPL license limits registry use without commercial exception
- **First signal for "discipline-enforcement harness explicitly targeting LLM over-engineering"** in clawfit's research-watch corpus
- Monitor for: star growth beyond 1k, enterprise case studies, published comparison data, and any re-licensing to MIT/Apache
