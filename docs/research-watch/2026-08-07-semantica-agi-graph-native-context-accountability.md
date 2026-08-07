# Research Watch: semantica-agi/semantica — Graph-Native Context and Accountability Infrastructure

- Repo: https://github.com/semantica-agi/semantica (⭐2,255; v0.6.0, July 21, 2026)
- Source: GitHub Trending Python (118 stars today, 2026-08-07)
- Self-description: "The Open Source Palantir for AI Agents"

## Why this is worth watching

Semantica occupies a gap in the agent stack that is growing in importance as regulatory scrutiny of AI decision-making intensifies: a deterministic, queryable infrastructure layer that sits beneath LLMs and vector stores to provide structured context, causal decision provenance, and explainable reasoning. The core thesis is that most agent decisions are black-box and ephemeral — semantica makes every AI choice a queryable first-class object with traceable causality, exportable in W3C PROV-O format (the format regulators accept for compliance audits). No LLM is required for graph construction, reasoning, or provenance — the deterministic layer operates independently of the model.

At v0.6.0 (July 21, 2026) with 2,255 stars, this is early-stage but with an active release cadence (roughly monthly major versions since January 2026) and a specific compliance positioning that distinguishes it from general-purpose graph databases and RAG frameworks. The first-class MCP server (15+ tools, modular since v0.5.0) makes it directly usable from Claude Desktop, Windsurf, Cline, and VS Code without code integration work.

## What stands out immediately

- **Decision provenance as first-class objects:** `record_decision()` creates permanent structured decision records; `trace_decision_chain()` retrieves full causal ancestry; `analyze_decision_impact()` maps downstream influence — decisions are queryable data, not logs
- **W3C PROV-O export:** provenance tracking across 17 modules (added v0.2.6, Feb 2026) exports in the standard regulators accept — designed for compliance audits, not just internal observability
- **Polyglot graph backends:** RDF triple stores (Oxigraph, Blazegraph, Jena, RDF4J) and Labeled Property Graphs (Neo4j, FalkorDB, Apache AGE, AWS Neptune) are swappable — no single vendor lock-in for the persistence layer
- **Deterministic reasoning alongside LLMs:** forward chaining, Rete networks, Datalog, SPARQL — the reasoning layer does not require LLM calls; this is symbolic AI complementing neural AI
- **First-class MCP server (15+ tools):** `extract_entities`, `record_decision`, `query_decisions`, `get_causal_chain`, `run_reasoning` — usable directly from MCP clients; modular plugin bundles since v0.5.0
- **Performance claims at scale:** 6,000x node search improvement (24ms → 0.004ms), 6.98x faster semantic deduplication on a 118k-node production graph — benchmarked at production scale
- **GraphRAG pipeline:** entity-aware chunking, conflict detection before merge, semantic deduplication — the ingestion pipeline positions semantica as an alternative to naive vector-store RAG

## Why clawfit should care

Semantica represents an emerging L5 (memory/observability) pattern that clawfit currently has no entry for: **structured causal memory with compliance-grade provenance**. Existing L5 entries in the corpus emphasize semantic retrieval (vector search, RAG) or behavioral logging (token traces, tool call logs). Semantica provides queryable causal graphs with regulatory export — a different capability profile.

The `record_decision()` primitive is specifically relevant to agent teams where audit trails are required: healthcare, finance, legal, government. These are exactly the domains where agent recommendations need to demonstrate not just what was decided but why, with traceable evidence. Clawfit's current filter set has no `compliance_audit_trail: bool` axis — this is an unmodeled requirement.

The first-class MCP integration also makes semantica a ready tool capability (L4) that any MCP-compatible agent can invoke. An agent using Claude Desktop can call `record_decision()` or `trace_decision_chain()` without any code integration — it works as a plugin to existing agent harnesses. This positions it at both L4 (tool capability) and L5 (observability/memory).

## Preliminary interpretation

- **Level 5 — Memory / Observability** (primary): causal decision provenance, queryable decision records, W3C PROV-O export — these are observability and memory primitives, not execution-layer concerns
- **Level 4 secondary** (MCP tools): 15+ MCP tools exposed to agent clients; directly callable as agent capabilities
- **Adjacent to:** LlamaIndex (RAG, L4), mem0 (semantic agent memory, L5), Zed DeltaDB (code provenance, L3/L5) — different use case but same observability impulse
- **Cross-watch:** Zed DeltaDB (2026-08-06, L3 code provenance — analogous provenance-tracking philosophy for code authorship vs. decisions); toris-agent (2026-08-04, L3 evidence receipt — similar evidence-trail pattern at task orchestration layer)

## Claims to verify

- **"6,000x node search improvement":** verify benchmark methodology — 24ms → 0.004ms is an implausible 6,000x improvement without context; likely a specific index-hit case vs. unindexed scan; check whether this is the median or best-case measurement
- **W3C PROV-O compliance for regulatory use:** verify whether the exported PROV-O passes validation against real regulatory audit tools, or whether "format regulators accept" is aspirational branding
- **MCP tool coverage vs. graph complexity:** verify whether the 15+ MCP tools expose the full semantica capability surface, or whether complex graph operations require Python SDK calls — the MCP surface may be a simplified subset
- **Deterministic reasoning claims:** forward chaining and Rete networks are well-understood; verify whether the Datalog implementation handles recursive rules correctly (this is a known correctness trap in Datalog implementations)

## Status

- v0.6.0 released July 21, 2026; active monthly release cadence since January 2026
- 2,255 stars — above research-watch threshold (100 stars); below registry threshold (5,000 stars)
- Registry eligibility: wait for growth to 5k stars and deterministic cost/latency profiling (graph query latency depends heavily on backend choice)
- Schema watch: `compliance_audit_trail: bool`; `provenance_standard: [none | w3c-prov-o | custom]`; `reasoning_type: [neural | symbolic | hybrid]`
- Cross-reference: Zed DeltaDB (2026-08-06), toris-agent (2026-08-04)
