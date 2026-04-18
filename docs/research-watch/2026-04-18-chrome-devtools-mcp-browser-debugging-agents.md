# Research Watch: ChromeDevTools/chrome-devtools-mcp

- Repo/Link: https://github.com/ChromeDevTools/chrome-devtools-mcp
- Source: GitHub Trending

## Why this is worth watching
Chrome DevTools published an official MCP server giving coding agents direct access to browser debugging, network inspection, DOM queries, console logs, and performance profiling. At 35,846★ it is the highest-starred MCP server in the taxonomy by a large margin. Official provenance (Chrome DevTools team) eliminates the trust question that plagues third-party browser MCP servers.

## What stands out immediately
- First-party MCP server from the Chrome DevTools engineering team itself
- Exposes Chrome remote debugging protocol over MCP: DOM, network, console, performance, storage
- Enables agents to run browser tests, inspect network calls, and iterate on UI bugs without leaving the agent session
- 35,846★ in a single trending window — strongest single-day MCP signal observed in this taxonomy
- TypeScript; integrates directly with Claude Code, Codex, Cursor, and any MCP-compatible agent

## Why clawfit should care
This is the clearest `qa` task enabler in the entire Level 4c layer. An agent doing browser QA previously needed Playwright (external) or Libretto (early-stage). chrome-devtools-mcp makes live browser state a first-class tool for any MCP-compatible agent. For orgs doing `qa` + `code-gen` on web apps, this is a tier-1 recommendation alongside serena and rtk. It also strengthens the case for a `web-qa` sub-task type distinct from general `qa`.

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool-use / action infrastructure (MCP server)**

Closest existing entry: Libretto (deterministic browser automation, early-stage). chrome-devtools-mcp is broader (full DevTools surface, not just automation) and has official provenance.

## Status
- High signal — add to registry and reference-levels.md
- Revisit star count in 30 days to confirm adoption is sustained vs. trending spike
