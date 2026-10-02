# Research Watch: Janus

- Repo/Link: https://github.com (exact repo unconfirmed from HN listing)
- Source: Hacker News (44 pts)

## Why this is worth watching
Janus is a Go binary that runs GGUF models via Vulkan GPU acceleration — enabling cross-platform local inference (NVIDIA, AMD, Intel, Apple) without CUDA dependency. This is a first signal for "Vulkan-first GGUF inference in Go" as a distinct runtime category, complementing existing CUDA-native and Metal-native local inference tools.

## What stands out immediately
- Single Go binary deployment model: no Python runtime, no CUDA toolkit required
- Vulkan backend: cross-GPU platform support (works on hardware where llama.cpp CUDA does not)
- GGUF format: compatible with the full Hugging Face quantized model ecosystem
- Go language: appeals to backend/DevOps teams already in the Go ecosystem
- Enables agent execution on hardware that lacks NVIDIA CUDA support (AMD GPUs, Intel Arc, cloud VMs without CUDA)

## Why clawfit should care
clawfit's hardware.json currently distinguishes `local-gpu` vs `local-cpu` without GPU vendor granularity. Janus expands the "local GPU" surface to non-CUDA hardware, which matters for cost modeling: an AMD GPU box with Vulkan-capable drivers can run GGUF models at GPU speeds without NVIDIA licensing costs. The `network: offline` + `hardware: local-gpu` combination in scoring may need to account for GPU vendor compatibility. If Janus reaches a stable release above 500★, it would be a candidate registry entry as an inference backend alternative to Ollama for Vulkan-capable environments.

## Preliminary interpretation
Current best reading:
- **Level 1 — Inference Runtime / Substrate (Vulkan local execution sub-type)**

## Status
- First signal for "Vulkan-based cross-GPU GGUF inference runtime in Go"
- Low current signal strength (44 HN pts); exact GitHub repo not confirmed from listing
- Related to existing patterns: nobodywho (cross-platform inference, mobile-first), sglang (GPU serving at scale) — but distinct vendor stack (Vulkan vs Metal vs CUDA)
- Monitoring — confirm repo and star count before considering for registry or canonical taxonomy
