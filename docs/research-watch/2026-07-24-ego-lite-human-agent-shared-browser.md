# Research Watch: ego-lite — Shared Browser for Human + Agent Parallel Work

- Repo/Link: https://github.com/citrolabs/ego-lite
- Source: GitHub Trending

## Why this is worth watching
ego-lite challenges the dominant pattern of giving each AI agent its own isolated headless browser instance. Instead, it runs a single macOS browser that both human and agent(s) use concurrently in isolated "Spaces," with agents inheriting the human's existing sessions (cookies, logins, bookmarks) automatically. Claimed 2.5× speed improvement and meaningful token reduction compared to separate-instance automation approaches.

## What stands out immediately
- **Shared session model**: agents reuse the human's authenticated browser state — no credential re-provision needed
- **JavaScript-function API**: agents write JS directly instead of CLI tool-calls; reduces round-trip tool invocations
- **Space isolation**: each agent gets a fully isolated workspace inside the same browser process
- **Kernel-level snapshot quality**: custom renderer handles nested iframes and complex DOM better than standard CDP/Playwright approaches
- **Compatible with any agent CLI** (Claude Code, Codex, Cursor); 1,612 stars, macOS now, Windows/Linux planned

## Why clawfit should care
This is a novel L4c capability pattern: rather than agents running their own ephemeral browsers, they share the human's live session. This changes the cost model for browser-use skills (lower token overhead) and the trust model (agents operate inside a user-owned browser, not a sandboxed headless one). If this pattern spreads, clawfit's `network` axis may need a `shared-browser` sub-mode distinct from `online` (API-driven) and `offline`.

## Preliminary interpretation
Current best reading:
- **Level 4c — Browser Capability Layer** (shared human-agent browser substrate)

The "parallel Spaces" pattern is distinct from existing browser-agent tools (Playwright MCP, Chrome DevTools MCP, browser-rs) which all assume agent-exclusive headless instances.

## Status
- First signal. Star count (1,612) below the 5k threshold for registry entry.
- Architecture claim (2.5× speed, token reduction) unverified against standard CDP automation.
- "When in doubt" rule applied — no canonical section change, no registry entry this run.
- Monitor for: (1) Windows/Linux release — broadens adoption signal; (2) integration with memory layers (cipher, serena) as a combined browser+code workflow.
