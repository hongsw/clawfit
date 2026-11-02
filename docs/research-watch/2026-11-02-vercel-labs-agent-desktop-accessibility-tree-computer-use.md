# Research Watch: agent-desktop — Desktop Accessibility-Tree Computer Use

- Repo: https://github.com/vercel-labs/agent-desktop (⭐8,908)
- Source: GitHub Trending (all languages, #1 by today-stars, 2,243 gained 2026-11-02)

## Why this is worth watching

`agent-desktop` is a Rust CLI and C library from Vercel Labs that gives any agent computer use on a desktop by reading the OS accessibility tree rather than taking screenshots and matching pixels. The core claim is reliability: accessibility trees expose the app's semantic UI structure (labels, roles, ref IDs) so agents can target elements by identity, not by position or visual appearance. When a layout changes, the element still has the same identity; when an element disappears, the tool returns `STALE_REF` rather than silently acting on the wrong target.

The project gained 2,243 stars in a single day, which is a strong adoption signal for a low-level tooling project. It is Apache-2.0 and distributed via npm with pre-built binaries for x64 and ARM64.

## What stands out immediately

- **Accessibility tree, not pixels**: reads macOS Accessibility API, Windows UIAutomation, and Linux AT-SPI; no vision model required for element location; avoids the grounding-model cost of Agent S or Claude Computer Use
- **Ref-based command model**: each snapshot returns a JSON map of UI elements with ephemeral refs; the agent acts on refs, then re-snapshots to verify; stale refs return a structured error with a `suggestion` field
- **Headless by default**: actions execute through the accessibility API without moving the pointer or taking focus; `--headed` flag enables physical input for apps that require real pointer events
- **~60 commands**: covering focus, type, key combos, scroll, drag, clipboard, screenshots, window management, and shell surfaces (Windows); macOS shell support is planned
- **Ships Agent Skills**: the binary includes `agent-desktop skills get desktop`, which exports the skill spec for agent harnesses (Claude Code, etc.) to register it as a tool
- **Language bindings**: `libagent_desktop_ffi` for in-process integration; no subprocess overhead for embedding frameworks
- **macOS requires Accessibility permission**, Windows needs no extra grant for apps at the same integrity level as the terminal, Linux needs `at-spi2-core`
- No screenshot-scraping fallback: the tool is committed to the accessibility-tree approach, which means it fails cleanly on apps with broken or absent accessibility support rather than silently degrading

## Why clawfit should care

The current computer-use landscape in the registry is screenshot/vision-based (Agent S: pixel coordinates via UI-TARS grounding; mobile-mcp: accessibility tree on mobile). `agent-desktop` introduces accessibility-tree-first computer use on **desktop** platforms, a gap in the current coverage. The distinction is not cosmetic: accessibility-tree approaches have deterministically lower cost per interaction (no vision model inference) and higher resilience to visual redesigns.

This also matters for the `offline_mid_codegen` and `solo_dev_codegen` profiles: a developer whose agent can reliably drive desktop GUIs (terminal emulators, browsers, desktop apps) via accessibility tree rather than screenshots can work on tasks that would otherwise require a vision-capable frontier model.

For registry: `agent-desktop` is a tool/library, not an agent or LLM. It doesn't fit the current `agents.json` schema (which targets deployable agent systems). A future `adapters.json` or `capabilities.json` could model it, but no registry action today.

## Preliminary interpretation

Current best reading:
- **Level 6 — Human Interface / Computer Use** (primary): directly drives desktop GUI interactions
- **Level 4 — Capabilities / Tools Layer** (secondary): ships as an MCP-compatible Agent Skills package that agent harnesses can register

## Claims to verify

- "Accessibility tree instead of pixels" reliability claim: depends entirely on whether target apps expose well-formed accessibility trees; many Electron apps, games, and older enterprise software have broken accessibility support; the tool's own failure mode (`AMBIGUOUS_TARGET`) is the tell
- The star spike (2,243 in one day) may be amplified by the vercel-labs org name; sustained adoption is the meaningful indicator
- Shell surface support is listed as "planned" for macOS; the current macOS implementation does not cover terminal interactions, which is a significant gap for coding agents
- No benchmark for comparison: unlike Agent S (OSWorld), there is no published task-success benchmark for `agent-desktop`; the reliability claims are architectural, not empirical

## Status

- New signal; not previously tracked
- Registry eligibility: tool/library; doesn't fit current `agents.json` schema; no registry addition
- Watch for: MCP server wrapper that exposes `agent-desktop` actions as tools; harness-native integration in Claude Code or Cursor; OSWorld or similar benchmark results
- Relation to existing signals: accessibility-tree approach first seen in `mobile-mcp` (2026-09-27, mobile); `agent-desktop` is the first signal for this approach on desktop platforms
