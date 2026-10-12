# Research Watch: Uber MCP Gateway — Enterprise MCP Deployment Architecture at Scale

- Repo/Link: https://www.uber.com/in/en/blog/designing-mcp-gateway/ (no public GitHub repo)
- Stars: N/A (official Uber Engineering blog post, October 1 2026)
- Source: GeekNews front page

## Why this is worth watching
Uber's engineering blog describes the production MCP Gateway that handles every MCP interaction across Uber's back-end. At 800+ MCP servers and 5,000+ tools, this is the largest publicly detailed enterprise MCP deployment architecture to date. It is not a concept or prototype: it describes a system in active production. The architectural decisions — control/data plane separation, AutoCrawler discovery, disabled-by-default enablement, protocol translation, PII redaction — represent a pattern that other large organizations building on MCP at scale will likely converge toward.

## What stands out immediately
- **Scale:** 800+ registered MCP servers; 5,000+ tools managed through a single gateway
- **Control/data plane split:** MCP Registry (control plane) stores configuration; Proxy Gateway (data plane) refreshes on a fixed cadence — no restarts for config changes
- **Protocol translation:** the gateway converts MCP calls to HTTP, gRPC, or TChannel and back; existing Uber APIs required no changes to become MCP-accessible
- **AutoCrawler:** a Cadence-based workflow scans Uber's IDL registry and native MCP server heartbeats to auto-discover and create MCP server + tool registrations
- **Disabled-by-default:** discovered tools are held off until the owning team reviews and explicitly enables them; config changes require approval and support rollback
- **Context-saving discovery (Omni MCP):** incremental tool discovery; Response Projection trims responses to only requested fields; Code Mode routes calls via the aifx CLI
- **Governance at the tool level:** authorization, PII redaction, and downstream execution run through Uber's Muttley service mesh sidecar — governance is structurally unavoidable, not advisory

## Why clawfit should care
- The control/data plane separation is the first publicly documented solution to the "which tools are available right now?" problem at enterprise scale — clawfit currently has no dimension for MCP toolset governance complexity
- Disabled-by-default plus approval workflow is a governance pattern worth surfacing for `governance_need: hard` profiles; the registry assumption that "MCP tool = available" breaks at this scale
- AutoCrawler (IDL → MCP registration) is a new-pattern signal for L4: dynamic, policy-gated MCP surface generation from existing API contracts is architecturally distinct from manually authored MCP servers
- PII redaction at the gateway layer (via Muttley sidecar) is the first signal for "MCP-level data loss prevention" as an infrastructure concern — not handled at the tool or harness layer
- This is the third Uber engineering signal in clawfit's scan history (after 70%+ agent PRs, Sept 2026, and MCP Jungle enterprise registry, Sept 2026). The convergence confirms Uber as a leading-edge enterprise deployment reference for the `large_exec` org profile

## Preliminary interpretation
Current best reading:
- **Level 4 primary — Capabilities / MCP** (enterprise MCP infrastructure: gateway, registry, protocol translation)
- **Level 2 secondary — Harness / Orchestration** (the gateway sits between agents and back-end services, mediating all tool invocations)
- Pattern name candidate: `enterprise-mcp-control-plane` — control plane + data plane split with approval-gated, auto-discovered tool registration

## Claims to verify
- The "5,000+ tools" figure is from the blog post; independent confirmation is not possible without access to Uber's internal registry
- Protocol translation fidelity (MCP ↔ TChannel especially) is asserted without latency/error data
- AutoCrawler discovery cycle time and error rate for IDL discrepancies are not disclosed
- Whether Omni MCP incremental discovery handles tool version changes or only additive discovery

## Status
- No public GitHub repo; registry entry not applicable
- Pattern is eligible for a `missing-recommendation-axes.md` note on "enterprise MCP governance" when a second corroborating signal surfaces from a different organization
- Monitor: other large engineering organizations publishing MCP deployment architecture posts
