# Research Watch: Google Open Knowledge Format

- Repo/Link: https://cloud.google.com/blog/products/data-analytics/
- Source: GeekNews (구글 Open Knowledge Format 공개 - AI에이전트를 위한 지식 공유 표준)

## Why this is worth watching
Google has unveiled a vendor-neutral specification enabling multiple AI agents to consume wikis and structured knowledge bases without per-agent translation layers. This directly parallels MCP (which standardises tool access) but targets the knowledge/document layer: agents from different vendors can read the same knowledge store in a common format. Google authorship gives it institutional weight that community proposals lack.

## What stands out immediately
- Vendor-neutral: any agent (Claude, Gemini, GPT-based) can consume the format
- Specifically targets multi-agent knowledge sharing — fills a gap MCP leaves open (MCP is tool-call protocol, not knowledge-schema protocol)
- From Google Cloud, so likely tied to their data-analytics and enterprise knowledge graph products
- Could become a standard knowledge interchange layer for enterprise multi-agent deployments

## Why clawfit should care
If Open Knowledge Format gains adoption, the clawfit taxonomy needs a "knowledge interchange layer" node between Level 4 (MCP/tooling) and Level 5 (research-loop systems). Enterprise tool recommendations for large teams with hard governance requirements should surface standards-compliant knowledge layers. This is also a signal that enterprise vendors are building proprietary knowledge-sharing standards to compete with open MCP.

## Preliminary interpretation
Current best reading:
- **Level 4–6 — MCP Ecosystem / Research-Loop Layer** (knowledge interchange protocol sub-type)

## Status
- New entry 2026-06-20 via GeekNews. Full spec detail not yet available. Track for GitHub repo and adoption signals.
