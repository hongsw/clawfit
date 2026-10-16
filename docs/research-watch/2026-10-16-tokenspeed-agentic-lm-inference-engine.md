# Research Watch: TokenSpeed — Agentic-Workload LLM Inference Engine

- Repo: https://github.com/lightseekorg/tokenspeed (⭐2,663)
- Source: GitHub Trending Python (374 stars today)

## Why this is worth watching
TokenSpeed is an LLM inference engine built around agentic workload characteristics: many concurrent requests with variable context, frequent prefill/decode ratio shifts, and latency-sensitive multi-turn completions. Its architecture—a C++ FSM scheduler with a Python execution plane—makes explicit engineering decisions that general-purpose inference engines (vLLM, TGI, TensorRT-LLM) leave implicit. At 2.7k stars with 374 new today (suggesting accelerating community discovery), and with benchmark claims on current-generation Blackwell and upcoming Rubin hardware, it merits tracking as an L7 infrastructure signal.

## What stands out immediately
- Scheduler models request lifecycles and KV cache state as a finite-state machine (FSM) in C++, with a Python execution plane — the explicit state machine approach is unusual; most inference schedulers use heuristic queuing rather than formal state tracking
- Pluggable kernel system with a centralized registry and plugin mechanism for heterogeneous accelerators — claimed support for B200, B300, GB200, GB300, MI355X, MI455X, and NVIDIA Rubin (not yet shipping hardware)
- MLA (Multi-head Latent Attention) kernels described as "among the fastest on Blackwell for agentic workloads" — vendor claim, unverified, but MLA is a specific architectural primitive (from DeepSeek) requiring separate optimization rather than being handled by standard GEMM kernels
- SMG-integrated AsyncLLM entrypoint for low-overhead CPU-side request handling — relevant for high-concurrency agentic workloads where many agents generate requests simultaneously
- Vendor-reported 685 tokens/s per user serving Qwen3.8-Flash-Next on GB300; 580 TPS on Qwen3.5-397B-A17B for agentic workloads (October 2026, unverified)
- Framing as "TensorRT-LLM-level performance with vLLM-level usability" directly targets the known trade-off in the inference engine market

## Why clawfit should care
TokenSpeed is oriented toward multi-agent, high-concurrency inference workloads. For clawfit's hardware and scoring model, this matters in two ways:

First, the "agentic workload" framing suggests that general FLOP-throughput benchmarks (used for single-inference evaluation) are not the right metric for agent deployments, where prefill/decode ratios shift per turn and request concurrency varies. If TokenSpeed's framing is correct, clawfit's current `latency` scoring (which uses general throughput proxies) may underweight scheduling overhead for concurrent agent workloads.

Second, the hardware target list (B200, B300, GB200, Rubin, MI455X) represents the current-generation and near-future high-end accelerator landscape. TokenSpeed tracking these targets while they're not yet widely deployed is a forward signal: the inference engine ecosystem is pre-adapting for hardware that will dominate 2027 cloud deployments.

Star count (2,663) is below most tracked items in this project (typically 5k+). The 374-star daily gain and the Blackwell-specific optimization focus justify inclusion despite the lower total.

## Preliminary interpretation
Current best reading:
- **Level 7 primary — Inference infrastructure / hardware substrate**: TokenSpeed operates at the layer where LLM inference request scheduling, KV cache management, and kernel dispatch happen — entirely below L1 base agents
- No meaningful L1–L6 secondary classification; this is pure infrastructure

## Claims to verify
- 685 tokens/s per user on GB300 for Qwen3.8-Flash-Next (vendor benchmark; hardware availability limits independent reproduction)
- "Among the fastest MLA kernels on Blackwell" (no public comparison methodology found at time of tracking)
- FSM scheduler correctness under concurrent agentic workloads (formal verification status unknown)
- MI455X and Rubin support timelines (hardware not yet shipping; claimed in roadmap context)

## Status
- 2,663 stars, 374 new today; MIT license
- Registry entry: not eligible under current schema (no equivalent hardware entry category for inference engine vs. hardware device; `hardware.json` tracks deployable hardware configurations, not software inference engines)
- 📡 note: first signal for "agentic-workload-optimized inference engine" as a distinct L7 sub-type; prior tracked inference engines (vLLM, Ollama, llama.cpp) are general-purpose; TokenSpeed is the first to explicitly optimize scheduling for concurrent multi-agent request patterns
