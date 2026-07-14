# Research Watch: Needle — 26M-Parameter Function-Call Model for Edge Devices

- Repo: https://github.com/cactus-compute/needle (⭐3,092)
- Source: GitHub Trending Python (daily), 2026-07-14

## Why this is worth watching
Needle is a purpose-built 26M-parameter model designed to execute tool/function calls reliably on phones, watches, and glasses. It beats larger models (FunctionGemma-270m, Qwen-0.6B, Granite-350m, LFM2.5-350m) on single-shot function-call benchmarks while running at a fraction of the parameter count. If the benchmark claims hold under independent testing, this represents a meaningful architectural departure: stripping everything except function-call capability into a model small enough for real edge hardware.

## What stands out immediately
- **26M parameters, not a quantized large model**: the architecture is built from scratch for function-call latency — 12 encoder + 8 decoder layers, grouped query attention (GQA), rotary positional embeddings (RoPE), no feed-forward networks in the encoder, tied embedding/output weights
- **Target hardware**: explicitly "phones, watches, glasses" — not "edge" as a marketing claim but as an architectural constraint that drove the design decisions above
- **Claimed throughput**: 6,000 tokens/sec prefill, 1,200 decode on Cactus production infrastructure; independent on-device numbers not yet published
- **Training compute**: 16 TPU v6e — relatively modest, consistent with focused narrow-task training rather than general pretraining
- **Benchmark comparison**: beats models 10–14x larger on single-shot function-call tasks; benchmark details (datasets, prompt format, evaluation harness) need independent verification
- **MIT license**: permissive, enabling deployment in commercial on-device applications without restriction
- **Use case implied**: on-device agent action dispatch — a phone-local model routes tool calls without round-tripping to a cloud LLM

## Why clawfit should care
Needle directly affects clawfit's `hardware: local` and `latency: low` scoring dimensions. Currently, clawfit's local hardware recommendations assume inference on laptops or embedded GPUs (Apple Silicon, CUDA edge). A 26M model that runs on a watch-class device represents a qualitatively different deployment profile: **sub-phone hardware**. If confirmed, this would expand the hardware axis beyond the current five entries (cloud, laptop, embedded, M-series, Raspberry Pi) to include a "micro-device" tier. The function-call specialization also challenges clawfit's implicit assumption that agents need a capable general LLM — for highly structured tool dispatch, a domain-narrow tiny model may suffice and score higher on latency/cost axes.

## Preliminary interpretation
Current best reading:
- **L1 primary** (base runtime model) — it is the LLM itself, not a harness or wrapper; primary architectural role is as the core inference engine
- **L7 secondary** (infrastructure) — the target deployment platform (edge/micro-device) puts it in the infrastructure layer when viewed from a deployment lens

## Claims to verify
- Independent function-call benchmark reproduction (which datasets? which prompt formats? zero-shot or few-shot?)
- On-device inference numbers on actual phone/watch hardware — the 6,000 tok/sec figure is on Cactus infrastructure, not a Snapdragon or Apple A-series chip
- Whether "beats FunctionGemma" gap holds when controlling for prompt format (function-call benchmarks are notoriously prompt-sensitive)
- Cactus infrastructure dependency: does Needle run on arbitrary inference backends or require the Cactus runtime?
- Parameter count (26M) vs. latency tradeoff at 4-bit quantization on real edge devices

## Status
- **Registry eligibility**: `llms.json` is the correct target if per-token cost is available; edge model pricing model is unclear (self-hosted = no per-token cost). Hold on registry entry until deployment cost model is confirmed.
- **Schema watch**: `hardware: micro-device` tier as a new hardware.json entry candidate; `model_specialization: function-call-only` as a distinguishing field
- **Open questions**: Is Needle useful as a component in a larger agentic system (dispatcher model) rather than the sole LLM? What is the failure mode when calls fall outside the trained function schema?
