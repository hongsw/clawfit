# Research Watch: Future AGI — Closed-Loop Agent Evaluation and Simulation Platform

- Repo: https://github.com/future-agi/future-agi (⭐1,300)
- Source: Web search / GitHub (2026-07-07)

## Why this is worth watching

Future AGI is an open-source, self-hostable platform that consolidates five functions into one system: multi-turn simulation, evaluation (50+ metrics), guardrails (18 built-in scanners + 15 vendor adapters), monitoring (OpenTelemetry-native), and prompt optimization. The integrated architecture contrasts with the fragmented approach of stitching together Langfuse (monitoring), separate eval frameworks, and separate guardrail libraries. The novel element is the closed feedback loop: production traces feed six prompt-optimization algorithms that autonomously rewrite prompts to resolve systematic failures — closer in spirit to the "Loop 4 Hill Climbing" pattern (tracked 2026-07-05 Art of Loop Engineering) than to passive observability tools. At 1,300★ this is well below the 5k registry threshold, but the functional scope and Apache 2.0 self-hostable stance make it a qualifying signal for L5 tracking.

## What stands out immediately

- **Multi-turn simulation** including voice agent scenarios — the only tracked L5 tool in this series that generates synthetic multi-turn test cases, not just evaluates production traces
- 50+ evaluation metrics combining LLM-as-judge, heuristic rules, and ML approaches in a single system — metric diversity is higher than typical eval-only frameworks
- 18 built-in guardrail scanners + 15 vendor adapters (Lakera, Presidio, Llama Guard) — guardrails are integrated, not a bolt-on; competes with Claw Patrol (tracked 2026-06-01, prompt injection firewall) at L5
- Six prompt-optimization algorithms that consume production traces to generate improved prompts automatically — this is active self-improvement, not passive monitoring
- OpenAI-compatible gateway routing 100+ providers — LLM gateway bundled with eval/observability (unusual; Langfuse does not do this)
- OpenTelemetry-native span ingestion across 50+ frameworks — standard integration surface, not a proprietary SDK requirement
- ~29k req/s throughput at P99 ≤21ms with guardrails enabled (on t3.xlarge) — claimed production-grade performance
- v0.5.10 (June 23, 2026), Apache 2.0 — maintained, self-hostable, no vendor lock-in
- Python (Django + Channels) + Go (gateway) + React frontend — production-grade multi-language architecture

## Why clawfit should care

clawfit's current L5 landscape includes Langfuse (observability-only, established), Claw Patrol (prompt injection defense, tracked Jun 2026), and microsoft/agent-governance-toolkit (policy enforcement, tracked Jul 2026). Future AGI occupies a different position: it is the first tracked L5 tool that closes the loop from monitoring → evaluation → prompt optimization without human intervention between steps. The "prompt optimization from traces" capability is the closest open-source equivalent to the behavior described in Art of Loop Engineering's Loop 4 (2026-07-05) — where harness configuration rewrites itself from production trace analysis. If this pattern validates at production scale, it introduces a new dimension for scoring: `self_improving: true` harnesses may warrant a reliability score uplift in long-running `statefulness: session` or `statefulness: persistent` profiles. The voice agent simulation scope also expands the relevance of this tool to the tracking voice cluster (Meetily, speech-to-speech, pocket-tts tracked today).

## Preliminary interpretation

Current best reading:
- **Level 5 primary — Memory / evaluation / observability**: Future AGI's core functions are all L5 — trace collection, evaluation, simulation, and guardrails are all directed at agent reliability and improvement
- **Level 2 secondary weak — Harness/wrapper**: the LLM gateway and prompt-optimization output could be used as a thin harness wrapper around model calls, but this is not the primary use pattern

First signal for "closed-loop simulation-to-optimization" as an L5 sub-type — distinct from:
- Passive observability (Langfuse: collects traces, no autonomous optimization)
- Prompt injection defense (Claw Patrol: filters adversarial input, no trace-based learning)
- Policy enforcement (agent-governance-toolkit: enforces rules, no trace-based rule revision)
The defining characteristic: production traces automatically generate improved prompt candidates without human authoring.

## Status

- 1,300★, v0.5.10 (June 23, 2026), Apache 2.0, Python 49.9% / JavaScript 42.1% / Go 6.2%
- Below 5k registry threshold (1.3k★); registry hold pending: threshold not met; `self_improving` field not in current schema; prompt-optimization effectiveness unverified by independent third parties
- ~29k req/s / P99 ≤21ms guardrail claim: measured on t3.xlarge under unspecified load profile; not independently benchmarked
- Schema watch: `self_improving: true/false` (candidate field for L5 tools and L2 harnesses that incorporate trace-based self-modification); `eval.simulation: true/false` (distinguishes simulation-capable tools from trace-only tools)
- Promotion criterion: 5k★ AND independent benchmark confirming trace-to-optimization pipeline reduces systematic failure rate on a documented agent task type
- Claims to verify: six prompt-optimization algorithms (names/methods not enumerated in available sources); 50+ metric count; Lakera/Presidio/Llama Guard adapter coverage confirmed in codebase
