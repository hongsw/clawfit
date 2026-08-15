# Research Watch: palmier-io/palmier-pro

- Repo/Link: https://github.com/palmier-io/palmier-pro
- Source: GeekNews front page (2026-08-15)

## Why this is worth watching
palmier-pro is an open-source macOS video editor (Swift, GPLv3) that exposes an MCP server, allowing Claude Desktop, Cursor, and Codex to directly interact with the video editing timeline. It is the first tracked L6 creative interface tool that treats the video timeline as an MCP-addressable resource rather than a standalone desktop app. 13.6k stars.

## What stands out immediately
- Native Swift implementation with a Premiere Pro–style timeline interface
- Built-in MCP server: agents can scrub, add clips, apply cuts, and trigger generative AI features (Seedance, Kling models) via tool calls
- Generative AI for video/image creation integrated into the editing loop — humans and agents work on the same timeline simultaneously
- Free core editor + MCP server under GPLv3; generative features require subscription login
- Requires macOS 26 (Tahoe) on Apple Silicon — hardware-constrained distribution window

## Why clawfit should care
This is the first tracked tool where an MCP server turns a creative production application (video editor) into an agent-addressable workspace. Prior tracked agent-video work (OpenMontage, L2, Python-orchestrated pipelines; h3.c, L7, inference-only) are either orchestration harnesses or pure inference engines — neither gives agents direct MCP-level access to a native video timeline. This creates a new sub-pattern: **L6 creative-app-as-MCP-resource** distinct from L4c (standalone MCP servers) and L2 (orchestration harnesses).

## Preliminary interpretation
Current best reading:
- **Level 6 — Human Creative Interface Layer** (primary): MCP-exposed video timeline enabling human+agent co-editing
- **Level 4c — MCP Capability Layer** (secondary): MCP server is built-in, not a wrapper — agents use it via standard tool-call protocol

## Status
- Watching: GeekNews signal, 13.6k stars, new macOS-only distribution constraint
- Two-signal rule: first tracked L6 creative app with embedded MCP server; need a second independent L6 app exposing MCP for creative production before canonical section entry
- Registry: not eligible (no deterministic cost/latency data; macOS 26 Tahoe requirement limits deployment scope for registry comparisons)
