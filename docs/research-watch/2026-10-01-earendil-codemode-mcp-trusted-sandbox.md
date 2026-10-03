# Research Watch: Earendil Codemode — Trusted Sandbox for MCP Tool Execution

- Repo/Link: https://earendil.com/posts/you-said-no-mcp/
- Source: Hacker News (593 points, 2026-10-01)

## Why this is worth watching
The Earendil team documented their architectural reversal on MCP: initially rejected for composition problems, then re-integrated via "Codemode" — a trusted JavaScript sandbox running on the harness side. The 593-point HN discussion shows this resonates strongly with developers working through the same MCP adoption decisions. It reframes MCP not as a passive server protocol but as something requiring an explicit trust-level separation in the harness.

## What stands out immediately
- **Codemode as trust boundary**: tool orchestration moves from the agent's sandboxed context into harness-trusted execution — enables better tool composition and ordering flexibility
- **Session transcript as state**: harness uses session transcripts rather than filesystems for state persistence, eliminating shared-state coordination problems
- **Deferred tool loading**: Codemode enables agents to load tools dynamically rather than at session start — reduces context bloat for large tool catalogs
- **Composition problem addressed**: the core original MCP criticism (tool calls don't compose well across contexts) is resolved by moving orchestration to the harness layer

## Why clawfit should care
The "trusted execution context for tool orchestration" is a new sub-pattern at the harness layer (L2/L4 boundary) that affects how the recommendation engine should reason about MCP-capable tools. Tools that support harness-level tool orchestration (vs. naive server passthrough) have meaningfully different capability profiles. This pattern also validates that MCP governance complexity is a real org-fit dimension — a signal for the `setup_complexity` and `governance_need` axes.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capability Layer (primary)**: Codemode is a harness-side capability delivery mechanism for MCP tools
- **Level 2 — Harness/SDK Layer (secondary)**: the Codemode sandbox is embedded in the Pi harness, making it an L2 execution context variant

## Status
- First signal for "harness-side trusted MCP execution sandbox" sub-type
- High community interest (593 HN pts) confirms this is an active architectural design question
- Tracking: active — watch for other harness frameworks adopting trust-boundary-based MCP integration
