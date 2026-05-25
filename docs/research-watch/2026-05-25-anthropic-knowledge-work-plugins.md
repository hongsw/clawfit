# Research Watch: Anthropic Knowledge Work Plugins

- Repo/Link: https://github.com/anthropics/knowledge-work-plugins
- Source: GitHub Trending (#4, 14k★)

## Why this is worth watching
Anthropic has shipped the first first-party multi-vertical knowledge-worker plugin pack under Apache-2.0. This is structurally distinct from `claude-plugins-official` (a distribution channel) and `anthropics/financial-services` (single regulated vertical) — it targets the full breadth of knowledge-work roles across 11 domains with production-ready MCP connectors.

## What stands out immediately
- 11 specialized plugins: Productivity, Sales, Customer Support, Product Management, Marketing, Legal, Finance, Data, Enterprise Search, Bio-Research, and Plugin Management
- 40+ enterprise tool integrations via MCP (Slack, Notion, Jira, HubSpot, Linear, Snowflake, Databricks, BigQuery, Figma, Asana, Microsoft 365, and more)
- Standardized manifest format: `.claude-plugin/plugin.json` + `.mcp.json` + `commands/` + `skills/`
- No code or infrastructure required — file-based, customizable, extensible
- 14k★ and 1.7k forks at time of capture; Apache-2.0; 80 commits on main

## Why clawfit should care
This is a registry-eligible L4b entry (above the 5k★ threshold) that fills a gap in the current tools_registry: the `exec`, `pm`, and `researcher` roles currently have few strong matches in non-coding task profiles. Adding this entry improves recommendation quality for the `large_exec_research` and similar knowledge-worker profiles. It also occupies a new cell in the L4b provenance × domain matrix: `(1st-party model-vendor) × (multi-vertical knowledge-work)`.

## Preliminary interpretation
Current best reading:
- **Level 4b — Domain skill packs (1st-party model-vendor × multi-vertical knowledge-work)**

Companion classification: each plugin bundles L4c (MCP connectors) inside the L4b container — same co-packaging pattern as `claude-plugins-official` and `cursor/plugins`, but applied to knowledge-work domains rather than IDE capabilities.

## Status
- Registry entry created in `clawfit/data/tools_registry.json` (14k★ exceeds 5k threshold)
- L4b canonical map entry added to `docs/reference-levels.md` under Domain skill packs
- Signal occupies new provenance cell: `(1st-party model-vendor) × (multi-vertical knowledge-work)`
