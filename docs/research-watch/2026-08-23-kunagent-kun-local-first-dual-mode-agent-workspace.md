# Research Watch: KunAgent/Kun — Local-First Dual-Mode AI Agent Workspace

- Repo: https://github.com/KunAgent/Kun (⭐6,200)
- Source: GitHub Trending (web search, August 23 2026)

## Why this is worth watching

Kun is a local-first AI agent workspace that runs a single runtime backing both a desktop Electron GUI and a terminal UI (TUI) simultaneously — sharing threads, objectives, and approval queues between the two. Most agent workspaces commit to one interface mode; Kun's dual-runtime design means a developer can start a session in the TUI, switch to the GUI for visual review, and return to TUI without session discontinuity. The 6,200-star count and MCP integration suggest early but non-trivial adoption.

## What stands out immediately

- **Dual-interface single runtime**: desktop GUI (Electron) and TUI share the same underlying agent execution state — objectives, threads, and approval gates are synchronized, not duplicated
- **Two workflow modes**: `Code` (software development, with design artifact capability) and `Work` (writing, documentation, task management); surface-level separation may reflect distinct tool/permission scopes underneath
- **MCP-native**: integrates Model Context Protocol as a first-class capability mechanism rather than a plugin — aligns with the current skill/tool ecosystem direction
- **Multi-LLM provider support**: not locked to a single API; local inference and cloud API targets both supported, consistent with local-first stance
- **Local-first data model**: sessions, records, and artifacts stored on-machine; cloud APIs called only for model inference — similar to apache/maka's design philosophy
- **Built with Vite + React + Tailwind + Electron**: standard TS stack; Node.js 22.19+ runtime requirement suggests targeting developers, not general consumers
- **Vitest test suite**: indicates structured development practice for a young project

## Why clawfit should care

Kun sits at L1/L2 boundary: it is both a base runtime (the place where agents run) and a harness (providing workspace features, approval flows, and multi-mode UI). The dual GUI/TUI design introduces a new variable for clawfit's interface dimension — currently `cli` vs `gui` vs `ide`; Kun suggests `cli+gui` as a first-class hybrid mode worth modeling. Also worth noting: Kun's MCP-first capability model and local-first storage align it closely with the emerging pattern of agents designed to run without mandatory cloud infrastructure, which has implications for the `network: offline` filter path in clawfit's scoring.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base Runtime**: primary. Kun is where agents run; it owns sessions, threads, and execution state.
- **Level 2 — Harness / Workspace**: secondary. Workspace features (approval queues, dual-mode UI, objective tracking) operate above the base runtime layer.

Compared to apache/maka (append-only event log, single author, incubation-stage), Kun targets a similar local-first niche but emphasizes the user-facing interface duality rather than the audit trail. Compared to Claude Code (CLI-first, terminal-native), Kun adds a simultaneous GUI layer without abandoning terminal users.

## Claims to verify

- Shared-state dual interface — whether GUI and TUI are truly synchronized or merely reading the same storage; synchronization semantics matter for multi-user or multi-window scenarios
- MCP integration depth — whether MCP is used for standard tool calls only, or also for resource discovery and server management
- Multi-LLM provider support — which providers are confirmed (Anthropic, OpenAI, local Ollama?); breadth matters for the `hardware: edge` scoring path
- `Code` vs `Work` mode separation — whether these are permission scopes, separate agent configs, or only UI skins

## Status

- Tracking: first signal 2026-08-23
- Stars: 6,200 — above 5k registry threshold, but no public cost/latency data for the workspace layer itself
- Registry hold: Kun is a client workspace, not a priced API; registry entry deferred until agent/LLM sub-selection within Kun is documented
- Watch: whether the dual-mode single-runtime pattern spreads (Autolith, apache/maka, Kun all arrive at local-first from different directions — a convergent pattern signal)
