# Research Watch: MCP 2026-07-28 RC — Stateless Protocol Core

- Source: https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- Also see: https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/ (SDK beta announcement), https://byteiota.com/mcp-goes-stateless-2026-release-candidate/ (community analysis), https://techcommunity.microsoft.com/blog/appsonazureblog/mcp-just-went-stateless-%E2%80%94-what-the-2026-spec-changes-about-scaling-on-app-servic/4430222 (Azure scaling implications)

## Why this is worth watching

This is the second major architectural revision to the MCP specification (the first was the 2025-11-25 tool-call format). Removing the session layer is not an incremental improvement — it changes the fundamental deployment contract for every MCP server already in production, making horizontal scaling native to the protocol rather than an operator-configured workaround. It arrives alongside a formal deprecation lifecycle policy and a Tasks redesign (SEP-2663), signalling that the spec is moving toward stability rather than continued rapid experimentation.

## What stands out immediately

- **Session layer removed entirely (SEP-2567):** `Mcp-Session-Id` header and the `initialize`/`initialized` handshake are gone. Any request can now land on any server instance; sticky routing is a protocol-level requirement no longer. Client metadata (client info, capabilities) migrates to `_meta` on every request.
- **Three new required headers per request:** `MCP-Protocol-Version: 2026-07-28`, `Mcp-Method`, and `Mcp-Name` must be present on every call, enabling traffic routing without body inspection. This is a hard breaking change for any HTTP middleware that strips unknown headers.
- **SSE long-lived streams replaced by Multi Round-Trip Requests:** Servers that previously held SSE streams open for interactive input now return `InputRequiredResult` with a `requestState` token; clients re-call the original method with `inputResponses` and the echoed state. Eliminates the server-side connection management burden.
- **Tasks moved to extension (SEP-2663), migration required:** The experimental core Tasks feature (from `2025-11-25`) is replaced by a stateless polling lifecycle — `tasks/get`, `tasks/update`, `tasks/cancel` — driven by the client after an initial `tools/call` returns a task handle. Existing implementations must migrate; there is no grace period stated.
- **Error code change: `-32002` → `-32602`:** Resource-not-found shifts from the MCP-custom code to JSON-RPC-standard "Invalid Params." Clients doing exact numeric error matching will silently misclassify errors after upgrade.
- **Roots / Sampling / Logging deprecated with 12-month runway (to ~mid-2027):** Official replacements given — tool parameters or resource URIs for Roots; direct LLM provider API for Sampling; `stderr` or OpenTelemetry for Logging. Deprecation does not mean immediate removal; a separate SEP is required post-runway.
- **`server/discover` method replaces the handshake:** Clients can fetch server capabilities on demand rather than only at connect time. Makes capability negotiation lazy and stateless.
- **Caching headers added (`ttlMs`, `cacheScope`):** List and resource responses now carry freshness duration and cross-user cache safety signals, modelled on HTTP `Cache-Control`. Enables proper CDN or proxy caching of MCP resource responses for the first time.

## Why clawfit should care

**Registry exposure is direct.** Every tracked L4c MCP server (chrome-devtools-mcp, unity-mcp, codex-plugin-cc, gitnexus, and ~7 others) implements the prior handshake model. The stateless RC is not backward-compatible; any tool listed with `statefulness: session` that relies on protocol-level session continuity will need a documented migration timeline, not just a version bump note.

**L2 harnesses with MCP routing assumptions need re-evaluation.** Harnesses that embed sticky-session routing logic (e.g., strands-agents/harness-sdk, go-micro, AutoHarness) assumed the protocol required per-connection affinity. That assumption is now architecturally incorrect. The scoring axis `statefulness: session` partially captured this but was modelling application-level state, not transport-level session; the distinction now matters explicitly.

**Manufact (L7 MCP cloud hosting, tracked 2026-07-02) becomes a more natural fit.** Stateless MCP servers are trivially load-balanced behind a standard HTTP proxy. Manufact's auto-deploy + PR preview model is significantly easier to operate against a stateless spec; clawfit's scoring note for `mcp_hosting` should acknowledge this.

**The Tasks extension gap:** Tools that implement long-running task patterns (the async variant of `tools/call`) must migrate from the experimental core Tasks to SEP-2663. This is a capability-layer schema question: does clawfit need a `task_protocol: stateless_polling | streaming` field to distinguish tools by their async model?

## Preliminary interpretation

Current best reading:
- **Level 5 — MCP / context layer** (this is the specification backbone that L5 MCP tools implement)
- **Level 4c cross-impact** (every tracked MCP server in the registry is affected; migration is not optional)
- This is a **protocol artifact**, not a deployable tool — it does not receive a registry entry; impact is tracked through the affected tool entries

No map mutation to `docs/reference-levels.md` warranted at this stage. However, the L4c section description currently reads as if MCP server authors only make tool-content decisions; it should eventually note that the transport contract (stateless vs. session-bearing) is now a first-class dimension of MCP server architecture.

## Claims to verify

- **Tier 1 SDK ten-week window (May 21 – July 28, 2026):** The official blog states Tier 1 SDKs must ship support within ten weeks. Confirm which SDKs are Tier 1 and whether Python and TypeScript official SDKs are actually shipping RC-compatible betas by the July 28 date. Source: SDK beta announcement blog post (see `Also see` link).
- **Tasks SEP-2663 migration requirement:** The blog says existing `2025-11-25` Tasks implementations "must migrate" but does not state a deadline. Verify whether there is a deprecation runway for the old Tasks core feature or whether it is cut immediately in this RC.
- **Error code `-32002` removal scope:** Confirm whether `-32002` appears in any official SDK helper (e.g., error factory methods) or only in specification text — this determines whether application code catches it directly or only through SDK abstractions.
- **`server/discover` replaces or supplements handshake:** The blog implies `server/discover` is a new on-demand capability fetch; verify that it is not simply a renamed `initialize` with the same one-shot semantics.
- **Sampling deprecation affects L4 tool patterns:** Several tracked tools use sampling (model-driven sub-calls) as their primary mechanism. Verify which registry entries currently depend on the `sampling` capability and flag them for `org_fit` notes.

## Status

- First signal for a stateless MCP specification at RC stage. Protocol-layer event; no registry entry. Action items: (1) audit tracked L4c MCP server entries for session-continuity assumptions; (2) add migration note to `statefulness: session` scoring documentation; (3) flag Sampling-dependent registry entries; (4) monitor SDK Tier 1 beta releases for confirmed compatibility.
