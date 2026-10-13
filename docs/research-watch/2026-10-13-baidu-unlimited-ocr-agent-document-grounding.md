# Research Watch: Baidu Unlimited-OCR — Agent Document Grounding via One-Shot Long-Horizon Parsing

- Repo: https://github.com/baidu/Unlimited-OCR (⭐27,278)
- Source: GitHub Trending Python (2026-10-13); released June 2026
- Stars: 27,278 (above 5k registry threshold, but below registry eligibility due to schema gap — see Status)

## Why this is worth watching
Baidu released Unlimited-OCR in June 2026 as a one-shot multi-page document parser that converts PDFs, scanned books, and dense technical documents into structured text in a single inference pass. The architectural choice — a fixed-size decoder cache using Reference Sliding Window Attention (R-SWA) — means memory does not grow with document length. This is distinct from the standard approach (chunked OCR + reassembly) and addresses a specific failure mode for agents: document grounding that loses cross-page structure (tables, formulas, footnotes) when pages are processed independently. As of October 2026 it is trending again on GitHub Python, suggesting ongoing developer interest after initial June launch.

## What stands out immediately
- **Architecture:** 3B parameters, ~500M active (MoE decoder); vision encoder + mixture-of-experts decoder; built on DeepSeek-OCR backbone
- **Memory behavior:** R-SWA with 128-token default window; fixed memory footprint across document length — this is the key architectural claim, enabling parsing of 40+ page PDFs without OOM on modest hardware
- **Benchmarks:** 93.92% on OmniDocBench v1.6 (immers.cloud; not independently verified against Baidu's own published materials)
- **License:** MIT — no licensing restriction for commercial use
- **Deployment:** Hugging Face Transformers, vLLM, and SGLang supported; two modes: `gundam` for single images, `base` for multi-page PDFs
- **Agent integration pathway:** Mixpeek documents a use case where agents receive faithful structured text rather than raw page images — reducing the vision-model overhead on the agent's own context window
- **Caveat on viral claims:** "100-page PDF in one shot" claims circulating on social media exceed Baidu's own tested range (~40+ pages); treat single-shot 100-page claims skeptically

## Why clawfit should care
- The current clawfit L4 capability layer has no tracked tool for "long-horizon document parsing as agent grounding" — there are retrieval/RAG systems, but not a dedicated one-shot parser that preserves cross-page structure
- This is a concrete second signal for L4 tools that improve document-grounded reasoning (first was headroomlabs/headroom 2026-10-09, which focused on context compression; Unlimited-OCR focuses on faithful initial extraction)
- For `primary_task: qa` or `primary_task: research` profiles handling technical documents (legal, scientific, financial), a pre-processing step with Unlimited-OCR could reduce hallucination on table and formula content that current chunked-OCR pipelines mishandle
- The vLLM + SGLang deployment path means it can run alongside existing inference stacks used in the clawfit `hardware: cloud` tier without new infrastructure investment
- 27k stars and four-month persistence on trending suggests genuine developer adoption, not a one-day spike

## Preliminary interpretation
Current best reading:
- **Level 4 primary — Capabilities / Document Grounding** (dedicated document parsing capability for agent pipelines)
- **Level 1 secondary** — it is a deployable model, but its primary use case is as a preprocessing tool for agent document tasks, not a base LLM for generation

This is not a general-purpose OCR tool. The MoE architecture and fixed-cache design are specifically optimized for the agent pipeline use case: extract structured content faithfully once, before the agent's context window fills. It is architecturally distinct from existing OCR-as-service tools (Tesseract, Google Document AI) in that it is designed to be agent-callable and runs in the same inference-stack ecosystem (vLLM, SGLang).

## Claims to verify
- 93.92% OmniDocBench v1.6 score: sourced from immers.cloud and not independently confirmed against Baidu's own published paper or benchmark leaderboard
- Parameter count (3B vs. 4B) conflicts across sources; likely 3B total with ~500M active per MoE forward pass
- Fixed memory behavior ("doesn't grow with output length") is an architectural claim based on R-SWA; actual GPU memory behavior for edge cases (dense formula pages, long tables) needs independent testing
- Release date: June 19–22, 2026 (two sources disagree on exact date within the same week)

## Status
- Above 5k star threshold (27,278★), MIT license, vLLM/SGLang deployment confirmed
- Registry eligibility gap: `agents.json` has no schema for document preprocessing tools; `llms.json` has no `use_case: document-grounding` type field
- Schema watch: `task_type: [generation | classification | embedding | document-parsing]`; `context_mode: [standard | fixed-cache | sliding-window]`; `supported_formats: [pdf | image | html | ...]`
- Monitor: whether Baidu publishes a formal paper with benchmarks; whether a third-party reproduces the OmniDocBench score; whether an MCP server wrapper emerges for direct agent integration
