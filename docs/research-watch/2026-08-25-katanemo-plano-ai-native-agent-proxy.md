# Research Watch: katanemo/plano — AI-Native Proxy and Data Plane for Agentic Apps

- Repo: https://github.com/katanemo/plano (⭐7,000+)
- Source: Web search / GitHub trending ai-framework topic

## Why this is worth watching

Plano moves agent infrastructure concerns — LLM routing, distributed tracing, safety filters — out of application code and into a centralized proxy layer. The architectural bet is that these concerns should be declared in YAML and handled at the data plane, not re-implemented in each agent. This is the Envoy pattern applied to the agent layer: treat agent orchestration as a networking problem with observable, policy-controlled flows.

The choice of Envoy as the base is not cosmetic. Production proxy infrastructure carries decades of battle-tested behavior around health checking, circuit breaking, and hot-reloading. Grafting agent-specific concerns (LLM routing, agentic signal tracing, guardrail filter chains) onto that base is a credible strategy for production deployments at scale — as opposed to rolling bespoke middleware in every organization's harness code.

## What stands out immediately

- **Envoy-native architecture**: Plano is a sidecar/proxy, not a library — agent routing and observability are handled at the network layer rather than in application code, so agents don't need instrumentation changes
- **LLM routing by semantic alias**: requests can be dispatched by model name, declared aliases, or automatic preference — separating what model the agent wants from which endpoint delivers it at deployment time
- **End-to-end OpenTelemetry tracing without instrumentation**: the proxy layer injects agentic signal traces automatically; developers don't add trace decorators to agent code
- **Guardrail filter chains**: moderation, safety, and content policies are declared centrally and applied per-route, not scattered across agent implementations
- **Lightweight 4B-parameter routing models**: LLM-aware routing decisions use small purpose-built models rather than expensive general-purpose ones — cost-pragmatic
- **YAML agent declaration**: agents are defined as first-class configuration objects, not code artifacts — enables infrastructure-as-code deployment workflows for agent fleets
- **749 commits, 108 open issues**: active development with a visible backlog, not a demo project

## Why clawfit should care

Plano addresses a real production gap in clawfit's current model. clawfit scores (agent, llm, hardware) triples and recommends configurations, but says nothing about what surrounds a deployed agent: how it routes to models, how it is observed, how safety policies are enforced. Plano occupies the layer between the agent runtime and the LLM endpoint — a layer clawfit has no scoring dimension for.

Two dimensions that Plano reveals as missing: (1) a `routing_layer: [none | gateway | proxy | service-mesh]` axis capturing whether the deployment has centralized model routing; (2) an `observability: [none | logs | traces | full-agentic-signals]` axis. A production organization using Plano would have meaningfully different infrastructure maturity than one calling the LLM API directly from agent code.

The 7,000-star signal also suggests this is not early-explorer territory — teams are actually deploying this, which means the surrounding ecosystem (harnesses, agents) is being adapted to assume a proxy layer exists.

## Preliminary interpretation

Current best reading:
- **Level 5 — Observability / Infrastructure Data Plane**: primary. Plano's core differentiation is automated agentic signal tracing and centralized observability without code instrumentation. The proxy carries traces, metrics, and policy enforcement that agent code does not need to implement.
- **Level 2 secondary**: the routing, orchestration, and YAML-declared agent topology also serve harness concerns — it wraps and coordinates agents above the base runtime.

Contrast with: deepagents (L2 harness, app-layer SDK), benchflow/awesome-evals (L5 eval library), katanemo is infrastructure, not application-layer.

## Claims to verify

- Whether "end-to-end tracing without instrumentation" requires agents to use a specific SDK or truly intercepts at the network level — the proxy claim needs testing against arbitrary agent runtimes
- Whether guardrail filter chains can be updated without restarting the proxy — hot-reload is the critical production requirement here
- Whether the 4B routing models need to be self-hosted or are embedded — cost and latency implications differ significantly
- 7,000+ stars — whether this reflects production deployments or interest from organizations evaluating the pattern

## Status

- Tracking: first signal 2026-08-25
- Stars: 7,000+ — above 5k registry threshold; however, no clean agent/LLM/hardware schema slot for an infrastructure proxy (no `routing_layer` or `observability` field in current registry schema)
- Registry decision: skip; schema mismatch, not a gap in data
- No canonical section change: single signal for "agent-layer proxy/data plane" pattern; two-signal rule requires a second (a comparable competitor or wide adoption in multiple major harnesses)
- Schema watch: `routing_layer: [none | gateway | proxy]`; `observability_tier: [none | logs | traces | agentic-signals]`
- Watch: whether major harnesses (hermes-agent, deepagents, Claude Code) add native Plano integration or whether Anthropic's own proxy layer (if any) covers this gap
