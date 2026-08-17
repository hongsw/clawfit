# Research Watch: MathCode — Math Formalization Coding Agent (Lean 4)

- Repo/Link: https://github.com/math-ai-org/mathcode
- Site: https://math-ai-org.github.io/mathcode/
- Source: Hacker News front page (2026-08-17)

## Why this is worth watching

MathCode is a terminal AI coding assistant with a built-in math formalization engine: it converts natural-language math problems into Lean 4 theorems and attempts formal proofs via an iterative agent loop. Unlike general coding agents (which produce executable code), MathCode's primary output is formally verified mathematical proof — a distinct artifact type. At 622 stars on its first HN appearance, it is above the 100-star tracking threshold for the corpus.

## What stands out immediately

- **Agent-mode proving:** iteratively writes proof candidates, reads Lean LSP error output, revises, and recompiles — the agent loop is specialized for a formal verification REPL, not a shell.
- **Multi-planner parallel strategies:** runs competing proof strategies simultaneously (parallel to orca's multi-model parallel worktrees, but at the proof-strategy level within a single model).
- **Tree-of-Subgoals decomposition:** structured decomposition of complex theorems into proving subgoals — closer to structured planning than open-ended chain-of-thought.
- **Persistent Lean REPL:** avoids 30-second compilation overhead by keeping a persistent REPL (~0.4s per check) — a latency optimization specific to formal language environments.
- **Mathlib lemma search integration:** agent queries the Lean Mathlib library for reusable lemmas — a domain-specific tool-use pattern absent from general coding agents.
- **Obsidian knowledge graph for theorem libraries:** reusable theorem/axiom libraries stored in an inspectable graph — L4a memory pattern in a math domain.

## Why clawfit should care

MathCode represents a new task sub-type not currently covered in clawfit's task taxonomy: `task: math-formalization` (distinct from `code-gen`, `research`, and `qa`). The proof-loop architecture — iterative write/check/revise against a formal verifier — is structurally analogous to the test-driven coding loop but constrained to formal mathematical logic. For research, legal, or scientific organizations that require verified reasoning (not just plausible output), a math formalization agent is a qualitatively different tool than a general coding agent. The Lean 4 runtime dependency also introduces a new `setup_complexity: high` signal (Lean 4 + Mathlib installation, ~1 GB download).

## Preliminary interpretation

Current best reading:
- **Level 2 — Specialized domain coding agent** (primary): agent harness built around a formal verification REPL (Lean 4), not a general shell. Closest L2 analog: ARC (adaptive test-time coding, 2026-04-07) — both optimize an agent loop against a verifier rather than a test suite.
- **Level 5 secondary:** formal proof generation is evaluation-as-output — the agent's work product is a verified proof, making the line between L2 (coding agent) and L5 (evaluation/verification tooling) blurry. Lean 4 is itself a proof checker, so the "evaluator" is the runtime, not a separate scoring module.

## Status

- 622 stars — above 100-star threshold; below 5k registry threshold
- No registry entry: specialized math domain limits breadth of org-fit applicability; no deterministic cost/latency data for general coding profiles
- Schema gap: `task: math-formalization` not present in current task taxonomy; `formal_verifier: lean4 | coq | agda | isabelle` not in schema
- Watch for: adoption by proof-assistant research groups, integration with Anthropic's formal-methods initiatives (if any), star velocity over 30 days
