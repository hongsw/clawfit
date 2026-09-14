# Research Watch: KiroCrew — Daemon-Mode Persistent Agent Workspace

- Repo: https://github.com/kirodotdev/KiroCrew (⭐3,900)
- Source: GitHub topics/ai-agent (updated 2026-09-14), confirmed trending
- Stars: 3,900 | Forks: 580 | Commits: 6,166 on main
- License: Apache 2.0
- Language: Python

## Why this is worth watching

KiroCrew is the first harness tracked in this log that explicitly models itself as a **daemon process** rather than an IDE extension, chat plugin, or CLI wrapper. Its persistence model — a Gateway process that survives restarts and accumulates workspace memory — is architecturally distinct from Claude Code, Cline, Aider, and every other L2 harness currently in the clawfit registry. The self-improvement claim ("corrections become durable lessons; patterns become reusable skills") is structurally similar to the Procedural Graphs self-modifying execution pattern tracked 2026-09-10, but applied to long-lived operational memory rather than single-run graph topology.

The Agent Client Protocol (ACP) it uses to drive `kiro-cli` is new to this log and is worth tracking as either a de facto inter-agent protocol or a proprietary interface — the distinction matters for interoperability scoring.

## What stands out immediately

- **Daemon architecture**: Runs as a background Gateway process, not within an IDE session; agent state persists across restarts, login sessions, and hardware reboots
- **Self-improvement loop**: Three-component mechanism — (1) correction→lesson persistence, (2) pattern→reusable-skill synthesis, (3) semantic embedding memory — none of which reset between sessions
- **ACP (Agent Client Protocol)**: Drives `kiro-cli` via ACP rather than direct model calls; not MCP — a distinct named protocol whose specification scope is unconfirmed
- **Scheduled/unattended execution**: `kirocrew cron`, webhook triggers, and messaging-channel events enable fully unattended operation
- **Checkpointed long tasks**: Long-running work resumes from validated checkpoints on failure, not from scratch
- **Multi-surface continuity**: Same agent state accessible via desktop app, web dashboard, CLI, Slack, Discord, Telegram, Teams, Webex, iMessage — 8+ surfaces sharing one workspace
- **OS sandboxing**: Linux namespaces and macOS Seatbelt for `kiro-cli` isolation; sensitive path blocking and credential redaction built in
- **MCP compatibility**: Supports MCP servers alongside its own ACP, meaning it can consume the L4 ecosystem without replacing it

## Why clawfit should care

The daemon model introduces a `persistence_model` axis that current scoring does not capture. Today, all tracked harnesses are session-scoped: they start, run a task, and stop. KiroCrew's memory accumulates across sessions, which has direct implications for:

1. **Governance profiles** (`governance_need: hard`): A harness that retains lessons indefinitely — including from mistakes or corrected misbehavior — represents a new risk surface not modeled in current filters. Durable lesson memory is also an audit challenge.
2. **Latency scoring**: Daemon-mode execution implies warm start times are effectively zero for recurring tasks — this breaks the current latency scoring assumption that each recommendation starts cold.
3. **Statefulness dimension**: The current `statefulness` filter has `session` and `stateless` values. KiroCrew is structurally `persistent` — a third value not in the current schema.
4. **Multi-surface continuity**: No current agent in the registry claims this property. Org profiles that need agent access from multiple channels (Slack + CLI + web dashboard) have no way to express this need today.

The Apache 2.0 license removes the enterprise copyleft barrier that would otherwise complicate governance-heavy profiles.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/Wrapper (Daemon variant)** (primary)
- **Level 5 — Memory/Observability** (secondary, via durable lesson+skill accumulation)

The daemon architecture and ACP layer place KiroCrew firmly in L2. The self-improvement mechanism (lesson persistence, skill synthesis) is a Level 5 behavior embedded directly into the harness rather than as a separate observability service — this hybrid L2+L5 placement is a new structural pattern in this log.

## Claims to verify

- **ACP specification**: Is Agent Client Protocol a published standard, a kiro.dev proprietary spec, or an alias for an existing protocol? If proprietary, how does it constrain interoperability with non-KiroCrew toolchains?
- **Self-improvement definition**: Is the lesson-persistence mechanism actually adaptive (changing future LLM behavior) or merely a durable memory retrieval system (user corrections stored and re-injected at context construction)? The latter is not self-improvement in any learning-system sense.
- **3,900 stars provenance**: KiroCrew was updated September 14 — is this a launch-day spike or organic accumulation? Forks (580) and commit count (6,166) suggest established development rather than a fresh repo.
- **ACP vs. MCP interplay**: The repo says it "supports MCP servers" alongside ACP. Does this mean ACP is used for harness→agent communication and MCP for agent→tool calls? If so, ACP is an internal orchestration bus, not a public protocol.
- **Sandbox depth**: Linux namespaces can be bypassed by misconfigured capabilities. Is the sandboxing model audited or self-declared?

## Status

- First tracking: 2026-09-14
- Stars: 3,900 (above 100-star threshold; below 5,000 registry threshold)
- Registry deferred: `statefulness: persistent` is not a current schema value; no public per-call pricing data
- Watch: Does a `persistence_model` or `statefulness: persistent` axis emerge from this and similar tools? Does ACP get documented as a public protocol?
- Related signals: Procedural Graphs self-modifying execution (2026-09-10), max-sixty/worktrunk parallel agent coordination (2026-09-12)
