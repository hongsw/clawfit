# Research Watch: agno — Multimodal Agent Runtime with MCP Interface v2

- Repo: https://github.com/agno-agi/agno (⭐26,000)
- Source: GitHub Trending Python (2026-07-09); v2.7.0 released 2026-07-07, v2.7.2 released 2026-07-09

## Why this is worth watching

Agno is a high-performance multimodal agent execution environment that shipped two major releases this week. v2.7.0 (July 7) introduced a dedicated `agnoctl` CLI, service account tokens (PATs), an eval suite runner (`agno.eval`), a GET /info discovery endpoint, and MCP interface v2 with an 8-tool operator surface and a single auth layer spanning REST, MCP, and WebSocket. v2.7.2 (July 9) added OAuth for the AgentOS MCP endpoint, AG-UI client tools, `agno connect` multi-target, and patched a path traversal security vulnerability. The pace — two releases in three days, both touching auth and protocol surface — is characteristic of a runtime in active production hardening rather than feature exploration.

MCP interface v2 with a defined 8-tool operator surface makes agno one of the few L1 runtimes with a versioned, MCP-native operating contract rather than MCP as an add-on. That matters for clawfit's tracking of how the MCP ecosystem is stratifying between runtimes that consume MCP servers and runtimes that expose MCP endpoints.

## What stands out immediately

- **MCP interface v2**: 8 named tools forming the operator surface for AgentOS; moves MCP from plugin to first-class protocol for agent-to-agent coordination
- **`agnoctl` CLI**: separate management binary (`agno connect` / `tokens` / `create`) — operational toolchain distinct from the Python runtime SDK
- **Service account PATs**: per-user session isolation for Foundry Hosting; implies multi-tenant deployment was a known production gap being closed
- **Eval suite runner (`agno.eval`)**: in-framework evaluation loop — not a separate tool; eval is a first-class primitive alongside inference
- **GET /info discovery endpoint**: self-describing endpoint; agent clients can discover capability surface without out-of-band documentation
- **AG-UI client tools**: integration with the emerging AG-UI standard for agent-client UI protocols
- **Path traversal security fix** in v2.7.2: CVE-style patch in the same release cycle as OAuth hardening — security surface is being actively audited
- **Auth unification**: single auth layer across REST/MCP/WebSocket removes the pattern where MCP endpoints had weaker auth than REST equivalents

## Why clawfit should care

Agno's MCP interface v2 with a versioned 8-tool operator surface is the closest current match to "agent as MCP server" that clawfit has tracked — not an MCP consumer, but an MCP provider. If the MCP 2026-07-28 RC stateless spec becomes stable (tracked 2026-07-05), runtimes that expose a versioned MCP endpoint rather than relying on long-lived sessions will have an architectural advantage in horizontal scaling. Agno's v2.7.0 architecture (stateless-compatible + discovery endpoint + PAT auth) is aligned with the RC's direction.

The built-in eval suite (`agno.eval`) is relevant to clawfit's L5 scoring: a runtime with integrated eval changes the cost/latency model for quality assurance — eval is no longer a separate tool deployment with its own overhead. If eval becomes the runtime's native quality gate rather than an external layer, clawfit's recommendation logic for `statefulness: session` use cases may need to account for runtime-native eval overhead.

Current clawfit filters do not distinguish between agent runtimes that expose MCP endpoints and those that consume MCP servers — agno is one of the first tracked signals where that distinction is operationally meaningful.

## Preliminary interpretation

Current best reading:
- **Level 1 primary — Agent runtime**: agno runs the agent execution loop (multimodal input, tool calling, multi-turn conversation) across its operator surface
- **Level 4c secondary — MCP endpoint**: AgentOS MCP endpoint (v2, 8-tool surface) makes agno itself a MCP capability server, not just a MCP client; this is a novel layer position for an L1 runtime

The MCP provider role is the structurally novel signal here — it suggests a new deployment pattern: an L1 runtime that is simultaneously an L4c capability server for other agents, enabling agent-to-agent coordination via a standardized protocol.

## Claims to verify

- "8-tool operator surface" — tool names and semantics not enumerated in available sources; surface area should be inspected against the MCP 2026-07-28 RC specification
- AG-UI client tools behavior under concurrent multi-target `agno connect` — concurrency model not documented
- PAT per-user session isolation: whether this is enforced at the runtime layer or delegated to Foundry Hosting infrastructure
- Eval suite quality: whether `agno.eval` runs human-written test cases or relies on LLM-as-judge (significant cost/reliability difference)
- Path traversal patch scope: whether CVE scope was limited to AgentOS endpoints or extends to local file tool execution

## Status

- 26,000★, v2.7.2 (July 9, 2026), Python primary, MIT license
- Registry eligibility: above 5k threshold; hold pending: (1) no `deployment_surface: agentOS` field in current schema; (2) MCP provider role has no current schema expression; (3) latency on reference hardware unverified; (4) eval overhead not quantified
- Schema watch: `mcp_role: [consumer, provider, both]` — agno is the first tracked L1 runtime that is also a versioned MCP provider; `eval_native: true/false` for runtimes with embedded eval loops
- Promotion criterion: independent latency benchmark on reference hardware + MCP provider role confirmed in second tracked L1 runtime (two-signal rule for new MCP-provider sub-type)
