# Research Watch: DeepGEMM — High-Performance CUDA Kernels for LLM Inference

- Repo: https://github.com/deepseek-ai/DeepGEMM (⭐8.6k)
- Source: GitHub Trending (daily)

## Why this is worth watching
DeepGEMM is a CUDA kernel library from DeepSeek AI targeting the tensor operations central to large language model inference and training: GEMMs in FP8/FP4/BF16, fused MoE operations with overlapped communication, MQA scoring, and expert routing. It achieves up to 1,550 TFLOPS on H800, compiles all kernels at runtime via DeepJIT (no CUDA compilation at install), and targets SM90/SM100 (H100/H200/Blackwell-era) architectures. Recent 2026 additions include DeepGEMM-Ascend support and Sparse Indexer functionality — extending the library beyond NVIDIA-only hardware.

## What stands out immediately
- Runtime JIT compilation via DeepJIT: zero CUDA compilation at install, kernels adapt at load time
- Targets SM90/SM100 (H100, H200, Grace Blackwell) — aligned with the 2026 inference hardware generation
- FP8 and FP4 support: critical for quantized inference efficiency at scale
- Fused MoE operations with overlapped communication — directly accelerates the MoE architectures seen in Beam (501B MoE) and Mistral Large 4 (1T MoE)
- DeepGEMM-Ascend: extends support to Huawei Ascend NPUs — not NVIDIA-only
- 8.6k stars, 1.4k forks — active community adoption
- Positioned as a "clean, accessible" learning resource alongside a performance tool

## Why clawfit should care
DeepGEMM addresses a gap in the tracked L7 infrastructure set: dedicated kernel-level optimization for the hardware that actually runs the L1 models clawfit scores. The library's FP8/MoE focus directly supports the inference efficiency claims of Beam and Mistral Large 4 — two October 2026 signals that both use MoE architectures with large total-parameter counts. For `hardware: self-hosted` scenarios, the DeepJIT runtime compilation model reduces deployment friction (no pre-compilation step). The Ascend support is strategically interesting for `governance_need: data-sovereignty` organizations in markets where NVIDIA GPU supply is constrained (notably South Korea, Japan, EU public sector).

## Preliminary interpretation
Current best reading:
- **L7 — Infrastructure / Substrate layer** (primary: GPU kernel library for LLM inference acceleration)

## Claims to verify
- "Up to 1,550 TFLOPS on H800" — benchmark methodology and comparison baseline not specified; H800 vs. H100 vs. H200 architecture differences affect interpretation
- Ascend support — confirm whether it is feature-complete or a subset of the NVIDIA kernel set
- FP4 support — verify whether FP4 kernels are production-ready or experimental

## Status
- New signal 2026-10-06 — 8.6k stars, active DeepSeek AI project; registry-ineligible (infrastructure library, not a billable inference service); relevant as supporting infrastructure for open-weight self-hosted deployment scoring at L7
