# Research Watch: Laminar — Agent Observability and Silent Failure Detection

- Repo/Link: https://github.com/lmnr-ai/lmnr (Apache 2.0, ~3,100 stars)
- Source: Hacker News Show HN (23 points, 2026-10-19)
- Funding: $3M seed, March 2026, led by Atlantic.vc (YC S24)

## Why this is worth watching
Laminar is an open-source observability platform specifically for AI agents, targeting what the founders call "silent failures" — agent runs that complete without errors but produce wrong outcomes. The product combines OpenTelemetry-native tracing with a "Signals" feature where users describe desired behaviors in plain language, and Laminar backfills those structured events across historical traces. At 3.1k stars and with Browser Use shipping it as the default observability option in their documentation, it has real adoption beyond YC-network usage.

## What stands out immediately
- OpenTelemetry-native tracing — agents emit standard OTEL spans; no custom SDK required for basic integration
- "Signals" feature extracts structured events from plain-language outcome descriptions and applies them retroactively to historical traces
- Replay-style debugger allows re-running from a specific agent decision point — useful for tight iteration loops
- SQL access to trace data — teams can run ad-hoc queries on agent behavior without leaving the tool
- Agent graph view (currently beta) visualizes the decision structure of multi-step agent runs
- Browser Use lists Laminar as its default observability option — a Tier-2 adoption signal
- $3M seed raised; founding team background in agent infrastructure
- ~3,100 stars; small but growing within a nascent observability subcategory

## Why clawfit should care
clawfit currently has no observability dimension in its scoring or registry. A recommendation engine that places agents in production workflows cannot ignore whether those agents have observable behavior. Laminar is the first standalone agent-observability platform with meaningful adoption and open-source availability. This is a L5 signal worth tracking because: (a) harnesses that bundle observability (e.g., as a default integration) will score differently on `setup_complexity` and `debugging_surface`, and (b) if clawfit ever adds a `debuggability` dimension to org_fit scoring, Laminar would be the reference implementation to calibrate against.

## Preliminary interpretation
Current best reading:
- **Level 5 — Memory / Observability / Evaluation**: core function is tracing and debugging agent behavior in production; overlaps with eval infrastructure (online evals) but the primary use case is run-level observability rather than benchmark evaluation.

## Claims to verify
- Whether the Signals backfilling feature is deterministic or uses LLM calls internally (affects cost and reliability)
- Whether OTEL compatibility covers all major agent frameworks (LangGraph, OpenHands, Claude Code) or requires per-framework shims
- Browser Use adoption claim: verify in the official Browser Use docs (not Laminar's own claims)
- Whether the replay-style debugger works for stateful long-running agents (not just single-turn)

## Status
- ~3,100 stars — below 5,000 registry threshold; not a registry candidate now
- Apache 2.0 license; actively maintained
- First standalone L5 agent-observability signal with cross-framework adoption evidence
- Watch for: second major harness adopting Laminar as default; would trigger two-signal rule for an "agent observability" subcategory update to reference-levels.md
