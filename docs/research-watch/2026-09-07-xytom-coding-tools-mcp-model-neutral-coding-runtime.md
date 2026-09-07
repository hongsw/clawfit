# Research Watch: coding-tools-mcp — Model-Neutral Safe Coding Runtime over MCP

- Repo: https://github.com/xyTom/coding-tools-mcp (⭐1,009)
- Source: GitHub Trending Python (2026-09-07); WebSearch for MCP coding tools 2026
- Homepage: https://coding-1afcb9be.mintlify.app

## Why this is worth watching

coding-tools-mcp is a Python MCP server that gives any MCP-compatible agent access to 19 coding tools: file operations, shell execution, git commands, and language runtime management — all confined to a single declared workspace directory. What distinguishes it from the growing catalog of MCP coding tools is the explicit three-tier permission model (`safe` / `trusted` / `dangerous`) and OS-level sandboxing via Linux Landlock. This is not application-level path restriction — it is kernel-enforced filesystem confinement.

The multi-client positioning is also explicit in the documentation: Claude Desktop, Claude Code, Cursor, VS Code, Windsurf, Gemini CLI, and custom agents are all listed as supported clients with configuration snippets. The tool is explicitly model-neutral, which distinguishes it from skill packs that target a specific agent (OpenClaw skills, Anthropic skills, etc.).

Created 2026-05-21; Apache-2.0; available on PyPI and npm. Last pushed 2026-09-03.

## What stands out immediately

- **Three-tier permission model**: `safe` (read-only file access, no execution), `trusted` (full file operations + shell execution within workspace), `dangerous` (full access including cross-workspace operations); permission mode is declared at startup, not per-call
- **Landlock kernel confinement on Linux**: OS-enforced filesystem isolation in addition to the application-level workspace path restriction — agents in a containerized or multi-tenant environment get kernel-level guarantees, not just application-level promises
- **19 tools across 4 categories**: Files/Search (read, write, search, diff, find), Execution (shell, REPL sessions, long-running processes with PTY), Git (status, diff, commit, push, branch), Runtime (package install, language version check, environment inspect)
- **Context-efficient results**: paginated and summarized output reduces token consumption; long command output is chunked and can be requested page-by-page
- **Interactive sessions with PTY support**: agents can maintain persistent terminal sessions (useful for `pip install` + `python script.py` sequences that share environment state)
- **Remote deployment options**: HTTP tunneling (for remote agent access), Docker containerization, Cloudflare Workers sandbox — the tool is designed for cloud deployment, not just local developer use
- **dsh-plugin topic**: tagged as a `dsh-plugin`, suggesting integration with the `dsh` (developer shell hub) ecosystem, which is an additional distribution channel
- **169 forks relative to 1,009 stars (1:6 fork ratio)**: high fork ratio relative to stars suggests use in production toolchains, CI pipelines, or agent infrastructure rather than pure reference interest

## Why clawfit should care

1. **Model-neutrality as an explicit design goal distinguishes this from agent-specific skill packs**: clawfit's registry currently conflates "agent capability" (things an agent can do) with "agent-specific skill" (things a specific agent runtime exposes). coding-tools-mcp is a capability server that works identically for Claude Code, Cursor, and Gemini CLI — it is not a Claude skill or an OpenClaw plugin. A `capability_compatibility: [claude-only | openai-compatible | model-neutral]` dimension would surface these as a distinct category in recommendations.

2. **Permission tiers map directly to clawfit's existing `statefulness` and `network` filters but at finer granularity**: the three-tier permission model (safe/trusted/dangerous) is an orthogonal axis to current filters. A `safe`-mode deployment would be appropriate for untrusted code review tasks; `trusted` for standard development; `dangerous` for refactoring agents with broad file access. Current clawfit filters cannot express this distinction.

3. **OS-level sandboxing is a first signal in this log**: Landlock is the first kernel-enforced confinement mechanism documented in a research-watch entry. Prior security-related signals (METATRON, cve-mcp-server) addressed network isolation; coding-tools-mcp addresses filesystem isolation. For multi-tenant agent deployments where multiple users' agents run on shared infrastructure, kernel-level guarantees are the correct isolation primitive — application-level restrictions are bypassable by a sufficiently capable agent.

4. **Standard MCP coding server pattern confirmed by two independent implementations**: coding-tools-mcp (May 2026) and the model-neutral coding MCP described in OpenClaw's extension ecosystem are two independent implementations of the same concept: a standalone MCP server providing safe code execution for any agent. Two independent signals make this a confirmed sub-type of L4, distinct from agent-bundled execution environments.

## Preliminary interpretation

Current best reading:
- **Level 4 — Capabilities / Skills / MCP (primary)**: coding-tools-mcp is a capability server; it exposes file, execution, and git operations as MCP tools consumed by agents at inference time; it does not manage agent lifecycle or state
- **Level 2 — Harness / Wrapper Layer (secondary)**: the workspace confinement, permission tiers, and execution context management are harness-level concerns — they constrain what an agent can do and enforce operational boundaries, which is what a harness does

## Claims to verify

- Whether Landlock confinement is enabled by default or opt-in; Landlock requires Linux kernel ≥5.13 and explicit activation — the claim matters only if it's on by default in the Docker container
- Whether the `dangerous` permission mode actually bypasses cross-workspace restrictions or merely grants additional within-workspace capabilities; the naming is strong but the implementation scope matters
- Whether the PTY session management correctly handles agents that issue commands and then abandon the session (orphaned processes are a real concern in multi-agent deployments)
- Whether the Cloudflare Workers sandbox variant has meaningful execution time limits that would break long-running build tasks

## Status

- 1,009 stars (above research-watch threshold 100★; below registry threshold 5k★)
- Created 2026-05-21 (within 6-month window ✓); Apache-2.0; PyPI and npm distribution
- Not eligible for current registry: no schema slot for MCP capability servers; no deterministic per-execution cost (self-hosted tool, cost is local compute)
- First "model-neutral MCP coding runtime with OS-level sandboxing" signal in this log
- Watch: whether Landlock + HTTP tunnel deployment combination attracts enterprise adoption; whether star count grows past 2k as Windsurf and Gemini CLI users discover the multi-client positioning
