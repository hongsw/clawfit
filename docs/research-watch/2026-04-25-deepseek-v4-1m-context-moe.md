# Research Watch: DeepSeek V4 — 1M-Token Context MoE Model

- Repo/Link: https://deepseek.com / https://huggingface.co (DeepSeek V4)
- Source: Hacker News (1,786 pts, 1,392 comments — #1 on HN today); GeekNews (6 pts)

## Why this is worth watching
DeepSeek V4 is a Mixture-of-Experts model with a 1M-token context window — the longest public context window among open-weight models as of April 2026. The 1M context makes it directly viable for whole-codebase, whole-document, and multi-session agent contexts that currently require chunking or RAG workarounds. GeekNews notes it as "고효율 대규모 언어 모델" (high-efficiency large-scale language model) alongside the 1M token claim.

## What stands out immediately
- **1M token context**: eliminates RAG overhead for medium-to-large codebases; entire repo fits in context
- **MoE architecture**: selective activation keeps inference cost manageable despite model scale
- **Open-weight + Hugging Face availability**: usable with local inference hardware at sufficient VRAM; `network: offline` profiles become viable
- **HN traction**: 1,786 pts / 1,392 comments is the highest single-thread score on today's front page — exceeds GPT-5.5 announcement (203 pts)

## Why clawfit should care
If DeepSeek V4 is confirmed at strong SWE-bench / coding benchmark scores, it becomes a candidate for clawfit's LLM registry as a new tier: open-weight + offline + 1M context. This directly expands the `offline_mid_codegen` and `offline_mid_confidential` profiles beyond the current Qwen3-35B-A3B (tracked 2026-04-20). The model also challenges the assumption that 1M context requires a cloud API — local deployment at 16–24GB VRAM may be feasible with quantized variants.

## Preliminary interpretation
Current best reading:
- **LLM registry candidate** — revisit once SWE-bench Verified / LiveCodeBench scores are published and quantized inference requirements are confirmed

## Status
- Tracking. Do not add to registry until benchmark data is available. High urgency signal — 1,786 HN pts.
