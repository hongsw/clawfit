# Research Watch: mini-swe-agent — 100-Line Minimal AI Coding Agent

- Repo/Link: https://github.com/SWE-agent/mini-swe-agent
- Source: GeekNews front page

## Why this is worth watching
From Princeton and Stanford researchers (the SWE-agent team), mini-swe-agent strips the full SWE-agent framework down to ~100 lines of Python while retaining the core loop: read issue → understand codebase → apply fix. It is simultaneously a research artifact (minimal reproducible baseline) and a practical signal that productive coding agents do not require complex framework overhead. The "100 lines" framing will attract developer experimentation.

## What stands out immediately
- ~100 lines of Python — fully auditable, zero hidden complexity
- From the original SWE-agent team (Princeton + Stanford) — authoritative provenance
- Targets GitHub issue resolution specifically (not generic coding)
- Demonstrates that the essential agentic coding loop is extremely compact
- Natural baseline for evaluating what harness overhead actually buys

## Why clawfit should care
mini-swe-agent is a Level 1 signal that challenges the complexity assumption embedded in most Level 2 harness recommendations. If a 100-line agent can resolve GitHub issues, orgs with `setup_complexity` sensitivity may prefer this over full frameworks. It also provides a benchmark reference point: clawfit's scoring could use "what does a minimal agent achieve?" as a calibration baseline when justifying higher-complexity recommendations. The SWE-bench connection means there's an evaluation path already built.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base runtime (minimal reference implementation; also Level 5 as benchmark baseline)**

## Status
- Tracking: medium signal. Academic provenance gives credibility beyond star count. Not adding to registry (too minimal to be a production recommendation target), but tracking as a calibration reference and educational artifact.
