# Research Watch: ktransformers — CPU-GPU Heterogeneous LLM Inference Framework

- Repo: https://github.com/kvcache-ai/ktransformers (⭐18,270)
- Source: GitHub Trending all languages (rank 2, +328 today, 2026-07-19); also GitHub Trending Python (rank 2); peer-reviewed paper at ACM SIGOPS 2026

## Why this is worth watching

ktransformers is a framework from MADSys Lab (Tsinghua University) and Approaching.AI that enables efficient inference of large MoE models (DeepSeek-V3/R1, MiniMax-M3) on consumer hardware by routing computation heterogeneously: hot experts go to GPU, cold experts stay on CPU. It has 18k stars, was presented at ACM SIGOPS (operating systems peer review, not a benchmark preprint), and appeared on the "Agentic AI on Edge" track at GOSIM Paris 2026. It is trending today alongside the Qwen3.8 and Kimi K3 announcements — a pattern suggesting the market is actively bidding on local large-model inference infrastructure.

## What stands out immediately

- **Expert routing architecture**: AMX/AVX512-optimized CPU kernels handle "cold" experts; CUDA handles "hot" experts; asynchronous scheduling minimizes GPU stall between the two — 4.62–19.74× prefilling speedup and 1.25–4.09× decoding speedup vs. baseline (self-reported; ACM paper is the primary citation)
- **MoE-first design**: explicitly targets DeepSeek-V3/R1, MiniMax-M2.5/M3, and other sparse MoE architectures — not the standard dense models that airllm (layer-offloading) handles
- **Inference + SFT in one project**: the `kt-kernel` path handles inference; a separate `LLaMA-Factory` integration path handles fine-tuning, claiming 6–12× training speedup on MoE SFT workloads (self-reported)
- **Hardware breadth**: Intel (AMX/AVX2/AVX512), NVIDIA (RTX 4090, L20), AMD (ROCm), Intel Arc, Ascend NPUs — covers consumer, prosumer, and enterprise GPU tiers
- **SGLang integration target**: designed for drop-in SGLang compatibility, which is the primary serving framework for self-hosted high-throughput inference deployments
- **Academic backing**: ACM SIGOPS 31st Symposium (2026) publication — unusual for an active open-source inference project; suggests the CPU-GPU routing algorithm has survived peer review
- **Active release cadence**: MiniMax-M3 Day0 support June 21, 2026; DeepSeek-V4-Flash support May 2, 2026; GOSIM Paris May 6, 2026 presentation

## Why clawfit should care

ktransformers targets the specific gap between "small model on a 4GB GPU" (airllm's domain) and "cluster-scale inference" (vLLM's domain). Its primary case is: a single desktop workstation with a mid-tier GPU and substantial CPU RAM running a 230B-class MoE model at interactive throughput. This maps to a `hardware: local` + `latency: medium` + `budget: $0.00` + `network: offline` profile for 100B+ models — a profile that currently returns no valid recommendations in clawfit because no `llms.json` entry can satisfy that combination.

Concretely:
- A user with an RTX 4090 (24GB VRAM) + 128GB RAM running DeepSeek-V3 via ktransformers could achieve ~4–8 tok/sec (medium latency), $0/query, fully offline — a real recommendation candidate if the `hardware.json` schema gains CPU RAM as a dimension
- The intersection with airllm (tracked 2026-07-19) is significant: both address VRAM-constrained local inference, but ktransformers uses heterogeneous routing for MoE models at interactive throughput, while airllm uses layer-offloading for dense models at batch throughput. These are complementary, not competing.

Schema gap: `hardware.json` currently lacks `cpu_ram_gb` and `moe_routing_support` fields. Adding them would let clawfit distinguish ktransformers-compatible configurations from standard GPU deployments.

## Preliminary interpretation

Current best reading:
- **Level 7 — Inference runtime substrate** (CPU-GPU heterogeneous MoE inference layer below the agent runtime)
- Secondary: enabler for L1 base model deployments at scale ranges that standard GPU inference cannot cover
- Comparable role to airllm (L7, layer-offloading) but targeting MoE throughput rather than VRAM-minimum access

## Claims to verify

- The 4.62–19.74× prefilling speedup and 1.25–4.09× decoding speedup: source is the ACM SIGOPS paper and the project README. ACM peer review validates the algorithmic approach but not real-world throughput on user hardware — independent user benchmarks on consumer CPU-GPU combinations are needed.
- "6–12× training speedup" for MoE SFT: self-reported, no paper citation for the SFT path. The inference path has peer-reviewed validation; the training path does not.
- SGLang drop-in compatibility: stated in documentation; requires independent integration testing to confirm no behavioral divergence.
- Ascend NPU and Intel Arc support: listed but no benchmark data for these targets; may be partial or experimental.

## Status

- No registry entry: `hardware.json` schema does not have fields for heterogeneous CPU-GPU configurations; `llms.json` entries do not carry inference-framework constraints.
- Schema watch: `cpu_ram_gb: int`; `moe_routing_support: true/false`; `inference_framework: [standard | ktransformers | airllm | vllm | sglang]`; `active_params_b: float` (for MoE entries).
- Two-signal condition: ktransformers is the first explicitly MoE-optimized CPU-GPU routing framework tracked. A second independent framework using the same heterogeneous routing pattern would trigger a canonical L7 sub-type entry ("heterogeneous MoE inference").
- Cross-watch: airllm (2026-07-19) addresses the same hardware constraint space via a different mechanism (sequential layer offloading vs. expert routing). Together they confirm growing demand for consumer-grade large-model inference — potentially the two signals needed for a "consumer local LLM inference" L7 canonical sub-type. Evaluate after one more independent tool in this space.
