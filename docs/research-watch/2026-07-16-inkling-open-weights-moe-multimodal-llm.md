# Research Watch: Inkling — Thinking Machines Lab Open-Weights MoE LLM

- Repo/Link: https://thinkingmachines.ai/news/introducing-inkling/
- Source: Hacker News (583 points, 2026-07-16)

## Why this is worth watching
Inkling is a 975B-parameter MoE (41B active) open-weights model trained on 45 trillion tokens across text, images, audio, and video. With 583 HN points it is the highest-signal item on today's front page. It explicitly targets the "good base for customization" use case — not claiming top-tier benchmark performance, but offering open weights, a 1M token context window, and a fine-tuning platform (Tinker). The calibrated-uncertainty emphasis (forecasting, probability estimation) distinguishes it from instruction-following-first competitors.

## What stands out immediately
- 975B total / 41B active MoE — efficient active parameter budget at large scale
- 1M token context window — relevant for long-context agent loops and RAG
- Native multimodal: text, image, audio, video pretrain (not post-hoc adapters)
- Controllable thinking effort — dynamic compute scaling per request
- 30M+ RL rollouts for log-linear reasoning improvement
- Fine-tunable via Thinking Machines' Tinker platform; deployment partners listed
- Epistemics focus: calibrated uncertainty, not just accuracy maximization

## Why clawfit should care
Inkling is a candidate LLM backend for agent harnesses that currently list Claude or GPT-4. Its open-weights status means it is viable for `data_sensitivity: confidential` and `governance_need: hard` profiles that cannot use closed-API models. The 1M context window extends its fit for session-stateful agents. Multimodal pretrain positions it for voice/multimodal agent interfaces (L7). clawfit's LLM recommendation axis should eventually surface open-weights multimodal models as distinct from open-weights text-only models.

## Preliminary interpretation
Current best reading:
- **LLM layer** (not a harness or agent runtime — this is an inference backend)
- Closest existing tracked category: open-weights instruction-following LLM
- Secondary: multimodal agent backbone (L7 capability enabler)

## Status
- Tracking; no registry entry yet (pending: benchmark reproduction, deployment latency data, pricing on Tinker platform)
- Schema watch: `multimodal_pretrain: true/false`; `context_window_tokens`; `thinking_effort_control: true/false`
