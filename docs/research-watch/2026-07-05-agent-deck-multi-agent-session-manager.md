# Research Watch: agent-deck — Terminal Session Manager ("Mission Control") for AI Coding Agents

- Repo: https://github.com/asheshgoplani/agent-deck (432★ at time of capture; source signal claimed 46.4k — see Star Provenance note below)
- Also see: https://github.com/asheshgoplani/agent-deck/blob/main/README.md

## Why this is worth watching

agent-deck is a Go-native TUI session manager that wraps multiple concurrent AI coding agent sessions (Claude Code, Gemini CLI, OpenCode, Codex, Copilot, Cursor) behind a single tmux-backed terminal interface. Its architectural distinctiveness lies not in the multiplexing itself — tmux wrappers exist — but in two AI-specific additions: MCP socket pooling across sessions (shared Unix-socket processes with crash recovery), and the Conductor pattern (a designated persistent agent session that monitors other sessions and auto-responds or escalates). At 344 releases and v1.9.73 (June 21 2026), development cadence is high for a solo-maintained utility. Whether the star count represents the claimed 46.4k or the 432 visible on the repo page is the primary claim requiring independent verification before any threshold-based evaluation.

## What stands out immediately

- **Conductor pattern:** A named architectural concept where one persistent agent session is designated to watch, auto-respond, and escalate on behalf of all other sessions. This is structurally distinct from simple session multiplexing — the Conductor is itself an agent instance with its own identity file, state, and task log under `~/.local/share/agent-deck/conductor/`
- **MCP socket pooling:** Optional (`pool_all = true`) mechanism that shares MCP processes across sessions via Unix sockets. Vendor-claimed 85-90% MCP memory reduction and 3-second crash-recovery via reconnecting proxy — both vendor-authored metrics, not independently replicated
- **Session forking with context inheritance:** `f` key creates a new branch preserving conversation context, git worktree, uncommitted changes, and Docker isolation settings; supported for Claude Code, OpenCode, Pi, and Codex
- **Per-group Claude config:** Different session groups can authenticate against separate Claude accounts, enabling account-partitioned workloads in a single terminal
- **Telegram/Slack bot integration for Conductor:** One-to-one bot-per-conductor constraint is documented as intentional to prevent competing long-poll consumers — this level of async notification routing is unusual in terminal-layer tooling
- **tmux-backend with non-interference design:** Sessions use `agentdeck_*` naming prefix; existing tmux sessions are left untouched; optional dedicated tmux socket for full isolation
- **Go (86.9%), MIT license, SQLite persistence, Bubble Tea TUI:** Stack is consistent with the Go-native harness trend (go-micro tracked 2026-07-01); MIT and stdlib-adjacent dependencies lower adoption friction
- **Star provenance discrepancy:** Source signal cited 46.4k stars; the repo badge and public star count show 432 — a 100x gap that is unexplained. Either the signal source was erroneous, aggregated a fork network, or the count reflects a renamed or moved repository

## Why clawfit should care

clawfit tracks harnesses and wrappers at L2, but all current L2 entries are SDK-level or framework-level (LangChain deepagents, strands-agents, go-micro, Apache Burr, revfactory/harness). agent-deck introduces a different architectural sub-type: **terminal-session-level multi-agent harness** — the coordination layer operates in the terminal process manager, not in a Python/Go SDK called by a single agent. This is closer to cmux (terminal-multiplexed UX, tracked 2026-04-28) than to deepagents, but agent-deck adds active AI-awareness (session state detection, MCP lifecycle, Conductor orchestration) that cmux does not claim.

The MCP socket pooling claim is directly relevant to clawfit's scoring: if shared MCP processes reduce memory footprint 85-90% across concurrent sessions, `hardware: local` profiles with constrained RAM benefit materially. This claim needs independent replication before influencing scoring weights, but the problem it addresses — MCP process proliferation under multi-session workloads — is real and not currently modeled.

The Conductor pattern is architecturally adjacent to L3 (team harness/governance): a persistent orchestrator-agent that routes, monitors, and escalates is a governance pattern, not only a session management pattern. If the Conductor can enforce policy (e.g., block certain tool calls) rather than only notify, the L3 boundary becomes relevant. The current README describes notification/escalation behavior only, not blocking behavior.

## Preliminary interpretation

Current best reading:
- **Level 2 primary — Meta-wrapper / harness / orchestration layer** (terminal-session-level multi-agent coordinator; wraps L1 base runtimes — Claude Code, Gemini CLI, OpenCode, Codex — without replacing them; adds MCP lifecycle management, session forking, and Conductor meta-session orchestration on top of tmux)
- **Level 6 secondary — Human interface layer** (TUI is the HCI surface; Telegram/Slack Conductor integration extends human-agent interaction into async messaging channels)
- Not L3 primary: Conductor currently auto-responds and escalates, but no policy enforcement or blocking capability documented — the governance-gate characteristic is absent

Notable sub-type candidate: **terminal-session-level multi-agent harness** — distinct from SDK harnesses (L2 mainstream) by operating at the process/terminal layer rather than the library layer. Second independent signal needed before naming this sub-type formally.

## Claims to verify

- Star count: 432 visible vs. 46.4k cited in source signal — primary verification required before any threshold evaluation
- "85-90% MCP memory reduction" from socket pooling — vendor-authored metric; no third-party benchmark cited
- "3-second MCP crash recovery" — measurable but unverified; depends on session configuration and MCP server behavior
- Conductor auto-response: what agent model and prompt drives it? README references identity files and task logs but does not specify whether the Conductor uses the same underlying LLM as child sessions
- "Partial integration" for OpenCode, Codex, Copilot, Cursor — exact capability gaps relative to "full integration" (Claude Code, Gemini CLI) are not enumerated in the README

## Status

- Star count disputed (432 vs. 46.4k) — threshold evaluation blocked until discrepancy resolved
- First signal for terminal-session-level multi-agent harness sub-type; Conductor pattern is a named architectural concept not previously tracked in this taxonomy
- No map mutation: star provenance unresolved; single signal; MCP pooling claim unverified
- Promotion criterion: star count independently confirmed at ≥5k OR MCP socket pooling independently benchmarked AND a second terminal-session-layer multi-agent manager with comparable AI-awareness appears
