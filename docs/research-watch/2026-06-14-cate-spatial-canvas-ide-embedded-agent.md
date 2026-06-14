# Research Watch: Cate — Spatial Infinite-Canvas IDE with Embedded AI Agent

- Repo/Link: https://github.com/0-AI-UG/cate
- Source: GeekNews front page

## Why this is worth watching
Cate is a desktop IDE built on an infinite zoom/pan canvas where editors, terminals, browsers, documents, and AI agent threads coexist as spatial objects rather than stacked tabs. The embedded agent ("Pi") supports multiple AI providers (Anthropic, OpenAI, GitHub Copilot, Gemini, OpenRouter, Groq, Mistral, DeepSeek) via OAuth or API key. This challenges the assumption that an IDE must be linear/tabbed — it experiments with spatial memory as a navigation primitive for code-plus-agent workflows.

## What stands out immediately
- Infinite canvas with docking, splits, detachable windows, and saved layouts
- Monaco editors (VS Code engine) + xterm.js terminals + PDF/DOCX/image viewing
- Git-aware file tree with staging, branches, worktrees, and inline diffs
- Embedded "Pi" agent with per-chat model memory and multi-provider backend
- Electron 41 + React 18; runs macOS, Windows, Linux with prebuilt packages
- MIT license, TypeScript (98%), 1.4k stars

## Why clawfit should care
Cate is a first signal for **spatial/infinite-canvas IDE** as a discrete L7 sub-type. Current L7 IDE entries (Cursor, Cline, Continue) are all tab-linear. If the spatial paradigm gains adoption, it would introduce a new `ux_paradigm: spatial` dimension for IDE-layer tools — relevant to clawfit's interface-axis scoring. The multi-provider agent backend (L2 characteristics) embedded inside an L7 surface is also architecturally notable: Cate collapses what is typically a separate harness selection into the IDE choice itself.

## Preliminary interpretation
Current best reading:
- **Level 7 primary — spatial-canvas IDE sub-type (first signal)**
- **Level 2 secondary weak** — embedded multi-provider agent backend with per-chat memory

## Status
- First signal; 1.4k stars well below threshold
- No map mutation; no registry entry warranted at this stage
- Promotion threshold: 5k stars OR adoption report from a team replacing a tab-based IDE with Cate
