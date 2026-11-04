# Research Watch: NVIDIA Auto-Ontology — Semantic Database Context Layer for Agents

- Repo: https://github.com/NVIDIA/auto-ontology (⭐4,441)
- Source: GitHub Trending all-languages daily (2,053 stars gained today, 2026-11-04)

## Why this is worth watching

Auto-Ontology is NVIDIA's open-source layer that sits between an enterprise database and an agent. Rather than dumping raw schemas into the LLM context window, it compiles database metadata into a human-reviewed semantic ontology — a graph of business terms, SQL attributes, and table relationships — and then serves that ontology to agents through MCP, agent skills, and a REST API. Its claim is that agents make fewer data-retrieval errors when grounded in a certified semantic model than when given raw schema context. With 4,441 stars and 2,053 gained in one day, it is tracking faster adoption than typical enterprise data tooling.

## What stands out immediately

- **Human certification loop**: the ontology is not fully auto-generated and forgotten; people review and approve terms and SQL attributes in a web UI before agents use them, which is a meaningful architectural distinction from embedding-only RAG
- **MCP server as the primary agent interface**: the project ships a read-only MCP server, making it compatible with any MCP-aware agent (Claude Code, Cursor, Continue) without code changes
- **Text-to-SQL agent loop with self-repair**: the answering pipeline classifies intent, retrieves relevant ontology nodes by embedding search, writes SQL, checks filter validity, and runs a repair cycle on failure before returning an answer
- **Four configurable LLM roles**: reasoning (ontology build and SQL explanation), non-reasoning (fast steps like intent classification), embedding (indexing and retrieval), and reranking — with NVIDIA NIM defaults and any OpenAI-compatible endpoint as a drop-in
- **Companion evaluation repo**: a separate benchmark compares accuracy against schema-in-prompt baselines on BIRD and similar datasets — accuracy claims are at least partially verifiable, not just claimed
- **10-connector database support**: PostgreSQL, Snowflake, Databricks, DuckDB, and six others; broad enough to be relevant in real enterprise stacks
- **pgvector storage, not a dedicated graph database**: the semantic graph is stored relationally in Postgres 17 with pgvector; operationally simpler but not a pure graph traversal engine

## Why clawfit should care

Auto-Ontology is a signal in the growing pattern of "structured context layers" that sit between raw data stores and agent reasoning. It differs from general-purpose RAG (chunks of text retrieved by embedding) in that the ontology is a typed, human-approved schema layer with explicit relationships. If this pattern generalizes beyond databases (to code graphs, knowledge bases, product catalogs), it would constitute a distinct L4–L5 sub-type: **certified semantic context grounding**. NVIDIA shipping this as an open-source, MCP-first tool is a credibility signal — it is not a startup experiment. The accuracy-benchmarking companion repo is also relevant to clawfit's scoring model: if agents perform measurably better on structured queries when grounded in a certified ontology, that is a scoring dimension not currently represented in `scoring.py`.

## Preliminary interpretation

Current best reading:
- **Level 4 — Capability / skill / MCP layer (primary)**: exposes the ontology as a read-only MCP server that any agent can query as a tool
- **Level 5 — Memory / observability (secondary)**: the ontology functions as a certified semantic memory about the enterprise data model; human review loop is a form of knowledge-base governance

## Claims to verify

- Accuracy benchmark numbers on BIRD and similar datasets (companion eval repo exists but specific figures not yet read)
- Latency of ontology compilation on large schemas (number of tables, columns)
- Whether the MCP server is read-only only, or if future versions allow agents to propose ontology changes
- Production usage claims (NVIDIA internal teams, external design partners)
- KumoRFM integration for predictive questions: what exactly is routed there and under what conditions

## Status

- 4,441 ⭐, Apache-2.0, NVIDIA-maintained
- Registry action: **not yet** — MCP-exposed data layer is not an agent/LLM/hardware entry; no existing schema field for semantic context layers
- Watch for: second major vendor (Databricks, Snowflake, Microsoft) publishing a certified-ontology MCP server; that would confirm **certified semantic context grounding** as a distinct L4 sub-type worth a canonical entry
