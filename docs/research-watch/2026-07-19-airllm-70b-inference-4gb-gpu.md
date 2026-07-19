# Research Watch: airllm — 70B LLM Inference on a Single 4GB GPU

- Repo/Link: https://github.com/lyogavin/airllm
- Source: GitHub Trending (⭐23,323, +161 today, 2026-07-19)

## Why this is worth watching
airllm enables 70B-class model inference on a single 4GB consumer GPU by loading and unloading model layers sequentially (one layer in VRAM at a time, remainder on CPU RAM or disk) with optional 4-bit quantization. At 23k stars, it is one of the highest-starred edge inference libraries not yet tracked in clawfit's ecosystem map. Its primary relevance today: it has resurfaced on GitHub Trending, suggesting renewed developer interest in VRAM-efficient local inference after Kimi K3's release (a 2.8T-parameter MoE model that raises the bar for what "running locally" means).

## What stands out immediately
- Supports Llama, Mistral, Falcon, and Qwen 70B+ variants on hardware with as little as 4GB VRAM
- Technique: sequential layer offloading (not quantization-only; each transformer block is loaded, run, then unloaded)
- Python library; 3-line API to wrap any HuggingFace model
- Trade-off: throughput is very low (~1-3 tok/sec for 70B); acceptable for batch/offline use, not interactive
- 23k stars represents sustained adoption (project is ~2 years old with active maintenance)

## Why clawfit should care
clawfit's `hardware: local` category currently assumes sufficient VRAM for the selected model size. airllm breaks this assumption — it turns any machine with 4GB+ VRAM into a viable 70B host, at the cost of throughput. This directly affects the `latency` filter: for `latency: low` profiles, airllm is disqualifying (1-3 tok/sec); for `latency: high` (batch/async workflows), it becomes a cost-effective local 70B option. The library also supports the `budget: $0.00` + `network: offline` combination for large-model tasks — a slot clawfit currently cannot recommend a 70B-class option for.

## Preliminary interpretation
Current best reading:
- **Level 7 — Inference optimization infrastructure** (layer-offloading VRAM adapter)
- Not a standalone agent or LLM in the clawfit schema — a wrapper that changes what `hardware: local` can run

## Status
- First signal in this scan series (despite 23k stars — older project, not previously surfaced in daily scans).
- No registry entry: inference wrapper, not an agent/LLM/hardware schema match.
- Schema watch: `vram_requirement_gb: int`; `layer_offloading: true/false`; `throughput_tokps_4gb: float`; `max_model_size_b_at_4gb: int`.
- Scoring implication: hardware.json entries could gain a `vram_gb` field; airllm-wrapped configurations would score differently on latency vs. cost axes.
- Next evaluation: does airllm resurgence correlate with Kimi K3 interest (same-cycle GitHub Trending)? If so, signals growing demand for local-large-model inference, warranting a hardware.json schema discussion.
