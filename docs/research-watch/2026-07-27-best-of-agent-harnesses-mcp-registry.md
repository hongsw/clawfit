# Research Watch: best-of-Agent-Harnesses — Machine-Readable Harness Registry with MCP Exposure

- Repo: https://github.com/RyanAlberts/best-of-Agent-Harnesses (⭐404)
- Source: WebSearch / GitHub, July 2026

## Why this is worth watching

This repo is structurally interesting not because of its content — a curated list of 140+ agent harnesses — but because of its machine-readable surfaces: `harnesses.json`, `llms.txt`, and a PyPI-published MCP server exposing `recommend`, `compare`, `pick_harness`, and `search_harnesses` functions. In other words, it is a harness registry that is itself accessible by agents. An agent inside a harness can query best-of-Agent-Harnesses to discover and compare other harnesses. The circularity is intentional. This is a different pattern from static awesome-lists — it is a living, agent-queryable catalog of the same layer it describes.

## What stands out immediately

- 140+ harnesses catalogued across 12 categories: coding agent products, progressive-disclosure harnesses, frameworks, multi-agent orchestration, memory/state, evals, plugins, libraries
- `harnesses.json` contains structured data: stars, descriptions, complexity ratings, autonomy/recovery classifications, and concrete usage examples
- `llms.txt` format — the same format increasingly adopted for agent-friendly documentation (tracked in 2026-04-06-awesome-design-md.md)
- MCP server published to PyPI and the official MCP registry — any agent with MCP access can invoke `recommend` or `pick_harness` without loading the list into context
- Rescored weekly — not a static snapshot
- 128 commits; active as of July 2026

## Why clawfit should care

Two relevant observations:

1. **Competitive signal**: best-of-Agent-Harnesses overlaps directly with clawfit's recommendation function. An agent-queryable harness registry with MCP exposure is structurally similar to what clawfit would need to become if it added an MCP server surface. The `pick_harness` function is essentially clawfit's `recommend` command. The difference is that best-of-Agent-Harnesses is a curated-quality list with no scoring algorithm, while clawfit applies structured filters and weighted scoring. Tracking this project is useful for identifying gaps in clawfit's coverage and as a benchmark for recommendation quality.

2. **Architecture reference**: the combination of `harnesses.json` + `llms.txt` + MCP server is a publishable pattern for making any curated list agent-queryable. If clawfit wants an MCP surface, this repo is the nearest reference implementation in its own problem domain.

## Preliminary interpretation

Current best reading:
- **Level 4 — Capabilities / Discovery Layer** (an MCP server that exposes harness selection as a named tool call for agents)
- Secondary: L5 overlap (tracking and rating harnesses over time is a form of ecosystem observability)

## Claims to verify

- Whether the `recommend` and `pick_harness` MCP tools return results that are meaningfully better than keyword search over the JSON
- How "rescored weekly" is implemented — manual review, automated star fetching, or something else?
- Whether the 140+ count reflects active projects only or includes archived/unmaintained entries
- MCP server reliability and update cadence

## Status

- ⭐404 — above 100-star floor, below 5k threshold
- Not a registry candidate; star count and scope do not meet registry criteria
- First signal for "agent-queryable harness catalog" pattern — no prior tracked example of a harness registry with an MCP server surface
- Directly relevant to clawfit architecture discussions about MCP exposure
- Schema implication: if clawfit ever publishes an MCP server, best-of-Agent-Harnesses is the clearest prior art in the problem domain
- Monitor for: star growth, MCP server adoption by other agents, comparison quality vs. clawfit recommendations
