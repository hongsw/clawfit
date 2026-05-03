# inference-runtime substrate axis

This document tracks a different axis from `reference-levels.md`.

- `reference-levels.md` asks: **what layer of the agent ecosystem is this?**
- `inference-runtime-axis.md` asks: **what substrate actually makes the model run, fast enough, cheap enough, and on the right hardware?**

This matters because many high-signal AI tools are not best understood only as L1/L2/L4/L6 taxonomy entries. They also sit on a separate execution surface: the runtime / serving / optimization substrate.

---

## Why this axis exists

A recent 15-repo landscape roundup grouped together:
- vLLM
- llama.cpp
- Ollama
- Hugging Face Transformers
- PyTorch
- Unsloth
- exo
- FastChat
- llm.c
- MLC LLM
- FlashAttention
- whisper.cpp
- TensorRT-LLM
- MLX
- DeepSpeed

Those projects are not one category in the 7-layer map.

Some are:
- end-user local runtimes
- serving engines
- training / fine-tuning stacks
- low-level optimization kernels
- hardware-specific execution backends
- distributed execution patterns

But together they define a real comparison axis that clawfit should name explicitly.

---

## Defining question

> What runtime substrate should this team rely on to execute, serve, optimize, or fine-tune models under its actual latency, budget, and hardware constraints?

This is adjacent to model selection, but not the same thing.
A team can choose the same model family and still make a very different decision at the substrate layer:
- `llama.cpp` on a laptop
- Ollama for local developer UX
- vLLM for GPU serving
- TensorRT-LLM for NVIDIA-max throughput
- MLX for Apple Silicon
- MLC LLM for cross-platform compiled deployment

---

## Core sub-axes

### 1. Execution mode
What kind of runtime work is being done?

- **local interactive runtime** — e.g. `llama.cpp`, Ollama, MLX
- **production serving engine** — e.g. vLLM, TensorRT-LLM, FastChat
- **training / fine-tuning substrate** — e.g. PyTorch, Unsloth, DeepSpeed
- **compiler / portability layer** — e.g. MLC LLM
- **kernel / primitive optimization** — e.g. FlashAttention
- **educational / minimal substrate** — e.g. `llm.c`
- **distributed edge / home cluster** — e.g. exo
- **speech-specific local inference** — e.g. `whisper.cpp`

### 2. Hardware affinity
What hardware target does the substrate naturally favor?

- consumer CPU
- consumer GPU
- Apple Silicon
- NVIDIA datacenter GPU
- ARM / mobile / edge
- mixed-device cluster

This axis is separate from the hardware registry itself.
The hardware registry answers **what hardware exists**; this axis answers **what runtime best exploits it**.

### 3. Packaging level
How close is the tool to the end user?

- **framework** — PyTorch, Transformers
- **runtime engine** — vLLM, llama.cpp, MLX
- **developer UX wrapper** — Ollama
- **optimization library** — FlashAttention, DeepSpeed
- **cluster / orchestration layer** — exo

This matters because framework-level tools usually demand more engineering maturity than packaged local runtimes.

### 4. Optimization objective
What is the substrate mostly trying to optimize?

- throughput
- latency
- VRAM efficiency
- portability
- ease of local setup
- distributed scale
- educational transparency

A recommendation engine should not treat all “faster LLM” projects as equivalent when their objective functions differ.

### 5. Deployment posture
Where will this likely run?

- solo laptop / workstation
- team-local workstation fleet
- self-hosted server
- cloud GPU cluster
- edge / mobile device
- mixed local+cloud deployment

---

## Relationship to the 7-layer taxonomy

This axis should **complement**, not replace, the existing map.

Examples:
- Ollama can appear in the layer map as a runtime-facing tool, while also scoring as a **local developer UX substrate** on this axis.
- vLLM may show up in research-watch and hardware discussions, but on this axis it is primarily a **high-throughput serving substrate**.
- MLX is not just an Apple ecosystem signal; it is a **hardware-aligned runtime substrate**.
- FlashAttention is not a user-facing runtime at all, but it still matters because it changes the economics of downstream serving/training layers.

The 7-layer taxonomy answers **where a tool sits in the agent stack**.
This axis answers **how model execution is made practical**.

Both are needed.

---

## How this differs from issue #8 (hardware / infrastructure dimension)

Issue #8 asks for a stronger hardware and infrastructure dimension.
That work is about the environment:
- local vs cloud
- deployment surfaces
- hardware categories
- infrastructure context

This page is narrower and more operational.
It focuses on the **runtime substrate sitting between the model and the hardware**.

Put simply:
- **#8 = where the system runs**
- **this axis = how the model is actually executed efficiently on that system**

The two should cross-reference each other, but they are not the same gap.

---

## Implications for clawfit

The current clawfit framing already promises:
- agent + LLM + hardware recommendation

To make that promise more real, clawfit likely needs a future substrate-aware field or companion score such as:
- `runtime_substrate_fit`
- `hardware_affinity`
- `throughput_vs_latency_preference`
- `local_runtime_maturity`

Not all of these need to land in the scoring model immediately.
But the axis should be named now so later recommendation logic has a stable conceptual home.

---

## Near-term use inside the docs

For now, this axis is best used as:
1. a companion page to the taxonomy
2. a lens for interpreting new research-watch signals
3. a guardrail against dumping every LLM infra repo into one layer bucket

That is enough to improve the map without prematurely forcing schema changes.

---

## See also

- [ecosystem-axes.md](./ecosystem-axes.md)
- [ecosystem-overview.md](./ecosystem-overview.md)
- [reference-levels.md](../reference-levels.md)
- [Research Watch: 15-repo LLM runtime landscape](../research-watch/2026-05-03-llm-runtime-substrate-landscape.md)
