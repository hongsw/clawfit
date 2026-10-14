# Research Watch: Janas — SSD-Streaming Inference Engine for Mixture-of-Experts LLMs

- Repo/Link: https://github.com/prabanta-dev/janas (⭐380)
- Stars: 380
- Source: GeekNews front page (2026-10-14)

## Why this is worth watching
Janas is a C-based inference engine that keeps MoE model weights on an NVMe SSD and streams only the expert layers needed per token into a RAM cache. The stated result — running a 48 GB Qwen3-Next-80B-A3B model on a 32 GB laptop at 37 tok/s vs. llama.cpp's 2.8 tok/s — is a 13× throughput improvement on a machine that technically lacks sufficient RAM for the model. If this holds across hardware, it represents a qualitative change in what hardware is "sufficient" for large MoE inference. The caveat: this is one author's benchmark on one laptop; reproducibility is unverified.

## What stands out immediately
- **SSD-as-extended-memory:** Weights live on NVMe SSD; only active experts are loaded into RAM per token using `O_DIRECT`; free RAM is used as an expert cache
- **37 tok/s vs. llama.cpp's 2.8 tok/s** on Qwen3-Next-80B-A3B (48 GB model, 32 GB laptop): 13.2× claimed speedup — extraordinary if reproducible
- **Speculative decoding ("drafts"):** Draft tokens used natively to accelerate generation; 37 tok/s with drafts vs. 24 tok/s without
- **No external dependencies:** Pure C, links only against the C library; supports CPU (AVX2/AVX512) and GPU (Vulkan) with no mandatory GPU
- **MoE-first design:** The core streaming approach specifically exploits MoE sparsity — only activated experts (typically 2–8 of 64+) are loaded per token
- **Full toolchain:** `janas-chat`, `janas-mcp` (MCP server), `janas-server` (OpenAI-compatible HTTP API), `janas-bench`; directly usable by MCP-aware agents
- **Linux + Windows only (x86-64):** macOS and ARM are not mentioned; Apple Silicon is excluded at this time
- **13 model comparisons:** All show faster prompt processing and generation than llama.cpp at Q4_K_M; one exception (3-bit Qwen3-30B prompt read rate)

## Why clawfit should care
- The clawfit hardware registry currently treats laptop/consumer hardware as an inference tier with implicit RAM-ceiling constraints; janas breaks that assumption for MoE models
- `janas-mcp` means this runtime can be connected to MCP-native agents (Claude Code, Cursor, etc.) without a wrapper — it enters the stack at L4 (capabilities/MCP)
- If SSD-streaming inference generalizes to commodity hardware, the `hardware: local` tier in clawfit's registry needs an "NVMe-extended" sub-tier with distinct cost/latency characteristics
- The performance gap against llama.cpp (for MoE, specifically) suggests clawfit should not treat llama.cpp as a universal baseline for local inference scoring

## Preliminary interpretation
Current best reading:
- **Level 7 primary — Infrastructure / Inference Runtime Substrate** (local inference engine)
- Secondary at **Level 4 — Capabilities/MCP**: `janas-mcp` directly exposes the runtime as an MCP server for agent tool calls

The design is narrowly targeted: it only helps with MoE models (where sparse expert activation means most weights are never touched per token) and requires fast NVMe storage. Dense models don't benefit the same way. The constraint is hardware-specific: a slow HDD would make the approach unusable; a fast PCIe Gen4/Gen5 NVMe is the practical prerequisite. For the right hardware profile (laptop or desktop with fast SSD and ≥16 GB RAM), this is a meaningful new capability.

## Claims to verify
- 37 tok/s on Qwen3-Next-80B-A3B was measured on Intel Core Ultra 9 185H with Arc GPU + 32 GB + NVMe; results on AMD/NVIDIA hardware are described as "largely untested"
- llama.cpp comparison (2.8 tok/s) was measured on the same machine; independent reproduction needed
- `O_DIRECT` usage on Windows may behave differently than Linux; Windows performance claims are not separately benchmarked
- Heavy memory use "can push a desktop into swap" per the author's own warning — workload-dependent stability concern
- Format version 2 (`.jns` files) may change without notice; model availability on HuggingFace as `.jns` is limited at 380-star stage

## Status
- Not yet registry-eligible: 380 stars (above tracking threshold of 100), but cost/latency data is benchmark-only; no stable API or production deployment evidence
- First "SSD-streaming MoE inference" signal in the tracking record
- Monitor: cross-hardware benchmark results from community, macOS/ARM support, stability on non-Intel hardware
- Registry consideration: if performance is independently reproduced on ≥2 hardware configurations, consider adding an `inference_backend: ssd-streaming` field to hardware entries
