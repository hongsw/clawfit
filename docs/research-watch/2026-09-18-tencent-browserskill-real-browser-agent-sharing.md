# Research Watch: Tencent/BrowserSkill

- Repo/Link: https://github.com/Tencent/BrowserSkill
- Source: GitHub Trending (2026-09-18, #4, TypeScript, 1,302 stars today)

## Why this is worth watching
BrowserSkill takes a distinct approach to browser agents: instead of launching a headless or sandboxed browser, it lets AI agents operate inside the user's real, already-logged-in browser session without interrupting their work. This sidesteps authentication flows, CAPTCHA challenges, and session-cookie management that plague headless tools. Tencent backing signals enterprise intent.

## What stands out immediately
- Real browser session sharing — agents inherit all existing cookies, extensions, and logins
- Non-interrupting design — user and agent share the browser concurrently
- TypeScript; Tencent authorship (same org behind WeKnora, tracked 2026-09-17)
- Directly addresses the "authenticated state" gap that headless agents hit on corporate intranets

## Why clawfit should care
This is structurally distinct from tracked browser agents: webbrain (2026-09-14) exposes an MCP server for delegation; camofox (2026-09-07) is headless stealth; BrowserSkill is session co-presence. The pattern matters for `data_sensitivity: confidential` profiles where spinning up a second browser with copied credentials is not allowed. A `browser_sharing_model: [headless | mcp-delegated | session-shared]` axis is now a three-signal candidate.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capability layer** (browser capability extension for agents), with L6 secondary (user-facing browser control surface)

## Status
- Monitoring — 1,302★ below 5k registry threshold; re-evaluate at 5k
- Cross-reference: webbrain (2026-09-14), camofox (2026-09-07)
