# Research Watch: Runtime — Sandboxed Team Coding Agent Platform (YC P26)

- Repo: https://runtm.com (no public GitHub repo found as of 2026-05-22)
- Also see: Launch HN thread 2026-05-22; docs/research-watch/2026-04-11-twill-cloud-agent-delegation-yc.md; docs/research-watch/2026-04-07-freestyle-vm-sandboxes-coding-agents.md

## Why this is worth watching
Runtime is a YC P26 company (institutional validation, early stage) pitching team-wide sandboxed infrastructure for coding agents — not a new agent, but a managed platform that governs how existing agents (Claude Code, Cursor, Codex, Devin, Copilot, Gemini CLI) run inside an organization. The multi-agent compatibility claim and Slack/Linear/GitHub trigger integrations signal an explicit team-governance play rather than a solo-developer productivity tool. HN #12 at 59 pts suggests moderate but real signal on launch day.

## What stands out immediately
- Agnostic runtime: supports at least six named agents across three vendors — framed as infrastructure, not an agent product
- Trigger surface: Slack, Linear, GitHub as first-class dispatch points — team workflow integration, not CLI-first
- Real-time collaboration: watch mode and mid-session handoff are claims to inspect; no implementation detail is publicly verifiable without a repo
- Governance claims: live visibility into tool calls, chain of thought, and file changes — closer to an audit log than a guardrail
- "Saves ~9 months of infrastructure work" is a vendor-authored figure; no independent benchmark or case study available at launch
- No open-source component visible; proprietary managed service with no published pricing

## Why clawfit should care
Runtime directly targets the gap between solo-developer agent tools (L1 entries) and full enterprise governance stacks. Its team-dispatch-from-Slack model and cross-agent agnosticism make it a distinct topology from both Twill (async cloud PR delivery, L1-shaped) and Freestyle (raw VM substrate, L2-infrastructure). If the governance and observability claims hold, it would be the first entry in this taxonomy that combines L2 execution harness with L3 audit/visibility primitives as a unified managed service. That dual-layer collapse pattern is worth tracking regardless of eventual classification, because it maps directly to clawfit's `governance_need` filter axis.

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta wrapper / harness / orchestration layer** (primary: managed multi-agent execution harness for teams)
- **Level 3 secondary (weak)** — live tool-call and chain-of-thought visibility is L3-adjacent (governance/audit surface), but no SSOT, no behavioral spec, no sprint lifecycle is documented; not enough to claim L3 primary

Distinction from Twill (YC S25, L1 primary): Twill is an async PR-delivery service — the agent IS the product, output is a PR. Runtime treats agents as interchangeable workers; the platform is the product. Twill is L1 (managed cloud agent sub-type). Runtime is L2 (team execution harness). These do not overlap.

Distinction from Freestyle (L2 VM substrate): Freestyle provides raw VM infrastructure — no agent identity, no team dispatch, no governance surface. Runtime is one layer above: it assumes sandboxed execution is solved and adds agent routing, visibility, and team integration on top.

## Status
- New signal, early stage. YC P26 backing noted. No public repo, no independent benchmark. Hold for registry — revisit when pricing/docs are public or a case study surfaces. Flag: if the governance/observability surface matures, re-evaluate for L3 secondary promotion. "Sandboxed team agent platform" is a candidate sub-type under L2 not currently represented in the taxonomy.
