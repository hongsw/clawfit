# Research Watch: WebLLM — High-Performance In-Browser LLM Inference

- Repo/Link: https://github.com/mlc-ai/web-llm
- Source: Hacker News

## Why this is worth watching
WebLLM brings LLM inference directly into the browser via WebGPU, with no server required. From the mlc-ai organization (same team as MLC LLM), it targets fully local, privacy-preserving AI in web applications. This addresses a specific gap in clawfit's current model: browser-native agents that run entirely client-side are not representable in the current registry.

## What stands out immediately
- WebGPU backend — uses modern browser GPU APIs, no native install required
- Supports multiple open-weight models (Llama, Mistral, Phi, Gemma families)
- JavaScript/TypeScript API — directly consumable by web-based agent UIs
- Full offline capability after model download — zero server calls at inference time
- mlc-ai's MLC LLM is already referenced in clawfit's inference-runtime-substrate note

## Why clawfit should care
WebLLM creates a new hardware/deployment category: "browser" as an inference substrate. clawfit's current hardware registry covers local (edge), on-prem, and cloud. A browser-native deployment has distinct org_fit characteristics: zero infrastructure cost, user-device compute, strong data-locality, but limited model size and variable performance. Teams with strict data-sensitivity requirements (confidential/offline profiles) could run inference in browser without any server-side exposure.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base Agent Runtime / Inference Substrate** (browser-native variant)

## Status
- Surfaced on Hacker News 2026-09-03; mlc-ai org already in reference-notes
- Good candidate for hardware registry entry ("browser") and tools_registry addition
