# Research Watch: Microsoft Agent Framework v1.0

- Repo: https://github.com/microsoft/agent-framework
- Also see: https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/ (v1.0 release post, April 3, 2026); https://github.com/orgs/microsoft-foundry/discussions/177 (public preview announcement, October 2025); https://github.com/microsoft/semantic-kernel/discussions/13215 (SK migration discussion)

## Why this is worth watching

Microsoft has shipped a production-stable v1.0 unified SDK that formally retires AutoGen and Semantic Kernel as independent development targets, collapsing two separately tracked 50k★ and 26k★ projects into one repository. The consolidation is architecturally significant: it brings graph-based multi-agent workflow orchestration, declarative YAML agent definitions, and MCP/A2A protocol support under a single stable API surface with an LTS commitment — a combination no single open-source multi-agent framework has previously shipped at this maturity level. At 10k★ seven weeks after v1.0 general availability, velocity is moderate but the institutional weight behind it (Microsoft Foundry, Azure Durable Functions hosting) is disproportionate to the star count.

## What stands out immediately

### Architecture (validated from repo and devblog)
- **Graph-based workflows**: Deterministic, repeatable processes connecting agents and pure functions; supports checkpointing and "time-travel" (state hydration), human-in-the-loop approvals, and streaming — this is materially more capable than AutoGen's group-chat model
- **Dual-language SDK**: Python (50%) and C# (46%) with stated API symmetry; TypeScript (3%) in labs; rare among multi-agent frameworks to maintain parity across both ecosystems
- **Declarative YAML agent definitions**: Version-controlled agent specs — parallel to CLAUDE.md / AGENTS.md SSOT patterns tracked at Level 3, though here scoped to configuration rather than behavioral spec

### Agent capabilities (claims to inspect)
- **Multi-agent patterns**: Sequential, concurrent, handoff, group chat, and Magentic-One — the last being Microsoft's own multi-agent benchmark topology, carried forward from AutoGen research
- **Middleware hooks**: Content filtering, logging, compliance policy injection at the agent layer — a production-hardening feature absent from most open-source harnesses
- **Pluggable memory backends**: Foundry, Mem0, Redis, Neo4j, custom — reaches into Level 5 territory as an optional dependency
- **LLM provider coverage** (vendor claim): Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic Claude, Amazon Bedrock, Google Gemini, Ollama — all major API providers plus Ollama for offline-local

### Protocol interoperability (claims to inspect)
- **MCP support**: Model Context Protocol listed as a first-class integration; details of client vs. server role not specified in the repo README
- **A2A support**: Agent-to-Agent protocol listed alongside MCP; positions the framework as interoperability-forward in a market where protocol fragmentation is ongoing

### Migration posture
- AutoGen: maintenance-only (critical bug fixes and security patches, no new features) — effectively deprecated for development purposes
- Semantic Kernel: no hard deprecation timeline announced; compatibility layer exists (`AsChatClient` extension); community concern about diminishing PR review cadence is documented in the SK discussion thread
- Microsoft is providing migration tooling for both, but the "no forced timeline" message for SK creates a prolonged dual-support burden that could fragment the community

### Enterprise deployment path (claims to inspect)
- Azure Durable Functions hosting for long-running workflows
- Microsoft Foundry managed services integration
- OpenTelemetry observability dashboards built in

## Why clawfit should care

The registry currently has no Microsoft-origin entries at Level 2. AutoGen (historically a Level 2 signal) predates the registry's tracking scope, and Semantic Kernel was primarily a Level 4 capability/plugin framework. Microsoft Agent Framework v1.0 is the first Microsoft product that sits cleanly at Level 2 with enough production-readiness signals to warrant evaluation.

Two concrete implications:

**(a) Level 2 map entry candidate.** The graph-based workflow engine, multi-agent patterns, and stable API are all Level 2 characteristics by the reference taxonomy. The Magentic-One pattern in particular is a research-validated multi-agent topology (not just a configuration option) that distinguishes this from simpler harnesses. If the map is to include enterprise orchestration harnesses — as it currently does for LangGraph / deepagents — Microsoft Agent Framework deserves evaluation by the same criteria.

**(b) Scoring model implication: `.NET` as a runtime axis.** The dual Python/.NET SDK is unusual. Current agents.json and hardware.json entries implicitly assume Python-first runtimes. If .NET organizations adopt this framework as their canonical harness, clawfit's recommendation output for `team_size: enterprise` + `governance_need: hard` profiles may become incomplete without a `.NET-capable` flag on harness entries. Not a schema change today — flagged for the next scoring audit.

## Preliminary interpretation

Current best reading:
- **Level 2 — Meta wrappers / harnesses / orchestration layers** (primary classification — graph-based multi-agent orchestration with stable API, LTS commitment, enterprise deployment targets)
- Secondary Level 3 signal: declarative YAML agent definitions with version control creates a lightweight SSOT layer, but it is configuration-scoped rather than behavioral-spec-scoped; does not displace CLAUDE.md-style specs
- Secondary Level 5 signal: pluggable memory backends (Mem0, Neo4j, Redis) mean the framework spans into the memory/context layer as an optional component; not the primary character

Whether the reference-levels.md Level 2 section warrants a map entry: **yes, conditionally.** The condition is independent validation of the MCP and A2A integration depth (client-only vs. full server hosting) and confirmation that non-Microsoft LLM providers (Anthropic, Bedrock, Gemini) work outside Azure-hosted infrastructure. If both checks pass, this belongs in the Level 2 enterprise harness cluster alongside deepagents and the Anthropic sprint-contract pattern.

## Status
- Tracking. Do not add to ecosystem map today. Validate MCP/A2A integration scope and non-Azure LLM provider behavior before map inclusion. Re-evaluate at next 30-day scan cycle (2026-06).
- Watch: does the Semantic Kernel community migrate, stall, or fork? Fragmentation here would reduce Microsoft Agent Framework's effective coverage and affect enterprise recommendation confidence.
- Watch: does Magentic-One as a built-in multi-agent topology give this framework a measurable performance advantage on SWE-bench or equivalent agentic benchmarks? No third-party benchmark data found as of this writing.

## Note on data hygiene
v1.0 release post and GitHub repo README are the primary sources. Multi-provider LLM support and MCP/A2A integration claims are vendor-stated and have not been independently reproduced. Benchmark claims (if any emerge) should be treated as claims to inspect until third-party reproduction.
