# Research Watch: Upstage Solar Mini 4 — Agent-Optimized MoE LLM at $0.10/M Tokens

- Repo/Link: https://www.upstage.ai/blog/en/solar-mini-4
- Source: GeekNews front page (2026-10-04, 4 pts) + multiple AI benchmarking outlets

## Why this is worth watching

Solar Mini 4 is Upstage's October 1 commercial model: 35B total parameters, 3B active per token (MoE architecture), 512K token context, priced at $0.10/M input tokens. The combination of MoE efficiency, 512K context, and explicit agent-workflow optimization is a distinct product position in a market dominated by models optimized for chatbot quality. Upstage has shipped consistently in the sub-10B-active range (prior Solar models), and Mini 4 is their first entry targeting the enterprise agent-infrastructure segment directly with benchmarks from agentic SaaS automation tasks (AutomationBench-AA, τ³-Banking) rather than standard knowledge or reasoning evaluations.

## What stands out immediately

- **3B active parameters per token with 35B total**: MoE architecture means inference cost scales with active parameter count, not total parameter count — effectively a 3B inference price point with broader knowledge coverage than a dense 3B model
- **512K context window with 128K max output**: unusually large output ceiling relative to competitors at this price; enables long-form agent outputs (full file rewrites, multi-document summaries) without truncation
- **AutomationBench-AA: 22.3%** — a real-SaaS-workflow benchmark measuring agent execution success on production tools (not a synthetic reasoning benchmark); this is the signal that distinguishes agent-oriented tuning from general capability
- **τ³-Banking: 47.2** — domain-specific evaluation; Upstage has historically targeted Korean enterprise and financial sectors; this is not a general-purpose deployment claim
- **Single H100 80GB GPU (quantized)**: on-premise deployment without multi-node infrastructure; the addressable market for self-hosted corporate inference just became accessible to organizations with one H100
- **70 tokens/second throughput at 32 concurrent requests on two H100s**: production-load throughput numbers are published, not typical for a model launch announcement
- **$0.10/M input tokens**: approximately 10x cheaper per input token than GPT-4o-class models; not the cheapest available, but positioned as "quality-per-dollar for repetitive agent workloads"

## Why clawfit should care

Solar Mini 4 is a candidate for the `clawfit/registry/llms.json` registry. It has deterministic public pricing ($0.10/M input, need to verify output token pricing), a clear task profile (agent workflows, long-context document processing), and a measurable latency floor (70 tok/s at standard load). The 512K context is currently the largest available in this price bracket — relevant for clawfit's `statefulness: session` and `statefulness: persistent` filters where context window is a hard constraint. The MoE architecture also means the `budget` filter calculation needs to use active parameter count as the cost basis, not total parameter count, which is a scoring assumption worth auditing.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base LLM** (primary): commercial API model for agent task execution
- No secondary level: Solar Mini 4 is a model, not a harness or capability layer

This is the first Upstage model with explicit agent-optimization benchmarks published at launch. Prior Solar models (Solar 1 through Solar Mini 3) were tracked as general-purpose Korean-language strong models; Mini 4 represents a deliberate repositioning toward the agent infrastructure market segment. Whether the repositioning reflects real capability differentiation or is marketing-layer only is the key claim to verify.

## Claims to verify

- Output token pricing: $0.10/M covers input; output pricing is not consistently stated across sources and needs direct Upstage documentation verification before registry addition
- AutomationBench-AA methodology: who runs the benchmark, what SaaS tools are included, and whether the 22.3% score is competitive (the benchmark's zero-shot baseline and best-in-class scores are not published in Upstage's announcement)
- Whether "single H100 quantized" refers to weight quantization to int4/int8 and what quality degradation that introduces relative to the unquantized API
- Native Korean fluency claims: prior Solar models had demonstrated Korean benchmark leads; Mini 4 carries the same claim but no multilingual benchmark comparisons are published yet
- τ³-Banking: this benchmark appears to be a proprietary Upstage-commissioned evaluation; independent replication is needed before treating this score as external validation

## Status

- Registry eligibility: pending output token pricing confirmation and AutomationBench-AA competitive context
- 512K context, $0.10/M input, MoE 35B/3B active, announced October 1, 2026
- No GitHub repository (commercial API model)
- Monitoring for independent benchmark replications and output token pricing publication
- Relationship to LLM registry: if output pricing is confirmed, this would be the first MoE model in the registry — may require a schema field for `active_parameters` distinct from `total_parameters`
