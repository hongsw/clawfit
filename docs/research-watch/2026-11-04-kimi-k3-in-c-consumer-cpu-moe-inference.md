# Research Watch: kimi-k3-in-c — 2.78T MoE Inference on a Single Consumer CPU in C99

- Repo: https://github.com/FareedKhan-dev/kimi-k3-in-c (⭐10,130)
- Source: GitHub Trending all-languages daily (351 stars today, 2026-11-04)

## Why this is worth watching

kimi-k3-in-c is a dependency-free C99 implementation that runs the 2.78-trillion-parameter Kimi K3 model for inference on a single consumer CPU with approximately 8.24 GB of RAM. No GPU, no BLAS, no external libraries. It uses MXFP4 quantization, AVX2/SIMD vectorization, and linear attention to make a mixture-of-experts model run on commodity hardware. At 10,130 stars it has cleared the top of the GitHub trending chart, which is unusual for a low-level inference engine. The pattern parallels what llama.cpp and ggml did for dense models — a single-file C implementation that radically lowers the hardware bar — now applied to a MoE architecture at a scale that was previously cloud-only.

## What stands out immediately

- **2.78T parameters on 8.24 GB RAM**: this is a dramatic compression claim — the entire Kimi K3 MoE parameter space fits in DRAM on a consumer laptop through MXFP4 quantization; independently verifying this is the first priority
- **C99 with zero external dependencies**: the portability ceiling is minimal; builds on any system with a C99 compiler, no Python, no CUDA driver, no package manager — this is a meaningful distribution advantage
- **MoE-specific implementation**: mixture-of-experts routing at this scale requires sparse activation; the implementation handles MoE dispatch in pure C99 without framework support, which is a non-trivial engineering task
- **MXFP4 quantization**: MXFP4 (microscaling FP4) is a newer quantization format that NVIDIA and Microsoft have been promoting at the hardware level; a pure-CPU implementation of it in C99 is unusual
- **AVX2/SIMD vectorization**: targets CPUs with AVX2 support (Intel Haswell+, AMD Ryzen), not arbitrary CPUs; this bounds the portability claim somewhat
- **Linear attention**: the README topic includes linear attention, suggesting the implementation avoids the full O(n²) attention cost on long contexts — relevant for single-CPU viability
- **10,130 stars in what appears to be a short window**: the velocity of adoption suggests the developer community is eager for a CPU-first MoE inference path and not just for Kimi specifically

## Why clawfit should care

kimi-k3-in-c is the first signal for a **C99 from-scratch inference engine targeting a MoE model at frontier scale**. Prior CPU-first inference signals tracked by clawfit are dense-model focused (karpathy/nanochat, ds4-antirez local DeepSeek Metal, janus-go-gguf-vulkan). If a C99/C-first MoE inference approach proves accurate and production-viable, it changes the hardware recommendations clawfit makes: a consumer laptop with no GPU but sufficient RAM and AVX2 support becomes a credible local inference host for a model that previously required a data center. This directly affects the `hardware: local` and `network: offline` profiles. The adoption of MXFP4 is also a signal about where the quantization format ecosystem is heading — the hardware entry for `local-consumer-cpu` might need an `mxfp4_support` flag in the future.

## Preliminary interpretation

Current best reading:
- **Level 7 — Infrastructure / inference layer (primary)**: a bare-metal inference engine for a specific model family, targeting consumer CPU hardware with no cloud dependency

## Claims to verify

- Actual RAM usage on a real consumer CPU (8.24 GB claim — is this peak or average? Does it fit in 16 GB or require 32 GB in practice?)
- Output quality vs. cloud Kimi K3: is MXFP4 at this compression level producing degraded outputs?
- Actual AVX2 speed (tokens per second on a mid-range laptop CPU — not stated in the About section)
- Whether the implementation covers only text, or also the multimodal capabilities of Kimi K3
- Whether FareedKhan-dev is the original implementor or a port/fork of an earlier internal implementation

## Status

- 10,130 ⭐, Apache-2.0 (above 5k registry threshold)
- Registry action: **not yet** — accuracy and tokens-per-second data not confirmed; model variant is Kimi K3 specifically (not a general-purpose inference engine); schema field for MXFP4 support does not exist in hardware.json
- Watch for: a second C99 or Rust from-scratch MoE inference engine (not a llama.cpp fork) for a different model family; that would confirm the pattern that community-written MoE inference engines are becoming a distinct sub-type of L7 infrastructure
