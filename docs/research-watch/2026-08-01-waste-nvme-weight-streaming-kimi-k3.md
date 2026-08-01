# Research Watch: WASTE — Weight-Aware Streaming Tensor Engine

- Repo: https://github.com/sqliteai/waste (⭐598)
- Source: Hacker News (305 pts, 2026-08-01)

## Why this is worth watching

WASTE is a four-day-old C inference engine that runs the full 2.78-trillion-parameter Kimi K3 MoE model on a consumer laptop by streaming activated expert weights directly from NVMe, using available RAM as a bounded LRU cache. The 305 HN points on a repo with 598 stars indicates the practitioner community recognized this as technically significant well before the star count caught up. It is the second published NVMe-streaming inference engine in this scan series after turbo-fieldfare (Swift+Metal, Gemma 4 26B-A4B, 2026-07-29), and the first to target a 2.78T-parameter model — three orders of magnitude larger than turbo-fieldfare's 26B target.

## What stands out immediately

- No third-party runtime dependencies — pure C, embeddable; no CUDA, no PyTorch, no llama.cpp dependency chain
- Memory model: model trunk stays in RAM; expert weights are streamed from NVMe on activation; remaining RAM becomes a cache of recently-used experts (LRU eviction)
- CLI output visible in README shows per-inference statistics: 9,038 expert cache hits / 14,514 misses = 38% hit rate at run time; 46.24 GB used of 64 GB budget
- Achieves 0.62 tok/s on the demo hardware — below interactive chat speed but usable for batch agent tasks (analysis, review, research summaries)
- Apache 2.0 license — permissive for commercial embedding
- Created 2026-07-28 (4 days ago), Apache-2.0, sqliteai org (same provenance as SQLite-derived projects)
- First inference engine to publish NVMe expert cache hit/miss ratio as a primary metric — makes storage I/O bandwidth the operational variable, not VRAM

## Why clawfit should care

Two direct taxonomy implications:

1. **Hardware tier expansion**: clawfit's `hardware.json` has five tiers (cloud, workstation-gpu, consumer-gpu, apple-silicon, edge). WASTE introduces a new operational dimension: NVMe I/O bandwidth rather than VRAM capacity is the bottleneck. A 64 GB RAM + fast NVMe machine (consumer workstation, high-end MacBook) can now serve 2.78T-param MoE inference that previously required multi-GPU server racks. This is structurally parallel to turbo-fieldfare (2026-07-29, SSD-streamed inference for 26B MoE on Apple Silicon) but at ~100× scale. Two independent signals now exist for NVMe-streaming as a viable inference substrate (`inference_strategy: ssd-streamed` flagged 2026-07-29 for turbo-fieldfare).

2. **Kimi K3 self-hosting path**: Kimi K3 is already tracked as the leading frontier coding agent model (FrontierSWE 81.2%, tracked 2026-07-18). The IMEC self-hosting study (2026-07-30) established a 20% hardware cost premium yields 20% task resolution improvement over cloud inference. WASTE provides the first concrete mechanism for self-hosting K3 on single-machine consumer hardware, at 0.62 tok/s — slow for interactive coding but viable for scheduled batch agent tasks (nightly review runs, migration validation, documentation generation).

## Preliminary interpretation

- **Level 7 — Infrastructure** (inference engine; enables L1 base model deployment on hardware not previously capable)
- Secondary: **Level 1** (the inference backend that makes K3 accessible as a local L1 runtime for agent harnesses)

## Claims to verify

- 0.62 tok/s on what specific hardware configuration (CPU, RAM size, NVMe type/speed)? The README demo mentions "64 GB" available RAM and an expert cache; NVMe model not specified
- Expert cache hit rate of 38% — is this typical across different prompt types, or specific to the Italian-capital toy query? Agent workloads (code navigation, sequential tool calls) may have different expert reuse patterns than conversational prompts
- Does WASTE support tool-use / function-calling output format, or raw completion only? A 2.78T MoE without function-call support cannot serve as an agent backend despite the throughput potential
- Kimi K3 weight availability: 2.78T-param weights require substantial storage (~1–5 TB depending on quantization); verify public download path and format compatibility

## Status

- First signal; 598 stars but 305 HN points provides independent validation
- No registry entry: hardware/throughput data too configuration-specific (NVMe speed, RAM size, CPU generation) to produce the deterministic latency value required by `hardware.json`
- Two-signal confirmation for `inference_strategy: ssd-streamed`: turbo-fieldfare (2026-07-29, 26B Apple Silicon) + WASTE (2026-08-01, 2.78T x86/ARM); different scale and implementation but same strategic pattern — NVMe replaces VRAM as the primary capacity constraint. **Two-signal rule met for schema formalization of `inference_strategy: ssd-streamed`.** Recommend adding `inference_strategy` to the `hardware.json` or `evidence-schema.md` in the next review cycle.
- Cross-watch: turbo-fieldfare (2026-07-29, L7/L1, SSD-streaming for 26B Gemma on Apple Silicon); IMEC Kimi K3 self-hosting benchmark (2026-07-30, L1 cost data)
