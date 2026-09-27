# Research Watch: Microsoft Data Formulator — DataAgent-Driven Analysis Platform

- Repo: https://github.com/microsoft/data-formulator (⭐17,418)
- Source: GitHub Trending daily (+111 today)

## Why this is worth watching

Data Formulator is a Microsoft Research project that deploys a persistent "DataAgent" to drive data analysis sessions rather than treating each query as a one-shot LLM call. The DataAgent discovers data sources, clarifies ambiguous requests, proposes loading plans, and executes analyses — acting as an ongoing collaborator rather than a stateless transformer. The v0.8 beta reframe ("load → ask → review → branch") signals a deliberate shift toward agentic workflow thinking in a traditionally BI-adjacent domain.

## What stands out immediately

- "Data Threads" feature: branched exploration without losing earlier analytical context — each branch is a named path, not just an undo stack
- Unified DataAgent: one agent handles source discovery, request clarification, loading plans, and execution — not a pipeline of separate models
- Style-refinement agent as a separate, composable module — specialization without full agent decomposition
- Multi-LLM backend: OpenAI, Azure OpenAI, Anthropic, and Ollama via LiteLLM — backend-agnostic from day one
- 30+ chart types powered by Flint (open-source visualization language) — output format is structured, not just text
- DuckDB for large dataset handling — agents don't call APIs per row; data stays local
- TypeScript/React + Python: frontend and backend separation kept explicit; not a monolithic notebook approach

## Why clawfit should care

Data Formulator is a domain-vertical agent harness for data analysis — analogous to how Claude-Code-Game-Studios is a vertical harness for game development. It demonstrates that "agentic data analysis" is maturing enough to warrant a purpose-built orchestration layer rather than generic LLM calls. For clawfit: (1) the `DataAgent` pattern (one agent as persistent analysis coordinator) is structurally L4 with L6 characteristics — it extends capability into a new domain while maintaining a human-facing interface; (2) the multi-LLM support via LiteLLM matters for scoring — any org evaluating this would care about cost/latency of the backing LLM, not the tool itself.

## Preliminary interpretation

Current best reading:
- **Level 4/6 — Domain Capability Extension + Analysis Interface Surface**: the DataAgent extends coding/analytical capabilities (L4) while maintaining an interactive human exploration interface (L6)
- Structural parallel to domain-vertical L2/L3 harnesses but oriented around data exploration rather than code generation

## Claims to verify

- Whether Data Threads truly preserve full branch state or just metadata references — the distinction matters for large datasets
- Production maturity of the DataAgent discovery module — early demos often show curated data sources
- Whether the Anthropic/Ollama backends are first-class or treated as fallbacks; LiteLLM integration sometimes degrades structured output reliability
- Whether "30+ chart types" via Flint represent a stable API or early feature claims

## Status

- Tracking; 17,418 stars — well above threshold but no direct inference cost data (DataAgent's cost depends on backing LLM choice)
- Registry ineligible: no fixed inference cost/latency — DataAgent delegates to user-configured LLM backend
- First signal for "DataAgent-pattern" in analytical workflow tools; too early for sub-type promotion but worth cross-date tracking
