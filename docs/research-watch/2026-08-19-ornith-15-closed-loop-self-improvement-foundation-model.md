# Research Watch: Ornith-1.5 — Closed-Loop Self-Improving Foundation Model

- Link: https://ornith.ai/ornith_1_5.html
- Prior signal: `docs/research-watch/2026-06-30-ornith-1-self-improving-agentic-coding.md` (511★ at tracking)
- Source: Hacker News (85 points, 2026-08-19)

## Why this is worth watching
Ornith-1.5 extends the self-scaffolding approach from Ornith-1.0 (tracked 2026-06-30) into a fully closed self-improvement loop: the model now generates its own training tasks, constructs task-specific scaffolds, and produces solution rollouts — all three stages under RL optimization simultaneously. This is architecturally distinct from fine-tuning on human-labeled data and from Ornith-1.0's dual-optimization (scaffold + trajectory only). If the closed-loop generalizes beyond controlled environments, it represents a qualitative shift in how L1 foundation models acquire capability.

## What stands out immediately
- Full three-stage closed loop: task generation → scaffold construction → solution rollouts, all jointly optimized via GRPO
- Reward signal integrates validity (well-formed tasks), frontier difficulty (target ~20% success rate), and novelty (distinct from prior tasks)
- Three scales shipped: 397B MoE, 35B MoE, 9B dense — MIT license
- "Models propose progressively harder tasks beyond current capabilities" — curriculum difficulty is self-determined, not human-curated
- Open-source with MIT license; vLLM/SGLang compatible (OpenAI-compatible API) as with Ornith-1.0
- 85 HN points on launch; Ornith-1.0 launched at 140 HN points — slightly lower velocity but builds on established signal

## Why clawfit should care
Ornith-1.0 introduced the hypothesis that L1 models could blur into L2 by absorbing scaffold responsibility. Ornith-1.5 strengthens this: the model now generates its own training curriculum, which overlaps with L5 (evaluation / self-improvement). If the pattern proliferates, clawfit's current architecture assumes clean separation between (L1 model) and (L2 harness) choices — Ornith-1.5 challenges that boundary more forcefully than any prior signal. The `self_scaffolding` capability flag noted as a future gap in the 2026-06-30 doc becomes more urgent.

## Preliminary interpretation
- **Level 1 — Base Agent Runtime** (primary; foundation model serving as its own curriculum generator)
- **Level 5 — Evaluation / Self-Improvement** (secondary; closed-loop RL training from self-generated tasks)
- The L1/L5 boundary collapse is the architecturally interesting element, not just the performance

## Claims to verify
- Benchmark SOTA claims: "state-of-the-art among open-source models" — no specific leaderboard positions listed; need SWE-Bench, Terminal-Bench numbers to compare with Ornith-1.0 and contemporaries
- Closed-loop generalization: self-generated curriculum may overfit to distribution of initial tasks; no out-of-distribution generalization results cited
- Task novelty scoring: "distinct from prior tasks" claim requires operational definition of task distance
- Scale efficiency: whether 9B dense reaches competitive agentic performance vs larger open-source models not stated

## Status
- Second signal for Ornith (first: 2026-06-30, Ornith-1.0 at 511★). Registry eligibility: blocked pending public GitHub star count and deterministic cost/latency data. The closed-loop self-improvement pattern now has two time-separated observations from the same project — trend is consistent. Two-signal rule for taxonomy promotion not met (Ornith is a single project; would need a second independent model with closed-loop self-improvement to promote a sub-type).
