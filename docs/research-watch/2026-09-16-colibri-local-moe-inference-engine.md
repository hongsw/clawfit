# Research Watch: colibri — Pure-C Local MoE Inference Engine

- Repo/Link: https://github.com/JustVugg/colibri
- Stars: ⭐ 33,797
- Source: GitHub Trending (2026-09-16)

## Why this is worth watching

colibri makes a bet that the right unit for running frontier Mixture-of-Experts models locally is a pure-C runtime with experts streamed lazily from disk, sidestepping the memory-cliff that blocks most consumer hardware from loading full MoE weights. This is a different architectural choice from llama.cpp (quantization-first) and vLLM (GPU memory paging): rather than fitting the model, it never fully loads it. That distinction matters for the long tail of developer machines that cannot hold even a quantized Mixtral or DeepSeek R2 in RAM.

## What stands out immediately

- **Pure C, zero external deps**: installs from source with a standard C compiler; no CUDA driver, no Python environment, no build system beyond make.
- **Expert streaming from disk**: on each forward pass, only the active expert shards are read from disk; inactive expert weights are never in RAM.
- **"Hardware you already own"**: framing explicitly targets the secondary market — a 2020 laptop, a NAS, a Raspberry Pi 5 cluster — as valid inference hardware for MoE frontier models.
- **No quantization requirement**: the streaming architecture means you can run float16 experts on a 16 GB laptop without fitting the entire model in memory at once.
- **33k stars in trending**: unusually fast uptake for a low-level C runtime, suggesting it fills a real gap not covered by higher-level tooling.

## Why clawfit should care

clawfit's hardware dimension currently models local execution as a binary property (supports_local: true/false). colibri introduces a third axis: **can run models that require more VRAM than the device has**, via streaming. A hardware entry's `vram_gb` ceiling may become less decisive if streaming engines proliferate. Scoring for local privacy profiles (offline + confidential) should account for this class of tool when it matures.

## Preliminary interpretation

Current best reading:
- **Level 0 — Bare inference substrate**: below the LLM serving layer; a hardware-close runtime rather than an agent or harness.

## Status
- Tracking: new signal, watching star trajectory and model compatibility list.
