# Research Watch: "Is Grep All You Need?" — Harnesses Reshape Agentic Search

- Repo/Link: https://arxiv.org/abs/2605.15184
- Source: Hacker News (113 pts, 52 comments, 2026-06-10)

## Why this is worth watching
This is the first peer-reviewed empirical study that places *harness choice* above *retrieval strategy* as the dominant variable in agentic search accuracy. The paper tests grep vs. vector retrieval across Claude Code, Codex CLI, Gemini CLI, and a custom harness (Chronos) on LongMemEval. Key finding: grep generally outperforms vector retrieval for exact-match queries (names, paths, error strings), but overall accuracy depends more strongly on which harness is used than on retrieval method. This directly validates the core design decision in clawfit: that recommending the right harness is more important than recommending the right LLM or retrieval backend.

## What stands out immediately
- Controlled experiment: 116 questions from LongMemEval, 3 provider CLIs + custom harness
- Grep wins over vector for literal matching (names, paths, error strings)
- Harness architecture effect dominates retrieval strategy effect
- Uses Claude Code, Codex, Gemini CLI as production test surfaces — real-world validity

## Why clawfit should care
clawfit's current scoring weights latency (0.5), cost (0.25), LLM preference (0.15), baseline (0.1) — retrieval strategy is not scored at all. This paper confirms the harness-first selection approach is empirically correct. Additionally, if grep-capability is a meaningful differentiator between harnesses (e.g., Aider's grep-heavy design vs. embedding-heavy tools), adding a `retrieval_mode` field to the registry could help disambiguate tools for QA/research tasks.

## Preliminary interpretation
Current best reading:
- Meta-signal validating clawfit's harness-centric recommendation model
- **No new layer needed; potential `retrieval_mode` field for L1/L2 tools (low priority)**

## Status
- Signal documented; no registry mutation. Consider adding `retrieval_mode: [grep, vector, hybrid]` to the org_fit schema in a future scoring iteration.
