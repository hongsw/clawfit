# Research Watch: 15-repo LLM runtime substrate landscape

- Source: LinkedIn post by Stanislav Beliaev (public post, accessed 2026-05-03)
- Link: <https://www.linkedin.com/posts/stasbel_best-15-repos-for-ai-engineers-to-run-llms-share-7455659983360319489-G4Lk>
- Date observed: 2026-05-03

## Why this matters

This is a useful signal not because every repo belongs directly in clawfit's registry, but because the list makes a hidden axis visible:

**the runtime substrate layer between “I picked a model” and “the model runs well enough on real hardware.”**

clawfit already frames itself as an agent + LLM + hardware recommendation engine. This repo cluster shows that model choice and hardware choice are still incomplete unless we also name the substrate that connects them.

---

## The 15 repos grouped by function

### 1. Production serving / high-throughput inference
- **vLLM** — high-throughput serving, continuous batching, GPU utilization
- **TensorRT-LLM** — NVIDIA-specific peak-throughput inference stack
- **FastChat** — chat-serving / evaluation / orchestration surface for LLM systems

### 2. Local / offline / developer-friendly runtimes
- **llama.cpp** — local inference standard on consumer hardware
- **Ollama** — easiest packaged local UX for running common open models
- **MLX** — Apple Silicon-native array/runtime substrate
- **whisper.cpp** — local speech inference analogue for the Whisper family

### 3. Training / fine-tuning / optimization frameworks
- **PyTorch** — base deep learning framework
- **Transformers** — model architecture and inference/training abstraction layer
- **Unsloth** — faster fine-tuning + VRAM efficiency for LLM adaptation
- **DeepSpeed** — distributed training + memory optimization

### 4. Portability / compiler / low-level optimization
- **MLC LLM** — compiled deployment across devices/platforms
- **FlashAttention** — kernel-level memory/throughput optimization primitive
- **llm.c** — minimal raw C/CUDA implementation, useful as a learning/calibration substrate

### 5. Distributed alternative topology
- **exo** — distributed inference across multiple personal devices / home cluster

---

## Read on the signal

The important pattern is that the post mixes together tools from different layers but one practical concern:

> How do I make LLM execution economically viable under real constraints?

That concern cuts across:
- serving
- local inference
- fine-tuning
- hardware specialization
- low-level optimization
- portability

This suggests clawfit needs a companion axis that asks not just:
- what agent stack fits?
- what model fits?
- what hardware fits?

but also:
- **what runtime substrate fits?**

---

## Candidate substrate dimensions exposed by this list

1. **Execution mode**
   - local runtime
   - serving engine
   - training/fine-tuning substrate
   - optimization primitive
   - portability/compiler layer

2. **Hardware affinity**
   - Apple Silicon
   - NVIDIA datacenter GPU
   - consumer CPU/GPU
   - mixed-device cluster
   - edge/mobile

3. **Optimization goal**
   - throughput
   - latency
   - VRAM efficiency
   - portability
   - simplicity of local setup
   - educational transparency

4. **Packaging level**
   - framework
   - engine
   - wrapper UX
   - kernel library
   - distributed topology layer

---

## clawfit implication

This should **not** become a bulk registry import.
The better move is:
1. define the substrate axis explicitly
2. use it to interpret future repo signals
3. later decide which individual projects deserve first-class registry records

In other words, the immediate output is a **better map**, not a longer tool list.

---

## Relationship to existing gaps

This signal overlaps with the open hardware/infrastructure gap, but it is not identical.

- Hardware / deployment asks: where does the system run?
- Runtime substrate asks: how is model execution made efficient on that environment?

That distinction is important if clawfit wants to stay recommendation-oriented instead of collapsing everything into a single “infra” bucket.
