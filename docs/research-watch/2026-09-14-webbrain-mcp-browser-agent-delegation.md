# Research Watch: WebBrain — MCP-Native AI Browser Agent for Chrome/Firefox

- Repo: https://github.com/webbrain-one/webbrain (⭐1,000)
- Source: GitHub topics/ai-agent (updated 2026-09-14)
- Stars: 1,000 | Forks: 121
- License: GPL-3.0 (v33.0.0+); earlier releases MIT
- Language: JavaScript (monorepo, Chrome/Firefox extensions)

## Why this is worth watching

WebBrain is the first browser-agent tool in this log to expose a **dedicated MCP server** that lets coding agents (Claude Code, Cursor, Codex) delegate browser tasks to an already-authenticated browser session. The prior browser-agent entries — camofox, browser-use, ARTEMIS (Android, 2026-09-12) — are either standalone tools or require separate authentication. WebBrain's model is different: it acts as a shared browser capability layer that any MCP-capable coding agent can call on demand.

The agent-to-agent delegation model (L2 coding agent → L4 browser capability → web surface) is structurally new to this log. It extends the MCP ecosystem beyond tool-call primitives into a pattern where a specialized perception-action agent (the browser) is delegated to by a higher-level orchestrator. ARTEMIS introduced this on Android; WebBrain brings it to the browser.

## What stands out immediately

- **MCP server as first-class interface**: Running WebBrain as `--mcp-server` exposes browser as a tool to any MCP client — Claude Code, Cursor, Codex can call it without embedding browser code themselves
- **Authenticated session sharing**: The MCP mode uses an already-signed-in browser session, bypassing the re-authentication problem that makes headless browser agents fail on OAuth/SSO-protected pages
- **Three distinct operational modes**: Ask (read-only/query), Act (interaction/automation), Dev (scripting/debugging) — each with different tool access and risk profile
- **Deterministic by default**: Temperature 0.15 for browser control — unusual choice, positions the tool as a precision executor, not a conversational agent
- **106 built-in provider cards**: OpenAI, Claude, Gemini, Azure, AWS Bedrock, Mistral, DeepSeek, plus local models (Ollama, llama.cpp, vLLM) and WebGPU (experimental)
- **Scheduling and polling**: `/schedule` for deferred tasks, `/watch` for condition-based polling — browser-level event loops without a separate orchestration layer
- **License change signal**: Earlier releases were MIT; v33.0.0+ is GPL-3.0. The relicensing decision suggests the maintainer is protecting a commercial advantage — enterprise forks would now trigger copyleft obligations
- **Token-aware auto-compaction**: Handles 16k-token minimum context requirement without user intervention; overflow recovery is built in

## Why clawfit should care

The MCP delegation model establishes a new sub-pattern in the L4 capability layer: **sub-agent delegation via MCP**. Previously, the model was: coding agent (L2) calls MCP tools (L4) directly. WebBrain introduces a third level: coding agent → browser agent (L4) → web interactions. This matters for scoring in three ways:

1. **Task coverage expansion**: Tools with `tasks: ["browser-automation"]` were previously separate from coding agents. WebBrain collapses that distinction — a coding agent using WebBrain can now handle browser tasks without switching tools. Current task-based filtering treats these as separate decision branches.
2. **Network/authentication scope**: The MCP-delegated-authenticated-session model means `network: online` tools using WebBrain inherit the user's session permissions. No current filter handles the distinction between an agent with its own credentials vs. one borrowing a user's authenticated session.
3. **License constraint**: The GPL-3.0 relicensing is a hard constraint for enterprise profiles with `governance_need: hard`. No current registry field captures copyleft exposure from a browser-capability dependency.

Cross-surface pattern: ARTEMIS (Android, 2026-09-12) + WebBrain (browser, 2026-09-14) are two signals within 48 hours for "MCP-compatible native surface automation." ARTEMIS is Google-official (Apache 2.0); WebBrain is community-maintained (GPL-3.0). Same structural role, different surfaces and governance. Not yet two signals for the same sub-type, but approaching it.

## Preliminary interpretation

Current best reading:
- **Level 4 — Capabilities/Skills (Browser perception+action)** (primary)
- **Level 6 — Human Interface** (secondary, for the direct extension mode)

The MCP server mode is what makes this interesting at L4: it enables browser automation as a composable capability that any L2 harness can call. The direct extension mode (user interacts with the side panel) is a pure L6 surface. The two modes target different audiences with different architectural implications.

## Claims to verify

- **MCP server compatibility in practice**: Does the WebBrain MCP server actually work with Claude Code's current MCP client implementation? The description says coding agents "can delegate browser tasks" but this may be aspirational — MCP server implementations vary in schema compatibility.
- **Authenticated session isolation**: When a coding agent delegates via MCP, does WebBrain run in the user's existing tab context (risky — the agent has access to all cookies/sessions) or in an isolated context? The security boundary is unclear from available documentation.
- **GPL-3.0 scope**: Does the GPL-3.0 license on the extension itself propagate to code that *uses* the MCP server, or only to derivative works of the extension? LGPL would not propagate; GPL might. Enterprise legal teams will need to assess this before adopting WebBrain as an MCP dependency.
- **1,000 stars threshold**: The project is right at the minimum tracking threshold (100 stars). The 121 forks suggest active use rather than star farming, but the community size is small relative to ARTEMIS (2,500 stars) or camofox (tracked earlier).
- **Temperature 0.15 rationale**: This is a low-temperature choice that limits creative problem-solving in novel UI patterns. The rationale for this default is not documented; it may introduce failure modes on dynamic or unusual web interfaces.

## Status

- First tracking: 2026-09-14
- Stars: 1,000 (above 100-star minimum; well below 5,000 registry threshold)
- Registry deferred: Stars below threshold; GPL-3.0 license complicates enterprise use; no public pricing for the managed "WebBrain Compass 1.0" model
- Watch: Does the MCP delegation model become common across browser/surface agents? Does ARTEMIS + WebBrain trigger a two-signal "MCP surface delegation" canonical pattern in a future scan?
- Related signals: ARTEMIS Android agent (2026-09-12, L4/L6), camofox browser agent (tracked earlier), browser-use framework (tracked earlier)
