# Research Watch: MCP Roadmap August 2026 — Agent Identity, Progressive Discovery, and Agentic Primitives

- Repo/Link: https://blog.modelcontextprotocol.io/posts/mcp-roadmap/ (official protocol blog)
- Source: Hacker News front page, rank 4, 120 points (2026-08-22)
- Star threshold: not applicable — official protocol governance document, bypasses threshold

## Why this is worth watching

The 2026-07-28 MCP specification finalized the stateless core. This new roadmap document (published 2026-08-22) describes what comes next. It differs qualitatively from the March 2026 roadmap: several items have moved from "exploratory" to "concrete focus areas," suggesting the Working Groups have converged on design direction. The most structurally significant priority is **agent identity** — specifically abandoning API keys in favor of Workload Identity Federation (OpenID Connect pattern) for agents running as cloud workloads. This shifts MCP from a tool-calling protocol to one that can express "who the agent is" in an auditable, federated way.

A second priority — **progressive discovery for large tool catalogs** — addresses a real scaling problem: today, enumerating all tools in a large MCP server can consume substantial context before any task begins. Progressive discovery would let clients query available tools lazily, which directly changes how clawfit's recommendation of MCP-heavy tool stacks should be analyzed.

## What stands out immediately

- **Agentic messaging primitives**: server-initiated events and task maturation — not just request-response; agents can receive asynchronous signals from servers
- **HTTP-native transport unification**: resolves the current ambiguity between SSE, WebSocket, and HTTP POST; standardizes deployment across hosting environments
- **Agent identity via Workload Identity Federation**: agents get verifiable identity credentials (not API keys) aligned with OAuth/OpenID Connect — distinct from human user auth and designed for cloud workloads
- **Progressive tool discovery**: clients can enumerate large catalogs lazily rather than upfront — context-critical for large plugin ecosystems
- **Improved SDK developer experience**: explicit investment in ergonomics and spec conformance, which historically has lagged the spec itself
- The post explicitly positions these as priorities "picked up from the previous roadmap," confirming they were identified but not resolved in earlier cycles
- Working Groups (not Core Maintainers alone) now review proposals — governance is decentralizing
- Published on the same day as this scan; HN rank 4 with 120 points

## Why clawfit should care

**Agent identity** is the most consequential item for clawfit's scoring model. Current scoring has no dimension for "can this stack prove who the agent is to external services." If Workload Identity Federation becomes part of MCP, then MCP-connected stacks gain a governance property that simpler direct-API stacks lack. For org profiles with `governance_need: hard`, this becomes a filter dimension.

**Progressive tool discovery** matters for clawfit's `budget` filter: a stack that requires 8,000 tokens of tool enumeration before the first task step fails in low-budget contexts, even if the per-step cost is cheap. This is currently invisible to clawfit's recommendation logic.

**Server-initiated events** change the latency profile of agent-server interaction: pushing from polling-pull to event-push reduces latency but increases infrastructure complexity. Relevant to clawfit's `latency` filter for real-time profiles.

## Preliminary interpretation

- **Cross-cutting protocol governance** (no single layer)
- **L4 primary** (capabilities/tool protocol) — agent identity and progressive discovery both change the capability layer
- **L7 secondary** (infrastructure) — Workload Identity Federation is a deployment-infrastructure concern

## Claims to verify

- Whether "Workload Identity Federation" means support is planned, or a draft spec exists — the roadmap doesn't link to a concrete proposal
- Which Working Group owns the agent identity item, and whether a timeline exists
- Whether progressive discovery will break backward compatibility with existing MCP clients
- Whether server-initiated events require changes to the 2026-07-28 stateless spec or ship as an extension
- Whether "HTTP-native transport unification" deprecates SSE or merely standardizes it alongside HTTP POST

## Status

- Tracking: first signal 2026-08-22
- No star count (official protocol governance)
- Registry eligibility: not applicable — protocol spec, not a tool/runtime
- Schema watch: potential new dimension `agent_auth_mode: [api-key | oidc-workload-identity]`; `tool_discovery: [eager | progressive]`
- Prior MCP tracking: spec RC 2026-07-05, final spec 2026-07-29; this roadmap is post-spec strategic direction
