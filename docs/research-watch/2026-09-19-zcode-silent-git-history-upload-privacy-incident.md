# Research Watch: ZCode — Silent Git History Upload Privacy Incident

- Repo/Link: https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/
- Source: Hacker News (247 pts, 89 comments)

## Why this is worth watching
ZCode (tracked 2026-07-02 as China-native coding agent built on GLM-5.2) was found to silently upload users' full git workspace history to Zhipu AI cloud infrastructure. Forensic analysis by blogger `ferstar` found workspace snapshot uploads triggered on session open, auto-save events, and background sync — without explicit user consent. This is the first confirmed privacy incident for a tracked L1 coding agent.

## What stands out immediately
- Uploads happened on session open and without user interaction
- Full git history (not just active files) was transmitted
- Upload destination: Zhipu AI cloud servers (Z.ai infrastructure)
- No clear disclosure in ZCode's terms of service at time of incident
- HN 247 pts, 89 comments — significant community reaction, not a niche finding
- ZCode's free tier may have used workspace data for model training (unconfirmed)

## Why clawfit should care
clawfit currently scores `data_sensitivity: confidential` and `governance_need: hard` profiles against `network: offline` tools. ZCode is classified `network: online`. This incident confirms that `network: online` coding agents can have undisclosed telemetry behaviors that violate `data_sensitivity: confidential` requirements. The existing `containment_level` axis candidate (from rubyhack.ai 2026-09-12 + collusion.wiki canonical pattern) now has a concrete corporate-product precedent alongside autonomous-agent incidents. This is the first signal where a *commercial coding agent product* (not a rogue agent) silently transmitted data — raising the governance bar for all online coding agents in the registry.

## Preliminary interpretation
Current best reading:
- **Level 3 — Orchestration / Governance** (primary): governance failure in a commercial harness
- **Level 1 — Base Runtime** (secondary): impacts L1 scoring for ZCode

## Status
- Incident confirmed; ZCode tracked (2026-07-02)
- No patch or disclosure statement from Zhipu AI found at scan time
- Strengthens case for `data_telemetry_disclosure: [none | partial | full]` registry field
- Second signal for "commercial product with undisclosed data exfiltration" pattern; prior signal was rubyhack.ai (supply-chain, autonomous agents); this is first commercial-product signal
