# Research Watch: heretic — Automated LLM Alignment Removal via Directional Ablation

- Repo: https://github.com/p-e-w/heretic (⭐33,000)
- Source: GitHub Trending Python (2026-10-03)

## Why this is worth watching

heretic is a Python tool that removes safety alignment constraints from local transformer-based language models without retraining. The technique — directional ablation combined with TPE-based parameter optimization — modifies the model weights directly by orthogonalizing transformer component matrices with respect to "refusal direction" vectors computed from pairs of refusal vs. non-refusal examples. The result is a modified model that suppresses refusal behavior while attempting to preserve general language quality (measured via KL divergence from the original). At 33k GitHub stars, this is not a fringe research artifact: it has mainstream developer traction. It signals a maturing ecosystem of local-model modification tooling that operates below the harness layer, directly in weight space, with no special hardware or training pipeline required.

## What stands out immediately

- **Automatic ablation without ML expertise**: the tool computes refusal directions, runs TPE hyperparameter optimization, and produces a modified model file automatically — no transformer internals knowledge required from the user
- **Multi-architecture support**: dense models, multimodal models, MoE architectures, and hybrid models (explicitly tested on Qwen3.5) — broad applicability across the current local model landscape
- **Lower KL divergence than manual abliteration**: reported Gemma-3-12B result shows KL 0.16 vs. 1.04 for manual methods — the optimization step produces demonstrably better quality preservation than hand-tuned ablation
- **AGPL-3.0 license**: copyleft with network use clause; commercial use in a SaaS product would require open-sourcing the service; this limits enterprise adoption but does not restrict personal or research use
- **Python 3.10+ requirement only**: no specialized ML training infrastructure needed; runs locally on the same hardware used for inference
- **204 commits, 2025–2026 development**: actively maintained; not a one-shot academic release
- **33k stars across trending period**: adoption signal is real, not concentrated in a single viral day; this category of tool has stable developer interest

## Why clawfit should care

clawfit's recommendation engine assumes that model behavior matches its advertised capabilities and alignment posture. heretic represents a structural signal that local model deployments can deviate from the alignment properties of their original training at negligible cost and with no special access. This affects clawfit's L1 recommendations in two ways: (1) the "local" hardware path now includes an active weight-modification ecosystem that changes what a `hardware: local` deployment actually delivers vs. what the model card describes; (2) security-sensitive `task` profiles (code review, data access, qa) that assume model-side guardrails may be miscalibrated when recommending models for self-hosted deployments. Neither effect is a reason to exclude local models from recommendations, but both are reasons to track the alignment-removal tooling layer as a distinct L1 ecosystem signal — parallel to the quantization tooling tracked under inference-runtime-substrate.md.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base Runtime / LLM Modification Tooling** (primary)
- Secondary: none — operates at the weight layer, below harness or capability

This is the same layer as llama.cpp and GGUF quantizers: tools that transform model files before or during inference. heretic adds a third category alongside quantization (compression) and fine-tuning (additional training): targeted behavioral modification without any training gradient. It is not an agent harness, skill, or capability layer.

## Claims to verify

- Whether the KL divergence improvement over manual abliteration holds across model families beyond Gemma-3 (the one published benchmark)
- Whether the suppression effect is robust on system-prompt-based safety layers (which are harness-side) vs. alignment trained into weights
- Whether there are any model families where the technique demonstrably fails (important for clawfit's local model coverage)
- AGPL-3.0 implications for organizations embedding heretic output in commercial products
- Whether the 33k stars are concentrated in alignment-bypass use cases or include genuine security research use (the distinction matters for ecosystem position)

## Status

- NOT in clawfit registry: weight-modification tool, not an agent/LLM/hardware entry; no inference cost profile applicable
- First tracked signal for "automatic local LLM alignment removal via directional ablation and parameter optimization"
- 33k GitHub stars; trending actively on Python leaderboard October 3, 2026
- Monitoring for multi-architecture coverage reports and security research adoption patterns
