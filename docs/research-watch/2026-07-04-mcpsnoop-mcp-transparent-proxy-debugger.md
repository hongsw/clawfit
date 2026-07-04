# Research Watch: mcpsnoop — Transparent Proxy/Debugger for MCP

- Repo/Link: https://github.com/kerlenton/mcpsnoop
- Source: Hacker News (Show HN, 44 points, 13 comments, 2026-07-04)

## Why this is worth watching

mcpsnoop positions itself as "Wireshark for MCP" — a transparent proxy that sits inline in the actual data pipe between AI client and MCP server, capturing live JSON-RPC traffic. This is architecturally distinct from the official MCP Inspector, which connects as a separate client and therefore sees only test-client traffic rather than production traffic patterns. At 127 stars and pre-1.0, this is an early signal, but it arrives in the same week as two browser-vendor MCP capability layers (Chrome DevTools MCP, Safari MCP Server) — a cluster of MCP-layer tooling attention that warrants noting.

## What stands out immediately

- Inline proxy design: captures actual agent-to-server JSON-RPC stream, not a sidecar or shadow client — traffic authenticity is the architectural claim
- Hung-call detection with live timers: addresses a real production pain point (MCP server hangs are opaque without tooling)
- Tool-call replay: lets developers retrigger a captured call without re-running the full agent session
- Capability handshake inspector: exposes what MCP servers advertise during initialization, useful for diagnosing mismatches between client expectations and server capabilities
- Query filtering via typed tokens (`tool:`, `status:`, `dir:`): structured log exploration, not raw stream dump
- Single binary, zero-configuration: low-friction install, relevant to `setup_complexity` scoring
- Go (99.3%), MIT license: aligns with the Go-native harness trend (go-micro tracked 2026-07-01); portable cross-platform binary

## Why clawfit should care

The registry has no current L4c observability entry for the MCP protocol layer — all tracked MCP tools are capability providers (MCP servers), not protocol-level observers. mcpsnoop is the first signal for "MCP protocol debugger" as a sub-type distinct from MCP Inspector (separate client) and Manufact Cloud Inspector (hosted, browser-based). The hung-call detection feature is directly relevant to `latency: low` profiles: agents that depend on MCP tool calls with undetected hangs violate latency constraints silently. A clawfit user debugging why their `latency: low` recommendation is underperforming in practice would benefit from this class of tool, even though it has no per-call cost or star threshold to qualify for registry entry today.

## Preliminary interpretation

Current best reading:
- **Level 4c — Capability / Tool-use layer** (MCP developer tooling sub-type: protocol-level observability infrastructure for the MCP tool-call surface)
- Not L5: mcpsnoop does not provide memory, context, or a new MCP server surface — it observes existing MCP traffic

## Status

- First signal; 127★ well below registry threshold (5k★); pre-1.0; no production deployment evidence
- No map mutation: first signal for "MCP protocol debugger" as a named L4c sub-type; insufficient for taxonomy update
- Promotion criterion: 2k★ OR adoption documented by a tracked L1/L2 agent runtime as a default debugging path, OR second independent inline MCP proxy tool appears
