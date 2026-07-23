# Research Watch: mediar-ai/screenpipe — Ambient Screen Context Provider for AI Agents

- Repo: https://github.com/mediar-ai/screenpipe (⭐20,400)
- Source: Hacker News Launch HN (YC S26, 2026-07-23)

## Why this is worth watching
screenpipe is a YC S26-backed local application that continuously records a user's screen and audio, exposing that stream as queryable context for AI agents. The architectural claim is direct: instead of agents asking users "what were you working on?", agents can query a continuously updated local database of screen content. At 20,400 stars and app-v2.5.132 released today (July 23, 2026), this is not a prototype — it is a production-grade tool with an active install base before today's formal HN launch.

The structural distinction from other context/memory tools in the corpus: existing L5 tools (mem0, Engram, OpenWiki, codebase-memory-mcp) persist context that agents have already been told about, or that CI/CD pipelines have generated. screenpipe makes the user's actual screen state — applications, windows, text, audio — the source of truth, without requiring the user to narrate or annotate anything. This is passive ambient observation rather than active context injection.

## What stands out immediately
- **Continuous screen and audio capture:** records 24/7 by default; timestamped multimodal log (screen OCR + audio transcription) stored locally in a queryable database
- **Local-first and private:** Rust binary; all capture, storage, and processing on-device; no cloud dependency for capture — API connectivity optional for LLM-powered queries
- **MCP server integration documented:** agents connect to screenpipe via MCP, querying the local capture database with natural language or by timestamp range
- **app-v2.5.132 released July 23, 2026:** the v2.5.x series numbering (132 patch releases) indicates a very high release cadence — likely daily or sub-daily, signaling active use and responsive iteration
- **YC S26 backing:** institutional validation; runway confirmed; not a solo hobby project
- **Rust primary (60.1%):** performance-critical capture pipeline; consistent with always-on 24/7 recording without perceptible system overhead
- **20,400 stars at launch confirmation:** community existed before the YC announcement; pre-installed base is evidence of organic prior adoption
- **"Plug into your agents" framing:** the product is explicitly positioned as an input layer for AI agents, not a standalone productivity tool

## Why clawfit should care
screenpipe represents an L5 pattern not yet in the scan corpus: **passive ambient context capture** as an agent input layer. Every prior L5 signal requires active curation — users annotate facts into mem0, CI/CD generates OpenWiki pages, developers build codebase-memory-mcp indexes. screenpipe requires no user action after installation; context accrues passively by virtue of the user working normally.

Two concrete implications for clawfit recommendations:
1. A profile doing `task: code-gen` + `statefulness: session` currently has no L5 context enrichment option that does not require explicit annotation. screenpipe fills that slot.
2. The `data_sensitivity` axis needs a new trigger: screenpipe captures everything on screen, including credentials, private documents, and personally identifying information. Any recommendation including screenpipe should surface `data_sensitivity: confidential` as a prerequisite. The current registry has no `captures_ambient_screen: true/false` flag to trigger that warning automatically.

The `network: offline` + `local: true` profile is strengthened by screenpipe's local-first design, but the LLM-powered query path still requires an LLM endpoint (online or local), so the effective `network` requirement depends on the query mode chosen.

## Preliminary interpretation
Current best reading:
- **Level 5 — Memory / Observability / Evaluation** (primary: continuous ambient context capture stored as queryable local memory for agents — "passive context accumulation" sub-type, first signal for this specific pattern)
- **Level 4c** has a secondary claim via the MCP server integration, which makes screen content actionable to agents as tool-call context

## Claims to verify
- MCP tool surface: which specific MCP tools does screenpipe expose? (query-by-timerange, query-by-content, streaming vs. batch retrieval, search quality on code-heavy screens vs. general text)
- Storage growth rate: what is the disk usage of 24/7 capture at typical screen activity levels? (1 TB fill time affects `hardware: local` recommendations)
- Offline query mode: does the local LLM query path work fully offline, or does the NL query interface require a cloud LLM endpoint even in local-first mode?
- OCR accuracy: quality on IDE UIs with syntax highlighting vs. plain text vs. terminal output (determines utility for `task: code-gen` vs. `task: research`)
- Privacy model: are capture data encrypted at rest? (determines `data_sensitivity: confidential` compatibility)

## Status
- First signal; YC S26 + 20.4k stars confirm adoption above noise threshold; passive ambient context capture is a first signal for this L5 sub-type
- No registry entry: `tools_registry.json` has no ambient-context-capture category; schema lacks `context_source` field
- Schema gaps: `captures_ambient_screen: true/false`; `context_source: [manual | documented | ambient-screen | ambient-audio]`; `requires_lm_for_query: true/false`
- Data sensitivity flag needed: any recommendation including screenpipe warrants automatic `data_sensitivity: confidential` prerequisite surface in the output
- Monitor for: second independent "passive ambient context capture" tool to confirm L5 sub-type; storage and privacy audit by independent security researcher
