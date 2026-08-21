# Research Watch: NVIDIA-NeMo/Switchyard — Rust LLM Traffic Router with API Protocol Translation

- Repo: https://github.com/NVIDIA-NeMo/Switchyard (⭐2,034)
- Source: GitHub Trending (weekly, +932 this week); NVIDIA-NeMo organization

## Why this is worth watching

Switchyard is a Rust proxy and library from NVIDIA's NeMo team that routes LLM API traffic across multiple providers while translating between OpenAI Chat Completions, Anthropic Messages, and OpenAI Response API formats. The provenance is the signal: a routing/translation layer authored by NVIDIA-NeMo (the same team behind NeMo Megatron and production training infrastructure) is not a weekend side project. NVIDIA's interest in cross-provider routing reflects a practical need — NeMo's production users run inference across NIM, vLLM, Ollama, and external APIs; a unified routing layer that handles protocol translation removes an integration pain point.

At 2,034 stars and "pre-alpha" status, Switchyard is too early for production adoption claims. But the architecture choices (Rust, typed composable routing algorithms, Prometheus metrics) suggest it is being engineered for production reliability, not as a research demo.

## What stands out immediately

- **Bidirectional protocol translation**: OpenAI Chat Completions ↔ Anthropic Messages ↔ OpenAI Response API — clients use native formats; Switchyard converts at the proxy layer without client changes
- **Named routing strategies**: LLM classifier routing (model chooses backend), stage routing (pipeline stages with different backends), escalation routing (fallback chain), random distribution — typed and composable, not just round-robin load balancing
- **NVIDIA NIM and vLLM as first-class self-hosted backends**: alongside Ollama — signals the target use case is enterprise inference over local GPU clusters, not just multi-cloud
- **Prometheus metrics built-in**: requests, errors, latency, token usage — not an afterthought; Prometheus is a standard observability choice for Kubernetes-native deployments
- **Dual deployment model**: standalone proxy server OR embeddable Rust library — embeddable mode means it can be wired into Rust-native agent runtimes without a subprocess hop
- **Pre-alpha self-disclosure**: the README explicitly says "not recommended for production use" — honest about current readiness state
- **2,034★ in pre-alpha**: suggests developer interest in the routing layer before production claims are warranted

## Why clawfit should care

clawfit recommends (agent, llm, hardware) triples but does not model the routing layer between the agent and the LLM. Switchyard occupies the gap: it enables a single agent configuration to transparently access multiple LLM backends with protocol translation. This is relevant to clawfit's `hardware` and `network` dimensions because an agent that routes through Switchyard can use `cloud` or `self-hosted` LLMs interchangeably without code changes.

More specifically: if Switchyard matures, a clawfit `hardware: cloud` recommendation and a `hardware: self-hosted` recommendation could share the same agent and LLM entry — differentiated only by which Switchyard routing strategy is active. The current schema treats hardware as a property of the recommendation, but Switchyard is infrastructure that makes that property runtime-configurable.

NVIDIA-NeMo provenance also makes this a candidate to watch for NIM integration patterns: if Switchyard becomes the standard routing layer for NVIDIA NIM deployments, it will show up in production architectures that clawfit's enterprise profiles need to model.

## Preliminary interpretation

- **Level 2 secondary — Harness/wrapper layer** (sits between agent and LLM backend; handles routing and protocol translation)
- **Level 7 primary — Infrastructure / Gateway layer** (operates as infrastructure between application layer and inference backends)

Alternative reading: if the LLM classifier routing strategy gains traction (a model decides which backend to route to), Switchyard acquires properties of an L2 meta-harness decision layer.

## Claims to verify

- "Typed, composable routing algorithms" — whether the typing is enforced at compile-time (Rust type system) or runtime JSON validation only
- LLM classifier routing: what model performs the classification, at what latency cost, and whether the classifier adds meaningful selection vs. static routing rules
- Anthropic Messages API translation fidelity: whether tool use, streaming, and multi-turn format round-trip cleanly between OpenAI and Anthropic formats (edge cases in schema differences)
- NIM integration: whether the "NVIDIA NIM support" is tested against production NIM endpoints or is spec-based
- Release cadence: pre-alpha self-disclosure with 2k stars; watch whether NVIDIA treats this as a core NeMo product or a community contribution

## Status

- 2,034★ — above 100-star research watch threshold; below 5k registry threshold
- No registry entry: below threshold; no public cost/latency data for self-hosted Switchyard overhead
- **Schema watch:** `routing_layer: [none | static | llm-classifier | switchyard | ...]`; `protocol_translation: [openai | anthropic | both]`
- Two-signal rule: Switchyard is the second signal (after omniroute, tracked 2026-07-01) for "Rust-native LLM router with typed routing strategies" as an emerging sub-category under L7 infrastructure
- Watch trigger: production release or NIM integration documentation
