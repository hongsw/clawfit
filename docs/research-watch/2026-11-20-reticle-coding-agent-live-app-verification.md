# Research Watch: Reticle — Coding Agent Live App Verification

- Repo/Link: https://github.com/reticlehq/reticle
- Source: GeekNews front page

## Why this is worth watching
Reticle is a tool that lets coding agents verify their own output by directly operating a web or desktop app: clicking buttons, filling inputs, checking that login or payment flows work as intended. This is structurally different from computer-use (generic UI automation) — it is specifically a post-generation verification step closing the loop between code change and observable feature correctness.

## What stands out immediately
- Agents drive real browser/desktop UI to confirm that features work end-to-end
- Positioned as a verification harness complement to coding agents, not a replacement
- Addresses the "code generates but does the feature actually work?" gap
- Integrates with existing coding agent CLIs (Claude Code, Codex, Cursor mentioned in description)
- Addresses the Harvard-confirmed bottleneck: code review bottleneck partially relievable by automated verification

## Why clawfit should care
Live app verification by agents is a new harness-layer behavior: it extends L2 (harness) into L6 (UI interaction). For `governance_need: hard` orgs concerned about automated deployment, Reticle represents a trust signal — agents that self-verify before shipping. The `task: qa` profile would benefit from a `verification_mode: live-app` annotation. First signal for "coding-agent live app self-verification" as a distinct capability.

## Preliminary interpretation
Current best reading:
- **Level 2 — Agent Harness** (verification layer wrapping the agent loop), with **Level 6 — Interface** as secondary (uses real UI as verification surface)

## Status
- First scan 2026-11-20 (GeekNews)
- Registry entry deferred pending star count confirmation
- 📡 Watch: second coding agent tool positioning explicitly as "agent-driven live verification" would confirm this as a canonical L2 sub-type
