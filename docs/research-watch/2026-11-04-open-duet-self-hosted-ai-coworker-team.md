# Research Watch: Open Duet — Self-Hosted AI Coworker Team with Approval-Gated Routines

- Repo: https://github.com/Anil-matcha/open-duet (⭐6,760)
- Source: GitHub Trending Python daily (2026-11-04)

## Why this is worth watching

Open Duet is an open-source workspace for creating named AI agents (called coworkers), assigning them roles and workspaces, and running them as a coordinated team. It supports lead agents that delegate to specialists, scheduled and webhook-triggered routines, per-agent persistent memory, and human approval before any action is committed. It is engine-agnostic: agents can run on Claude Code, Codex CLI, Gemini CLI, ACP-compatible agents, or OpenAI-compatible APIs including Ollama. At 6,760 stars it has significant adoption for a tool that is explicitly "in active development." Its architecture represents a convergence of the personal-agent (single-user, approval-gated) and multi-agent (lead/specialist delegation) patterns.

## What stands out immediately

- **Engine agnosticism across all major harnesses**: Claude Code, Codex CLI, Gemini CLI, ACP-compatible agents, Cursor, OpenRouter, and Ollama all supported — avoids hard coupling to one provider, relevant for teams that run multiple coding agents
- **Lead/specialist delegation model**: a lead agent (Claude or Codex only) splits requests into subtasks, hands them to specialist agents, waits for reports, and synthesizes; each specialist runs in a separate conversation with its own workspace
- **Four approval modes**: Ask first, Accept edits, Approve for me, Plan only — this is a meaningful autonomy dial, not a binary; "Plan only" is a soft validation mode that parallels what clawfit's `autonomy_level` scoring might need
- **Per-agent memory with user edit access**: agents store and recall notes and past conversations; users can inspect and edit what is stored — this is an explicit auditability feature that most memory tools lack
- **Composio integration + MCP Marketplace**: external tool access is handled through the user's own Composio key, keeping credentials user-owned; MCP Marketplace browsable from within the app
- **Phone app pairing with self-hosted server**: the mobile pairing is a signal about expected use case — the user is intended to be mobile and reviewing agent actions asynchronously
- **Docker isolation is opt-in and experimental**: the "isolated computers" feature uses Docker containers but is not the default setup; most deployments run agents without compute isolation

## Why clawfit should care

Open Duet is structurally similar to the kirocrew/daemon pattern tracked in September 2026, but with a broader engine matrix, explicit approval modes, and a phone app for async review. It is the third high-star signal (after TAOS and kirocrew/daemon) in the "persistent multi-agent workspace with human approval" sub-type. If a third distinct tool (not a variant of the same codebase) confirms this pattern, the two-signal rule would be met for a canonical section addition in reference-levels.md. The approval-mode taxonomy (Ask first → Accept edits → Approve for me → Plan only) is also a useful vocabulary reference when designing the `autonomy_level` dimension that `missing-recommendation-axes.md` calls for.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness / wrapper layer (primary)**: manages a team of agents, coordinates lead/specialist delegation, handles memory and routines across engines
- **Level 3 — Team workflow / SSOT layer (secondary)**: scheduled and webhook-triggered routines with structured approval states approach a team workflow primitive

## Claims to verify

- Whether "isolated computers" (Docker) is production-ready or still experimental (README describes it as experimental/opt-in)
- Lead agent restriction to Claude or Codex only: is this a capability constraint or a policy choice?
- Whether the MCP Marketplace is the same marketplace tracked at `2026-07-13-mcp-gateway-registry-enterprise-control-plane.md` or a separate catalog
- Suparagent hosted web app: what it costs, whether it syncs data from self-hosted instances
- How memory persists across engine restarts on the self-hosted path

## Status

- 6,760 ⭐, Apache-2.0, Anil-matcha (community maintainer, not a funded startup)
- Registry action: **not yet** — multi-agent workspace tool is not an agent/LLM/hardware entry; no matching schema fields
- Relationship to prior signals: kirocrew/daemon (2026-09-14, L2 persistent agent workspace), TAOS (2026-07-01, L2 self-hosted AI agent OS) — this is the third signal in the "persistent multi-agent workspace with human approval" cluster; watch for two-signal rule on this sub-type
