# Research Watch: holaOS — Concurrent Multi-Agent Workspace with Shared Local Memory

- Repo: https://github.com/holaboss-ai/holaOS (⭐7.1k)
- Source: GitHub Trending (all languages, 2026-08-14)

## Why this is worth watching

holaOS is an open-source Electron-based AI agent workspace that runs Claude Code, Codex, and a native holaOS agent in a single application with shared local memory and tools. The architectural claim — multiple third-party agent CLIs operating within a shared memory layer with access to the same MCP-connected tools — represents a different integration model than existing multi-agent environments: rather than orchestrating agents from above (paseo, DeerFlow), holaOS provides a shared environment that agents inhabit simultaneously. At 7.1k stars on GitHub Trending, it is the first tracked entry for this specific "concurrent workspace" pattern.

## What stands out immediately

- **Three simultaneous agent backends**: Claude Code, Codex, and holaOS native agent — potentially concurrent in isolated Spaces rather than sequential or orchestrated
- **Shared local memory as plain files**: persistent context stored as plain files readable and editable by the user — same inspectable-memory design principle as ReMe's wikilink files (2026-08-09) and LifeOS's Atlas asset graph (2026-08-10)
- **HolaApps Marketplace**: interactive applications (Notion, browsers, custom tools) running side-by-side with agents — an embedded app layer within the workspace, not just MCP tool connections
- **100+ one-click OAuth integrations**: Gmail, Slack, GitHub, Linear, and others plus MCP protocol support
- **Built-in frontier model access**: Kimi K3, GLM 5.2, GPT 5.6, Claude Opus 5 — BYOK also supported
- **Rich media and document generation**: image, video, audio generation; native document export (.xlsx, .pptx, .docx) — content creation as first-class workspace capability
- **Modified Apache 2.0 with commercial-distribution conditions**: permissive base but commercial distribution restricted
- **7.1k stars, 632 forks**: above 5k threshold in star count; fork count (~9% fork-to-star ratio) indicates active customization

## Why clawfit should care

holaOS represents a new integration pattern at the L2/L6 boundary: a **concurrent multi-agent desktop workspace** where multiple independent agent CLIs operate with shared memory. The tracking landscape so far:

- Single-agent workspaces: craft-agents (L2, document-centric, 2026-04-30)
- Multi-agent orchestrators: DeerFlow (L2, orchestrator-controlled dispatch), paseo (L2/L3, delegate-primitive-based)
- ADEs with parallel model execution for comparison: orca, openchamber, paseo committee mode

holaOS differs in that agents are not orchestrated by a coordinator nor run in parallel for output comparison — they share a workspace with shared memory. This is closer to a shared development environment (IDE analogy) than a task orchestrator. The HolaApps Marketplace also represents an embedded app layer distinct from tool registries (MCP) or skill packs (L4b). **Schema watch:** `workspace_model: [single-agent | orchestrated-multi | concurrent-shared]`; `app_marketplace: bool`; `memory_access: [isolated | shared-filesystem | shared-server]`.

## Preliminary interpretation

- **Level 2 primary** (harness/wrapper): multiple agent CLIs wrapped by a shared workspace environment with unified memory and tool access
- **Level 6 secondary** (human interface): Electron desktop app as the human-facing surface; HolaApps as an embedded in-workspace application layer

## Claims to verify

- **"Simultaneous" multi-agent**: verify whether Claude Code and Codex genuinely run concurrently or whether holaOS switches between them sequentially with shared state; the Electron single-process model may serialize agent execution
- **Shared memory implementation**: verify whether "shared memory" means a single filesystem directory accessible to all agents or whether there is a structured memory server mediating access
- **Modified Apache 2.0 scope**: determine what "commercial-distribution conditions" restrict (reselling the app? SaaS wrapping? embedding in a commercial product?) — the license modification affects enterprise adoption
- **HolaApps Marketplace openness**: verify whether this is an open contribution system or a curated set controlled by holaboss-ai

## Status

- 7.1k⭐, Modified Apache 2.0, TypeScript/Electron, macOS/Windows/Linux
- **Registry eligibility: no** — no deterministic cost/latency data; the workspace is free/self-hosted; model costs vary by BYOK provider
- **First signal for "concurrent multi-agent desktop workspace with shared local memory"** — distinct from orchestrators and parallel-execution ADEs
- **No canonical section change**: single signal; the L2 multi-agent workspace sub-type needs a second independently developed tool with the same concurrent shared-workspace model before adding a stable taxonomy entry
