# Research Watch: Mirage — Unified Virtual Filesystem for AI Agents

- Repo/Link: https://github.com/strukto-ai/mirage
- Source: GeekNews front page

## Why this is worth watching

Mirage mounts 20+ cloud services and databases (S3, Google Drive, Slack, Gmail, Redis, MongoDB, GitHub, Notion, Linear, and more) as a single Unix-like virtual filesystem tree, allowing AI agents to read, write, and pipe data across backends using familiar bash semantics. Agents interact with a unified FS rather than learning separate APIs per backend. Integrations exist for OpenAI Agents SDK, Vercel AI SDK, LangChain, Pydantic AI, CAMEL, and OpenHands.

## What stands out immediately

- 20+ backends under one mount tree: cloud storage, Google Workspace, collaboration (GitHub, Linear, Notion), comms (Slack, Discord), databases (MongoDB, Redis), local (RAM, Disk, SSH)
- Apache-2.0 license, TypeScript + Python dual implementation
- No MCP server documented — integration is SDK-level (Agents SDK, LangChain adapters)
- Filesystem abstraction is a different integration pattern from MCP tool calls: agents issue bash-like commands rather than structured tool invocations
- 2.5k★ — below the 5k registry threshold

## Why clawfit should care

Mirage occupies a new L4c sub-niche: **unified agent filesystem abstraction** — structurally distinct from existing L4c entries (MCP servers, browser automation, workflow bridges). Where n8n-mcp exposes workflow templates via MCP, Mirage exposes live data backends via filesystem semantics. The SDK-level integration (not MCP) is architecturally notable: it attaches at the agent SDK layer rather than the tool-protocol layer, making it relevant for harnesses running Agents SDK or LangChain but not for pure Claude Code plugin setups. The `online` + multi-backend nature means `data_sensitivity: confidential` profiles should treat it with caution.

## Preliminary interpretation

Current best reading:
- **Level 4c — Capability Extension / Tool-Use Layer**
- Sub-type candidate: unified agent filesystem abstraction (distinct from MCP tool-call bridge, distinct from workflow platform bridge)

## Status

- 2.5k★, Apache-2.0, TypeScript+Python — below 5k threshold
- Deferred per threshold rule; promotion threshold: 5k★ OR a second tool offering SDK-level unified FS abstraction across 10+ backends
- Watch: whether MCP server support is added (would strengthen L4c classification and expand reachability to Claude Code users)
