# Research Watch: llama-modchip — 284B DeepSeek on 64 GB RAM, No GPU

- Repo/Link: https://github.com/synchopate/llama-modchip
- Source: Hacker News (345 points)

## Why this is worth watching
llama-modchip is a set of llama.cpp kernel patches and quantization tools that run a 284B-parameter MoE model (DeepSeek-V4-Flash) on a consumer x86 CPU with 64 GB RAM and no GPU at 9–15 tok/s decode. It demonstrates that the hardware threshold for large-scale offline inference is now within reach of a mid-range developer workstation.

## What stands out immediately
- **Extreme compression:** 284B weights squeezed to ~57 GiB via 1.71-bit quantization
- **Sparse activation:** only 13B parameters are active per token — CPU-feasible per-token compute
- **Hardware targets:** AVX-512/AVX2 x86 and ARM64 (Apple Silicon, Raspberry Pi 5 experiments ongoing)
- **Speculative drafting + KV snapshot restore** improve throughput on constrained hardware
- **GPU optional:** hybrid mode can offload some layers to a GPU if present, but zero-GPU is the default

## Why clawfit should care
clawfit's `offline_mid_codegen` profile scores tools on network=offline capability. Until now, offline profiles could only realistically run sub-30B models. llama-modchip moves the threshold to 284B with active-parameter parity to frontier models, strengthening the case for recommending local-first coding agents (ZeroClaw, ATLAS, Aider + local backend) to teams with confidential data constraints. The hardware registry may need a new tier for "high-RAM CPU workstation."

## Preliminary interpretation
Current best reading:
- **Level 5 — Local Inference Runtime** (sits beneath agent harnesses; enables offline use of frontier-scale MoE models)

## Status
- Tracking: v2.4.0, active development — monitor for adoption by mainstream agents (Aider, Continue, OpenHands)
