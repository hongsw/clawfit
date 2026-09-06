# Research Watch: OpenMed — Local-First Healthcare AI with MCP Server and 2,200+ Medical Models

- Repo: https://github.com/maziyarpanahi/openmed (⭐5.2k)
- HuggingFace org: https://huggingface.co/OpenMed (398M+ downloads)
- Source: GitHub Trending Python (2026-09-06); #1 most-referenced org in HF State of Open Source report (Spring 2026)

## Why this is worth watching

OpenMed is the largest open-source medical AI collection, built local-first from July 2025 by a single engineer and now at 5.2k GitHub stars, 2,200+ models on Hugging Face, and 398M+ downloads. The core design decision is a hard data-locality guarantee: clinical data, PII, and patient records never leave the device. This is not a cost-optimization choice — it is a compliance requirement framing (HIPAA, GDPR) that shapes the entire architecture. The project ships an MCP server, a FastAPI REST service, a Python SDK, and native mobile bindings — making it callable from within any MCP-compatible coding agent without custom integration.

The significance for clawfit is not that healthcare AI exists, but that OpenMed is the first L1 tool in this log that is explicitly designed around a regulatory data-sensitivity constraint (`data_sensitivity: hipaa`) as its primary architectural driver, and that it deploys as a local inference layer with agent-accessible API surfaces. v2.3.0 is the current release; the project has grown from 0 to 5.2k stars in ~14 months, with 4,092 commits.

## What stands out immediately

- **HIPAA-first architecture**: all 2,200+ models run on-device; no patient data leaves the network; this is the founding constraint, not a feature
- **MCP server shipped**: medical analysis and PII de-identification are exposed as callable MCP tools; any Claude Code or MCP-compatible agent can call them without custom code
- **FastAPI REST service**: `/analyze`, `/pii/extract`, `/pii/deidentify` endpoints; self-hosted at localhost; OpenAI-compatible interface possible
- **Cross-platform inference**: Python SDK, iOS/Swift via OpenMedKit, Android/Kotlin via ONNX Runtime Mobile, browser via Transformers.js — same models across every deployment surface
- **21 languages, 33 PII routes**: clinical NER, pharmaceutical identification, disease detection, anatomy recognition, genetic analysis — specialty coverage is broad, not just NER on English text
- **Trained on Huawei Ascend / MLX (Apple Silicon)**: hardware-diverse training pipeline; models are quantized and validated across NVIDIA, Apple, mobile, browser runtimes
- **#1 HF State of Open Source (Spring 2026)**: most-referenced medical AI organization; ecosystem recognition, not self-reported

## Why clawfit should care

1. **`data_sensitivity` schema gap, now the most concrete signal yet**: prior signals (collusion.wiki 2026-09-04, HIPAA framing in IBM Bob 2026-09-04) mentioned data sensitivity as a concern; OpenMed is the first tool where HIPAA compliance is the design driver for local inference, not a side effect. A `data_sensitivity: [none | internal | confidential | hipaa | gdpr]` field in the registry schema would let clawfit surface OpenMed over cloud-API alternatives when a user profile includes healthcare or regulated-data workflows.

2. **`task` gap — medical NER and de-identification are not in the current taxonomy**: current task categories (code-gen, qa, documentation, planning, research) don't include clinical NLP tasks. OpenMed confirms this category is real, scalable, and has production tools.

3. **MCP server as registry entry pattern**: OpenMed packages specialist models as MCP tools callable from coding agents. The pattern (local specialist AI + MCP exposure) could justify a new registry entry type: a locally-deployed MCP skill-pack rather than a base agent or LLM.

4. **Registry candidate (borderline)**: 5.2k stars above the 5k threshold; however, OpenMed is not an agent, harness, or general-purpose LLM — it is a specialist model collection. No per-token API pricing exists (local inference, hardware-dependent). Registry entry deferred until schema can represent specialist-domain model packs with local-only pricing.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base Runtime / Inference Layer (primary)**: OpenMed is a collection of locally-deployed specialist models serving clinical NLP workloads; the inference happens on-device via MLX, ONNX, Transformers.js, or Ollama-compatible runtimes
- **Level 4 — Capabilities / Skills / MCP (secondary)**: the MCP server exposes the specialist models as callable agent tools; from an agent's perspective, OpenMed is a skill/capability layer for clinical analysis

## Claims to verify

- Whether the "2,200+ models" metric reflects distinct fine-tuned variants (different specialties/languages) or includes GGUF/ONNX quantization variants of the same base models — the distinction matters for evaluating actual coverage breadth
- Whether the MCP server handles multi-turn clinical conversations or is single-call only
- Whether the HIPAA guarantee holds under all deployment configurations (FastAPI REST service in a Docker container with network access could leak data if misconfigured)
- Whether v2.3.0 benchmarks against clinical NLP baselines (e.g., BigBIO, MedMCQA, ClinicalNLP evaluations) or only on the project's own test sets
- Whether Huawei Ascend training history creates export-control considerations for US/EU healthcare deployments

## Status

- 5.2k stars, above research-watch threshold (100★) and above registry threshold (5k★)
- Not eligible for current registry schema: no general-purpose agent task type, no deterministic per-token API pricing (local-only), no `data_sensitivity` schema field
- **Two-signal building pattern — compliance-justified local inference (same scan today):** OpenMed (HIPAA healthcare) + METATRON (security air-gap, today) are two same-day signals that both argue for local inference on compliance/regulatory grounds rather than cost or offline-availability grounds. This compliance motivation is distinct from prior local inference signals (FreeToken, AirLLM, waste-nvme, WebLLM). Pattern noted; no canonical section change — two signals confirm the sub-type motivation but the registry schema needs `data_sensitivity` before it becomes actionable.
- Watch: whether OpenMed releases an API tier with metered pricing; whether v3.0 expands to reasoning-capable clinical agents (not just NER/PII)
