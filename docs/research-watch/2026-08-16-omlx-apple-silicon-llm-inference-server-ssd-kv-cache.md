# Research Watch: oMLX — Multi-Model LLM Inference Server for Apple Silicon with SSD KV Cache Tiering

- Repo: https://github.com/jundot/omlx (⭐18,791)
- Source: GitHub Trending (Python, daily) 2026-08-16
- License: Apache 2.0
- Language: Python 3.11–3.13
- Platform: macOS 15.0+, Apple Silicon required

## Why this is worth watching

oMLX is a macOS-native LLM inference server that addresses a specific operational problem: running multiple models on a single Apple Silicon machine without manually juggling memory across separate server processes. Its most technically distinctive feature is a tiered KV cache system — hot blocks in unified RAM, cold blocks spilled to SSD — that extends effective context length beyond what fits in physical memory and persists KV state across server restarts. This is a different approach from the "load one model, restart for another" pattern that characterizes Ollama and llama.cpp's standard usage.

With 18.8k stars and a menu bar interface, oMLX is positioned between the practitioner-facing LLM inference servers (llama.cpp, vLLM, MLX) and the consumer-facing GUI tools (LM Studio, Unsloth Desktop). It occupies the "power-user local multi-model" niche: someone running Claude 3.5 Haiku for fast completions, a local vision model for image analysis, and an embedding model for retrieval — all on the same M4 Max, managed from the menu bar.

## What stands out immediately

- **Tiered KV cache (RAM → SSD):** hot cache blocks reside in unified memory; cold blocks are evicted to SSD and restored on demand. KV blocks persist across server restarts — a model resumed after reboot retains prior context window state. First tracked Apple Silicon inference tool with a documented RAM-to-SSD KV eviction path.
- **Multi-model LRU serving:** multiple models loaded concurrently; least-recently-used models evict from memory to make room for incoming requests. Manual load/unload controls available alongside automatic LRU. Distinct from single-model inference servers.
- **OpenAI AND Anthropic API compatibility:** exposes both OpenAI-compatible `/v1/` endpoints and Anthropic Messages API endpoints from a single server process. Clients targeting either API surface work without modification — eliminates the "which local proxy to run" coordination problem.
- **Menu bar interface:** macOS menu bar icon for model loading, status, and admin access. Built-in admin dashboard with chat, benchmark runner, and model management. No separate admin process or CLI flags required for common operations.
- **Model profiling system:** users define saved configuration bundles — context limit, quantization, batch size — per model. Bundles are named and reused across restarts; the intent is "pin everyday models in memory, auto-swap heavier ones on demand."
- **Experimental multi-Mac distributed inference:** early support for distributing a single model inference across multiple Apple Silicon machines over local network. No stable documentation yet, but the architecture supports it.
- **Vision models, embeddings, rerankers:** inference scope extends beyond text-only LLMs. Embedding and reranker model support enables local RAG pipelines where every component (retriever, reranker, generator) runs on the same machine.
- **Scale indicators:** 18.8k stars, 1.6k forks, 2,304 commits, 720 open issues — sustained growth with active development. Not a weekend project.

## Why clawfit should care

The inference-runtime-substrate reference note currently documents Ollama, llama.cpp, vLLM, and MLX as the canonical Apple Silicon inference paths. oMLX is a new point in that space: not a framework (no training), not a single-model server (multi-model LRU), not a GUI fine-tuning tool (inference only). It extends the Apple Silicon inference axis with two capabilities that no tracked tool currently offers together:

1. **SSD KV cache tiering** — changes the effective context capacity from "bounded by RAM" to "bounded by SSD," relevant for `hardware: local_mac` profiles doing long-context tasks
2. **Multi-model concurrent serving** — enables profiles that need an embedding model + a chat model + a vision model simultaneously without process restarts

For clawfit's `hardware: local_mac` profiles, oMLX changes the scoring landscape for multi-model local deployments. The `offline_mid_codegen` profile (Goose + llama.cpp + local GPU) doesn't require multi-model serving, but a `local_multi_task` profile (code completion, embedding for RAG, vision for image review) would find oMLX's LRU management directly useful.

**Schema exposure:** `multi_model_concurrent: bool`; `kv_cache_tier: [ram_only | ram_ssd]`; `persistent_kv_across_restart: bool`; `admin_interface: [cli | menu_bar | dashboard | none]`.

**Cross-signal with Unsloth Desktop (2026-08-14) and Soup (2026-08-15):** Both Unsloth Desktop and Soup address local fine-tuning on consumer hardware; oMLX addresses the serving side of the same stack — after fine-tuning a LoRA adapter with Soup, the result could be loaded into oMLX alongside a base model for multi-model concurrent serving. The fine-tune → adapter serve → local inference path is increasingly cohesive across tracked tools.

## Preliminary interpretation

- **Level 1 — Base runtimes / inference runtime sub-type** (primary): oMLX is an inference server. It executes model weights and returns completions; it does not orchestrate agent loops or provide harness behavior. The tiered KV cache and multi-model LRU are runtime-level features, not harness-level features.
- **Level 7 — Infrastructure** (secondary): the menu bar interface and admin dashboard make oMLX a local infrastructure appliance — a managed service on personal hardware. The admin layer separates it from bare inference servers like llama.cpp, which have no management surface.
- Not L2 (harness): oMLX does not call agents, dispatch tasks, or manage agent memory. It serves completions to agents that call it.
- Not L6 (human interface): the admin dashboard is an operational interface for the server operator, not a human-agent collaboration surface.

## Claims to verify

- SSD KV cache persistence claim: "blocks persist even after server restarts" — does persistence extend across macOS reboots, or only across oMLX process restarts? The distinction matters for `hardware: local_mac, statefulness: persistent` profiles.
- Anthropic Messages API compatibility: which API version is targeted? Does structured output (tool use) over the Anthropic endpoint work, or only basic completions?
- Multi-Mac distributed inference: "experimental" — what is the current state? Is it functional for any production-adjacent use case, or a stub in the codebase?
- Performance relative to MLX + llama.cpp baselines: oMLX uses MLX internally (Python + Apple Silicon optimizations); the question is whether the multi-model LRU overhead imposes a meaningful throughput penalty vs. single-model MLX serving.

## Status

- **Registry eligibility:** not yet — oMLX is an inference server, not an agent; no `agents.json` schema mapping. Could qualify for a new `inference_runtime` registry file if clawfit adds one.
- **No canonical section change:** single signal for "multi-model tiered-cache Apple Silicon inference server" pattern; second independent inference server with RAM-to-SSD KV tiering would confirm the pattern.
- **Watch trigger:** oMLX crosses 25k stars OR publishes stable multi-Mac distributed inference docs OR a tracked L2 harness (Goose, Aider, Claude Code) documents oMLX as a recommended local backend alongside Ollama.
