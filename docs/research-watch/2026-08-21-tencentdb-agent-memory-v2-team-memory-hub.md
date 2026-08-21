# Research Watch: TencentDB Agent Memory v2.0 — Team-Level Memory Hub for Multi-Agent Collaboration

- Repo: https://github.com/TencentCloud/TencentDB-Agent-Memory (⭐20,000+)
- Source: PR Newswire / Tencent Cloud announcement (2026-08-13); MarkTechPost coverage (2026-08-07)
- Note: Update to previously tracked tool (docs/research-watch/2026-07-10-tencentcloud-tencentdb-agent-memory.md, 8,155★ at time of original tracking)

## Why this is worth watching

The v2.0 release represents a qualitative shift in scope, not just a feature increment. The original TencentDB Agent Memory (tracked July 10, 2026 at 8,155★) was a 4-tier individual agent memory system. v2.0 extends the same architecture to team-level shared memory — converting team conversations, documents, code repositories, and institutional knowledge into persistent memory assets that any authorized agent can retrieve across sessions. Stars tripled from 8,155 to 20,000+ in roughly 90 days, suggesting adoption beyond Tencent's internal use.

The claim worth scrutinizing: shared team memory solves a real coordination problem (multiple agents re-doing research the team already did), but it also introduces a new failure mode — stale or incorrect shared memory propagating errors across all agents that draw on it. The v2.0 announcement does not prominently address memory freshness, eviction policy, or conflict resolution when multiple agents write concurrent updates.

## What stands out immediately

- **Four reusable team memory asset types**: Chat Memory (interaction history), Skill (reusable procedures), LLM-Wiki (structured document pages), Code-Graph (indexed code symbols and call relationships) — structured output formats, not flat text dumps
- **Role-based memory assembly**: different agent platforms assemble memories based on "roles and tasks" — suggests access control beyond flat namespace sharing, though the granularity is unverified
- **Named platform integrations**: Tencent CodeBuddy, OpenClaw, Claude Code listed as supported agent platforms — not a generic API, but verified connector points
- **Three multi-architecture Docker images (linux/amd64, arm64)**: single-command deployment; MIT license — self-hostable without TencentDB cloud dependency, which answers one open question from the July tracking
- **Star velocity**: 8,155 → 20,000+ in ≈90 days post-open-source — unusually fast growth for a memory infrastructure tool; Tencent's developer marketing likely contributes but community uptake is verifiable via PR activity
- **No published freshness/eviction documentation visible in announcement**: the PR release does not describe how stale memories are invalidated or corrected — a structural gap for production use

## Why clawfit should care

The July 2026 tracking note identified `statefulness` as a binary filter (`stateless | session | persistent`) that cannot distinguish between individual-persistent and team-persistent memory. v2.0 makes this distinction concrete: an agent system that is `statefulness: persistent` may now mean either single-agent history or shared team memory — fundamentally different operational characteristics for multi-agent profiles.

The `Code-Graph` memory type is the most novel: indexed code symbols and call relationships stored as persistent memory rather than re-indexed per session. For clawfit profiles involving large codebases, this is a different cost/latency tradeoff than session-level retrieval.

clawfit currently has no scoring dimension for multi-agent coordination readiness. v2.0 is the second signal after loopx (2026-08-04) for "durable shared state across agent teams" as a distinct capability category.

## Preliminary interpretation

- **Level 5 primary — Agent memory / persistence layer** (team-scoped long-term memory system)
- **Level 2 secondary — Multi-agent harness** (role-based memory assembly suggests the memory layer is taking on coordination semantics that belong to an orchestrator)

The boundary between L5 (memory infrastructure) and L2 (agent coordination) is blurring in v2.0. This is worth watching as a taxonomy stress point.

## Claims to verify

- "Role-based memory assembly": whether this is access control (different agents see different memory subsets) or just different query templates per role — the distinction matters for governance
- "Claude Code integration" claim: whether the integration is a documented MCP connector or just an example use case in the README
- Memory freshness: how stale entries are handled when a code-graph changes after the initial indexing
- MIT license scope: whether the MIT license covers the server and all connectors or only the SDK

## Status

- 20,000+★ — well above 5k registry threshold
- Original tracking: 2026-07-10 at 8,155★; v2.0 Team Memory is a new capability set warranting independent tracking
- Registry eligibility: hold pending `memory_scope: [individual | team]` schema field — this is the new dimension v2.0 exposes
- **Schema watch:** `memory_scope: [individual | team | org]`; `memory_asset_types: [chat | skill | wiki | code-graph]`
- Two-signal rule update: v2.0 + loopx (2026-08-04) = two signals for "team-scoped durable agent memory" as a taxonomy sub-type; candidate for `### Team-level persistent memory` subsection under L5 on next canonical update pass
