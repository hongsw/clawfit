# Research Watch: Headroom — LLM Context Compression

- Repo/Link: https://github.com/chopratejas/headroom
- Source: GitHub Trending

## Why this is worth watching
Headroom intercepts context — tool outputs, logs, RAG chunks, files, conversation history — before it reaches the LLM and compresses it using format-aware engines, claiming 60–95% token reduction with answer quality preserved. With 152 releases and active development through June 2026, this is not a proof-of-concept; it is a production-targeting library with a HuggingFace-hosted model trained on agentic traces. It addresses a cost and latency pressure point that will intensify as agent context windows grow longer.

## What stands out immediately
- Four distinct compression engines: SmartCrusher (JSON), CodeCompressor (AST-aware for 6 languages), Kompress-base (custom model on agentic traces), CacheAligner (KV-cache prefix stabilization)
- Reversible Compressed Representation (CCR): originals stored locally; LLM can retrieve on demand via `headroom_retrieve` tool call — this is a verifiable design claim, not just marketing
- Benchmarks on GSM8K, TruthfulQA, SQuAD show ±0.000 to +0.030 accuracy delta — claims to inspect, not independently validated
- Deploys as Python/TypeScript library, proxy server, or MCP server; named integrations include Claude Code, Cursor, Codex, LangChain, Agno, Strands
- Image compression via ML router (40–90% reduction) extends scope beyond text-only context
- Apache 2.0 licensed; runs locally — no data leaves the host unless the LLM call itself does

## Why clawfit should care
clawfit's scoring model weights latency (0.5) and cost (0.25) but has no mechanism to account for middleware that materially alters both axes before a call reaches the LLM. A (agent, llm, hardware) triple scored at a given latency/cost profile could behave differently with headroom in the pipeline — especially for cost-sensitive `budget` filter candidates near the cutoff. The `network: online` / `statefulness: session` combinations that accumulate large context windows are the exact workloads headroom targets. There is currently no scoring dimension for context-compression middleware, and no registry category that would surface it as a complementary recommendation.

## Preliminary interpretation
Current best reading:
- **Level 5 — Memory / MCP / context layer** (context-compression sub-type; sits between the retrieval/memory layer and the LLM surface, operating on what reaches the model rather than what is stored)
- Secondary framing as Level 4 (capability/tool-use) is plausible given the MCP server deployment mode and the `headroom_retrieve` tool call pattern, but the primary function is context shaping, not skill execution

## Status
- Tracking: first signal for context-compression middleware category; scoring model gap flagged — cost and latency weights do not account for pipeline middleware effects; registry does not yet have a middleware/compression category; flag docs/reference-levels.md L5 description for possible sub-type annotation at next review cycle
