# Research Watch: TeamAI CLI — Cross-Agent Team Management Platform

- Repo: https://github.com/Tencent/teamai-cli (⭐2,849)
- Source: GitHub Trending (today, +563 stars)

## Why this is worth watching
TeamAI CLI is a Tencent-backed TypeScript tool that treats agent skill/rule/MCP/hook distribution as a git-based synchronization problem across an entire engineering team. Rather than configuring Claude Code, Codex, OpenCode, Cursor, and CodeBuddy independently, it federates configuration through a shared repository. This is the first major enterprise technology company (Tencent) to publish a cross-agent team synchronization CLI under MIT license.

## What stands out immediately
- Covers 7+ AI coding agents simultaneously: Claude Code, Codex, CodeBuddy, WorkBuddy, OpenCode, Cursor, and "other AI agents"
- Three-layer architecture: Team Execution (distribute skills/rules/docs/agents/hooks/MCP configs), Team Context beta (automatic knowledge recall, codebase knowledge graph), Team Improvement beta (usage-pattern tracking, outdated-knowledge archiving, dashboards)
- Synchronization via shared git repository — role-based resource distribution (different agent configs per team member role)
- Supports GitHub, GitLab, GitCode, and other git providers
- TypeScript, MIT license, 695 commits on main branch — not a prototype
- Team Context layer builds a real codebase knowledge graph for AI understanding of the full repo

## Why clawfit should care
This is the clearest L3 signal in this log for "team SSOT generator" as a distinct product category. The existing registry has individual agent tools but no entry for cross-agent team configuration management. Tencent's backing gives this enterprise credibility that most community harness projects lack. The Team Improvement layer — tracking which skills/rules teams actually use and archiving stale ones — is the first usage-analytics-feedback loop on agent configuration seen in this scan log.

The 7+ agent coverage means it is not a Claude Code harness specifically; it occupies the meta-level above agent choice, treating agent selection as a runtime variable per team member. This is a structural gap in clawfit's current taxonomy: `agents.json` tracks individual agents, but no schema expresses "multi-agent configuration federation."

## Preliminary interpretation
- **Level 3 — Team Workflow / SSOT Generator** (primary: cross-agent skill and config distribution)
- **Level 4 — Capabilities/Skills** (secondary: distributes skills and MCP configs as the payload)

Multi-level classification note: the git-based synchronization mechanism is L3 (governance/SSOT), but the artifacts it distributes — skills, MCP configs, hooks — are L4 objects.

## Claims to verify
- "7+ AI agents" — confirm all integrations are functional, not just listed
- Team Context "automatic knowledge recall" — is this a RAG layer or just index-based? Performance benchmarks not cited
- Tencent origin — verify MIT license is genuine for the full codebase, not just the shell
- 695 commits — verify the project has active maintenance past initial burst

## Status
- New — strong candidate for a future `team_management` or `cross_agent_config` registry type
- Star count: 2,849 (well above 100-star threshold)
- Registry eligibility: blocked (no schema slot for configuration management tools; no per-agent cost/latency data)
