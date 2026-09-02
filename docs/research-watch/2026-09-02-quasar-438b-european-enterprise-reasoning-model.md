# Research Watch: Quasar 438B — European Enterprise Reasoning Model

- Repo/Link: https://multiversecomputing.com/resources/introducing-quasar-438b-europe-s-leading-ai-model
- API: https://dashboard.compactif.ai
- Source: Hacker News (137 points, 2026-09-02): "Quasar 438B: Europe's Leading AI Model"

## Why this is worth watching

Quasar 438B is Multiverse Computing's first 400B+ parameter model and, notably, targets enterprise coding agents and multi-step reasoning tasks rather than general chat. It is released via the CompactifAI API — not open-weight — and is explicitly positioned for software development agents, technical copilots, and research systems. The HN traction (137 points) and European provenance are both notable: 137 points on a model release is above typical reception for European labs, and EU-origin models carry distinct regulatory positioning under the AI Act that American-origin models do not.

## What stands out immediately

- **438B parameters**: the parameter count puts it in the same tier as Tencent Hy4-preview (770B/49B active), GLM-5.3 (744B), and similar frontier-tier models tracked recently — but as a dense model rather than MoE (architecture not confirmed in the announcement)
- **Intelligence Index score of 43** on Artificial Analysis Intelligence Index v4.1.1: a specific, externally validated benchmark score rather than self-reported; makes cross-model comparison possible without re-running evaluation
- **Terminal-Bench v2.1 score of 69.3**: directly targets the coding/terminal task type; this score is verifiable and specific to the agentic coding task category clawfit's registry covers
- **Long-context score 75.0 on AA-LCR evaluation**: relevant for `task: research` and `task: code-gen` use cases where large context windows reduce round-trip tool calls
- **Response speed**: 500 tokens in 15.3 seconds including reasoning — a specific latency figure, not a range; this maps to clawfit's `latency: high` category given that reasoning-model output is slower than standard completion
- **English + Spanish only**: language scope is narrower than most 400B+ models — relevant for European enterprise customers but limits addressable market globally
- **API-only, not open-weight**: deployment is through CompactifAI dashboard — no local deployment path; relevant for clawfit's `hardware: cloud` filter exclusively
- **No MoE architecture confirmed**: if dense (not confirmed), the inference cost profile differs materially from MoE models at similar parameter counts — cost estimates based on parameter count alone would be misleading

## Why clawfit should care

Quasar 438B is a potential `llms.json` registry candidate. The combination of a Terminal-Bench v2.1 score (69.3), an externally validated Intelligence Index score (43), and a specific latency figure (500 tokens / 15.3s) is the most complete set of independently verifiable data points seen for any new model released in recent scans. The current `llms.json` registry lacks any European-origin model entry; Quasar 438B would be the first.

The registry entry is blocked on two items: (1) per-token API pricing from dashboard.compactif.ai is not in the announcement and must be confirmed before a `cost` field can be set; (2) the model architecture (dense vs. MoE) is unconfirmed, which affects whether the latency figure (15.3s for 500 tokens including reasoning) represents an inference efficiency or a reasoning step overhead.

The EU-origin positioning under the AI Act introduces a possible future `compliance` schema dimension not currently in clawfit's registry — enterprise customers in regulated EU industries (finance, healthcare, public sector) may select models in part on regulatory alignment, not only on capability and cost.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base Runtimes / Foundation Models** (primary): Quasar 438B is a base reasoning model accessed via API; it provides the underlying inference capability for agent stacks rather than the orchestration or capability layer itself
- No secondary level: the announcement addresses the model only; no harness, tool, or skill layer is described

## Claims to verify

- Whether per-token pricing is available on dashboard.compactif.ai and whether it is comparable to frontier-tier models at similar capability levels (necessary for registry entry)
- Whether the model architecture is dense or MoE — the announcement uses "438B parameters" without specifying activated parameters, which would distinguish dense from MoE at inference time
- Whether the Intelligence Index score (43) and Terminal-Bench score (69.3) were run independently or commissioned by Multiverse Computing — Artificial Analysis benchmarks are typically independent but require confirmation for this model
- Whether the "500 tokens in 15.3 seconds including reasoning" latency figure represents median, p50, or a best-case measurement under low load
- Whether the English + Spanish scope reflects training data limitation or deliberate product positioning, and whether additional language support is planned

## Status

- Potential registry candidate (llms.json) blocked on confirmed per-token pricing and architecture confirmation
- First European-origin 400B+ model in this research-watch log
- If pricing is confirmed and architecture resolves to a single cost profile, this warrants a `llms.json` entry as: `task: [code-gen, qa, research]`, `latency: high` (reasoning overhead), `hardware: cloud`, `weights: proprietary`
- Watch: CompactifAI API pricing page; independent replication of Terminal-Bench v2.1 score; whether EU AI Act compliance claim is formally documented
