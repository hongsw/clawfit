# Inference Runtime Substrate Axis

*Companion note to `docs/reference-levels.md` · Addresses GitHub issue #9*

---

## What this axis is

The **inference-runtime substrate** is the software layer that sits between the hardware and the model/agent. It answers: *how does the LLM actually run on this machine?*

This layer is distinct from:
- **Level 1 agents** (Claude Code, OpenCode) — these are the user-facing runtimes that *call* a model
- **The `hardware` filter in clawfit** (`laptop`, `workstation`, `cloud`) — that describes *where* the compute lives
- **Issue #8** (hardware/deployment gap) — that concerns what hardware clawfit recommends; this concerns the *software stack* that turns hardware into callable inference

The substrate layer is implicit in every clawfit recommendation. When `network: offline` is selected and a local model is needed, the user still has to pick an inference backend. Naming this axis makes that choice legible.

---

## Sub-dimensions

| Sub-type | What it does | Representative repos |
|----------|-------------|----------------------|
| **Serving framework** | High-throughput HTTP API server; concurrent requests; datacenter GPU | vLLM, FastChat |
| **Local runtime + developer UX** | Packaged CLI/desktop app; pulls models; single-user | Ollama, llama.cpp |
| **Hardware optimizer / compiler** | Kernel-level or compiler-level speedup; sits inside other runtimes | FlashAttention, TensorRT-LLM, MLC LLM, MLX |
| **Distributed home cluster** | Shards model across multiple consumer machines on LAN/WAN | exo |
| **Training + fine-tuning substrate** | Full training stack; inference is secondary | Unsloth, DeepSpeed, PyTorch, HF Transformers |
| **Domain-specific runtime** | Inference for one modality only (audio, vision) | whisper.cpp |
| **Educational / minimal** | Proof-of-concept or teaching artifact | llm.c |

---

## The 15-repo landscape (issue #9 source list)

These 15 repos were the motivating evidence for this axis. Classification:

**Serving (datacenter / multi-user):**
- [vLLM](https://github.com/vllm-project/vllm) ⭐ ~45k — high-throughput, memory-efficient inference server; PagedAttention; the de facto open-source serving framework for datacenter GPUs
- [FastChat](https://github.com/lm-sys/FastChat) ⭐ ~38k — training + serving; OpenAI-compatible API; multi-model
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) ⭐ ~10k — NVIDIA compiler + runtime optimized for H100/A100; enterprise datacenter

**Local runtime + developer UX:**
- [Ollama](https://ollama.com) ⭐ ~130k — packaged local runtime; model pull/run CLI; most common offline substrate for clawfit `network: offline` profiles
- [llama.cpp](https://github.com/ggerganov/llama.cpp) ⭐ ~80k — C++ inference engine; GGUF format; runs on CPU, Metal, CUDA, ROCm; broadest hardware coverage

**Hardware optimizer / compiler:**
- [FlashAttention](https://github.com/Dao-AILab/flash-attention) ⭐ ~17k — IO-aware attention kernel; used inside most other frameworks, not directly by end users
- [MLC LLM](https://github.com/mlc-ai/mlc-llm) ⭐ ~20k — universal deployment compiler; targets WebGPU, iOS, Android, Metal, CUDA, ROCm; compilation-first approach
- [MLX](https://github.com/ml-explore/mlx) ⭐ ~20k — Apple Silicon-native array framework; the inference substrate for Apple Silicon offline profiles; used by Ollama's Metal backend and mlx-lm

**Distributed home cluster:**
- [exo](https://github.com/exo-explore/exo) ⭐ ~30k — run large models across multiple consumer devices (MacBooks, iPhones, etc.) as a heterogeneous cluster; P2P network

**Training + fine-tuning:**
- [Unsloth](https://github.com/unslothai/unsloth) ⭐ ~40k — 2× faster QLoRA fine-tuning on consumer GPUs; 70% less VRAM; offline fine-tuning substrate
- [DeepSpeed](https://github.com/microsoft/DeepSpeed) ⭐ ~38k — distributed training + inference; ZeRO optimization; Microsoft
- [PyTorch](https://github.com/pytorch/pytorch) ⭐ ~90k — foundational ML framework; everything else runs on or compiles through it
- [HF Transformers](https://github.com/huggingface/transformers) ⭐ ~145k — model hub + inference pipeline + fine-tuning; the entry point for most practitioners

**Domain-specific:**
- [whisper.cpp](https://github.com/ggerganov/whisper.cpp) ⭐ ~38k — C++ port of OpenAI Whisper; CPU + Metal + CUDA; STT substrate for offline voice input (see Ghost Pepper at Level 7)

**Educational / minimal:**
- [llm.c](https://github.com/karpathy/llm.c) — Karpathy's minimal GPT training in pure C; research/teaching artifact; not a production recommendation target

---

## How this maps to clawfit decisions

The substrate axis intersects clawfit's existing filters:

| clawfit filter | Substrate implication |
|----------------|-----------------------|
| `network: offline` | User needs a local substrate. Practical choices: Ollama (easiest), llama.cpp (broadest hardware), MLX (Apple Silicon best perf) |
| `network: online` | Substrate is opaque (cloud provider handles it). No user decision needed. |
| `hardware: laptop` | Apple Silicon → MLX/Ollama; x86 → llama.cpp/Ollama |
| `hardware: workstation` | CUDA GPU → Ollama/llama.cpp + FlashAttention; AMD → llama.cpp ROCm |
| `hardware: cloud` | Serving framework territory (vLLM, TGI, TensorRT-LLM); managed by infra team |
| `latency: low` | Local: quantized GGUF via llama.cpp/Ollama; Cloud: provider-managed |
| `cost_per_1k_tokens: 0.0` | Free = local = need a substrate; Ollama or llama.cpp are the default picks |

---

## What this axis is *not* (boundary with issue #8)

Issue #8 (hardware/deployment gap) asks: *should clawfit add a field for the hardware the user runs on?*

This note (issue #9) asks: *should clawfit name the software stack that sits between hardware and model?*

The two are related but non-overlapping:
- A user could pick `hardware: workstation` (the #8 dimension) and still need to choose between Ollama, vLLM, and llama.cpp (the #9 dimension)
- The substrate choice is mostly relevant when `network: offline`; for `network: online` it is opaque
- Resolving #8 (expanding the hardware taxonomy) does not resolve #9 (naming the inference software stack)

---

## Recommendations for clawfit v0.4

1. **No registry schema change needed now.** The substrate is implicit in `network: offline` + `hardware: *` combinations. A future `inference_substrate` field would be an enhancement, not a fix.

2. **Add substrate guidance to the offline recommendation output.** When clawfit returns an offline recommendation, append a note like: *"Ollama or llama.cpp recommended as the local inference substrate for this hardware profile."*

3. **Track MLX separately from Ollama for Apple Silicon profiles.** MLX's Metal-native performance gap vs. GGUF is material; currently both map to `hardware: laptop` without distinction.

4. **Consider `inference_backend` as an optional tag in the LLM registry** for models that have confirmed quantized variants (e.g., `unsloth_available: true`, `mlx_available: true`, `gguf_available: true`).
