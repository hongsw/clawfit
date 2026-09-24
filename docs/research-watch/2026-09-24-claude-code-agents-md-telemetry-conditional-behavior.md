# Research Watch: Claude Code reads AGENTS.md only when telemetry is on [fixed]

- Repo/Link: https://szypowi.cz (HN thread: news.ycombinator.com)
- Source: Hacker News front page (439 points, 250 comments)

## Why this is worth watching
A blog post and HN thread today disclosed that Claude Code was conditionally reading `AGENTS.md` — the canonical agent governance instruction file — only when telemetry was enabled. Anthropic marked the issue as fixed. This is a second-tier governance signal: not a new tool, but a behavior gap in the most-used coding agent harness that directly implicates the governance layer (L3). The 439-point score and 250-comment thread indicate significant practitioner concern.

## What stands out immediately
- `AGENTS.md` is the de-facto agent instruction standard across multiple runtimes (Claude Code, Codex, Goose); conditional reading breaks cross-runtime governance contracts
- The linkage between telemetry state and instruction-following is architecturally surprising — telemetry should be orthogonal to instruction loading
- Anthropic confirmed and fixed it, indicating a regression rather than intentional design
- Community reaction focused on trust and predictability of harness governance, not just the specific file
- Closely related to the 2026-09-19 ZCode silent git-history upload and 2026-09-22 Meta Muse zero-day: third cross-date signal for "commercial AI agent configuration-layer / governance behavior gaps"

## Why clawfit should care
clawfit scores tools on `governance_need` and network trust axes. This event illustrates that governance compliance of a harness is not a binary property — it can regress in a patch. The scoring model currently treats governance as a static metadata field; this signal argues for a `governance_regression_risk` or `instruction_loading_reliability` axis candidate. It also strengthens the case for the `attack_surface` pattern noted in 2026-09-22 scan notes.

## Preliminary interpretation
Current best reading:
- **Level 3 — Governance / Instruction Layer** (primary signal)
- **Level 2 — Harness/SDK** (secondary; the behavior gap was in the harness implementation)

## Status
- First research-watch doc for this specific behavior class
- Third cross-date signal for "commercial agent governance behavior gap" pattern (ZCode 2026-09-19, Meta Muse 2026-09-22, Claude Code today)
- Three signals from three different vendors in five days — pattern building toward canonical axis candidate `governance_regression_risk`
- No registry action (not a new tool; behavior gap in existing tracked tool)
