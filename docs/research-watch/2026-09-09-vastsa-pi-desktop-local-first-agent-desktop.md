# Research Watch: PI-Desktop — Local-First AI Coding Agent Desktop

- Repo: https://github.com/vastsa/PI-Desktop (⭐1,567)
- Source: GitHub Trending (today, +393 stars)

## Why this is worth watching
PI-Desktop is a cross-platform desktop application ("Electron + Rust host core + pi Agent Harness + user-installable plugins") providing a standalone workspace for coding agents, projects, models, tools, and long-running sessions. At version 0.14.x in "Early Preview," it is actively maintained (2,032 commits) and gaining momentum. It occupies the "native desktop agent IDE" slot that Cursor and Windsurf hold for AI-augmented editors — but PI-Desktop's framing is agent-first rather than editor-first: three modes are Agent, Plan, and Goal.

## What stands out immediately
- Electron + Rust core combination — UI flexibility + performance-sensitive process management in native code
- Three operational modes: Agent (autonomous), Plan (review before execute), Goal (high-level objective decomposition)
- Extensibility via four separate primitives: Skills, MCP servers, Subagents, and Plugins — each independently composable
- Multi-provider: OpenAI, Anthropic, local models, OpenAI-compatible APIs
- Permission-aware: code review capabilities, explicit agent action approval gates
- Local data storage — no mandatory account, no relay service; data-sensitive profiles can use it without egress
- Cross-platform: macOS, Windows, Linux
- LGPL-3.0 license — allows commercial use with open core disclosure requirements
- 2,032 commits, still "Early Preview" — suggests sustained development predating the current visibility burst

## Why clawfit should care
PI-Desktop is the first desktop-native agent workspace in this scan log that explicitly separates Agent/Plan/Goal operational modes as first-class user-facing concepts. The Plan mode (human reviews before execute) directly implements the human-approval pattern that appeared as a design signal in trueforge (2026-09-02) and AAS v17 (2026-09-08) — but here it is a per-session toggle at the desktop application layer rather than a skill-level or harness-level gate.

The Skills + MCP + Subagents + Plugins composition model means PI-Desktop is a potential host for any L4 capability (skills, MCP servers) without routing through a browser or CLI session. For `data_sensitivity: confidential` or `governance_need: hard` profiles that cannot use cloud-hosted agent workspaces, PI-Desktop's local storage + permission gates + local model support makes it a structurally distinct option from Cursor/Windsurf/Claude Code.

clawfit has no `desktop_app` agent type; PI-Desktop's architecture would require a new schema field to distinguish from CLI agents and browser-based agents.

## Preliminary interpretation
- **Level 2 — Harness / Wrapper Layer** (primary: desktop agent harness with permission model)
- **Level 4 — Capabilities / Skills** (secondary: Skills + MCP + Plugin composition)

The Rust core for process management is L1-adjacent (inference substrate) but PI-Desktop does not own inference — it delegates to the configured model provider. L2 is the appropriate primary level.

## Claims to verify
- "Early Preview" at 0.14.x with 2,032 commits — unusual for a preview; confirm whether earlier commits are from a different project base or pre-cursor work
- LGPL-3.0 commercial implications — verify whether the plugin interface is covered or only the core
- Local model support — confirm supported backends (Ollama? llama.cpp? LM Studio?) and whether local inference is fully functional vs. experimental
- Rust core scope — what specifically runs in Rust vs. Electron/Node? Process isolation? Sandboxing?

## Status
- New — tracking as first desktop-native agent workspace with explicit Agent/Plan/Goal modes in this scan log
- Star count: 1,567 (above 100-star threshold; below 5k for registry)
- Registry eligibility: blocked (below 5k threshold; no `desktop_app` schema slot; no deterministic cost/latency data independent of chosen model provider)
