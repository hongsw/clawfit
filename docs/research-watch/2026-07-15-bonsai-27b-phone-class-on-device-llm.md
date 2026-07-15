# Research Watch: Bonsai 27B — Phone-Class On-Device LLM

- Repo/Link: https://prismml.com
- Source: Hacker News

## Why this is worth watching
PrismML's Bonsai 27B is the first 27B-parameter class model confirmed to run on a smartphone (1-bit quantized variant at 3.9 GB), with a 5.9 GB ternary variant for laptops. It supports tool calling and agentic workflows on-device, which is a direct hardware-selection signal for clawfit's offline/local execution dimension.

## What stands out immediately
- 1-bit quantization at 3.9 GB runs on iPhone; ternary at 5.9 GB targets laptop
- Claims 14× less memory, 8× faster, 5× lower energy vs standard 16-bit
- Supports tool calling, multi-step reasoning, multimodal understanding
- Backed by Caltech research; not just a fine-tune but an architecture-level efficiency push
- Positions against cloud dependency ("intelligence per bit" framing)

## Why clawfit should care
The clawfit hardware layer scores local vs cloud execution — Bonsai 27B expands the viable local execution tier to include phones and low-end laptops for 27B-class capability. This affects `offline_mid_codegen` and `offline_low_budget` profile recommendations: currently only smaller models (7B–13B) are assumed phone-viable. If Bonsai 27B adoption grows, the hardware registry and latency assumptions may need updating.

## Preliminary interpretation
Current best reading:
- **Level 3 — Base Model / Inference Runtime** (on-device LLM enabling agentic runtimes at phone tier)

## Status
- New signal; no prior tracking. Watch for: GitHub release of weights, adoption in harness layers, integration with local runtimes like llama.cpp or MLX.
