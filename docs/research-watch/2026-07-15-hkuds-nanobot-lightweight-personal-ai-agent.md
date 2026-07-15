# Research Watch: HKUDS/nanobot — Lightweight Self-Hosted Personal AI Agent with Multi-Channel Gateway

- Repo: https://github.com/HKUDS/nanobot (⭐45,700)
- Source: GitHub Trending Python, 2026-07-15

## Why this is worth watching

Nanobot (v0.2.2, June 23, 2026) is a self-hosted AI agent runtime that exposes a single agent loop across six communication channels simultaneously: Telegram, Discord, Slack, WeChat, Feishu, Mattermost, and email. At 45.7k stars and 8.1k forks on a June 2026 release, its velocity is comparable to the fastest-trending agent harnesses tracked this year. The project sits between L1 (base runtime — it runs the agent loop) and L2 (harness — it wraps multiple LLM providers and multiplexes channels), with a WebSocket gateway that decouples the agent from any single interface. The "ultra-lightweight" framing and "truly own" positioning are marketing claims that require stress-testing against actual resource consumption and data isolation guarantees, but the architecture makes a coherent argument for personal-sovereignty agent deployment.

## What stands out immediately

- **Multi-channel agent loop**: a single agent instance serves Telegram, Discord, Slack, WeChat, Feishu, Mattermost, and email — the channel list spans both Western and East Asian platforms, an uncommon combination
- **WebSocket gateway architecture (port 8765)**: messages from any channel enter a normalized gateway, then a single LLM-driven loop decides tool invocations — the transport decoupling is explicit in the architecture documentation
- **"Dream" persistent memory**: long-term memory is named and modeled as a distinct component, not just session history; the naming suggests intentional design rather than an afterthought
- **Tool inventory**: file operations, shell commands, web search/fetch, MCP, and image generation are native; this is a materially broader tool scope than most personal-tier agents
- **OpenAI-compatible provider layer**: supports Claude, ChatGPT, Ollama, vLLM, and custom endpoints via named model presets; provider switching is config-file, not code-level
- **Python/TypeScript split**: 77.7% Python backend, 21.7% TypeScript frontend; the split suggests a browser-accessible admin interface, not just a CLI
- **Scheduled automations and goal-based execution**: these imply a persistent scheduler, not just a stateless request handler — material for self-hosted infrastructure design
- **v0.2.2 is the sixth release in an active cadence** — 3,490 commits indicates this is not a launch-burst project

## Why clawfit should care

Nanobot is the first tracked tool that combines L1 runtime capabilities (agent loop, tool execution, persistent memory) with L6 interface multiplexing (six simultaneous channels) as a single self-hosted binary. Clawfit's current hardware dimension scores `cloud` vs `local` deployment, but nanobot introduces a hybrid: locally-hosted server with cloud LLM backends. More concretely, the multi-channel gateway is a new capability axis not currently scored: which agents can serve a user across contexts (desktop Slack, mobile Telegram, email) without context fragmentation? The `statefulness: session` filter in clawfit treats memory as binary; nanobot's "Dream" component suggests a `statefulness: persistent-cross-channel` tier may be missing from the taxonomy. The MCP integration as a native tool means nanobot is also an MCP consumer, placing secondary signal pressure on L4c.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/Wrapper** primary (wraps multiple LLM providers behind a unified agent loop with channel multiplexing)
- **Level 1 — Base Runtime** secondary (provides the agent loop, tool execution, and memory substrate)
- **Level 6 — Human Interface** secondary (multi-channel gateway is a significant interface layer)

## Claims to verify

- Whether "ultra-lightweight" resource consumption holds under multi-channel concurrent load (the WebSocket gateway serving six channels simultaneously with persistent memory has non-trivial resource requirements)
- Whether the "truly own" data sovereignty claim is accurate when using cloud LLM backends (cloud provider receives all messages even if the server is self-hosted)
- Whether WeChat and Feishu integrations work outside China (both require business account approval for API access)
- Whether "Dream" persistent memory is encrypted at rest or accessible in plaintext on the host filesystem
- Whether the 45.7k star velocity (rapid for a June 2026 project) reflects organic adoption or a viral HN/GeekNews spike — the star-growth-type distinction matters per the 2026-07-14 zero-cost-fallacy signal

## Status

- **Registry eligibility**: conditional — stars (45.7k) meet the 5k threshold; schema maps to L2 harness; but public cost/latency data is undefined (self-hosted, no benchmark published for nanobot-specific overhead). Registry entry blocked pending benchmark data.
- **Schema watch**: `statefulness: persistent-cross-channel` as a new statefulness tier candidate; `channel_multiplexing: true/false` as a new agent capability field; `data_sovereignty: [cloud-dependent | hybrid | fully-local]` as a deployment field candidate
- **Open questions**: Is nanobot's star count driven by the HKUDS lab's prior work (DeepTutor, Vibe-Trading both trending simultaneously), suggesting a lab-wide marketing push rather than community validation? All three HKUDS projects appear in today's trending lists.
