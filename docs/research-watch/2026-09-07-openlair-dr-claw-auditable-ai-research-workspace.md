# Research Watch: Dr. Claw — Auditable Human-in-the-Loop Wrapper for AI Research Workflows

- Repo: https://github.com/OpenLAIR/dr-claw (⭐1,058)
- Source: HuggingFace daily papers 2026-09-07 (arXiv 2609.00365, published 2026-08-31, 5 upvotes); GitHub Topics: claude-code, ai-scientist, auto-research
- Paper: "Dr. Claw: An AI Scientist Workspace for Vibe Research" — https://arxiv.org/abs/2609.00365

## Why this is worth watching

Dr. Claw is not another coding agent. It is a wrapper around existing coding agents — specifically Claude Code and Gemini CLI — that adds a controllable, auditable orchestration layer: persistent state objects that survive session restarts, a reusable skill library that codifies research procedures, and multi-executor coordination that lets the same workflow run against different backends. The paper frames this as "vibe research" — the mode of AI-assisted research where humans iterate quickly with AI executing, rather than either manual research or fully autonomous AI research.

The key claim in the paper, and the reason it matters for this log, is the measurement methodology: the authors hold the executor constant (same Claude Code backend) and vary only the orchestration layer, isolating the harness contribution to task outcome. On research completeness metrics, the orchestration layer alone — not the model — accounts for meaningful performance differences. This is empirical evidence for what clawfit's taxonomy implicitly assumes: that L2 harness choice matters independently of L1 model choice.

Created 2026-02-26; AGPL-3.0 with GPL-3.0 upstream components. Last pushed 2026-09-06.

## What stands out immediately

- **Wraps, does not replace, coding agents**: Dr. Claw's design assumption is that Claude Code or Gemini CLI already runs tasks adequately — the problem is the lack of auditability, state persistence, and recovery when long sessions fail or diverge. It provides these without changing the executor.
- **Persistent state objects**: task state (hypotheses, intermediate results, file dependencies, decision log) is stored as durable structured objects that survive crashes, session timeouts, and executor switches
- **Reusable skill library**: research procedures (literature review protocols, experiment templates, analysis pipelines) are codified as callable skills; each skill invocation is logged with inputs and outputs for auditability
- **Multi-executor coordination**: the same skill invocation can target Claude Code, Gemini CLI, or a custom executor; the paper demonstrates switching executors mid-workflow for cost optimization
- **Human-in-the-loop gates**: the workflow has explicit human approval checkpoints before destructive operations (file writes, external submissions, resource allocation); not fully autonomous
- **Failure recovery walkthrough**: the paper includes a demonstrated failure-recovery scenario; this is notable because most agent workflow papers only show the happy path
- **Claude Code mentioned 4 times in topics**: topics are `ai-agents, ai-scientist, auto-research, claude-code, claude-science-desktop-alternative, claude-science-free, literature-review, paper-writing, research-assistant` — explicitly positioned as a free/open alternative to Claude Science Desktop features

## Why clawfit should care

1. **Executor isolation methodology is directly relevant to clawfit's scoring model**: clawfit's current scoring mixes model-contribution and harness-contribution without disentanglement. Dr. Claw's paper explicitly measures harness contribution in isolation. The result — harness choice changes research completeness scores even with an identical model backend — is empirical evidence that L2 and L1 scoring dimensions should be separable in clawfit's recommendation engine.

2. **"Research harness wrapping coding agents" is a new registry niche**: clawfit's current registry has coding agents (Claude Code, Cline, Aider) and research tools (OpenResearch, Refly) but nothing in the "harness that wraps a coding agent for research workflows" category. Dr. Claw occupies this niche explicitly. A `task: research` agent that scores well on `statefulness: persistent` and `latency: medium` would benefit from awareness of this harness category.

3. **Skill library as L3 concern, not L4**: the reusable skill library in Dr. Claw is not a capability (L4) — it is a codified, version-controlled workflow specification (L3 in taxonomy terms, closer to the SSOT/team-workflow layer). This blurring of L2/L3 for research workflows mirrors the pattern seen in ECC (workflow enhancements, 2026-06-30) and Prime Agent (SSOT-style task state, 2026-08-25) — but in an academic paper context that provides structural analysis rather than just implementation.

4. **"Vibe research" as a named workflow mode signals a real user segment**: the paper coins "vibe research" as the mode where humans iterate quickly with AI executing. This is analogous to "vibe coding" (fast-iteration coding with AI) but for research. The user segment — solo researchers using Claude Code for literature review, experiment design, and paper writing — is not the primary user clawfit targets, but their requirements (persistent state, skill reuse, multi-session auditability) are shared with enterprise research teams. The paper's named framing will likely attract citations and follow-on tools.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness / Wrapper Layer (primary)**: Dr. Claw wraps existing coding agent executors and adds orchestration, state management, and constraint enforcement — these are definitionally harness-layer concerns
- **Level 3 — Team Workflow / Executable SSOT (secondary)**: the persistent state objects and skill library form a codified workflow specification that survives individual sessions and is sharable/versionable — this is L3 territory even though the tool is solo-focused today

## Claims to verify

- Whether the "research completeness" metric used in the paper has an independent definition or is an author-defined metric; an author-defined metric with no external baseline has limited evidential weight
- Whether persistent state objects survive a full process restart (real persistence) or only in-memory (session-scoped persistence); the paper implies the former but the implementation should be checked
- Whether multi-executor coordination requires pre-configured API keys for each executor, or whether Dr. Claw can dynamically route based on context
- Whether the AGPL-3.0 license is a practical barrier for commercial research teams (AGPL requires source disclosure for network-deployed services)
- The "claude-science-desktop-alternative" topic is a strong claim — whether the feature set actually matches or exceeds Claude Science Desktop capabilities is unverified

## Status

- 1,058 stars (above research-watch threshold 100★; below registry threshold 5k★)
- Created 2026-02-26 (6.4 months ago; marginally outside 6-month window); arxiv paper 2026-08-31 (within 6 months); HF daily paper 2026-09-07 — major recent announcement qualifies it
- Not eligible for current registry: no schema slot for "research harness" category; no deterministic per-session cost (wraps third-party agents whose pricing varies)
- First harness-wrapping-coding-agent signal specifically for research workflows in this log
- Watch: whether the paper attracts citations that generate follow-on tools in the same niche; whether the `claude-science-desktop-alternative` claim is substantiated by feature comparison; whether star count grows beyond 1k after HF paper visibility today
