# Research Watch: Lemmalog — Datalog Engine for LLM Agent Memory

- Repo: https://github.com/JordyZomer/lemmalog (⭐190)
- Source: GeekNews (via pwning.systems: "LLM 메모리를 만들다 우연히 프로그램 분석 엔진이 된 이야기")

## Why this is worth watching

Lemmalog applies program analysis techniques — specifically Datalog's stratified logical rules and provenance tracking — to the problem of LLM agent memory. Most agent memory systems treat recall as retrieval: embed facts, query by similarity. Lemmalog treats it as reasoning: maintain a dependency graph of derived conclusions, automatically retract stale inferences when facts change, and surface derivation chains on demand. The author arrived at this design while building a vulnerability research assistant; the core observation is that agents don't just forget facts — they forget which conclusions depended on which facts, and continue reasoning from invalidated premises.

At 190 stars it is early-stage, but it ships as a working MCP server with Rust source and MIT license, meaning it integrates with Claude Code, Cursor, or any MCP-compatible host without additional scaffolding.

## What stands out immediately

- **Retractable conclusions**: when an input fact is invalidated, all derived conclusions that depended on it are automatically withdrawn — solving a class of LLM "continuity failure" that vector stores cannot address
- **Provenance chain**: `why()` queries return the derivation path for any conclusion, enabling explainability of the agent's current belief state
- **Temporal intervals**: facts can carry validity timestamps; the engine distinguishes historical from current state without the agent needing to manage that explicitly
- **45x context compression**: reported 45x reduction in context tokens vs. full-transcript approaches (LongMemEval F1: 0.463, comparable to SimpleMem at 0.480; LoCoMo F1: 0.533)
- **MCP server packaging**: ships with an MCP interface — drop-in with Claude Code or any MCP host, no framework integration needed
- **Rust implementation**: deterministic execution, no GC pauses, single binary; relevant for low-latency agent tool calls
- **Early community interest**: 9 points on GeekNews; the post is in Korean, suggesting adoption signal beyond English-speaking developer communities

## Why clawfit should care

This is a concrete alternative architecture for `statefulness: persistent` agent profiles. Current clawfit registry entries that claim persistent memory (e.g., hermes-agent, OpenHuman) typically use vector stores or relational DBs. Lemmalog represents a structurally different approach: inference-based rather than retrieval-based. If it matures, it could justify a new `memory_model: [vector | relational | logic | hybrid]` metadata axis in the agent schema.

The MCP integration is directly relevant: Lemmalog can augment any existing agent in the registry that supports MCP, without replacing the base runtime. This is a composable memory layer, not a competing framework — the design pattern is worth tracking for how clawfit thinks about capability stacking at L4/L5.

## Preliminary interpretation

Current best reading:
- **Level 5 — Memory / Observability** (primary): the Datalog engine is itself the memory system; it does not run agents, it tracks what the agent knows and can explain why
- **Level 4 — Capabilities / MCP** (secondary): ships as an MCP server; the integration surface is an MCP tool call, not a library import

## Claims to verify

- Whether the LongMemEval and LoCoMo benchmarks used standardized evaluation splits (the 0.463 and 0.533 F1 figures are not exceptional; the context compression claim is the more distinctive assertion)
- Whether the 45x context compression holds across agent types or is specific to vulnerability-research-style tasks where facts are frequently retracted
- Whether the MCP server is production-stable or a proof-of-concept — the repo is young and the author frames it as a personal project
- Whether Datalog stratification is a real bottleneck in practice (negation-as-failure semantics require stratified programs; complex dependencies could produce unsatisfiable strata)
- Whether the Rust binary has been tested against Claude Code and other MCP hosts, or only against the author's own Claude setup

## Status

- Tracking: first signal 2026-08-30
- Stars: 190 GitHub (2026-08-30); source: GeekNews + pwning.systems
- Registry decision: hold. Lemmalog is a memory server, not an agent or LLM. The registry has no slot for memory modules; a schema extension would need design before an entry makes sense.
- Watch: whether the MCP interface stabilizes; whether adoption grows in vulnerability research or broader agentic tool use; whether provenance chains prove useful in real multi-step agent tasks
