# Research Watch: korea-data-mcp — Korean Public API MCP Gateway

- Repo/Link: https://github.com/YoungsoonLee/korea-data-mcp
- Source: GeekNews Show GN (2026-10-31)

## Why this is worth watching
A developer has packaged DART (Korea's public corporate disclosure system), the Public Data Portal (공공데이터포털), and the National Legal Information Center (국가법령정보) as a single MCP server, making Korean government data directly callable by any MCP-capable agent. It is the first signal for "national government open-data platform as MCP server" as a distinct sub-type distinct from the existing Korean law MCP (2026-04-07) which was limited to statutes.

## What stands out immediately
- Three distinct government data categories in one server: corporate filings, public datasets, and legal text
- Motivated by the observation that AI agents frequently misread Korean-language API docs — the MCP wrapper normalizes output format
- Show GN submission format: community-built, not an official government project
- Prior tracked adjacent signals: korean-law-mcp (2026-04-07, statutes only), nomadramas-k-skill (2026-08-02, skill collection)

## Why clawfit should care
This is an MCP ecosystem expansion signal at L4. As government open-data MCP servers emerge (Korea today, likely EU/US to follow), the `network: online` scoring for research and data-retrieval tasks gains a new class of structured-API alternatives to raw web scraping. The pattern — wrap a messy national API into a clean MCP surface — is replicable to any country's public data, making this a leading indicator for a broader L4 sub-type.

## Preliminary interpretation
Current best reading:
- **Level 4 — MCP server / capability layer** (primary): exposes government data as MCP-callable tools
- **Level 3 — Governance / access control** (secondary): tiered by data type (public, financial disclosure, legal)

## Status
- New signal; no registry entry (specialized domain, below general-purpose MCP server threshold)
- Watch for: analogous public-data MCP servers for EU, US, or other Asian government data portals
- Third Korean-ecosystem signal (after korean-law-mcp 2026-04-07 and k-skill 2026-08-02)
