# Research Watch: MakazhanAlpamys/Soup — YAML-driven LLM fine-tuning with layer streaming for consumer GPU constraints

- Repo: https://github.com/MakazhanAlpamys/Soup (⭐1,600)
- Source: GitHub Trending (Python, daily) 2026-08-15; GIGAZINE coverage August 6, 2026; Product Hunt; Hacker News discussion

## Why this is worth watching
Soup is a command-line tool that collapses LLM post-training into a single YAML config and one `soup train` command. Its distinct technical contribution is **layer streaming**: instead of loading an entire model into GPU memory, it keeps the frozen base model in RAM and feeds the GPU one decoder layer at a time, achieving a 3.32 GB peak VRAM footprint for an 8B-parameter model on a 4 GB laptop GPU. This is not quantization alone (quantization reduces precision; layer streaming reduces the live VRAM footprint for the training pass itself). The combination of layer streaming + LoRA adapters makes on-device fine-tuning of 8B models possible on hardware that was previously reserved for inference only.

For clawfit's hardware axis, this matters: the boundary between "fine-tuning requires cloud" and "fine-tuning is local" has shifted. A developer profile with a mid-range laptop GPU (4 GB VRAM, RTX 3050 class) can now fine-tune an 8B model locally using Soup, then run the resulting adapter via Unsloth Desktop (tracked 2026-08-14) or ante (tracked 2026-08-10). The fine-tune → local deploy → agent bridge workflow is now achievable end-to-end on consumer hardware.

## What stands out immediately
- Layer streaming implementation: frozen base model stays in RAM; GPU receives one decoder layer at a time during the training pass; measured 3.32 GB peak VRAM at 119.6 tok/s on RTX 3050 laptop GPU (4 GB VRAM) — specific and reproducible hardware claim
- Single YAML config covers the full post-training pipeline: data preprocessing, training method selection, adapter merge, export format, serving
- 23 training methods: SFT, DPO, ORPO, KTO, and 19 others — broader training method coverage than most single-tool fine-tuners
- 142 ready-made recipes for common base models and task types
- 17 export/quantization formats: GGUF, ONNX, TensorRT, AWQ, GPTQ, and more — outputs compatible with all major inference runtimes
- Ecosystem integrations: HuggingFace Hub, Unsloth, DeepSpeed, vLLM, Ollama, SGLang, FlashAttention, Weights & Biases
- OpenAI-compatible serving: `soup serve` exposes a trained model as an OpenAI API endpoint
- Apache-2.0 license; MePlay, Inc. backing; v0.73.2 current release; 783 commits
- No SSH, no external infrastructure required: stated design goal is to work entirely locally without cloud compute

## Why clawfit should care
clawfit currently models hardware as a coarse three-axis choice: cloud, local-GPU, phone/edge. Soup introduces a refinement to the local-GPU axis: the distinction between "local GPU sufficient for inference" and "local GPU sufficient for fine-tuning." With layer streaming, a 4 GB VRAM GPU crosses the fine-tuning threshold for 8B models — a profile previously classified as "inference only" is now potentially "fine-tuning capable."

**Schema exposure:** `local_finetuning: [none | cloud-required | local-gpu-4gb | local-gpu-8gb | local-gpu-16gb+]`; `training_method: [supervised | dpo | rlhf | multiple]`; `vram_floor_gb_for_8b_ft: 4`; `layer_streaming: bool`.

**Cross-signal with Unsloth Desktop (2026-08-14):** Unsloth Desktop (L7/L2, 71.4k stars) also enables local fine-tuning and agent bridge in a no-code GUI; Soup is a CLI tool with more granular control and a broader training method library. Both signals confirm that local fine-tuning on consumer hardware is a real workflow in 2026, not a hobbyist edge case. **Two-signal convergence:** Unsloth Desktop + Soup = two independent tools shipping in the same week targeting the same capability gap (4–8 GB GPU fine-tuning without cloud infrastructure). This is a same-week two-signal pattern but different mechanisms (GUI no-code vs. CLI YAML) and different target users (no-code vs. practitioner) — discovery log only; not the same architectural sub-type for canonical L1 section change.

**For `offline_mid_codegen` and similar profiles:** the ability to fine-tune a domain-specific adapter locally and then run it through an agent harness (e.g., ante + llama.cpp, or Unsloth Desktop's `unsloth start claude`) creates a new profile axis: locally-fine-tuned domain model → local inference → agent loop. No cloud LLM cost, full data sovereignty. clawfit does not currently model this workflow.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base runtimes** (model preparation / adaptation sub-type): Soup prepares the model artifacts that L1 inference runtimes (llama.cpp, vLLM, Ollama, SGLang) serve; it is not a runtime itself but a direct precursor to one
- Not L2 (harness): Soup does not orchestrate an agent loop — it prepares model weights that agents use
- Not L4 (capabilities): it does not expose tools to a running agent — it produces the artifact consumed by the model loading step

The closest analogy in the taxonomy: Unsloth Desktop (2026-08-14, L7 primary / L2 secondary) was classified at L7 because the primary delivery surface is a desktop GUI with agent bridge; Soup's primary delivery is a CLI fine-tuning tool with no built-in agent bridge, making L1 the more accurate primary classification.

## Claims to verify
- Layer streaming benchmarks: 3.32 GB peak / 119.6 tok/s on RTX 3050 — verify against independent reproduction (GIGAZINE coverage confirms the claim but is a secondary source)
- Training method breadth: 23 methods listed — are all of them genuinely implemented or are some stubs/placeholders in early state?
- Integration with Unsloth: does Soup's LoRA adapter output format interoperate directly with Unsloth Desktop's fine-tuned model bridge, or is there a conversion step?
- Memory constraint boundary: is 4 GB VRAM the floor, or does it work on 3 GB (e.g., integrated graphics) with further quantization?

## Status
- Registry eligibility: **Not yet** — fine-tuning CLI tool, does not map to `agents.json`, `llms.json`, or `hardware.json` schema; clawfit models agents and inference runtimes, not training pipelines
- Open questions: Is Soup a solo-developer project or does MePlay, Inc. have commercial plans? Is the Apache-2.0 license stable or is a commercial license planned?
- Watch trigger: Soup's layer streaming technique adopted by a major fine-tuning framework (e.g., Unsloth, Axolotl, LLaMA-Factory) OR star count crosses 5,000 with deterministic VRAM benchmarks published for a broader model range
