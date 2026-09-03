# Research Watch: Portless — Named Local URLs for Agents

- Repo/Link: https://github.com/vercel-labs/portless
- Source: GitHub Trending

## Why this is worth watching
Portless replaces ephemeral localhost port numbers with stable named URLs — both for human developers and, explicitly per the repo description, for agents. As agents increasingly need to discover and call local services, numeric ports are a friction point (they change, they conflict, they require configuration). Named URLs are a small step toward an agent-readable local service mesh.

## What stands out immediately
- Targets developer/agent co-use from the start: "for humans and agents" is explicit in the description
- TypeScript/Vercel Labs provenance — likely integrates with Vercel's edge and Next.js ecosystem
- Eliminates the need for agents to be given port numbers via prompts or env vars
- Complements MCP server discovery patterns where tools register at predictable addresses

## Why clawfit should care
Addresses local-network friction for hybrid (online/offline-capable) agent setups. Clawfit currently has no "local service discoverability" axis in org_fit. This is a narrow infrastructure tool rather than a full agent, so registry addition is low-priority — but it signals a broader trend toward agent-friendly local environments that could inform a future `local_tool_discovery` feature tag.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capability / Plugin / Skill Layer** (local service discovery for agents)

## Status
- Trending 2026-09-03; first observation
