# Research Watch: code-review-graph — Local Code Intelligence Graph for AI Code Review

- Repo: https://github.com/tirth8205/code-review-graph
- Also see: https://github.com/colbymchenry/codegraph (nearest structural neighbor, L4c, 7 MCP tools; docs/research-watch/2026-05-09-codegraph-knowledge-graph-claude-code.md); https://github.com/abhigyanpatwari/GitNexus (L4c, ~31.5k★, 16 MCP tools, BM25+semantic hybrid)

## Why this is worth watching

Cited six weeks ago as an adjacent signal in the codegraph doc (2026-05-09), code-review-graph has since reached 19.7k stars and rank 9 on GitHub Trending All Languages (2026-07-18) — velocity that warrants standalone analysis. It narrows the code-intelligence niche to review-task context compression via MCP, and at 30 exposed tools posts the highest tool count in the L4c code-intelligence cluster observed to date. The growth from adjacent mention to near-top trending in six weeks is the primary flag.

## What stands out immediately

- **30 MCP tools** (impact analysis, semantic search, community detection, change detection, blast-radius tracing) versus codegraph's 7 and GitNexus's 16; tool count alone is not a quality signal
- **Token reduction claim: 82x median** (38x–528x across 6 repos); the prior adjacent-signal entry cited 6.8x — a metric definition change between versions is the likely explanation, not a factual error; both are vendor-authored and unverified
- **GitHub Action CI/CD integration** for risk-scored PR reviews with optional merge gates — extends beyond the MCP session layer into pipeline infrastructure, a pattern not present in codegraph or GitNexus
- **Multi-platform MCP target list**: Claude Code, Cursor, Codex, Copilot, Continue, Windsurf, Zed — widest stated compatibility in the L4c cluster
- **README self-discloses weaknesses**: recall metric is circular (same graph predicts and scores impact), MRR 0.35 on keyword search, ~33% recall on flow detection — honest disclosure, but each item requires independent verification
- **MIT, v2.3.6, 27 releases, Python 94%** — past prototype phase; same license tier as codegraph, lower friction than GitNexus (PolyForm Noncommercial)

## Why clawfit should care

Task framing is narrower than codegraph or GitNexus: code-review-graph is explicitly built for review workflows, not general code-gen queries. For clawfit profiles where `task: qa` and `statefulness: session` co-occur, this is a more precise fit than general-purpose code-graph tools. The GitHub Action layer means it also surfaces in infrastructure discussions. MIT licensing removes the PolyForm Noncommercial barrier that limits GitNexus for `governance_need: standard` profiles, and the multi-platform MCP compatibility list is the broadest of any tool in this sub-cluster.

## Preliminary interpretation

Current best reading:
- **Level 4c — Code intelligence / context graph MCP server** (primary): Tree-sitter → SQLite graph exposed as 30 MCP tools; session-scoped context compression targeted at code review tasks
- **Weak Level 7 secondary (CI/CD only)**: GitHub Action for merge-gated PR review reaches into pipeline infrastructure; insufficient for a primary L7 classification

## Status

- 19.7k stars, active release cadence (v2.3.6, 27 releases) — reference-levels candidate for L4c; token reduction metric discrepancy (6.8x prior reference vs. 82x current README) and self-disclosed recall/MRR limitations require verification before registry promotion. Distinct from colbymchenry/codegraph: narrower task scope (review vs. general intelligence), 4x more MCP tools, and CI/CD pipeline integration.
