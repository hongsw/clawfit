# Research Watch: Agent S — Generalist-Specialist Computer-Use Framework

- Repo: https://github.com/simular-ai/Agent-S (⭐12,550)
- Source: GitHub Trending weekly; three accepted papers (ICLR 2025, COLM 2025, TMLR 2026)

## Why this is worth watching
Agent S is a three-generation open-source computer-use framework from Simular AI that has consistently advanced the OSWorld benchmark: from 66.0% with S3 alone to 72.6% with Behavior Best-of-N sampling — the first published result exceeding reported human-level performance (~72%) on that benchmark. The production-deployed variant (Sai, sai.work) reported 73% on OSWorld 2.0 in August 2026, beating GPT-5.6 Sol's 62.57% at lower cost. The trajectory is notable because it corresponds to concrete architectural choices (dual-model split, open-weight grounding) rather than scaling alone.

## What stands out immediately
- **Dual-model architecture**: a large reasoning LLM (planning/decision) paired with a specialist grounding model (UI-TARS-1.5-7B or 72B) that translates decisions into pixel coordinates and PyAutoGUI actions — avoids routing both perception and strategy through one model
- **Behavior Best-of-N (bBoN)**: samples N full trajectories and selects the best via a learned behavior scorer; boosts OSWorld from 66.0% to 72.6%; distinct from token-level sampling, closer to parallel-agent selection
- **Cross-platform zero-shot transfer**: same S3 agent transfers from OSWorld (Linux) to WindowsAgentArena (50.2% → 56.6% w/ BoN) and AndroidWorld (68.1% → 71.6%) without platform-specific tuning
- **Hybrid GUI + code execution**: `call_code_agent` lets the agent switch from GUI clicks to Python/Bash for data-manipulation tasks — avoids forcing everything through visual grounding
- **Open-weight grounding dependency**: relies on ByteDance UI-TARS family, not proprietary vision APIs; reduces per-call cost and latency vs. Claude Computer Use or GPT-5 vision
- **Apache 2.0 license**: permissive; `pip install gui-agents`
- **Three generations in one repo**: S1 (Oct 2024, ICLR 2025 best-paper workshop), S2 (Mar 2025, COLM 2025), S3 (Oct 2025, TMLR 2026)
- Requires Go 1.25+ — no, sorry: Python runtime with OpenAI/Anthropic/Gemini/vLLM backend; model-agnostic

## Why clawfit should care
clawfit currently maps computer-use at L6 without differentiating single-model vs. dual-model (planning/grounding) architectures. Agent S's performance trajectory suggests the grounding model selection is a first-class variable — the same planning LLM produces materially different results depending on the grounding model. This is not currently represented in the registry. Additionally, the Behavior Best-of-N finding implies that a `parallel_rollouts` capability axis matters for computer-use tasks, distinct from the `latency` and `budget` dimensions already in the scoring model.

## Preliminary interpretation
- **L6 — Human Interface / Computer-Use** (primary): directly drives mouse, keyboard, and scroll on real desktop and web GUIs
- **L7 — Inference / Execution Infrastructure** (secondary): grounding model inference is a separable inference pipeline, not just a call to a frontier model

## Claims to verify
- 72.6% OSWorld claim: from S3 paper (arXiv 2510.02250, TMLR 2026 accepted) using bBoN + UI-TARS-72B; the 100-step evaluation protocol and task set matter for comparison validity — confirm the baseline is identical across competing systems
- "First to exceed human performance" framing: depends on the human-level reference number (~72% from OSWorld paper); human baselines vary by evaluator pool and time budget
- 73% on OSWorld 2.0 (Sai, production, August 2026): self-reported by Simular; OSWorld 2.0 evaluation protocol may differ from original OSWorld; confirm protocol equivalence before treating as a direct improvement
- GPT-5.6 Sol comparison (62.57%): OpenAI-reported on their eval; cross-org benchmark comparisons require identical task sets and step limits to be meaningful

## Status
- Three peer-reviewed papers; TMLR 2026 is the current generation
- Created October 2024; active as of September 2026 (last push)
- No registry entry warranted yet: computer-use framework, not a deployable LLM or agent harness in the clawfit registry sense; grounding model inference costs are not publicly standardized
- **First dedicated signal for "dual planning+grounding architecture for general-purpose computer-use"** in clawfit's research-watch corpus
- Monitor Sai (sai.work) for a billable hosted service with published latency/cost data that could qualify for a registry entry
