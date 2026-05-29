# Research Watch: ktx — Executable Context Layer for Data Agents

- Repo/Link: https://github.com/Kaelio/ktx
- Source: Hacker News (2026-05-29, Show HN, 52 pts, 10 comments)
- Also see: https://docs.kaelio.com/ktx/docs/getting-started/quickstart · https://www.ycombinator.com/companies/kaelio

## Why this is worth watching
ktx is a domain-specialized context layer that auto-ingests business knowledge (dbt, Looker, Metabase, Notion wikis) and generates a queryable semantic layer — YAML definitions of tables, joins, measures, and dimensions — then exposes that layer to agents via MCP. The "executable context" framing distinguishes it from general-purpose memory tools: context here is structured query knowledge, not conversation history. YC-backed, Apache-2.0, 304 stars at capture — early but commercially motivated.

## What stands out immediately
- Architecture is two-layer: a **wiki component** (markdown pages, auto-deduplicated, contradiction-flagged) and a **semantic layer** (YAML join graphs, chasm/fan-trap resolution, measure definitions) — agents consume both via MCP search tools
- MCP server launched on demand via `ktx mcp start`; compatible with Claude Code, Codex, Cursor, and OpenCode — integrations are first-class, not deferred
- Self-improving claim: learns from query history and warehouse usage patterns, not just static ingestion — but this is vendor-authored; no independent benchmark cited
- HN thread identified primary competitor framing as Wren AI (hand-authored semantic models) vs. ktx (auto-ingested from existing data tools); no direct comparison to general memory tools like Honcho or OpenViking
- TypeScript 82% monorepo (pnpm + uv); also ships a Python `ktx-daemon` for portable compute; 304 stars — below the 5k registry threshold
- YC-backed (Kaelio company page on YC) — commercial trajectory likely; open-source may be a top-of-funnel posture rather than a primary distribution commitment

## Why clawfit should care
The signal is layer-classification relevant rather than registry-relevant at this star count. ktx is the first tracked tool that positions itself specifically as a context provider for data/analytics agents rather than for general coding agents. This raises two clawfit schema questions: (1) whether `task: data-analysis` deserves a distinct filter path from `task: code-gen`, given that the context requirements differ structurally; (2) whether the MCP-native semantic layer pattern (structured business knowledge as queryable context) constitutes a distinct L5 sub-type separate from conversation-history memory and RAG-over-documents. The WrenAI signal (2026-03-28) flagged the analytics-vertical specialization pattern; ktx adds a context-infrastructure layer beneath WrenAI-class agents.

## Preliminary interpretation
Current best reading:
- **Level 5 — Memory / MCP / context layer** (primary): ktx functions as domain-specialized context infrastructure injected into agent sessions via MCP; it does not orchestrate execution or define workflow governance
- **Level 4 secondary (weak):** the semantic layer YAML files are agent-consumable capability artifacts, but they are consumed as context, not invoked as discrete skills or tools; the boundary is porous and the L5 classification is the cleaner fit

The "executable context" label in the repo description is marketing language for what is structurally a structured-knowledge MCP server with auto-ingestion. It is not an execution harness (L2) — ktx has no task dispatch, no session orchestration, and no workflow lifecycle; it only supplies what the agent knows about the warehouse before it writes SQL.

## Status
- 304 stars — below the 5k registry threshold; do not add to registry yet
- Apache-2.0 license clears governance blockers if star count crosses threshold
- YC backing increases probability of continued development, but also increases risk of the open-source repo becoming feature-frozen if a managed cloud tier launches
- Promotion threshold: 5k stars OR a second independent data-agent context layer tool adopting the auto-ingested semantic layer + MCP pattern (which would confirm the sub-type)
- Watch for: whether ktx publishes benchmark data comparing agent SQL accuracy with vs. without its context layer; that would move it from vendor claim to validated fact
