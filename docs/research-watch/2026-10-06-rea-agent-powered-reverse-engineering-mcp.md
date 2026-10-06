# Research Watch: REA — Agent-Powered Reverse Engineering via MCP

- Repo: https://github.com/morluto/rea (⭐8.1k)
- Source: GitHub Trending (all languages, daily)

## Why this is worth watching
REA is an MIT-licensed MCP server + CLI framework that routes agent investigation requests through disassembly backends (Hopper, Ghidra, IDA Pro) to analyze binaries, Electron apps, .NET assemblies, Android APKs, websites, and firmware — without uploading targets to external services. The project is locally novel in the tracked corpus: prior MCP security tools (hexstrike-ai, agent-guard) target credential hygiene and pentesting automation; REA targets comprehension of opaque closed-source software. Its three-phase model (Decompile → Understand → Recreate) is a reusable workflow template for agent-driven code archaeology.

## What stands out immediately
- Unified MCP server routing across Hopper, Ghidra, IDA Pro — provider selection is automatic and session-bound
- Supports: Mach-O, ELF, PE binaries; JavaScript/Electron; .NET assemblies; Android APKs; websites; firmware
- Three-phase investigation model: decompile → understand → recreate — directly maps to agent task decomposition
- No external uploads — analysis stays local, which is the critical constraint for proprietary software targets
- 8.1k stars, 1,041 commits — not a prototype; indicates production adoption
- Works with: Claude Code, Codex, Cursor, Gemini CLI, Windsurf, Devin, GitHub Copilot CLI
- MIT license — permissive; compatible with enterprise air-gapped use

## Why clawfit should care
REA represents a class of agent capability tool not yet addressed in the taxonomy: **closed-source comprehension tooling**. Existing L4 tools in the tracked set mostly enhance agents with data access (internet search, financial APIs, knowledge graphs) or security offense/defense (hexstrike-ai, agent-guard). REA extends agent capabilities into reverse engineering and codebase understanding without source access — relevant to `task: code-gen` and `task: qa` on private or legacy software stacks. The local-execution model is also a strong `data_sensitivity: confidential` signal: no binary leaves the machine. The session-bound router pattern is worth watching as an architectural model for other multi-backend MCP servers.

## Preliminary interpretation
Current best reading:
- **L4 — Capability / MCP layer** (primary: MCP server providing reverse engineering capabilities to agents)
- **L2 — Harness / Wrapper layer** (secondary: CLI orchestration layer managing provider routing)

## Claims to verify
- "No external uploads" — the local claim is central to the privacy story; verify Hopper and Ghidra remain purely local
- Ghidra version pinned at 12.1.4 — check for compatibility issues with recent Ghidra releases
- IDA Pro integration described as "optional read-only" — confirm MCP server does not write IDA databases

## Status
- New signal 2026-10-06 — 8.1k stars, MIT license, active development; registry-ineligible (no deterministic cost data — it's infrastructure tooling, not a billable LLM/agent service); L4 taxonomy slot confirmed
