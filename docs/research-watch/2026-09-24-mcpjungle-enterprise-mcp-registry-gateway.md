# Research Watch: MCPJungle — Enterprise MCP Server Registry and Gateway

- Repo: https://github.com/mcpjungle/mcpjungle (⭐1,254)
- Source: Web search / MCP ecosystem monitoring (via mcpmarket.com listing)

## Why this is worth watching
MCPJungle is a self-hosted registry and gateway that centralizes MCP server discovery for enterprise agent deployments. Rather than each agent configuring its own MCP connections, teams register servers once; agents discover tools through a single endpoint. This is the first tool in this scan to explicitly address the MCP proliferation problem: as the number of available MCP servers grows, managing which tools agents can reach becomes its own infrastructure concern.

## What stands out immediately
- **Single source of truth for MCP tools**: registers all MCP servers within an organization once; agents query one endpoint
- **Built-in access control**: per-server, per-team permission policies — relevant for enterprise governance requirements
- **Written in Go**: same language as google/ax (tracked 2026-06-05) and JoakimCarlsson/ai; a Go-native cluster may be emerging in the production-grade harness/infrastructure tier
- **Privacy controls**: claims data isolation between teams and agents accessing the same gateway
- **~1,254 stars**: above the 100-star monitoring threshold; active community with regular releases
- **Pattern validation**: MCPJungle + MetaMCP (separate signal, same day) represent two independent implementations of the "MCP gateway" sub-pattern — this is the two-signal condition for taxonomy consideration

## Why clawfit should care
clawfit tracks L4 as a flat capabilities/skills/MCP layer. MCPJungle is evidence that L4 is stratifying: raw MCP servers (the capabilities themselves) are now distinct from MCP infrastructure that manages access to those servers. If this sub-layer (call it L4-infra or MCP registry/proxy tier) becomes standard, clawfit's scoring model will need to account for whether an agent connects to MCP servers directly or via a managed gateway — with governance, auditability, and latency implications.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capabilities/Skills/MCP** (primary: manages and exposes MCP tool inventory)
- **Level 7 — Infrastructure** (secondary: enterprise registry, access control, network policy enforcement)

## Claims to verify
- Whether access control is policy-as-code or GUI-only
- Whether the gateway introduces meaningful latency vs. direct MCP connections
- Whether it supports both SSE and stdio MCP transport protocols
- License type and self-hosting constraints

## Status
- First research-watch doc; 1,254★ above monitoring threshold
- Pattern co-signal: MetaMCP (also logged today) provides a second independent implementation of "MCP aggregation gateway" — two-signal condition met for taxonomy consideration of an "MCP infrastructure" sub-layer within L4
- Registry eligibility: insufficient deterministic cost/latency data; no agents.json entry warranted (gateway infrastructure, not an agent runtime)
