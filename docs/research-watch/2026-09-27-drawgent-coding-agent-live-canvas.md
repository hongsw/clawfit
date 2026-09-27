# Research Watch: Drawgent — Coding Agent on a Live Excalidraw Canvas

- Repo/Link: https://tangled.org/yanndegat.tngl.sh/drawgent
- Source: Hacker News front page (2026-09-27)

## Why this is worth watching
Drawgent connects coding agents (Claude Code, Codex, opencode) to a live Excalidraw whiteboard, giving agents the ability to create and edit diagrams interactively. This is an early signal of agents crossing from text/code-only operation into shared visual workspaces — a qualitatively different interface modality than terminal or IDE.

## What stands out immediately
- Users annotate drawings with `AGENT:` notes; the agent reads the canvas via screenshots and scene data, edits it live
- "Laser zones" let users circle a diagram region and request targeted modifications to just that area
- Built in Rust with a React frontend; uses ACP (Anthropic's agent-communication protocol) bridges
- WebSocket-based real-time sync; supports end-to-end encrypted shared excalidraw.com rooms
- Agents see the canvas state via headless Chrome vision — spatial awareness, not just text

## Why clawfit should care
Drawgent is a signal that the action surface for coding agents is expanding into visual/spatial contexts — architecture diagrams, system design canvases, flow charts. For clawfit, this touches the interface layer of the 7-layer taxonomy: Level 7 (human–agent interface surfaces) and Level 4 (capability extension). It also raises a question for scoring: orgs doing architecture-heavy design work may prefer agents capable of visual collaboration over purely text-based ones.

## Preliminary interpretation
Current best reading:
- **Level 4/7 — Capability Extension + Interface Surface**: visual canvas is both a capability extension and a new human–agent interface modality

## Status
- Early / experimental; Rust-based, Hacker News front page 2026-09-27
- Watch for adoption and whether ACP-based canvas patterns generalize to other tools
