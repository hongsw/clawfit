# Research Watch: unclebob/swarm-forge — tmux-Based Multi-Agent Swarm Coordinator

- Repo/Link: https://github.com/unclebob/swarm-forge
- Source: GitHub Trending
- Stars: 1,827 (+81 today, 2026-08-08)

## Why this is worth watching

Robert C. Martin (Uncle Bob, *Clean Code* author) entering the agent-coordination space gives swarm-forge unusual credibility signal in the developer community. Its tmux+worktree approach is intentionally observable and self-hostable — a deliberate counter-position to opaque cloud orchestration layers.

## What stands out immediately

- **Role-separated worktrees**: Each agent role (spec, code, refactor, architect, harden, QA) runs in a dedicated git worktree — prevents merge conflicts and creates natural audit trails
- **Handoff protocol over shared state**: Agents exchange validated message files via a `handoffd.bb` daemon rather than sharing memory — simple, inspectable, offline-compatible
- **Configurable agent packs**: `two-pack`, `four-pack`, `six-pack` presets match swarm size to task complexity; `swarmforge.conf` per-project defines which agents run where
- **Multi-backend**: Supports claude, copilot, codex, and grok in the same swarm
- **Constitution files**: Layered prompt files per role enforce disciplined workflows without modifying base agent behavior
- **Clojure implementation**: Niche language choice signals prototype/research intent, not production SaaS

## Why clawfit should care

swarm-forge introduces a **role-segregated, worktree-isolated multi-agent pattern** distinct from current registry entries. Crystal and Claude Squad manage multiple agent sessions but don't enforce structural role separation with handoff queues. This pattern has governance implications: disciplined handoffs create auditable traces, which matters for mid/large org `governance_need: hard` profiles. Level 2 candidate alongside Crystal and Claude Squad.

## Preliminary interpretation

Current best reading:
- **Level 2 — Agent Harness / Orchestration Wrapper**

The tmux+daemon+worktree architecture is a harness pattern: it wraps multiple Level 1 agents (claude, codex, copilot) with coordination logic, role assignment, and quality gates. Not a base agent runtime itself.

## Status
- New; 1,827 stars, still early. Uncle Bob's authorship gives it outsized discoverability for the star count. Monitor for adoption; no registry entry yet.
