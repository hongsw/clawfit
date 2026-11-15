# Research Watch: Ace — GitHub Next Team+Agent Coding Environment

- Repo/Link: https://github.com/githubnext/ace
- Source: GeekNews

## Why this is worth watching
Ace is a macOS coding environment from GitHub Next where human teammates and AI agents share the same workspace: teammates discuss in channels, then mention an agent that reads the conversation and can ask clarifying questions before acting. This models a natural human–agent handoff that most IDEs still treat as separate workflows. It sits squarely at L2 (harness/wrapper) but with explicit team-communication integration that is rare at that layer.

## What stands out immediately
- Channels-first interface: team discussion and agent invocation are co-located
- Agent asks questions before executing — not fire-and-forget
- macOS-native (no web or Docker dependency)
- GitHub Next provenance means direct line to Copilot/Actions integration

## Why clawfit should care
Ace validates the emerging pattern of "team-aware harnesses" that sit above individual coding agents. For clawfit's recommendation engine, this is a signal that `team_size: ["small", "mid"]` orgs want harnesses that mediate both human and agent communication, not just agent execution. The `roles` dimension should expand to include `pm` for such tools since PMs drive channel discussions.

## Preliminary interpretation
Current best reading:
- **Level 2 — Agent Harness / Orchestration Wrapper**

## Status
- Tracking — GitHub Next experimental; watch for star growth and Copilot integration
