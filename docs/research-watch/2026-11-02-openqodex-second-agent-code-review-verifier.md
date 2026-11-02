# Research Watch: OpenQodex — Second-Agent Code Review for Coding-Agent Output

- Repo: https://github.com/openqodex/openqodex (⭐1,100)
- Source: GeekNews (Show GN item, 6 points, 2026-11-02)

## Why this is worth watching

OpenQodex is a command-line tool that runs a separate reviewer agent over code changes before they are pushed. The structural premise is: a coding agent that writes code should not also review its own output. OpenQodex addresses this by dispatching the review work to a second Claude Code or Codex session, running independently with no shared context from the authoring session. Static analysis scanners (22 built-in, including gitleaks and semgrep) run first, narrowing findings to changed lines only, before AI review begins.

The star count (1.1k) is above the 100-star research-watch threshold but well below the 5k registry threshold. The concept, however, is worth watching regardless of the current star count because it operationalizes a multi-agent verification pattern that is architecturally distinct from existing code-review tools.

## What stands out immediately

- **Authoring-reviewer separation**: the agent that wrote the code is explicitly excluded from reviewing it; a fresh Claude Code or Codex session is dispatched as the reviewer with no inherited context
- **Three-stage pipeline**: (1) static scanners find candidates; (2) Finder AI sessions propose problems with a quoted line as evidence; (3) Verifier AI sessions confirm or refute each candidate — false positives are explicitly modeled as an expected output
- **Quote-as-evidence constraint**: the Finder must quote an exact line from the code as the basis for each candidate; a quoted line that does not exist in the code causes the finding to be dropped; this structural constraint reduces hallucinated findings
- **22 built-in scanners**: includes gitleaks (secret detection) and semgrep; scanner findings are scoped to changed lines only, reducing noise from existing code
- **Multi-format output**: `report.html`, `report.md`, `report.json`, `report.sarif`; the SARIF format enables direct integration with GitHub Advanced Security and IDE diagnostics
- **MCP server for code-graph queries**: reviewers can ask structural questions about the codebase (call graph, type relationships) rather than reading files in sequence
- **Push-gate integration**: hooks warn by default and block on push if configured; the gate is opt-in, not default
- **Requires Claude Code or Codex as reviewer**: Cursor and Cline can initiate reviews but cannot serve as reviewers; the tool is practically gated on a Claude or OpenAI subscription

## Why clawfit should care

The "second agent as verifier" pattern is a specific instantiation of multi-agent workflows that clawfit does not yet model explicitly. The scoring system currently does not distinguish between:
- single-agent code generation
- single-agent generation + self-review
- dual-agent generation + independent review

This matters because the quality ceiling for agentic code generation may differ significantly between these configurations, and the relevant cost/latency tradeoff (extra reviewer session) is quantifiable.

Additionally, the push-gate integration is a direct signal that organizations are starting to add agent-output quality gates to their CI/CD pipelines — a new architectural surface that may warrant a future registry field (e.g., `supports_push_gate: true/false`).

## Preliminary interpretation

Current best reading:
- **Level 4 — Capabilities / Quality Gates** (primary): a capability added on top of coding agents to constrain and verify their output
- **Level 2 — Harness / Orchestration** (secondary): orchestrates multiple agent sessions (Finder, Verifier) in a structured pipeline

## Claims to verify

- Whether the authoring-session isolation is actually enforced (i.e., the reviewer session has no access to the original session context, not just no shared memory)
- Whether the quote-as-evidence constraint meaningfully reduces hallucination rates vs. unstructured AI code review; no benchmark data is currently published
- Whether the SARIF output is correctly formatted for GitHub Advanced Security ingestion (a common claim that frequently requires validation in practice)
- 1.1k stars at 0.x release: trajectory matters — is this growing steadily or a single spike? The project describes itself as pre-1.0

## Status

- New signal; not previously tracked
- Registry eligibility: 1.1k stars — below 5k threshold; no deterministic cost/latency data; no registry addition
- Watch for: star count growth to 5k; independent study comparing single-agent vs. dual-agent code review quality; adoption by a named dev team in a public post-mortem
- Relation to existing signals: Orkas (2026-10-31) used CLI coding agents as sub-workers; OpenQodex uses them as reviewers/verifiers — a different compositional role for the same tools
- 📡 note: first signal for "separate reviewer agent for coding-agent output" as a named, packaged tool; watch for a second tool or study formalizing the "independent reviewer" pattern in agentic coding workflows
