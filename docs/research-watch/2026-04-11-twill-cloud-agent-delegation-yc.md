# Research Watch: Twill.ai — Delegate to Cloud Agents, Get Back PRs

- Repo/Link: https://twill.ai
- Source: Hacker News (Launch HN: YC S25)

## Why this is worth watching
Twill is a YC S25 company (Hacker News front page, "Launch HN") framed around asynchronous cloud agent delegation: you submit a task, an agent works in the cloud, you get back a PR. This is a fundamentally different UX model from interactive coding assistants — it moves AI coding toward async work queues. The "PR as output" framing makes it immediately legible to any developer team already using GitHub workflows.

## What stands out immediately
- Async delegation model: no interactive session required; fire-and-forget with PR output
- Cloud-side execution: no local setup, no hardware requirements
- "Get back PRs" directly integrates into existing Git/GitHub workflows
- YC backing signals commercial trajectory and user validation
- No open-source component visible — proprietary managed service

## Why clawfit should care
Twill represents a new deployment topology for Level 1 agents: cloud-managed, async, PR-output. This differs from existing entries (Claude Code, OpenCode, Goose) which require interactive local sessions. For `team_size: large` orgs or PMs who want to delegate without managing agent infrastructure, Twill is a distinct option. It also raises the question of whether clawfit should track "managed agent services" as a distinct sub-category at Level 1.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base runtime / primary agent surface** (managed cloud agent service sub-type)

## Status
- New entry, high signal. YC S25 + HN front page launch. Add to registry. Monitor pricing model and GitHub integration depth. "Managed cloud agent" is a new Level 1 subtype not previously represented.
