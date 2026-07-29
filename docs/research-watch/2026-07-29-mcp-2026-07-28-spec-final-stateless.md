# Research Watch: MCP 2026-07-28 Final Specification — Stateless Transport Ratified

- Repo/Link: https://modelcontextprotocol.io/specification/2026-07-28/changelog
- Source: Hacker News (95 pts, 2026-07-29) — "MCP 2026-07-28 Specification: transport going stateless"
- RC first signal: `docs/research-watch/2026-07-05-mcp-stateless-spec-2026-07-28-rc.md`

## Why this is worth watching

The RC tracked 2026-07-05 has been ratified as the official MCP specification. This is no longer
experimental: the stateless design, MRTR pattern, and deprecated session primitives are now the
canonical protocol contract every MCP server must eventually implement. The spec ships alongside
SDK compatibility commitments, making migration pressure concrete.

## What stands out immediately

- **Final vs. RC delta — three new additions:** `subscriptions/listen` (long-lived POST stream
  replacing GET/SSE endpoint + `resources/subscribe`); explicit OpenTelemetry trace context
  propagation via `_meta` keys; custom `Mcp-Param-{Name}` headers from tool parameter
  `x-mcp-header` annotations.
- **Deterministic tool ordering required:** `tools/list` SHOULD return tools in deterministic order
  to enable client-side LLM prompt cache hits — first spec requirement explicitly motivated by
  inference cost reduction.
- **OAuth 2.0 Dynamic Client Registration deprecated** in favour of Client ID Metadata Documents.
  Any registry entry with a cloud MCP server that uses DCR-based auth needs an update note.
- **`server/discover` is now normative:** Clients MAY call it before any other request; response is
  cacheable with `ttlMs` + `cacheScope`. Makes lazy capability negotiation the recommended pattern.
- **MRTR (Multi Round-Trip Requests) replaces all server-initiated request patterns:** `roots/list`,
  `sampling/createMessage`, and `elicitation/create` all migrate to client-initiated retry with
  `inputResponses`. Affects any tool that relied on server-side sampling.

## Why clawfit should care

RC tracked 2026-07-05 identified action items; this final release triggers them:
1. **L4c audit is now mandatory** — `statefulness: session` entries that rely on protocol-level
   session continuity are non-compliant. Affected entries: chrome-devtools-mcp, unity-mcp,
   gitnexus, desktopcommandermcp (flagged 2026-07-09 as likely to break).
2. **Sampling-dependent tools must migrate** — entries that used MCP's `sampling/createMessage`
   capability (e.g., tools building internal LLM pipelines via sampling) face a 12-month deprecation
   runway (~mid-2027) but should be flagged now.
3. **`subscriptions/listen` changes the push model** — tools that exposed event streams via the old
   GET/SSE transport (resources subscription) need to document their migration path.
4. **Manufact (L7 MCP hosting, 2026-07-02) scoring rationale strengthened** — stateless MCP is
   trivially load-balanced; Manufact's value proposition is now protocol-native, not operator-add-on.

## Preliminary interpretation

Current best reading:
- **Cross-layer protocol event** (L4c + L5 scope)
- Not a deployable tool; no new registry entry warranted
- Triggers deferred audit actions from the 2026-07-05 RC signal

## Status

- Second signal for MCP stateless spec (first: RC, 2026-07-05). Final ratification. Action items
  from RC now active: audit L4c entries for session-continuity assumptions; flag sampling-dependent
  tools; update Manufact scoring rationale note.
