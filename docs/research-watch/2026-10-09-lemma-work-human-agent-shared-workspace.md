# Research Watch: Lemma — Open-Source Shared Workspace for Humans and AI Agents

- Repo/Link: https://github.com/lemma-work/lemma-platform
- Source: GeekNews front page 2026-10-09

## Why this is worth watching
Lemma positions itself as a persistent shared workspace where human team members and AI agents coexist as first-class participants with separate roles, permissions, and access scopes — rather than agents being invoked from a human-managed tool. The dual AGPL (backend/frontend) + Apache 2.0 (CLI, SDKs, skills, pod format) license split is designed to keep the pod bundle format open while allowing commercial hosting. It supports Claude Code, Codex, Cursor, and OpenCode natively.

## What stands out immediately
- **Pods as the unit of organization**: each team workspace (pod) contains shared tables, files, agents, workflows, permissions, and apps; coding agents can build an entire pod as files and import via CLI
- **Agent-as-teammate model**: agents hold their own roles and tool grants scoped to specific tables, files, and connectors — not a "call an agent to do X" model but an "the agent is on the team" model
- **Event-driven persistence**: agents keep running on schedules, webhooks, and table events even when all humans are logged off
- **Human-in-the-loop gates**: workflows explicitly mix agent steps with human approval steps
- **Multi-surface**: agents and humans interact via Slack, Teams, Telegram, WhatsApp, or email — all writing the same underlying records
- **Model flexibility**: Anthropic/OpenAI keys, Ollama, LM Studio, or Lemma-managed models
- **529 stars at tracking** — below the 5k registry threshold; early but appearing on GeekNews front page suggests Korean developer community interest

## Why clawfit should care
Lemma represents a new architectural pattern not yet explicitly tracked: a workspace where the primary organizational unit (the pod) is designed from the start to have both human and agent members with equivalent standing. Existing tracked tools either put agents in service of humans (coding agents, research loops) or coordinate agent-to-agent workflows (ClawTeam, DureClaw). Lemma's "agents as teammates" model is closest to the L3 team-workflow SSOT layer but extends into L6 (the actual human collaboration surface). The `team_size: large` + `governance_need: hard` + `output_destination: internal_product` profile is its most plausible registry target, but at 529 stars it needs significant adoption growth before a registry entry is warranted.

## Preliminary interpretation
Current best reading:
- **Level 3 — Team workflow / executable SSOT** (primary): Lemma defines the shared data model and workflow orchestration that both humans and agents operate within
- **Level 6 secondary**: the multi-surface interface (Slack, email, messaging) is a genuine L6 human interface pattern

## Status
- 529 stars — below the 5k registry entry threshold; monitoring
- Dual AGPL/Apache license: AGPL backend is a blocker for `governance_need: hard` without a Folks and Machines commercial license agreement
- First signal for "human-agent shared workspace with role-based agent membership" at L3
- Comparison: distinct from ClawTeam (agent-to-agent swarm, L3) and herdr (terminal multiplexer, L2); Lemma's distinguishing claim is the persistence of agent roles across sessions and the messaging-surface integration
