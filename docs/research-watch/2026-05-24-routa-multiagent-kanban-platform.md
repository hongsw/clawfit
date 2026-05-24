# Research Watch: phodal/routa — Workspace-First Multi-Agent Kanban Platform

- Repo: https://github.com/phodal/routa
- Also see: docs/research-watch/2026-05-23-kanbots-parallel-agent-kanban.md · docs/research-watch/2026-05-22-multica-team-agent-platform.md

## Why this is worth watching

Routa enters a Kanban + multi-agent space already occupied by Kanbots (tracked 2026-05-23) but takes a structurally distinct position: where Kanbots is agent-dispatch-first with Kanban as the UI surface, routa appears to lead with protocol pluralism — MCP, ACP, and the emerging A2A (Agent-to-Agent) standard — as its interoperability layer. At 1,300 total stars and 134 stars in a single trending day, velocity is real but the base is modest. TypeScript + Rust stack (62.8% / 27.4%) is consistent with performance-sensitive orchestration work.

## What stands out immediately

- Three declared protocols: MCP (tool-use), ACP (agent communication), A2A (agent-to-agent) — claim to inspect whether all three are implemented or aspirational at this stage
- Formal three-role agent architecture: Coordinator, Implementor, Verifier — a tighter role graph than multica's squad routing or Kanbots' undifferentiated parallel dispatch
- Review gate architecture with explicit verdict + fitness checks — structurally closer to an L3 governance primitive than anything in Kanbots or multica
- Git worktree support for local repo isolation — same execution substrate as Kanbots, but with role-partitioned agents rather than card-per-agent dispatch
- GitHub repository import as virtual workspaces — suggests the unit of work is the repository, not the individual task card
- Background task scheduling + webhooks — implies an event-driven model distinct from pull-based queue systems (multica)
- No confirmed license type from available signal; claim to inspect before assessing governance suitability

## Why clawfit should care

Routa adds a second independent signal to the Kanban + git-worktree L2 sub-type candidate first introduced by Kanbots (2026-05-23). Kanbots is the sub-type's first sample; routa is a credible corroborating signal — the two do not share the same architecture, but both collapse Kanban task management and git-worktree isolation into an agent orchestration surface. The A2A protocol support is the sharpest differentiator: A2A is Google's emerging inter-agent communication standard and its presence here positions routa at the L2/L5 boundary where agent coordination shades into context exchange. If A2A adoption grows, routa's multi-protocol stance could make it an earlier-mover registry candidate than Kanbots. The Coordinator/Implementor/Verifier role structure also edges toward L3 — the Verifier role with formal fitness checks resembles a sprint-contract verification mechanism, though whether this constitutes a behavioral spec or just a workflow stage is a claim to inspect.

## Preliminary interpretation

Current best reading:
- **Level 2 — Meta wrappers / harnesses / orchestration layer** (primary): routa coordinates L1 agent runtimes across named roles (Coordinator, Implementor, Verifier) with Kanban as the workflow surface and git worktrees as the execution substrate. This is harness-layer work — it routes and constrains agents, not defines their behavior.
- **Weak Level 3 secondary (candidate, not confirmed)**: the review gate with formal verdict + fitness checks is the strongest L3-adjacent signal in any Kanban-class tool tracked so far. Insufficient without documentation confirming a persistent behavioral spec artifact (SSOT) or sprint lifecycle contract. If a CLAUDE.md or equivalent spec file governs the Verifier's fitness criteria, L3 secondary becomes viable.
- Comparison with Kanbots: both share Kanban UI + git-worktree isolation; routa adds role specialization and protocol pluralism (MCP/ACP/A2A); Kanbots adds local-first Electron binary and a confirmed MCP integration (depth unverified). These are two distinct implementations of the same emerging sub-type — "role-structured Kanban + worktree agent harness" — distinct from Kanbots' "parallel dispatch Kanban + worktree."

## Status

- 1,300 total stars, 134 today — below the 5k registry promotion threshold; map mutation deferred
- Constitutes a second signal for the L2 "Kanban + git-worktree" sub-type candidate (Kanbots is the first); sub-type formalization requires review of both together — monitor for a third signal before promoting
- A2A protocol support is unverified depth; license not confirmed from available signal
- Watch: whether A2A adoption across routa and other tools accelerates inter-agent protocol standardization as a new L5-adjacent axis
