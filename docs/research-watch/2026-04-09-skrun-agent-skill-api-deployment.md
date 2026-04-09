# Research Watch: Skrun — Deploy Agent Skills as API

- Repo/Link: https://github.com/skrun-dev/skrun
- Source: Hacker News (Show HN, 41 pts)

## Why this is worth watching
Skrun operationalizes the gap between defining agent skills (SKILL.md files) and running them in production: it converts skill definitions into callable `POST /run` REST APIs. This is a new category — **skill deployment infrastructure** — distinct from both skill managers (lifecycle tooling) and MCP servers (tool-use connectors). It signals that skill packs are maturing into independently deployable microservices.

## What stands out immediately
- **SKILL.md → API**: Takes any skill definition and exposes it as a typed REST endpoint
- **Multi-model support**: Anthropic, OpenAI, Google, Mistral, Groq with automatic fallback
- **Stateful execution**: Persistent KV storage across invocations — agents remember context between calls
- **MCP + custom tools**: Supports both SKILL.md embedded tools and external MCP server tool bindings
- **Full dev lifecycle**: `skrun init`, `skrun dev` (local hot-reload), `skrun test`, `skrun deploy` → registry

## Why clawfit should care
Skrun introduces a new Level 4c pattern: **skill-as-service**. Currently clawfit's registry distinguishes tool-use infrastructure (MCP, Composio) from skill packs (L4b). Skrun blurs this line — a skill pack deployed via Skrun becomes an API endpoint callable by any agent. This changes the routing logic: clawfit may need a `deployment_mode` dimension (local-plugin / API-service / MCP-server) to correctly match skills to org contexts.

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool-use / action infrastructure** (skill-to-API deployment layer)

## Status
- Tracking — early (41 HN pts), but the pattern is new and worth watching
