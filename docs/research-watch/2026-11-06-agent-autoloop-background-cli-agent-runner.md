# Research Watch: agent-autoloop — Background CLI Agent Scheduler with Human-in-the-Loop Notifications

- Repo: https://github.com/KKKKhazix/agent-autoloop (⭐3,600)
- Source: munderdiffl.in agent-tools roundup 2026-11-05 / GitHub Trending

## Why this is worth watching

agent-autoloop is a zero-dependency Node.js kernel that runs any command-line AI agent (Claude Code, Codex, ACP) in the background against scheduled or event-triggered tasks, then sends decision cards to Feishu, DingTalk, Slack, Discord, or desktop notifications when human input is needed. Its first stable release (v1.0.0) shipped 2026-11-03. The pattern is structurally distinct from agent harnesses that keep a user in-loop via a UI: the user is entirely absent until an action requires explicit authorization. That's a narrower but practically significant use case — nightly maintenance, CI-event triage, recurring research briefs — that existing harnesses don't serve cleanly.

## What stands out immediately

- Zero external runtime dependencies; about 1,850 lines of kernel code; requires Node 24
- Works with any CLI agent that takes a prompt and prints a final reply — no SDK integration, no source changes required
- Human-in-the-loop trigger is decision-based (deletes, restarts, spend, outbound messages), not rate-based; agent runs silently otherwise
- State is derived from an append-only log committed to disk before acknowledgment — restores correctly from crash/kill (1,000 forced-kill tests per README)
- Hop-count limit of 8 prevents runaway agent chains
- External text (issue bodies, alert payloads) is passed as data files, not concatenated into prompts — reduces prompt injection surface
- Windows support stated as pending as of v1.0.0; macOS and Linux only currently
- v1.0.0 release notes: Claude Code, Codex, ACP, and Feishu tested end-to-end; webhook templates tested only against local mock services

## Why clawfit should care

clawfit recommends (agent, llm, hardware) triples for single-session use; it has no concept of a task scheduler layer that wraps an agent in long-running autonomous mode. agent-autoloop is a thin but structurally important bridge between "run an agent now" and "run an agent on a cron." If this pattern proliferates — which the 3.6k stars in under 72 hours suggests it might — clawfit's `statefulness` filter (stateless / session / persistent) may need a fourth value: `autonomous-loop`. Without that, clawfit cannot distinguish session-stateful agents from agents embedded in a background loop, and recommendation quality degrades for the growing set of users running overnight automation.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/wrapper** (schedules and supervises CLI agents; does not provide model, tools, or capabilities itself)
- **Level 3 secondary** (rules file governs triggers and working directories — a lightweight SSOT-layer concern)
- clawfit category: `agents.json` is not the right fit; this is a meta-layer above agents; closest analog: Orca (L2, fleet runner), but Orca has a UI and this explicitly has none

## Claims to verify

- "Zero runtime dependencies" — the README's claim; needs confirmation against `package.json` lock file
- Benchmark figures (88 ms cold start, 60 MB idle RSS, 2,394 writes/sec) are on Apple M5 Pro; no cross-platform figures
- 1,000 forced-kill crash-recovery tests: author-reported; no third-party replication
- Windows pending: check repo in one week — the author stated intent to deliver by 2026-11-07/08
- Hop-count limit of 8: implementation confirmed in source, behavior under adversarial prompt-chains not tested

## Status

- Tracking: first signal (GitHub Trending / munderdiffl.in 2026-11-05; v1.0.0 released 2026-11-03)
- Registry action: none — meta-scheduling layer, not a direct agent/LLM/hardware entry; no cost or latency data applicable; watch for adoption by major harnesses (Orca, Open Duet) as a plugin integration signal
