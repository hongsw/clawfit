# Research Watch: browser-rs-mcp — Lightweight Multi-Agent Stealth Browser Controller

- Repo: https://github.com/maestrojeong/browser-rs-mcp
- Also see: `docs/research-watch/2026-07-03-chrome-devtools-mcp-browser-agent-capability.md`; `docs/research-watch/2026-07-03-safari-mcp-server-apple-browser-agent-capability.md`

## Why this is worth watching

The multi-agent RAM problem is real: a standard Chromium instance consumes 200–500 MB, so browser-per-agent setups at scale are memory-prohibitive. browser-rs-mcp addresses this by delivering a 59-tool browser MCP server as a ~5 MB Rust binary and enabling multiple isolated agent sessions to share one browser profile via HTTP/SSE transport rather than spawning independent instances. The stealth mechanism is also architecturally distinct from other tracked tools — headful mode with persistent profiles rather than JavaScript injection, which changes the detection surface in meaningful ways.

## What stands out immediately

- **~5 MB binary, ~6 MB RSS (MCP server process)**: the footprint figure refers to the controller, not the Chromium process it drives; real RAM savings come from shared profile HTTP/SSE mode rather than binary size alone
- **HTTP/SSE transport for multi-agent sharing**: multiple agent sessions connect to one owner-scoped browser profile, avoiding per-agent browser spawning — sharing semantics (isolation, race conditions) are not yet benchmarked
- **Stealth via headful + persistent profiles**: differs from vibheksoni/stealth-browser-mcp (nodriver + CDP patches) and Patchright forks; the self-reported "0 detections on rebrowser-bot-detector.net" benchmark is unverified
- **59 tools via MCP**: navigation, page snapshots, element interaction, network routing, cookie/storage, diagnostics — comparable coverage to chrome-devtools-mcp (40+) and stealth-browser-mcp (97) in a smaller footprint
- **Accessibility tree + change diffs as return values**: avoids raw DOM dumps, reducing agent context window pressure per action
- **v0.1.10 released July 16, 2026**: 10 patch releases suggests active iteration, not a prototype spike

## Why clawfit should care

The shared-profile HTTP/SSE model is not present in other tracked browser MCP tools (chrome-devtools-mcp, safari-mcp, libretto, obscura) and directly addresses a resource constraint relevant to lower hardware tiers in hardware.json. If the sharing model holds under concurrent load, it lowers the floor for multi-agent browser use on the local workstation tier where spawning 3–5 independent Chromium processes is often impractical. The stealth approach also introduces a third distinct mechanism alongside the two already tracked (official CDP via chrome-devtools-mcp; JS-patch-based via stealth-browser-mcp variants), which may be relevant for `tasks: research` profiles accessing bot-resistant sites.

## Preliminary interpretation

Current best reading:
- **Level 4c — MCP Capability Server** (primary): browser automation tool delivered as an MCP server; agents consume it as a named tool layer, consistent with chrome-devtools-mcp and DesktopCommanderMCP classification
- **Level 2 — Harness** (secondary, tentative): the shared-profile HTTP/SSE mode introduces cross-agent session coordination that is closer to a harness-layer concern than a single-tool capability; not confirmed until sharing semantics are validated

## Status

- 1 star on 2026-07-18 (well below the 100-star tracking threshold); signal source is a GeekNews "Show GN" self-submission by the author — low organic signal, first-party origin
- Not registry-eligible at current maturity; schema watch: `browser_sharing_model: [per-agent | shared-profile]`; `stealth_mechanism: [js-patch | headful-persistent | cdp-native]`
- Monitor for: independent star growth beyond author network; benchmarked concurrent-agent sharing; third-party detection-evasion validation
