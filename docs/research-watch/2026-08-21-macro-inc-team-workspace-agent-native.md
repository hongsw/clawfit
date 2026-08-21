# Research Watch: macro-inc/macro — Unified Team Workspace with Agent-Native MCP Access and Shared Memory

- Repo: https://github.com/macro-inc/macro (⭐3,925)
- Source: GitHub Trending (weekly, +1,456 this week); macro-inc organization

## Why this is worth watching

Macro is an all-in-one team workspace (email, chat, docs, tasks, CRM, calls) built on Rust and SolidJS with AI agents as first-class participants rather than add-ons. The key structural claim: agents access the full platform via MCP with "no rate limits" and a "Unified Team Memory" — a daily-refreshed synthesis of conversations, emails, tasks, and calls that agents draw on without per-session re-summarization.

The interesting question Macro raises is not whether a unified workspace works — it is whether removing rate limits and providing persistent shared memory changes what agents can do in a team context compared to standard per-app integrations (Notion MCP, Linear MCP, Slack MCP as separate tools). At 3,925 stars trending this week, it is gaining developer attention, but whether the agent features are production-grade or marketing-level is unverified.

## What stands out immediately

- **No-rate-limit MCP agent access**: agents can query and write to all platform data without throttling — contrasts with third-party MCP connectors that inherit the source app's API rate limits
- **Unified Team Memory (daily refresh)**: cross-channel synthesis (conversations, email, tasks, calls) stored as persistent memory for agent retrieval — addresses the "context fragmentation across tools" problem for team agents
- **Agents as peer document collaborators**: agents edit markdown documents inside the platform's CRDT collaboration system alongside human editors — not a separate "AI draft" interface, but the same document editing primitive
- **Multi-model support**: Claude, OpenAI, Google, Anthropic-compatible models — platform-agnostic; agents are not locked to a specific provider
- **Rust + SolidJS stack**: Rust backend suggests performance and memory safety are first-order concerns; SolidJS is a reactive UI framework with lower overhead than React
- **AGPL-3.0 license**: copyleft with network-use clause — self-hosting is permitted but commercial deployments of modified versions must open-source; relevant for enterprise adoption decisions
- **5,139 commits, 3,925★**: mature codebase with growing community signal this week; the trending spike may reflect a recent feature release rather than initial launch

## Why clawfit should care

Macro represents a pattern not yet in clawfit's taxonomy: a tool where agents are embedded inside the human collaboration surface rather than operating as a separate tool alongside it. This is structurally different from agent-to-Notion MCP or agent-to-Slack integrations, where the agent is external and the platform is a data source. In Macro, the agent is a participant in the same workflow as the human.

The "no rate limit MCP" design is the most distinctive technical claim for clawfit's L4 (capabilities/MCP) taxonomy: a platform that removes the throttling constraint changes the cost model for agent tools (no backoff delays, predictable tool call latency). If this pattern spreads, clawfit's L4 capability scoring may need a `rate_limited: [yes | no | platform-managed]` dimension.

The CRDT document collaboration also creates a new L6 pattern: "agent-as-peer-collaborator" in a live document, distinct from "agent-as-generator" (produces a draft) or "agent-as-reviewer" (reads and comments). This is worth watching as a human-agent collaboration model.

## Preliminary interpretation

- **Level 6 primary — Human interface / human-agent collaboration layer** (the primary value proposition is a unified workspace where humans and agents share the same surface)
- **Level 5 secondary — Memory / observability** (Unified Team Memory is a persistent cross-channel context layer that agents retrieve from)
- **Level 4 tertiary — Capability layer** (no-rate-limit MCP access changes the capability economics for agents working in this workspace)

## Claims to verify

- "No rate limits" claim: whether this applies to all agent operations or only reads; writes may still be throttled to prevent data corruption
- Unified Team Memory freshness: daily refresh cycle means an agent querying memory in the morning may not see afternoon events — how stale memory is flagged or handled
- CRDT conflict resolution: when an agent and a human edit the same document simultaneously, how conflicts are resolved — whether agent edits are recoverable if they conflict with human intent
- Multi-model routing: whether model selection per agent is user-configured or platform-determined (cost vs. capability tradeoff hidden from user)

## Status

- 3,925★ — above 100-star research watch threshold; below 5k registry threshold
- No registry entry: below threshold; Macro is not an agent or LLM itself but a platform hosting agents — does not map to current `agents.json` schema
- **Schema watch:** `agent_integration_model: [external-mcp | platform-embedded | peer-collaborator]`; `rate_limited: [yes | no | platform-managed]`
- Two-signal rule: Macro is the first signal for "agent-native team workspace with no-rate-limit MCP" pattern; watch for second project before taxonomy promotion
- AGPL note: copyleft license with network-use clause limits commercial adoption without open-sourcing modifications — relevant for enterprise clawfit profiles with `governance_need: hard`
- Watch trigger: third-party latency benchmarks for agent MCP tool calls vs. separate MCP server connectors; CRDT conflict handling documentation
