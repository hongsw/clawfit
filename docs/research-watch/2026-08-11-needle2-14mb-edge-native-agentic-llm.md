# Research Watch: Needle2 — 14 MB Agentic LLM for Edge Devices

- Repo/Link: https://cactuscompute.com/
- Source: Hacker News ("Show HN", 114 pts, 2026-08-11)

## Why this is worth watching
Needle2 is a 14 MB agentic LLM from CactusCompute that runs on phones, wearables, smart home devices, and robots — smaller than any edge LLM previously tracked (prior floor: 28M-parameter model on an $8 microcontroller, 2026-07-26). The model explicitly supports tool calling, device use, and structured extraction, making it purpose-built for agent workflows rather than just chat inference.

## What stands out immediately
- **14 MB total size** — fits in RAM on microcontrollers and wearables; the smallest tracked inference footprint by roughly an order of magnitude
- Targets four distinct form factors: phones, wearables, smart home, robots
- Native tool-calling and structured extraction support (not retrofitted)
- CactusCompute is positioning this as a commercial product line (docs portal, commercial framing)
- HN front-page visibility at 114 pts indicates meaningful developer interest

## Why clawfit should care
clawfit's hardware dimension currently models cloud, on-device (phone/laptop GPU), and local server deployment; sub-100 MB edge inference for embedded devices is an uncovered segment. If Needle2 ships a deployable runtime (SDK + GGUF quantization docs), it represents a new `hardware: embedded` axis that clawfit cannot yet recommend for. **Schema exposure:** `deployment_form_factor: [cloud | local-gpu | phone | wearable | embedded | robot]`; `model_size_mb: N`.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base runtime (edge/embedded sub-cluster)**

The model is the runtime — there is no separate framework layer. If CactusCompute ships a deployment SDK alongside the weights, a Level 2 harness entry would be warranted.

## Status
- New signal; watch for weight release, benchmarks, and SDK documentation
- Do not add to registry until deployment path is confirmed (weights + runtime)
