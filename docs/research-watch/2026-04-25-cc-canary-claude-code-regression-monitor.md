# Research Watch: CC-Canary — Claude Code Quality Regression Monitor

- Repo/Link: https://github.com/delta-hq/cc-canary
- Source: Hacker News (37 pts, 18 comments)

## Why this is worth watching
CC-Canary reads the JSONL session logs Claude Code writes to `~/.claude/projects/` and measures session-level quality metrics — tool-mix, read:edit ratio, reasoning-loop phrases, self-admitted errors, premature stops, token usage, cost, and thinking depth. It uses a composite health score with argmax regression detection to surface the date quality changed. The tool was used to document the Claude Code thinking-redaction quality regression in production (17,871 thinking blocks, 234,760 tool calls, 6,852 sessions analyzed).

## What stands out immediately
- **Zero dependencies**: stdlib-only Python — no pip, no Node; runs on any machine with Claude Code session logs
- **Forensic quality**: generates a shareable regression report from local session data
- **New signal category**: stop hook violation rate (0→10/day) proposed as a machine-readable quality leading indicator
- **Practical governance relevance**: the tool catches the exact regression class that triggered the "I cancelled Claude" HN thread (751 pts, 445 comments)

## Why clawfit should care
CC-Canary is the first local tool for *quantitative monitoring* of coding agent quality across sessions — distinct from capability benchmarks (lm-evaluation-harness) and trace-level observability (Langfuse). It fills a gap at Level 5: **per-session behavioral health monitoring**. For `governance_need: hard` profiles using Claude Code at scale, session quality monitoring becomes a new audit surface. The delta-hq provenance (DeFi/crypto infra team) also signals that production teams outside pure software development are now instrumenting Claude Code quality.

## Preliminary interpretation
Current best reading:
- **Level 5 — Research / evaluation / benchmark** (per-session behavioral health monitoring sub-type)

## Status
- Tracking. 37 HN pts at launch. stdlib-only design is highly adoptable; revisit when star count is confirmed.
