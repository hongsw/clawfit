# Research Watch: Microsoft Decision-1 — Fast Decision Model for Agent Control

- Repo/Link: https://commandline.microsoft.com/microsoft-decision-1-model-foundry/
- Source: Hacker News front page (125 pts, 48 comments)

## Why this is worth watching
Microsoft has entered the structured decision model space — explicitly targeting agent control — with a post-trained Qwen3.5-9B at $0.042/M input tokens (output free). This is the **eighth+ cross-date signal** for the Jev/typed-decision-model pattern that has been building since 2026-09-16 (TypeSafe Jev → OpenJev → ConvAI RL-NAR → Kev → JevBench → agent-jev → Ollaya → OpenAI Decisions API → now Microsoft Decision-1). Microsoft's entry confirms this pattern as a stable architectural primitive warranting first-party support from major platforms.

## What stands out immediately
- **Architecture**: post-trained Qwen3.5-9B for single-pass calibrated probability output; open base model means the architecture is reproducible
- **Output format**: structured options (yes/no, multiple-choice, rubric-based) with calibrated probabilities, not free-form text
- **Agent control use cases**: routing, verification, workflow step approval/rejection, incident triage, safety screening, AI response judging
- **Availability**: Microsoft Foundry + OpenRouter — immediate commodity access, no private API waitlist
- **Pricing**: $0.042/M input, output free — order-of-magnitude cheaper than a standard LLM call for classification tasks

## Why clawfit should care
This confirms the two-tier architecture pattern at the action layer: a full LLM for generation, a decision model for routing/verification. clawfit's `tasks` field currently assumes all agent inference uses full LLM calls; tools that swap LLM calls for Decision-1 style models at branching points will have materially different latency and cost profiles than a naive single-model estimate. The `governance_need: hard` profiles (offline_mid_codegen) already score decision model runtimes (Ollaya) highly; Decision-1 via OpenRouter may score similarly for online + hard-governance profiles.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base LLM runtime (decision model sub-type)** — single-purpose structured output model hosted on commodity provider infrastructure
- **Level 5 secondary** — evaluator/judge use case (rubric scoring of agent actions)

## Status
- Eighth+ signal for the Jev/decision-model pattern — **pattern is now mainstream, not niche**
- Registry candidate: could be added to `clawfit/registry/llms.json` as a decision-model LLM entry with `task_type: decision`, `latency: low`, `cost_per_1m_input: 0.042`, `cost_per_1m_output: 0`
- Two-signal rule note: OpenAI Decisions API (2026-09-30) + Microsoft Decision-1 (today) = **two first-party platform entries in 10 days** — sufficient for a canonical sub-section addition at L1 describing "decision model sub-type" if a third platform entry arrives
