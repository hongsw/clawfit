# Research Watch: openai-agents-go — OpenAI Agents SDK Ported to Go

- Repo: https://github.com/nlpodyssey/openai-agents-go (⭐273)
- Source: GitHub search (Go agent runtime, created ~2025-12)

## Why this is worth watching
The OpenAI Agents Python SDK introduced a minimal but influential set of primitives — Agents, Handoffs, Guardrails, structured output — that have become a reference architecture for L1 agent runtimes. nlpodyssey/openai-agents-go is a direct port of that SDK to Go with full feature parity: same three core primitives, same provider-agnostic design, MCP integration via the official Go MCP SDK (from Anthropic), voice support, and session persistence. Its significance is not novelty of design but ecosystem extension: it brings this architecture to Go's deployment contexts (static binaries, low-overhead containers, native concurrency, strict type safety) where running a Python runtime is an operational constraint.

## What stands out immediately
- **Full primitive parity with Python SDK**: Agents (instructions, tools, guardrails, handoffs), Handoffs (agent-to-agent transfer), Guardrails (input/output validation) — all ported
- **MCP support via official Go SDK**: integrates with both hosted MCP and local MCP servers using Anthropic's MCP Go SDK — the first Go agent framework confirmed to use the official MCP Go SDK in production
- **Provider-agnostic from the start**: supports OpenAI Responses API, Chat Completions API, and third-party LLMs via LiteLLM proxy; not locked to OpenAI despite the name
- **Go-native concurrency**: agent loops map to goroutines with `context.Context` cancellation — no async/await translation layer, no Python GIL equivalent
- **Compile-time type safety**: agent/tool definitions are statically typed, catching misconfiguration at compile time vs. Python's runtime failures
- **Full example set matching Python**: customer_service, financial_research_agent, handoffs, hosted_mcp, mcp, research_bot, voice — indicating deliberate feature tracking
- **Apache-2.0 license**, Go 1.25+ required; actively maintained (last push 2026-10-07, 9 open issues)
- 273 stars, small community but stable trajectory

## Why clawfit should care
clawfit's registry and scoring currently assume Python-native deployments (implicit in the agent ecosystem). Go agent runtimes occupy a different deployment niche: services where Python startup cost, memory footprint, or cross-compilation to static binaries matters (embedded systems, container sidecars, CLI tools deployed as single binaries). The openai-agents-go port, particularly with its MCP + session + voice support, is a signal that the L1 agent primitive set is now crossing into Go production environments. If clawfit adds a `runtime_language` or `deployment_model` axis, Go runtimes would be a distinct category alongside Python, TypeScript, and Rust runtimes already visible in the ecosystem.

## Preliminary interpretation
- **L1 — Base Agent Runtime** (primary): implements the fundamental agent loop, handoffs, guardrails, and structured output — directly comparable to the Python OpenAI Agents SDK it ports
- **L4 — Capabilities / MCP** (secondary): MCP integration means it functions as a Go-native MCP client

## Claims to verify
- "Full feature parity" with Python SDK: the repo claims parity; verify against the Python SDK's v0.0.x CHANGELOG for any features the Go port has not yet implemented (e.g., tracing integrations, streaming modes)
- MCP Go SDK attribution: confirm it uses Anthropic's official `modelcontextprotocol/go-sdk` vs. a third-party Go MCP implementation
- Voice support: listed as a feature; verify it handles both static and streaming voice modes as claimed

## Status
- 273 stars, actively maintained (push today, 2026-10-07)
- No registry entry warranted: base runtime, not a scored LLM or hardware entry; star count below the 5k registry threshold
- **First signal for "Go-native port of the OpenAI Agents SDK with MCP support"** in clawfit's research-watch corpus
- Monitor for: star growth beyond 1k, enterprise adoption reports, and whether the MCP Go SDK becomes the de-facto Go MCP client (which would elevate this repo's structural importance)
