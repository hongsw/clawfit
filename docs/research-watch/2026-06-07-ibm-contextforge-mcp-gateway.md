# Research Watch: IBM ContextForge (mcp-context-forge)

- Repo: https://github.com/IBM/mcp-context-forge
- Also see: https://github.com/IBM/mcp-context-forge/blob/main/README.md

## Why this is worth watching
ContextForge is the first IBM-backed open-source project to occupy the MCP infrastructure layer: rather than being an MCP server that exposes one set of tools, it is a gateway that federates many MCP servers, REST/gRPC APIs, and A2A agents under a single authenticated endpoint. The combination of gRPC-to-MCP translation, unified tool registry, OpenTelemetry observability, and Kubernetes/Helm packaging signals a push toward enterprise-grade production deployment of MCP — distinct from the research-stage or single-team MCP tooling tracked so far. At 3.8k stars and a v1.0.2 release (2026-05-26), it is past proof-of-concept stage.

## What stands out immediately
- **Gateway + registry pattern, not a simple proxy**: ContextForge maintains centralized registries for tools, prompts, and resources; POST to `/gateways` registers a remote MCP server, and virtual servers are assembled from the tool catalog — this is active federation, not pass-through routing
- **Protocol translation is substantive**: gRPC-to-MCP translation via server reflection, REST-to-MCP adaptation with automatic JSON Schema extraction, and transport coverage across HTTP/JSON-RPC/WebSocket/SSE/stdio/streamable-HTTP — claims to inspect: "automatic JSON Schema extraction" depth is unverified
- **A2A routing claimed for OpenAI and Anthropic agents**: described as "A2A (Agent-to-Agent) integration for external AI agents (OpenAI, Anthropic, custom)" — how deep this integration goes vs. API forwarding is unconfirmed
- **Governance features are concrete, not aspirational**: JWT auth with JTI token revocation, RBAC across federated calls, rate limiting, content-size DoS guards, SSRF protection with domain allowlisting, credential encryption at rest — these are implementable controls with specific technical descriptions
- **OpenTelemetry observability across federated gateways**: distributed tracing with vendor-agnostic OTLP output; backends listed (Phoenix, Jaeger, Zipkin, Tempo, DataDog, New Relic) are real products, not placeholders
- **Multi-cloud deployment with Helm charts**: AWS, Azure, GCP, IBM Cloud, OpenShift; Redis-backed caching for federation; production database via PostgreSQL (SQLite for development)
- **7,000+ tests**: an unusually high test count for a project at this star level; IBM provenance makes CI rigor plausible but has not been independently audited
- **Admin UI via HTMX + Alpine.js**: in-process management dashboard; no external frontend framework dependency
- **Tech stack**: Python/FastAPI primary (81.1%), with Rust (4.2%) component whose purpose is not specified in top-level README — worth investigating
- **Apache 2.0 license**: permissive; IBM-hosted open-source with enterprise contribution patterns

## Why clawfit should care
ContextForge sits at a level below individual MCP tool servers (L4) and above base runtimes (L1): it is the infrastructure through which an enterprise exposes and governs a curated set of MCP tools to its agents. For clawfit's recommendation engine, this introduces a category of tooling the current registry cannot represent — the gateway that mediates between agents and the capability layer. If a team needs unified MCP access control across multiple backend services, ContextForge is the natural recommendation surface, but clawfit's current schema has no field for "gateway/federation layer" and the filter logic assumes agents call tools directly. The governance controls (JWT, RBAC, rate limiting) also mean ContextForge partially overlaps with L3 (team governance layer) — specifically with Claw Patrol (agent security firewall, 2026-06-01), which enforces policy at the HTTP/SQL wire level. The distinction: Claw Patrol sits between agents and production services as a runtime security guard; ContextForge sits between agents and their tool catalog as a federation and discovery layer. These are complementary, not competing, but clawfit does not currently have a way to recommend both together.

## Preliminary interpretation
Current best reading:
- **Level 4 primary — Capability / skill / plugin / tool-use layer**: ContextForge's defining behavior is assembling, federating, and routing agent tool calls across heterogeneous MCP servers and APIs; the unit of composition is the tool catalog entry, not the agent orchestration step
- **Level 3 secondary candidate — Team governance layer**: JWT RBAC, rate limiting, token revocation, SSRF domain allowlisting, and credential encryption together constitute an access-control and policy enforcement surface for team-level tool governance — strength of this classification depends on whether rate-limit and RBAC enforcement is blocking or advisory in practice (unverified)
- **Level 5 weak secondary**: OpenTelemetry distributed tracing across federated gateways provides observability over context flow between agents and tools — this is infrastructure-facing, not agent-memory-facing; weak signal only
- Not L2: ContextForge does not orchestrate agent execution or manage agent lifecycle; agents call through it, but it does not dispatch or sequence agent steps
- Not L1: it has no autonomous planning loop or base runtime role

Notable subcategories:
- First observed "MCP federation gateway" sub-type at L4 — distinct from individual MCP tool servers (HexStrike, Agent-Reach, fff) and from context-compression middleware (Headroom); single signal, sub-type formalization deferred per single-signal rule
- Joins Claw Patrol (L3 agent security firewall) as the second enterprise-governance-oriented signal in two weeks; together they sketch a nascent "enterprise MCP governance stack" pattern, but that pattern requires a third independent signal before naming

## Status
- New signal — first observed 2026-06-07; 3.8k stars (below 5k registry threshold), v1.0.2 released 2026-05-26; IBM-backed open-source; hold pending star-threshold crossing and independent verification of gRPC-to-MCP translation depth and A2A routing claim
- Registry candidate for `task: orchestration` + `governance_need: hard` + `team_size: mid/large` + `network: online` profiles once above 5k stars and gRPC/A2A claims are functionally verified
- Flag for schema-analyst: a "gateway/federation layer" role is unrepresented in the current filter schema; ContextForge is the first concrete evidence for this gap
- Flag for scoring-analyst: if ContextForge is in the stack, the effective capability surface is the federated tool catalog, not the individual agent's direct tool calls — the current (agent, llm, hardware) triple scoring model has no slot for a tool gateway intermediary
- Watch criterion: 5k stars OR a documented production deployment by a named organization OR independent verification of A2A routing depth beyond API-key forwarding
