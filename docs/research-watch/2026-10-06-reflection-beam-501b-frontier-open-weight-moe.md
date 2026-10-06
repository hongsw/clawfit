# Research Watch: Reflection Beam — 501B Open-Weight MoE for Agentic Coding

- Repo/Link: https://reflection.ai/blog/introducing-beam
- Source: Hacker News (277 pts, 73 comments)

## Why this is worth watching
Reflection AI's Beam is a 501B sparse MoE model with 23B active parameters, releasing under Apache 2.0 later in October 2026. It posts SWE Bench Pro v2-Hard at 77.2% and MCP Atlas at 78.7%, putting it at frontier-class on coding and tool-use benchmarks while claiming 3–4× less inference compute than comparable models. This is the first open-weight model explicitly benchmarked on MCP Atlas.

## What stands out immediately
- 501B total / 23B active MoE — larger active count than the ~3B-active tier (Kolibri, Solar Mini 4) but still inference-efficient relative to total size
- 256K context, extended to 1M via midtraining
- Apache 2.0 weights (releasing Oct 2026) — broadest permissive license tier
- TerminalBench v2.1: 80.1 and MCP Atlas: 78.7 both directly measure agent workflow performance
- "Controllable reasoning effort" to balance response length vs. compute cost

## Why clawfit should care
Beam adds a new point on the open-weight capability frontier: 23B-active-parameter MoE at frontier coding performance. The MCP Atlas benchmark score is directly relevant to clawfit's `network: online` tool scoring. When weights drop, it could become a legitimate self-hosted alternative to frontier API models for `data_sensitivity: confidential` or `governance_need: hard` orgs. Also relevant as a second signal for "frontier-class open-weight model scoring on MCP tool-use benchmarks."

## Preliminary interpretation
Current best reading:
- **Level 1 — Base Agent Runtime / LLM** (primary)

## Status
- New signal 2026-10-06 — weights not yet released, Apache 2.0 pending; benchmarks self-reported; monitoring for third-party evals and weight release confirmation
