# Research Watch: HarnessRouter — Unified Harness Protocol Reference Implementation

- Repo: https://github.com/HarnessRouter/harnessrouter (⭐2,600)
- Source: Web search / GitHub Trending; multiple fork mirrors visible
- Latest release: v0.11.2 (August 29, 2026)
- License: Apache-2.0

## Why this is worth watching

HarnessRouter is a self-hosted router that runs Codex, Claude Code, Hermes, PI, DSH, and other coding agent harnesses through a single OpenAI-Responses-compatible API. It implements the Unified Harness Protocol (UHP — schema version `uhp-2026-08-11.openapi.yaml`), a publicly versioned open standard for harness execution semantics including harness selection, persistent sessions, files, cancellation, and harness-managed tools and skills. The fork pattern visible across multiple independent GitHub mirrors (codehornets, timothybrush, bhardwajRahul, aug2uag, hiro-nikaitou) suggests practitioners are actively evaluating and distributing this. 2,600 stars with 264 forks indicates traction beyond hobby use.

The co-signal here is **treg** (already tracked today, 2026-09-25): treg is "OpenRouter for agent tools" (tool-level routing), while HarnessRouter is routing at the harness/session level. These are two independent implementations of the same routing-abstraction idea applied at different layers of the stack. Two signals from different organizations on the same day constitute the two-signal condition for "agent routing with open protocol" as a named pattern.

## What stands out immediately

- Implements UHP, a versioned open protocol — not a proprietary API; other vendors can implement the same contract
- Deliberately uses OpenAI Responses API shape for UHP compatibility, enabling existing SDKs and streaming parsers to work with UHP servers
- Self-hosted, Apache-2.0 — operator controls keys and infrastructure; explicit "your keys, your infrastructure" framing
- Supports persistent sessions across harness boundaries — agents maintain state even when the underlying harness changes
- v0.11.2 indicates active development (not an abandoned prototype)
- Multiple fork mirrors across independent GitHub accounts suggest practitioners are active consumers, not just stargazers
- Starter kit templates for slides, sheets, dashboards, and video generation point toward enterprise document workflow use cases

## Why clawfit should care

clawfit currently models harnesses as discrete registry entries with fixed cost and latency. HarnessRouter changes this assumption: if a router sits between the user and the harness, the effective cost and latency depend on the routing decision, not a single harness identity. This introduces `routing_overhead` as a new axis candidate distinct from `latency: low/medium/high`.

The UHP protocol is the more strategically important signal: if UHP adoption grows, harness switching costs collapse and `setup_complexity` for multi-harness deployments drops significantly. clawfit's `network: online` and `statefulness: session` scoring would need to account for UHP-mediated sessions as a distinct deployment mode.

The "99.8% cost savings" claim (from the repo description) should be treated as marketing; the verified claim is that routing between harnesses based on task type is a real optimization surface — not that any single configuration saves that much.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/Wrapper Layer** (primary: harness routing and session abstraction)
- **Level 3 — Governance/Protocol Layer** (secondary: UHP as an open, versioned execution contract)

## Claims to verify

- Whether UHP is a one-company standard or has independent contributors/governance
- Actual latency overhead of routing through HarnessRouter vs. direct harness connection
- Whether session persistence is true agent state or just conversation replay
- Whether the "99.8% cost savings" refers to harness switching or per-task routing optimization

## Status

- Above 100-star threshold (2,600★); below 5k registry threshold
- v0.11.2 with active release cadence indicates this is not abandoned
- **Two-signal condition met** for "harness/tool routing with open protocol" (treg + HarnessRouter, same day, different layers); not yet a canonical sub-type (both signals arrived same day; need cross-day confirmation)
- Monitor for UHP adoption by additional vendors; if a second harness independently implements UHP, canonical L2/L3 sub-type promotion is warranted
