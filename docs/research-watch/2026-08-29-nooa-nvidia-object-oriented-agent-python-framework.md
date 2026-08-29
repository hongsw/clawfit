# Research Watch: NOOA — NVIDIA Object-Oriented Agents, a Single-Class Python Agent Framework

- Repo: https://github.com/NVIDIA-NeMo/labs-OO-Agents (⭐1,900)
- Source: WebSearch ("NVIDIA NOOA agent framework 2026"); MarktechPost; The New Stack; arxiv 2607.20709

## Why this is worth watching

NOOA (NVIDIA Object-Oriented Agents) collapses the standard agent-building stack — prompt template, tool registry, orchestration layer, type validator — into a single Python class. The framework's stated thesis is that the existing agent tooling ecosystem adds incidental complexity: a developer already has Python classes, docstrings, type annotations, and a REPL; NOOA proposes these are sufficient primitives for LLM-backed agents without an additional abstraction layer.

Released July 30, 2026 as a research alpha (v0.0.8, Apache 2.0), NOOA comes from NVIDIA's NeMo Labs group with an accompanying arXiv paper (2607.20709). The framework reports 82.2% on SWE-bench Verified using GPT-5.5, reaching that score with roughly half the token budget of peer frameworks (1.1M tokens vs ~2.2M, 28 model calls vs ~66). Whether the benchmark environment is controlled fairly against those peers requires independent review.

The "single-class" design is a deliberate architectural counter-position to frameworks like CrewAI, AutoGen, and LangGraph, which model agents as configuration objects or nodes in a graph.

## What stands out immediately

- **Agent = Python class**: fields are state, methods are capabilities, docstrings are prompts, type annotations are contracts — the mapping is literal, not metaphorical; a class with `...` method bodies hands those bodies to an LLM loop
- **Jupyter-style REPL execution**: models write and run Python inside the class context, giving them access to the full typed interface of the agent object; this is code-as-action rather than tool-call-as-action
- **82.2% SWE-bench Verified (GPT-5.5)**: competitive with frontier benchmarks; the 28-call, 1.1M-token budget claim needs verification against a standardized comparison setup
- **AST validation + module deny-lists**: static checks on generated code before execution; NVIDIA explicitly states these are defense-in-depth, not a containment boundary — the boundary is a container or VM
- **Requires Python 3.12–3.13**: a hard dependency that narrows deployment environments; projects on Python 3.10 or 3.11 cannot adopt NOOA without a runtime upgrade
- **Apache 2.0 license**: commercially permissive; no constraint on production deployment
- **Research preview status**: v0.0.8 alpha — API surface may change; not intended for production yet; NVIDIA labels it "research software in active development"

## Why clawfit should care

NOOA represents a distinct L1/L2 position in the taxonomy: it is simultaneously a base runtime (the REPL loop and LLM call management live here) and an opinionated harness (the class-as-agent pattern enforces a specific orchestration style). This dual-layer occupancy is unusual and affects how clawfit would categorize it.

For clawfit's `task: code-gen` filter, NOOA's REPL-based code execution and SWE-bench performance make it a plausible registry candidate — but only if API pricing is confirmed (the framework calls external LLM APIs; cost depends on the upstream provider choice, not NOOA itself). The lack of a deterministic cost schema blocks registry entry today.

The "single-class" design philosophy also has implications for clawfit's `statefulness` filter: class fields persist across method calls within a session, but NOOA doesn't appear to implement cross-session state persistence natively. The `statefulness: session` classification applies, but users expecting persistent agents would need to add state serialization themselves.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base Runtime** (primary): NOOA manages the LLM interaction loop, REPL execution, and code-as-action layer — the foundational agent execution substrate
- **Level 2 — Harness/SDK** (secondary): the class-as-agent pattern is an opinionated framework choice that functions as a harness, structuring how developers build agents

This is closer to a base runtime than to a pure harness: the REPL and LLM call loop are NOOA's own, not wrappers around an external agent runtime.

## Claims to verify

- Whether the 82.2% SWE-bench Verified figure uses the same task subset and evaluation harness as peer comparisons (token budget comparisons are only meaningful with controlled environments)
- Whether "28 model calls per task" is an average or a median; outliers on complex tasks could distort the figure significantly
- Whether the AST checks meaningfully reduce unsafe code execution, or whether a determined adversarial prompt can bypass the deny-list
- Whether Python 3.12 is a hard dependency of the core framework or of specific tool integrations — critical for enterprise deployment compatibility
- Whether NVIDIA intends to maintain NOOA as a production framework or deprecate it in favor of NemoClaw (their integrated security stack, already tracked 2026-08-15)

## Status

- Tracking: first signal 2026-08-29
- Stars: 1,900 GitHub (2026-08-29); arxiv 2607.20709
- Registry decision: hold. NOOA is a framework wrapper — it calls external LLMs (GPT-5.5 was used in benchmarks, but it is model-agnostic). No fixed cost/latency profile of its own; cost is entirely upstream-provider-dependent. A registry entry is not meaningful until NOOA is paired with a specific LLM that already has a registry entry.
- Watch: whether v0.1.0 or similar milestone stabilizes the API surface; whether NemoClaw supersedes NOOA in NVIDIA's roadmap; independent SWE-bench validation
