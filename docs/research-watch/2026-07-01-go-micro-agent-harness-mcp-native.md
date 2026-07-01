# Research Watch: Go Micro — Go Agent Harness with Native MCP/A2A

- Repo: https://github.com/micro/micro
- Also see: https://go-micro.dev/

## Why this is worth watching
Go Micro is a 23,000+ star Go framework that has pivoted from microservices infrastructure into a unified agent harness — with MCP tool generation, A2A inter-agent communication, memory, and guardrails all built in as first-class primitives rather than bolt-ons. The Anthropic/OpenAI/Atlas Cloud sponsorship is a credibility signal that warrants scrutiny independent of star count. The Go angle matters: most harnesses in the current registry are Python-first, so a production-grade Go entrant with protocol-native design covers a runtime gap clawfit has not formally tracked.

## What stands out immediately
- **MCP generation is automatic**: service endpoints are exposed as MCP tools without manual schema authoring — this is a claim to inspect, not a validated implementation detail
- **A2A built in**: inter-agent delegation via Agent-to-Agent protocol sits alongside MCP at the framework level, not as a plugin
- **Per-agent composition model**: each agent is assembled from discrete Go interfaces — model, memory, tools, planner, guardrails, execution middleware — all swappable
- **Hybrid workflow design**: deterministic code paths hand off to agents for dynamic sub-tasks; agents can return to deterministic paths — explicit acknowledgment that pure-agentic is not always appropriate
- **Developer CLI**: `micro new`, `micro run`, `micro chat` follow the pattern of established CLIs (similar surface to `cargo new`, `deno run`) — lowers onboarding friction
- **Apache 2.0, production-readiness claim**: framework describes itself as production-ready, though independent production case studies are not yet surfaced in public docs
- **Sponsorship composition**: Anthropic + OpenAI + Atlas Cloud sponsoring the same framework is unusual; worth monitoring whether that constrains or accelerates protocol choices

## Why clawfit should care
Go Micro is the first Go-native harness signal with dual-protocol coverage (MCP + A2A) that clawfit has logged. The existing registry agents are Python-dominant; if Go Micro reaches meaningful adoption, clawfit's agent recommendations will have a language/runtime mismatch with teams building Go services. More structurally: the automatic MCP-from-endpoint generation pattern, if validated, compresses the tool-authoring step that currently sits between L2 (harness) and L4 (tool/plugin layer) — suggesting it could serve as a bridge entry that scores well on both dimensions simultaneously. The hybrid deterministic/agentic workflow model also maps cleanly to clawfit's `statefulness` filter axis.

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta wrappers / harnesses / orchestration layers** (primary classification: assembles and coordinates agents as composable Go interfaces with built-in planning and delegation)
- Secondary: **Level 4 — Capability / skill / plugin / tool-use layer** (automatic MCP tool generation from service endpoints, if validated, would make L4 coverage implicit within the harness)
- The A2A protocol support adds a weak secondary signal toward **Level 3** (governance/SSOT) but the framework does not appear to define policy or team-level SSOT constructs — this remains speculative until docs confirm otherwise

## Status
- First signal — 2026-07-01; starred trajectory and sponsorship justify immediate registry consideration; hold for promotion until MCP auto-generation claim is independently verified and at least one production case study is public
