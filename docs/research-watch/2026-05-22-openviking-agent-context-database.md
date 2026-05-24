# Research Watch: OpenViking — Agent Context Database

- Repo: https://github.com/volcengine/OpenViking
- Also see: agentmemory (L5, MCP-native 4-tier), ClawMem (L5, on-device SQLite), mem0/cognee (prior L5 entries)

## Why this is worth watching

OpenViking (Volcengine/ByteDance, 24.4k stars, +130 today) is architecturally unusual in that it unifies three context types — Memory, Resources, and Skills — under a single virtual filesystem rather than treating them as separate subsystems. The hierarchical three-tier loading (L0/L1/L2 abstraction ladder) is a concrete approach to token reduction that differs from vector-only RAG. Vendor benchmark figures (83% token reduction vs. baseline OpenClaw on LoCoMo10) are notable in scale but require independent reproduction before being treated as validated.

## What stands out immediately

- Virtual filesystem paradigm: `viking://` URIs map all context into a navigable directory tree; agents issue `ls`, `find`, `grep` rather than opaque embedding queries — retrieval paths are human-readable and inspectable
- Three unified context domains under one address space: `viking://memory/` (task memories, interaction records), `viking://resources/` (docs, repos, web), `viking://agent/skills/` (operational instructions, learned capabilities) — the skills sub-tree is structurally distinct from the other two and overlaps L4
- L0/L1/L2 stratification: L0 is a single-sentence summary for triage, L1 is a ~2k-token planning overview, L2 is full detail loaded on demand; this reduces token consumption at retrieval time rather than only at compression time
- Retrieval is multi-step: intent analysis → vector-based directory positioning → hierarchical refinement → recursive drill-down — not flat top-k similarity
- No MCP server documented in the README; integration points are OpenClaw, LangChain, LangGraph at the SDK level (same pattern as Mirage, deferred 2026-05-21)
- AGPLv3 main license is a hard constraint for commercial deployments; CLI and examples carry Apache 2.0 separately — split-license shape requires careful evaluation per org profile
- Python 81%, TypeScript 6.6%, Rust 5.8%; 38 releases — not a prototype
- Supported LLM providers are Volcengine-first (Doubao), then OpenAI, Kimi, GLM — Anthropic/Claude not listed as a first-class provider

## Why clawfit should care

The `viking://agent/skills/` sub-tree blurs the L5/L4 boundary in a different direction from prior entries: agentmemory bleeds into L3 via multi-agent coordination tools; OpenViking bleeds into L4 by storing skills (operational instructions, capabilities) inside the memory address space. If skills in OpenViking are executable and not merely descriptive, clawfit's recommendation logic would need to score it across two layers simultaneously — similar to the agentmemory L5/L4 dual classification. The AGPLv3 license makes it a non-starter for `governance_need: hard` profiles without a commercial license agreement. The LoCoMo10 benchmark claims are vendor-authored; the 83% token-reduction figure is large enough that independent reproduction would meaningfully change how this fits against other L5 candidates on cost-sensitive profiles.

## Preliminary interpretation

Current best reading:
- **Level 5 — Memory / MCP / context layer** (primary; three-domain unified context store, hierarchical retrieval, virtual filesystem paradigm; reference docs/reference-levels.md)
- **Level 4 — Capability / skill / plugin / tool-use layer** (secondary; `viking://agent/skills/` sub-tree stores operational instructions and learned capabilities alongside memory — not a clean L5-only tool)
- No MCP server documented — integration is SDK-level only, same deferred pattern as Mirage; this limits reach to LangChain/LangGraph harnesses and rules out direct Claude Code plugin usage until MCP support is confirmed

## Status

- 24.4k stars, AGPLv3 main / Apache 2.0 CLI; below no threshold by star count, but map mutation deferred: (1) no MCP server limits scope vs. existing L5 entries; (2) vendor-authored benchmark claims on LoCoMo10 unverified; (3) AGPLv3 license requires resolution before commercial registry guidance; (4) Anthropic/Claude provider not listed first-class. Revisit if MCP support ships or an independent reproduction of the token-reduction claim appears.
