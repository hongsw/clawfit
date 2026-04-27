# Research Watch: cmux — Ghostty-based Multi-Agent Terminal UX

- Repo: https://github.com/manaflow-ai/cmux
- Source: hongsw GitHub stars (recent), 15,587★, Swift
- Also see: docs/research-watch/2026-04-23-zed-parallel-agents-threaded-ide.md (IDE-threaded parallel agents)

## Why this is worth watching
cmux is a native macOS terminal (Swift + AppKit, powered by libghostty) explicitly built around the problem of running multiple AI coding agents side-by-side. Where Zed Parallel Agents (2026-04-22) absorbed multi-agent orchestration into the IDE thread model, cmux is the same problem solved at the terminal-multiplexer layer: vertical tabs + per-pane notifications instead of editor threads + worktrees. 15.6k stars on a macOS-only Swift app is a strong signal that "which terminal?" is becoming a meaningful axis for multi-agent coding workflows, not just "which IDE?" or "which harness?"

## What stands out immediately
- **Not a Ghostty fork** — separate Swift/AppKit app that uses libghostty as a rendering engine; reads existing Ghostty configs. Distinct provenance from the Ghostty project itself.
- **Vertical tabs as agent dashboard**: each pane's sidebar entry surfaces git branch, linked PR status/number, working directory, listening ports, and latest notification text — i.e. metadata specifically chosen for monitoring concurrent agent sessions, not generic shells.
- **OSC-driven notifications**: picks up terminal escape sequences (OSC 9 / 99 / 777) plus an explicit `cmux notify` CLI to drive blue-ring pane indicators and illuminated tabs when an agent needs attention. This is the load-bearing mechanism for "manage N agents without staring at all of them."
- **Explicit agent integrations named**: Claude Code, Codex, OpenCode. `cmux claude-teams` command runs Claude Code's teammate mode with agents as native pane splits — "no tmux required" framing.
- **Install surface**: DMG or `brew install --cask cmux`. Socket API + keyboard shortcuts for control.
- **Claim to inspect, not yet validated**: docs do not describe git worktree isolation, per-pane filesystem scope, or backend mixing within one workspace — features Zed parallel agents ship explicitly.

## Why clawfit should care
This is the **terminal-multiplexed counterpart to Zed's IDE-threaded pattern** — same problem (managing concurrent coding agents without losing track of who needs attention), different surface. For clawfit's recommendation engine the implication is that the Level 6 (human interface) layer is fragmenting along workflow surface lines:
- IDE-native threaded: Zed parallel agents
- Terminal-native multiplexed: cmux
- Mobile-remote: Happy (2026-04-16)
- Web-control: claudecodeui

For `solo/small` profiles whose primary surface is a terminal (Claude Code CLI, Aider, OpenCode), cmux substitutes from below for tmux + manual notification scripts. It does **not** substitute for harnesses (Crystal, ccpm, claude-squad) the way Zed does — cmux is UX/notification-focused, not orchestration-focused. That distinction matters: a user can run cmux *and* a harness, whereas Zed parallel agents tends to displace the harness.

**Registry decision**: 15.6k★ exceeds the 5k cutoff but cmux is a terminal UI — it does not map cleanly onto agent / llm / hardware schemas. Track here, do not auto-add to registry. If clawfit later models `interface_surface` as a dimension, cmux becomes a candidate entry under `terminal_multiagent`.

## Preliminary interpretation
Current best reading:
- **Level 6 — Human interface / multimodal layer** (terminal multiagent UX sub-type)
- Adjacent to **Level 7 (infrastructure)** because libghostty is a rendering substrate, but cmux's value is the human-facing notification + sidebar model, not the rendering engine.
- Sibling to Zed parallel agents (Level 6 IDE sub-type) under a shared "concurrent-agent monitoring surface" pattern.

## Status
- Tracking. macOS-only limits addressable profile share; revisit if Linux/Windows port appears or if `interface_surface` becomes a clawfit scoring dimension.
