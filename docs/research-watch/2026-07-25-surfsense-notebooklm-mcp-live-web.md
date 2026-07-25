# Research Watch: SurfSense — Open-Source NotebookLM Alternative with MCP-Native Live Web Connectors

- Repo: https://github.com/MODSetter/SurfSense (⭐15,457)
- Source: GitHub Trending Python (rank 5, 2026-07-25)

## Why this is worth watching

SurfSense is a self-hosted research assistant that exposes live social and web data sources — Reddit, YouTube, Instagram, TikTok, Google Search, Google Maps, Indeed, Amazon, and general web crawl — simultaneously as a REST API, a user-facing web interface, and native MCP tools. The MCP-native exposure is the structural distinction: a Claude Code or Cursor agent can call `surf_reddit`, `surf_youtube`, or `surf_web` as first-class MCP tool calls, injecting live social and web content directly into an agent's context without user-intermediated copy-paste. The NotebookLM comparison frames the product for end users, but the MCP tool layer positions it as agent infrastructure for live-data retrieval.

At 15.5k stars, 1,477 forks, v0.0.30 (June 2026), and no equivalent tracked tool in the clawfit corpus that combines this connector breadth with native MCP exposure, SurfSense represents a first signal for a new sub-type in the L4c/L5 boundary zone.

## What stands out immediately

- **Dual interface design:** the same 10+ data connectors are exposed as REST endpoints (for developer/API consumption) and as MCP tools (for agent tool-call consumption) — one implementation serves both surfaces
- **10+ specialized scrapers:** Reddit, YouTube, Instagram, TikTok, Google Search, Google Maps, Indeed, Amazon, general web crawl — each with domain-specific extraction logic, not generic HTTP fetch
- **Hybrid retrieval:** semantic + full-text search with hierarchical indices and reciprocal rank fusion — knowledge base retrieval, not raw web pass-through; 50+ file formats for local document ingestion alongside live web
- **LangGraph agent layer:** planning and sub-agent delegation built in — not a passive RAG store; actively orchestrates multi-step retrieval sequences
- **Docker + Watchtower self-hosted deployment:** air-gap-capable for local document indexing (live connectors require internet); SaaS option with per-item billing also available
- **v0.0.30 (June 26, 2026):** active development; 1,477 forks signal research community customization
- **FastAPI + Next.js architecture:** Python backend with TypeScript frontend — maintainable bifurcation, common in production RAG tools (serena, screenpipe, etc.)
- **15.5k stars in ~18 months** from initial public release

## Why clawfit should care

SurfSense sits at the intersection of L4c (MCP server providing live web and social connectors) and L5 (knowledge management with persistent research state). No existing clawfit registry entry addresses live social + web + local document hybrid retrieval via MCP. For profiles with `task: research` or `task: data-analysis` and `network: online`, SurfSense fills a gap that no tracked tool currently covers.

Two dimensions expose schema gaps in the current model:

1. **Connector breadth is not modeled.** `network: online` captures that a tool needs internet access, but not what kind of internet data it retrieves. A tool that fetches general URLs is structurally different from one that ingests Reddit threads, YouTube transcripts, and TikTok content with domain-specific extraction. `connector_breadth: [single | multi-source | live-social]` would distinguish them at filter time.

2. **MCP data server vs. MCP tool server.** Existing L4c MCP tracking (chrome-devtools-mcp, unity-mcp, serena, desktopcommandermcp) covers tools that perform operations on behalf of an agent. SurfSense is a data provider — its MCP tools return retrieved content, not execution results. The schema has no field for `mcp_server_role: [operator | data-provider | hybrid]`.

Cross-watch with screenpipe (2026-07-23, L5 passive ambient screen context): SurfSense and screenpipe both extend agent context with non-document data, but from opposite directions — SurfSense actively fetches on demand from external sources; screenpipe passively accumulates from the local user's screen. These are distinct sub-types within L5 context augmentation.

## Preliminary interpretation

- **Level 4c primary:** MCP server exposing live web and social connectors as agent-callable tools — the MCP tool layer is the primary technical contribution; the web UI is secondary
- **Level 5 secondary:** persistent knowledge base with hybrid retrieval, LangGraph orchestration, and multi-format ingestion — knowledge management infrastructure alongside the connector layer
- Not L1 (does not define a model or runtime); not L2 (does not wrap or orchestrate agents — it provides data access capabilities to agents)

First signal for "live-data-connector MCP server" sub-type. One signal; "when in doubt" rule applied — no canonical section change.

## Claims to verify

- **Social platform connector legality and reliability:** Reddit, Instagram, TikTok, and Google Maps actively block scrapers and enforce ToS against automated access; long-term connector reliability is unverified; ToS compliance status unclear
- **"50+ file format" ingestion claim:** verify which formats are natively parsed (e.g., PDF, DOCX, XLSX) vs. which fall back to generic text extraction (e.g., arbitrary binary)
- **Self-hosted offline mode scope:** what works without internet — local document indexing only? Or can connectors be configured for local mock data?
- **LangGraph sub-agent delegation with user-provided LLM:** is the LangGraph orchestration layer using a user-configured LLM endpoint or a hosted model? License implications differ.
- **Reciprocal rank fusion quality:** no published benchmark vs. plain semantic or plain BM25 retrieval on research-style QA tasks; "hybrid" retrieval is not inherently better

## Status

- First signal for SurfSense and for "live-data-connector MCP server" sub-type
- Registry candidate: **No for agents.json** — SurfSense is data retrieval infrastructure, not an agent runtime; MCP server schema absent from current registry; `tools_registry.json` does not exist
- Schema gaps: `connector_breadth: [single | multi-source | live-social]`; `mcp_server_role: [operator | data-provider | hybrid]`; `mcp_data_connectors: list[str]`
- Cross-watch: screenpipe (2026-07-23) for passive vs. active context augmentation distinction; serena (2026-07-23) for code intelligence MCP server (different task scope)
- Monitor for: second independent live-data-connector MCP server signal to validate sub-type; ToS compliance resolution for social platform connectors; published retrieval quality benchmark
