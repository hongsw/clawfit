# Research Watch: Agentic Code Review (Osmani)

- Repo/Link: https://addyo.substack.com/p/agentic-code-review
- Source: GeekNews (에이전틱 코드 리뷰 — AI 엔지니어링 역량이 발전하면서 코드 리뷰가 핵심 역량으로 부상)

## Why this is worth watching
Addy Osmani's analysis presents data-backed evidence that AI agent code generation has outrun human review capacity: code output is up 4x but productivity gain is only ~12%, review duration increased 441.5%, and PRs merged with zero review are up 31.3%. This is an ecosystem-level signal that the verification bottleneck is now the primary risk in agent-assisted development — not code generation quality. The article benchmarks four AI review tools with concrete data (617 distinct flagged locations, 93.4% caught by exactly one tool).

## What stands out immediately
- Verification gap: agents generate code "in less time than it takes me to read this paragraph" while human review speed is unchanged
- Tools benchmarked: CodeRabbit (widest coverage), Greptile (82% bug-catch rate, high false positives), Anthropic Code Review (<1% incorrect findings, best precision), and a fourth unnamed tool
- Key finding: 93.4% of flagged issues were caught by exactly one tool — no single reviewer dominates; heterogeneous review is more effective
- Critical structural problem: agents discard their reasoning after code generation; the first human reviewer sees code with no authorship intent
- Anti-pattern named: "borrowed confidence" — having AI review AI-generated code without capturing reasoning first
- Recommended practice: tier PRs by risk (not author), require evidence before review begins, scrutinize test changes (agents rewrite tests to match broken behavior), keep humans on the merge decision

## Why clawfit should care
This is a Level 5 signal: as agent code generation (Level 1–2) commoditizes, the evaluation and verification layer (Level 5) becomes the differentiating capability. clawfit currently has no registry entries for code review agents (CodeRabbit, Greptile) — both are candidates for a new `security-testing` / `qa` category alongside NVIDIA SkillSpector. The 441.5% increase in review duration also means `latency: high` for any workflow that includes full human review — clawfit's latency dimension for code-gen tasks should account for downstream review cost, not just generation time.

## Preliminary interpretation
Current best reading:
- **Level 5 — Research-loop / Evaluation Layer** (agent-driven code review as a closed evaluation loop over Level 1–2 output)

## Status
- High signal: methodology piece with quantitative data, from a credible author (Addy Osmani, Google Chrome team). Signals maturation of the verification sub-cluster. Watch for CodeRabbit and Greptile to appear on GitHub Trending as this bottleneck drives tool adoption.
