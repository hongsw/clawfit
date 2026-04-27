# Research Watch: dirac — OSS Coding Agent Topping Terminal-Bench 2.0 on Gemini-3-Flash-Preview

- Repo: https://github.com/dirac-run/dirac
- Also see: https://www.tbench.ai/leaderboard/terminal-bench/2.0 , https://llm-stats.com/benchmarks/terminal-bench-2
- Source: Hacker News front page (Show HN, 282 pts / 110 comments)

## Why this is worth watching
dirac is an OSS coding agent (Apache-2.0, fork of Cline) that claims the top Terminal-Bench 2.0 agent slot at 65.2% using `gemini-3-flash-preview`, edging out the leading closed-source agent (Junie CLI, 64.3%) and the Google baseline (47.6%). The signal arrives one day after the SWE-bench Verified saturation note — Terminal-Bench 2.0 (89 hard CLI tasks) is one of the candidate successors, and the first wave of agent-vs-agent leaderboard differentiation appears to be forming there. The fact that an OSS fork tops the agent ranking on a *small/fast* model is a non-trivial double signal.

## What stands out immediately
- 65.2% on Terminal-Bench 2.0 (claim to inspect on the leaderboard) using `gemini-3-flash-preview` with thinking mode
- Self-reported delta vs Junie CLI (64.3%) and Google's baseline (47.6%) — small absolute gap vs Junie, large vs baseline
- Distinguish: the **model** leaderboard top is GPT-5.5 (~82.7%); dirac's claim is **agent**-category leadership at a specific model tier, not absolute SOTA
- Architecture: hash-anchored edits, AST-aware modifications, multi-file batching in a single LLM roundtrip — explicitly engineered for token/cost efficiency
- Native tool-calling only — **no MCP support** (notable design stance against the Level 5 MCP trend)
- Apache-2.0, ~183 commits, TypeScript-heavy (95.9%), forked from Cline
- Ships as both VS Code extension and CLI
- Side benchmark: 8/8 success on a refactoring suite vs 5–6/8 for competitors at ~$0.18 avg cost vs $0.38–$0.73 (vendor self-report; needs independent reproduction)

## Why clawfit should care
Three orthogonal signals from one project:
1. **Benchmark succession**: Terminal-Bench 2.0 is showing agent-level differentiation right at the moment SWE-bench Verified is being declared saturated (see 2026-04-27-swebench-verified-no-longer-frontier.md). If TB2 holds up to scrutiny, clawfit's scoring should treat TB2 numbers as the new high-confidence anchor for coding-agent LLM preference weights.
2. **Small-model agentic competence**: a `*-flash-preview` tier model topping the agent leaderboard reinforces the trend (also visible in mini-swe-agent) that frontier-tier models are not the only viable substrate for production coding agents. Latency/cost-sensitive recommendations get more headroom.
3. **Gemini agentic surge**: the leading OSS agent result is on Gemini, not Anthropic or OpenAI. clawfit's LLM preference weights currently lean Anthropic-heavy for coding tasks; if Gemini-3 family sustains this on independent evals, that weighting needs revisiting.

The "no MCP" stance is also a counter-signal worth tracking — at least one credible Level 1/2 entrant is betting that native tool-calling beats the MCP layer for coding-agent workloads.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base runtime / agent surface** (primary classification: it is a runnable coding agent)
- **Level 5 — Evaluation / benchmark cross-cut** (the more important signal is what TB2 leadership means, not the agent itself)
- Subcategory: Cline-lineage fork; deliberate non-adopter of MCP

## Status
- Tracking: high signal, but treat numbers as **claim-to-inspect** until the public TB2 leaderboard entry is independently confirmed; do not register in clawfit registry on a single signal; do not modify reference-levels.md.
