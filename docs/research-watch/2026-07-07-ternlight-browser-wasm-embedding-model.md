# Research Watch: Ternlight — Browser-Native WASM Embedding Model

- Repo/Link: https://ternlight-demo.vercel.app
- Source: Hacker News (31 points, 2026-07-07)

## Why this is worth watching
Ternlight delivers a production-weight embedding model (7 MB base, 5 MB mini) that runs entirely in the browser over WASM with no server round-trip. The ternary (BitLinear) quantization approach that achieves this footprint is the same direction BitNet has been pushing at the LLM layer — this is a signal that sub-10 MB semantic models are becoming an engineering expectation, not a research curiosity. Practical client-side semantic search without an API key or network dependency opens new deployment surface for offline and privacy-sensitive applications.

## What stands out immediately
- **Footprint:** 7 MB base / 5 MB mini, distributed as a single npm package — no separate model download step
- **Speed claim:** ~5 ms per embedding on CPU; cached calls approach 0 ms (claim, not independently validated)
- **Quantization method:** Ternary (BitLinear) weights — same family as BitNet; architecture described as transformer layers with attention, but internal details are from demo docs, not peer review
- **Runtime:** Browser WASM inference, no GPU required; confirmed to work on CPU
- **License:** MIT
- **HN signal:** 31 points is low-to-moderate — tool is early but credible enough to reach front page

## Why clawfit should care
clawfit's `network: offline` filter currently routes to local hardware profiles (llama.cpp, Ollama, Apple Silicon). Ternlight introduces a third path: browser-as-edge-compute for the embedding sub-task. If the speed claim holds, agents using retrieval or semantic routing could offload embedding to the client entirely, removing a server dependency and changing how clawfit should model latency and cost for RAG-style workflows. The npm distribution path also matters — this is targeting JS/browser agent tooling, not Python-native stacks.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base runtime** (inference substrate below agent harnesses; browser WASM as edge inference surface, analogous to LiteRT-LM at the mobile layer)
- Secondary: Level 7 (edge/hardware) given the browser-as-compute framing

## Status
- New; added 2026-07-07. Low-to-medium priority. Speed and quality claims need independent benchmarking before any registry consideration. Track for follow-up if npm adoption accelerates or a GitHub repo surfaces.
