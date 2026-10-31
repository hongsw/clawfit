# Research Watch: TanStack AI 1.0 — Cross-Framework Agent SDK with Stable Core and Experimental Harness

- Repo: https://github.com/TanStack/ai (⭐3,300)
- Source: GitHub Trending (Python, daily, 2026-10-31)

## Why this is worth watching

TanStack AI reached stable 1.0 in October 2026 after a 0.x incubation period. The stable 1.0 covers the core API surface: streaming chat, typed tools, structured outputs, multimodal prompts, and 23 provider adapters. A separate `@tanstack/ai-harness` package and CLI remain at 0.x and experimental. The project's architectural stance — tree-shakable adapter packages, no lock-in, support for every major JS framework — makes it the most framework-neutral AI toolkit tracked to date.

The 1.0 stability signal is meaningful because TanStack has established credibility in the frontend ecosystem (TanStack Query, Router, Table) and 1.0 is a commitment to API stability that enterprise teams evaluate. The harness remaining at 0.x is honest: it shows the project is not overclaiming stability on the most complex part.

## What stands out immediately

- **23 provider adapters** with a common interface: OpenAI, Anthropic, Gemini, OpenRouter, Ollama, Groq, and others; `openaiCompatible` option covers any OpenAI-style API; no single-provider lock-in by design
- **AG-UI stream protocol**: streams use standard AG-UI events; a run ends with a `RUN_FINISHED` event instead of a `[DONE]` sentinel — conformance with the AG-UI protocol tracked 2026-06-06
- **MCP in both directions**: `createMCPServer` exposes TanStack tools to MCP hosts (Claude Desktop, Cursor, etc.); WebMCP support in both directions; MCP servers can be loaded as a harness plugin
- **Portable agent skills**: SKILL.md format skills can be loaded by any tool-calling model as needed; harnesses can expose skills as slash commands; coding assistants can use TanStack AI skills to write correct TanStack AI code — skill distribution pattern similar to anthropics/skills (2026-05-11)
- **Harness delegates to external coding agents**: `@tanstack/ai-harness` can hand off coding tasks to Claude Code, Codex, OpenCode, Grok Build, or any ACP agent in a sandbox (11 sandbox providers supported); the harness as coordinator, coding agent as executor pattern
- **Code Mode**: model writes and runs TypeScript in an isolated sandbox to orchestrate tools — in-process code execution as an agent primitive
- **Durable sessions**: harness sessions are durable, users can steer a running turn, approvals can wait across restarts; the harness can run as CLI, web app, IDE (ACP), or MCP server
- **OpenTelemetry observability**: built-in tracing and cost tracking

## Why clawfit should care

TanStack AI's architecture spans L2 (harness) and L4 (MCP/skills/capabilities) with 1.0 API stability on the core. Its 23 provider adapters make it the widest-coverage AI toolkit tracked — broader than Mastra (TypeScript, 2026-07-27), Vercel EVE (filesystem-first, 2026-10-11), or Unreal Agent (async, 2026-09-23), each of which had narrower provider support or platform assumptions.

The skill distribution mechanism and coding agent delegation pattern directly parallel the clawfit scoring dimension of `LLM preference`: a team using TanStack AI can swap providers without changing application code, making the `budget` and `latency` constraints more dynamic than they are in single-provider harnesses.

Registry implication: at 3.3k stars, TanStack AI is below the 5k threshold for registry addition. But the 1.0 release, MIT license, and provider-neutral stance make it a watch-level signal for when stars grow. The framework-neutral client surface (React, Vue, Solid, Svelte, Preact, Angular) is not modeled in the current registry schema — a potential `client_surface` field for the agents registry.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness / Wrapper** (primary): `@tanstack/ai-harness` provides durable sessions, agent coordination, and harness lifecycle management; the stable 1.0 core is the foundation
- **Level 4 — Capabilities / Skills / MCP** (secondary): MCP bidirectional support, SKILL.md portable skills, Code Mode, and 23 provider adapters are capability-layer additions

## Claims to verify

- Whether `@tanstack/ai-harness` 0.x is production-ready despite the 0.x label — the blog notes "sessions are durable" and "approvals can wait across restarts," which suggests real production use
- Whether the 11 sandbox providers for coding agent delegation are tested integrations or aspirational compatibility
- Star count growth trajectory: 3.3k now vs. launch date — rapid growth would indicate developer adoption faster than star count alone suggests
- Whether the AG-UI conformance is tested interoperability or self-declared; the AG-UI 1.0 spec (if it exists) would be the reference

## Status

- New signal; not previously tracked
- Registry eligibility: below 5k threshold at 3.3k stars; no registry addition
- Watch for: growth past 5k stars and confirmed production harness use — would trigger registry candidacy review
- Relation to prior signals: AG-UI protocol (2026-06-06), anthropics/skills (2026-05-11), Mastra (2026-07-27), Vercel EVE (2026-10-11) — TanStack AI is the first to combine all four patterns (AG-UI, skills, MCP, multi-provider) in one stable package
