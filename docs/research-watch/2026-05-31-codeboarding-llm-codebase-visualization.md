# Research Watch: CodeBoarding — LSP + LLM Interactive Architecture Diagrams

- Repo: https://github.com/CodeBoarding/CodeBoarding
- Also see: VS Code Marketplace (CodeBoarding extension), Open VSX registry

## Why this is worth watching

CodeBoarding reached GitHub Trending Python #7 (1,974 total stars, 36 today) and GeekNews front page (36 points) on the same day — cross-platform surfacing that is rare for a dev-tooling utility at this star level. The hybrid LSP + Multi-Agent System pipeline occupies a structurally distinct position: static analysis provides a deterministic call-graph skeleton; LLM reasoning interprets architectural intent on top of it. The output — a `.codeboarding/` folder of Mermaid diagrams and component docs — follows the same "structured markdown context for AI consumers" pattern introduced by CLAUDE.md and now being formalized across multiple agents.

## What stands out immediately

- **Two-phase hybrid pipeline (claim to inspect):** LSP handles deterministic symbol resolution and change detection; a multi-agent LLM layer assigns architectural meaning (component roles, subsystem boundaries) that LSP alone cannot infer. The incremental update mode re-runs only on diffs, not full repositories — a practical engineering decision that implies the LLM cost per run is non-trivial.
- **`.codeboarding/` output pattern:** The generated folder is designed to persist in the repo alongside CLAUDE.md, AGENTS.md, or SKILL.md — readable by agents as pre-digested architectural context before they touch code. This is not incidental; the README explicitly frames one use case as "monitor AI agent code generation with architectural context."
- **Mermaid.js as the output format:** Machine-readable enough for agents to parse; human-readable enough for PR review. Avoids proprietary diagram formats. Clickable navigation between component files implies the doc structure is a graph, not a flat dump.
- **800+ open-source repos visualized (claim to inspect):** Social proof for the analysis engine. Independent verification of diagram accuracy has not been checked.
- **Provider breadth:** Supports Anthropic, OpenAI, Google, Ollama, AWS Bedrock, Vercel AI Gateway, OpenRouter — no model-vendor lock-in. Local Ollama support makes offline or confidential-codebase use cases plausible (depth unverified).
- **Three integration surfaces:** CLI (CI automation), VS Code extension (in-editor view), GitHub Action (CI diagram freshness) — coverage across the three dominant agent surfaces for code-gen tasks.
- **Python 95.2% of codebase, v0.12.0, 21 releases, 173 forks, 8 open issues:** Active maintenance cadence at a pre-1.0 maturity stage; not an abandoned proof-of-concept.

## Why clawfit should care

**On the LSP+LLM hybrid vs. pure-LLM code understanding:** Pure-LLM code understanding relies on the model's context window to reconstruct structure from raw source. LSP-grounded analysis pre-resolves symbol references, import graphs, and call chains deterministically — the LLM receives a structured graph to interpret rather than raw tokens to scan. This matters for large repositories where the relevant context is spread across files the LLM would not see simultaneously. The hybrid approach is analogous to the RAG pattern at Level 5 but applied to code structure rather than knowledge retrieval; the LSP is the retrieval layer, the LLM is the synthesis layer.

**On whether `.codeboarding/` is a meaningful trend:** The pattern of generating a structured, agent-readable context folder from a repo is now confirmed across at least three independent signals: CLAUDE.md (behavioral spec for agents), AGENTS.md (OpenAI's cross-platform equivalent, documented in reference-levels.md), and now `.codeboarding/` (architectural context for agents). These are not the same artifact type, but they share the structural goal of pre-digesting project-specific context so agents spend less context-window budget on first-principles discovery. A fourth signal at comparable reach would make this a formalizable cross-cutting axis. For now it is a candidate pattern, not a confirmed sub-type.

**On L4 placement:** CodeBoarding is not an agent. It produces a capability-augmenting context artifact that other agents consume — it extends what a code-gen agent can understand about a repo before touching files. This maps to **Level 4 — Capability / skill / plugin** as a "codebase context generation" capability tool. It is not L5 (no retrieval pipeline at runtime; it generates static docs, not dynamic context injection) and not L2 (it does not orchestrate or harness agents). The closest taxonomy neighbors are gitnexus (code knowledge graph MCP, L5 primary — different in that gitnexus serves context at query time via MCP; CodeBoarding generates persistent docs upfront) and gitagent (git-native agent distribution, L3 — different in that gitagent is about versioning agent definitions, not generating architectural docs). CodeBoarding is structurally closer to an LSP-powered documentation capability than to a memory or orchestration tool.

## Preliminary interpretation

Current best reading:
- **Level 4 — Capability / skill / plugin layer** (primary: LSP+LLM codebase context generation capability; produces agent-readable `.codeboarding/` docs that extend agent architectural awareness)
- Potential secondary: **Level 6 — Human interface / multimodal layer** (VS Code in-editor interactive diagrams serve a human visualization surface, not just an agent context surface) — weak secondary, not load-bearing for classification
- Not Level 5: output is static pre-generated docs, not runtime MCP context injection or dynamic retrieval

Distinction from gitnexus (L5): gitnexus serves live graph queries to agents via MCP protocol at task time. CodeBoarding generates persistent Mermaid docs into the repo upfront, then leaves them for humans and agents alike to consume passively. The write-authority and invocation timing are different.

## Status

- New signal — first observed 2026-05-31; 1,974 total stars, below the 5k registry threshold
- No registry entry; no reference-levels.md change warranted
- Flag for schema-analyst: "codebase context generation" as an L4 sub-capability type is not currently represented in the taxonomy; CodeBoarding is the first dedicated tool for this function. Promotion threshold: a second independent LSP-or-AST-backed codebase-context-generation tool at ≥5k stars, or CodeBoarding itself crossing 5k.
- Watch: if `.codeboarding/` folder adoption spreads to multiple agents as a de-facto architectural context convention (similar to how CLAUDE.md spread), reconsider for a cross-cutting axis note in `docs/reference-notes/`.
