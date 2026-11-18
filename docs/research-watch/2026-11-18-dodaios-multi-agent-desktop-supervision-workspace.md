# Research Watch: Dodaios — Multi-Agent Desktop Supervision Workspace

- Repo: https://github.com/Dodaios/Dodaios (⭐418)
- Source: GitHub Trending Python (19 stars today, 2026-11-18)

## Why this is worth watching

Dodaios is a cross-platform desktop application that runs multiple coding agents (Claude Code, Codex, and others) side by side in a single workspace, with a human-facing "lead assistant" (voice or chat) that orchestrates task splitting, agent assignment, and trust-layer approvals. Its explicit positioning — "Be the CEO, not the babysitter" — describes a specific interface design intent: shifting the human role from monitoring agent execution steps to approving decisions at defined trust boundaries. With 418 stars and 6,662 commits, it is not a weekend project.

## What stands out immediately

- **Lead assistant as orchestrator**: a voice- or chat-accessible assistant writes task briefs, splits large jobs into sub-tasks, and starts coding agents on each sub-task — this is a human-delegating-to-multiple-agents interaction model, not a human monitoring a single agent
- **Per-agent git worktrees**: each running agent gets its own isolated worktree with separate diff review and commit/push/PR actions — this avoids agents clobbering each other's working tree, which is a known failure mode in multi-agent coding setups
- **Trust layer with named categories**: requires human confirmation for payments, credentials, permanent deletion, and first contact with new people — the named categories (not just "sensitive actions") imply a schema-driven approval system, not an ad hoc confirmation dialog
- **Local memory as a single editable file**: the app's memory about the user, contacts, and projects is stored in one local file the user can directly edit — readable memory over opaque vector databases, at the cost of scalability
- **Multi-model support**: Claude, OpenAI, Gemini, Ollama via own plans or API keys — not locked to a single vendor; Ollama support means local/offline model use is in scope
- **Cross-platform desktop + headless server**: runs as a desktop app on Windows/macOS/Linux or as a headless server — the headless option is unusual for a desktop-first product and may indicate server-side multi-agent orchestration use cases
- **6,662 commits, 146 forks, 15 open PRs**: development activity consistent with an active project; unsigned installers and preview status on phone calls and most plugins indicates early-but-real, not demo-only

## Why clawfit should care

Dodaios represents a third distinct pattern at the L6 (human interface) layer, alongside fleet managers (OpenMausBot, Orca — monitoring without approval) and plan review workspaces (plannotator — reviewing plans before execution). The Dodaios pattern is different: a human-led orchestrator that assigns work to multiple agents in parallel and approves trust-boundary decisions in real time. This is "multi-agent CEO interface" rather than "monitor" or "plan reviewer."

For clawfit, Dodaios is relevant to the `statefulness: session` and `statefulness: persistent` recommendation axes — users who want persistent memory and cross-session context are the same users who would use a tool like Dodaios. The per-agent worktree architecture also surfaces a gap in clawfit's registry: `workspace_isolation: per-agent` is not a current field, but it distinguishes Dodaios-style systems from single-agent harnesses at the L6 layer.

## Preliminary interpretation

Current best reading:
- **Level 6 — Human Interface** (primary): desktop application providing multi-agent supervision, task orchestration, and trust-boundary approvals for a human user
- **Level 2 — Harness/Wrapper** (secondary): orchestrates agent assignment, task splitting, and git worktree management — harness-level functionality delivered through a desktop UI

## Claims to verify

- Whether the trust layer schema (payments, credentials, permanent deletion, first contact) is extensible by users or hard-coded — matters for enterprise adoption where trust categories differ
- Whether "headless server" mode supports multi-user access or is single-user only — the distinction determines whether this is a personal tool or a team-level orchestration layer
- Whether Ollama integration supports all locally hosted models or only a specific subset
- Whether per-agent worktrees are created programmatically or require manual git configuration per agent — the former is an architectural feature, the latter is a workflow suggestion

## Status

- First scan: 2026-11-18
- Registry action: **deferred** — 418 stars is below the 5,000 threshold for registry addition; preview status on key features (phone calls, most plugins); no cost/latency data applicable (desktop app)
- 📡 Note: Dodaios is a candidate second signal for "multi-agent desktop supervision workspace" if compared with Craft Agents (`2026-04-30-craft-agents-oss-document-centric-agent-desktop.md`); however Craft Agents is document-centric with a different interaction model; this is a first signal specifically for the "CEO-style task-delegation interface with per-agent worktree isolation" pattern at L6; monitor for a second tool combining voice/chat orchestration + per-agent isolation + trust-layer approvals
