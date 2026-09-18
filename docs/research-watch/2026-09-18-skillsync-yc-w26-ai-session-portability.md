# Research Watch: Skillsync (YC W26) — AI Session Portability

- Repo/Link: (URL not extracted from HN — launch post only)
- Source: Hacker News — "Launch HN: Skillsync (YC W26) – AI chat sessions made portable across agents" (41 pts, 46 comments, 2026-09-18)

## Why this is worth watching
Skillsync makes AI chat sessions portable across different agents and providers, letting users resume a conversation started in Claude Code in Cursor, or from one provider to another, without losing context. YC W26 (current batch) signals funding and near-term distribution. This directly addresses the statefulness/portability axis that the registry currently only models as `statefulness: [stateless | session | persistent]`.

## What stands out immediately
- Cross-agent session portability — not just within one provider
- YC W26 batch; HN launch with meaningful discussion (46 comments)
- No open-source repo found; appears to be a hosted service
- Complements but differs from Salesforce AgentScript's `statefulness: persistent` (2026-09-15) — that's persistence within one agent runtime; this is portability across runtimes

## Why clawfit should care
The current `statefulness` field models longevity within a single agent; it does not model cross-agent or cross-provider handoff. Skillsync is the first tracked tool whose PRIMARY purpose is inter-agent session handoff. A `portability_model: [isolated | exportable | cross-agent]` axis would let clawfit recommend Skillsync (or similar) for teams who switch between agents mid-project. Relevant to `team_size: large` profiles with heterogeneous AI tool stacks.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness/wrapper layer** (session state management across agent runtimes), with L3 secondary (governance of session continuity)

## Status
- Monitoring — hosted service, no public pricing confirmed; revisit when repo or pricing page surfaces
- Cross-reference: KiroCrew daemon persistence (2026-09-14), AWS pizza-bot background inbox (2026-09-15)
