# Research Watch: AutoCua — Multi-Platform Computer-Use Agent Framework

- Repo: https://github.com/ComputerUseAgent/AutoCua (⭐1,100)
- Source: munderdiffl.in agent-tools roundup 2026-11-05

## Why this is worth watching

AutoCua is a Python framework that provides computer-use agents across macOS, Windows, Linux, Chrome, iOS Simulator, and real Android devices through a single `run_agent(...)` call. Unlike browser-only computer-use tools (browser-use, agent-desktop), it unifies desktop OS, browser, and mobile control under one API. The multi-agent design (parent + coder + scout) and credential vault (credentials are typed by the runtime, not passed to the model) are architecturally notable for teams building production CUA deployments. It sits in a cluster with Orca (fleet runner with computer-use mode), agent-desktop (Vercel, accessibility tree only, no model), and Google Artemis (Android only); AutoCua is the broadest-platform single-library option tracked so far.

## What stands out immediately

- Single `pip install AutoCua` entry point with per-platform mode parameter (desktop, shell, browser, mobile)
- Screen understanding combines OS accessibility tree + OCR, then presents numbered elements — avoids pixel coordinate guessing
- Input goes through the OS input layer, not a debugging port — reduces detection risk for browser automation
- Chrome browser agent drives user's own Chrome instance via extension; headless uses a separate instance
- Mobile: iOS Simulator or paired iPhone/iPad, Android emulator or real device
- Parent → coder → scout agent chain; scout agents are read-only (reduces blast radius from autonomous writes)
- Credential vault: runtime types credentials, model never sees values
- Parallel runs, desktop app, Telegram control, 10 model providers
- No automated test suite in the repository — README-stated limitation
- Windows: requires Interception UAC kernel driver (non-commercial license unless purchased separately)

## Why clawfit should care

clawfit's `task` dimension has no computer-use value — the taxonomy recognizes `code-gen`, `qa`, `research`, and `general` but not `computer-use`. AutoCua, together with agent-desktop (tracked 2026-11-04) and Google Artemis (tracked 2026-09-12), constitutes a third-signal cluster for multi-platform computer-use as a distinct agent task category. The two-signal rule was met when agent-desktop and Artemis were tracked; AutoCua is the third signal confirming this category has depth. If a `task: computer-use` value is added to clawfit's filter schema, the scoring weight for `latency: low` and `statefulness: session` would need separate calibration — CUA tasks have different latency characteristics than code-gen.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/wrapper** (wraps OS/browser/mobile input APIs and model calls into a unified agent loop)
- **Level 6 secondary** (human interface: controls human-facing UIs on behalf of users)
- clawfit: not a direct `agents.json` entry (no cost/latency data); signals a gap in the `task` filter dimension

## Claims to verify

- "Any model" support via 10 providers: which providers have been tested; whether tool-call format is provider-normalized
- Credential vault: implementation reviewed? Whether the model's context window ever includes credential values needs code audit
- Mobile: iOS real device (not just simulator) support — README says "paired iPhone/iPad" but no independent confirmation
- Benchmark for multi-agent chain: no published numbers — task completion rate against SWE-bench or equivalent unstated
- No automated test suite: how is the library validated before releases?

## Status

- Tracking: first signal (munderdiffl.in 2026-11-05)
- Registry action: none — CUA framework, no cost/latency data; confirms third signal for `task: computer-use` cluster alongside agent-desktop and Google Artemis
