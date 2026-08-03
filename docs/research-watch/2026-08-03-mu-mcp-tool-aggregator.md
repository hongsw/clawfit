# Research Watch: Mu – Tools for Agents

- Repo/Link: https://github.com/micro/mu
- Source: Hacker News (Show HN)

## Why this is worth watching
Mu bundles 67 tools across web search, news, weather, markets, mail, file storage, calendar, and image generation behind a single MCP endpoint. Unlike thin wrappers, it runs actual infrastructure: an SMTP server with DKIM, a search index, an app sandbox, and a wallet system — all in a single Go binary. The AGPL-3.0 self-hosted option or hosted service at micro.mu gives orgs a one-connection path to a broad tool surface.

## What stands out immediately
- 67 tools via one MCP config entry — solves the "too many MCP servers" coordination problem (cf. graph-tool-call signal, same day)
- Real infrastructure per tool: own SMTP server, own search index, own storage — not API proxy wrappers
- 4,004 commits despite only 112 stars — high development intensity relative to visibility
- CLI and web UI in addition to MCP mode
- AGPL-3.0 (self-hostable) with hosted option at micro.mu

## Why clawfit should care
Mu is a concrete new entry point for the L4c MCP tool layer. Most tracked MCP servers are single-domain (chrome-devtools-mcp, korean-law-mcp, tradingview-mcp). Mu introduces a "mega-aggregator" sub-type that solves tool-count friction by collapsing dozens of connectors into one. If adoption grows, this changes how orgs onboard to the MCP capability layer — one install vs. N server configs. Also directly relevant to the "too many tools degrades performance" signal (graph-tool-call, 2026-08-03).

## Preliminary interpretation
Current best reading:
- **Level 4c — MCP tool infrastructure / mega-aggregator sub-type**

Schema gap: no current field for `mcp_tool_count` or `aggregator_type: [single-domain | multi-domain]`.

## Status
- First signal. 112 stars. AGPL-3.0. Self-hostable. Registry entry added at `tools_registry.json`.
