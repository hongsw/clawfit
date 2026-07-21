# Research Watch: Colibrì — Consumer-Hardware MoE Inference Runtime

- Repo: https://github.com/JustVugg/colibri (⭐17,430)
- Source: GitHub Search API — new repos (July 2026), created 2026-07-01, v1.0.0 released 2026-07-19

## Why this is worth watching

Colibrì is a pure-C, zero-dependency inference engine designed specifically for mixture-of-experts (MoE) models on consumer hardware. Its v1.0.0 landed July 19 at 17k stars after 19 days — an uptake rate comparable to the fastest-rising inference tools in the clawfit scan history. The core bet: MoE architectures activate only a sparse subset of parameters per token (~40B of 744B in GLM-5.2), so a runtime that streams only the needed expert weights from disk can run a 744B model on a machine with 25GB of RAM rather than 744GB. This is architecturally distinct from llama.cpp-style quantization of dense models: Colibrì does not reduce model precision to fit in memory; it reduces memory residency by exploiting the activation sparsity that is fundamental to the MoE design.

## What stands out immediately

- **Three-tier memory hierarchy**: dense components (~17B params, 9.9GB int4) stay in RAM; 19,456 routed experts (~370GB on disk) stream on demand; optional VRAM tier for acceleration. The system "treats VRAM, RAM, and storage as one managed memory hierarchy."
- **Predictive expert prefetch**: 71.6% predictability one layer ahead enables asynchronous streaming that partially hides the disk I/O latency — the key performance lever differentiating this from naive on-demand loading
- **Learning cache**: automatically pins frequently-used experts in RAM based on actual workload; adapts without user configuration
- **Precision policy**: default policy never silently changes model precision or router semantics — an explicit anti-footgun commitment against the common practice of silent quantization fallback
- **Token-exact validation against transformers oracle**: output must match the transformers reference implementation token-for-token; numeric drift is treated as a bug
- **Performance range**: 0.05–0.1 tok/s on 25GB baseline; 1.07 tok/s on single RTX 5070 Ti; 1.8 tok/s on 128GB CPU desktop; 5.8–6.8 tok/s on 6× RTX 5090 (full residency). Baseline throughput satisfies only `latency: high` batch workloads — not interactive use.
- **Apache 2.0, pure C** — no CUDA or PyTorch runtime required at minimum configuration; CUDA optional for VRAM acceleration

## Why clawfit should care

Colibrì opens a previously unavailable slot in the clawfit recommendation space: `hardware: local-consumer` × `network: offline` × `model_size: frontier-scale` × `budget: $0.00`. Currently, clawfit's `local` hardware entries are bounded by what fits in dense quantized form (typically 7B–34B at int4). A 744B MoE model at frontier-class reasoning quality running on hardware many developers already own is a qualitatively different proposition.

The latency constraint is real: 0.05–0.1 tok/s on the minimum configuration rules out interactive agent use. However, for `task: qa` batch workflows or `task: research` asynchronous pipelines, throughput under 1 tok/s may be acceptable. The `latency: high` filter in `filters.py` would correctly suppress this from interactive recommendations while surfacing it for batch profiles.

Broader signal: MoE architecture is now the dominant design for frontier-scale models (GPT-4o, Gemini 1.5, Kimi K3, DeepSeek-V3). A consumer-hardware runtime purpose-built for MoE sparsity is not a curiosity — it is infrastructure for the current model generation.

## Preliminary interpretation

Current best reading:
- **Level 1 — Local Inference Runtime** (primary: the engine runs the model on-device via disk-streaming expert weights)
- Closest comparables: llama.cpp (dense model quantization, different problem), Ollama (dense model abstraction layer, not MoE-native), airllm (tracked 2026-07-19, layer-offloading for dense models). Colibrì is the first MoE-native consumer runtime in the clawfit scan corpus.

Not L2 or higher: Colibrì exposes an inference API and CLI but does not orchestrate agent behavior, manage tasks, or expose MCP tools.

## Claims to verify

- **17,430 stars in 19 days**: GitHub API-verified count; growth rate is consistent with the colibri meme/brand name attracting broad attention beyond the AI-infra audience. Need to verify whether adoption signals reflect genuine use or curiosity-driven starring.
- **744B on 25GB RAM at 0.05–0.1 tok/s**: physically plausible given MoE sparsity math (~40B active params × int4 ≈ ~20GB for active state + overhead). The claim rests on disk I/O latency being acceptable at this throughput; needs independent benchmark reproduction.
- **GLM-5.2 only**: README documentation covers only GLM-5.2 (int4 container with int8 MTP heads). Applicability to DeepSeek-V3, Mixtral, or other MoE architectures is not confirmed — generality to other MoE models is an open question.
- **"Token-exact validation against transformers oracle"**: a strong claim. Needs external reproduction — numeric equivalence across quantization boundaries is non-trivial to guarantee.

## Status

- No registry entry: single signal; hardware.json has no MoE-native runtime category; deterministic latency data for `local-consumer` hardware tier is not yet modeled.
- Schema gap: `moe_native: true/false`; `expert_streaming: true/false`; `active_params_b: float` (parameters activated per token, vs. total parameters); `min_ram_gb: int`.
- High-priority watch: if a second independent MoE-native consumer runtime appears, this pattern warrants a new L1 sub-type ("MoE streaming inference") in reference-levels.md.
- Cross-watch: airllm (2026-07-19, layer-offloading for 70B dense on 4GB VRAM) addresses an adjacent constraint differently. Together they define the emerging "extreme-hardware-constrained local inference" sub-space at L1.
