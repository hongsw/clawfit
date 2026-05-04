# Research Watch: Rapid-MLX

- Repo: https://github.com/raullenchai/Rapid-MLX
- Also see: docs/reference-notes/inference-runtime-substrate.md (L0 companion axis); https://github.com/ml-explore/mlx (upstream framework); https://ollama.com (primary comparison target)

## Why this is worth watching

Rapid-MLX is trending at +161 stars/day (GitHub Python #9 as of 2026-05-03) despite sitting below the usual 5k-star registry threshold at 1,002 stars. It fills a specific gap in the current inference-runtime-substrate map: MLX is already tracked as an Apple Silicon hardware optimizer, but Rapid-MLX adds an OpenAI-compatible REST API, continuous batching, and 17+ tool-call parsers on top of it — capabilities that mlx-lm and Ollama do not currently combine in one package. The explicit head-to-head benchmark table against Ollama (2.6x–3.2x throughput on multiple models) makes it a direct challenger to Ollama's position as the default offline substrate recommendation for `hardware: laptop, network: offline` profiles.

## What stands out immediately

- **Performance claims (claim to inspect):** Mac Studio M3 Ultra (256GB) benchmarks show Phi-4 Mini 14B at 180 tok/s (vs. 56 Ollama, 77 mlx-lm), Qwen3.5-9B at 108 tok/s (vs. 41 Ollama). The comparison is single-machine, self-reported; no independent third-party replication found.
- **Tool-call completeness:** 17 parser formats covering Qwen, DeepSeek, GLM, MiniMax, Llama families, plus automatic recovery when quantized models emit broken tool calls as raw text. This is operationally relevant for agent frameworks that depend on structured outputs.
- **Prompt caching for non-transformer architectures:** "DeltaNet state snapshots" claim to bring KV-cache-equivalent prompt caching to hybrid RNN/attention models (Qwen3.5), described in the README as "the first technique to bring prompt cache to non-trimmable architectures on MLX." This is technically distinct from what standard transformer caching does and warrants verification.
- **Continuous batching engine:** `BatchedEngine` is present in the codebase — addressing a capability gap in stock mlx-lm, which processes requests sequentially. Not independently validated.
- **OpenAI-compatible API surface:** Drop-in `http://localhost:8000/v1` endpoint. Means existing tooling (Cursor, Claude Code, Aider) can redirect to it without code changes.
- **Scope narrowing:** Apple Silicon only. No Linux, no Windows, no x86. Vision features require `torch`/`torchvision` (~2.5GB additional deps), partially undermining the "no heavy deps" positioning.
- **Cloud offload escape hatch:** Can route large-context requests to cloud LLMs when local prefill would bottleneck — a pragmatic design choice that complicates pure offline classification.
- **Self-diagnostic tooling:** `rapid-mlx doctor` subcommand for environment validation — signals the project is aiming at developer experience, not just raw performance.

## Why clawfit should care

The inference-runtime-substrate note (reference-notes/inference-runtime-substrate.md) explicitly flags: "Track MLX separately from Ollama for Apple Silicon profiles. MLX's Metal-native performance gap vs. GGUF is material; currently both map to `hardware: laptop` without distinction." Rapid-MLX is a direct response to that gap. If its performance claims survive independent replication, the current `hardware: laptop, network: offline` recommendation that defaults to Ollama becomes materially suboptimal for Apple Silicon users. Additionally, the 17-parser tool-call layer is directly relevant to `task: code-gen` profiles: agent frameworks that require reliable structured outputs from quantized models currently have no Apple Silicon-native option with this level of parser coverage. The cloud offload feature also introduces a hybrid `network: offline+online` profile that the current clawfit filter schema does not model.

## Preliminary interpretation

Current best reading:
- **Inference-runtime-substrate companion axis** — "Local runtime + developer UX" sub-type, Apple Silicon specialization. Not a Level 1 agent and not a Level 7 hardware entry; sits in the substrate layer beneath Level 1 agents, as described in the companion axis doc. Within the substrate taxonomy: closest to Ollama (local runtime + API server + developer UX) but implemented on MLX rather than GGUF/llama.cpp, and with materially richer tool-call support.
- Secondary relevance to **Level 4c** (tool-use layer): the 17-parser tool-call normalization engine could be extracted as a standalone capability; it is doing MCP-adjacent structured-output recovery work.
- **Not a Level 7 entry** — hardware optimization is the substrate, not the agent interface.

Star count (1,002) is below the 5k registry promotion threshold. The +161/day velocity and the direct Ollama comparison claim are the justification for watching it now rather than at threshold.

## Status
- Below 5k-star registry threshold; not added to reference-levels.md or any registry JSON. Re-evaluate at 3k stars or when an independent benchmark (non-self-reported) confirms or refutes the Ollama comparison claim. The "DeltaNet state snapshots" caching technique is a specific falsifiable claim that deserves its own verification pass before citing it in recommendation output.
