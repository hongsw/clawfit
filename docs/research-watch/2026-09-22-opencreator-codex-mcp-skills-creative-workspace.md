# Research Watch: OpenCreator — Codex-Native Creative Workspace with MCP and Skills

- Repo: https://github.com/krillinai/OpenCreator (⭐12.2k)
- Source: GitHub Trending TypeScript (161 stars today, 2026-09-22)

## Why this is worth watching
OpenCreator (formerly KrillinAI) is an open-source creative workspace that uses Codex CLI as its execution engine and MCP + Skills as its capability layer. It is structurally a Codex-native application: rather than building a proprietary agent loop, it delegates all task execution to Codex CLI and extends capabilities via standard MCP servers and reusable skill packs. The rename from KrillinAI to OpenCreator and repositioning toward "Skills + Agents" framing mirrors a broader market shift from bespoke agent applications toward assembling capabilities from standard agent primitives (L1 runtime + L4 capabilities).

## What stands out immediately
- **Codex CLI as the execution engine** — architecture depends on a standard base runtime rather than a custom one; this is a structural choice with portability implications
- **MCP + Skills as the capability layer** — aligns with L4 taxonomy; capabilities are composable, not hardcoded into the application
- 12.2k stars with sustained trending history suggests product-market fit in the creative AI tools space
- **Video, image, voice, and avatar creation** as the surface use cases — this is L6 (human interface / multimodal), not a developer tool
- Rebranding from KrillinAI to OpenCreator: the original name had limited discoverability; the new name emphasizes the "open" and "creator" positioning more clearly
- Supports video translation (dubbing + subtitle alignment), script generation, stick figure animation, smart dubbing — breadth of creative tasks handled through a common agent interface
- Both visual dashboard and conversational AI interfaces — dual-mode UX is typical for tools targeting non-developer creative users
- 770 commits on master branch — not a fresh project; rebranding implies strategic repositioning, not a new build

## Why clawfit should care
OpenCreator demonstrates an emerging pattern: **domain-specific applications assembled from standard agent primitives (Codex CLI + MCP + Skills) rather than built on custom agent code.** This has direct registry implications:
- The `tasks` field in agents.json is currently defined around developer workflows (code-gen, qa, research) — OpenCreator is the first tracked tool explicitly targeting creative production tasks (`video-edit`, `dubbing`, `image-gen`)
- The `hardware: cloud` + `task: creative-production` profile intersection is not represented in the current registry
- The Codex CLI dependency means platform churn risk: if Codex CLI's pricing or API changes, OpenCreator's cost structure changes with it — the registry's current cost data model doesn't capture this pass-through dependency
- As an open-source tool built on MCP/Skills, OpenCreator represents a use-case category (creative production automation) that may grow as the pattern of "assemble capabilities from standard primitives" scales beyond developer tools

## Preliminary interpretation
- **Level 4 — Capability / Skill / MCP layer (primary)**: the application's agent capabilities are entirely defined by its MCP server integrations and skill packs
- **Level 1 — Base Agent Runtime (secondary)**: Codex CLI as execution engine; OpenCreator inherits L1 properties from it
- **Level 6 — Human Interface / Multimodal (secondary)**: visual dashboard + creative content output (video, voice, avatar) positions it at L6 for the end-user interface

## Claims to verify
- Whether Codex CLI is a mandatory dependency or can be swapped for other runtimes (Claude Code, Goose, etc.)
- Whether the MCP servers it ships with are public or proprietary
- Star count trajectory before and after the KrillinAI → OpenCreator rename
- Whether the 12.2k stars accumulated under KrillinAI or post-rename (star history determines how much is brand equity vs. product)
- Licensing terms for the creative outputs (user data, generated content ownership)

## Status
- **First research-watch doc for OpenCreator (formerly KrillinAI)**
- 12.2k stars — above registry threshold (5k), but `tasks` field would require new creative-production task categories
- Registry candidate deferred: no deterministic cost/latency data (Codex CLI cost pass-through model); `task` types not in current enum; no clear latency profile
- Pattern note: first tracked example of "domain application built on Codex + MCP + Skills" — watch for similar Codex-native apps in other verticals as a second-signal test of this assembly pattern
