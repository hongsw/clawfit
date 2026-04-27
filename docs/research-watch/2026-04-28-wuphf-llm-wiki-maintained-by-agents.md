# Research Watch: wuphf — Karpathy-style LLM Wiki Maintained by Agents (Markdown + Git)

- Repo: https://github.com/nex-crm/wuphf
- Source: Hacker News Show HN (258 points, 114 comments) — https://news.ycombinator.com/item?id=47899844
- Karpathy origin gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Related implementations: lucasastorian/llmwiki, Astro-Han/karpathy-llm-wiki, Ar9av/obsidian-wiki, Pratiyush/llm-wiki

## Why this is worth watching
wuphf is the first non-toy implementation of Karpathy's "LLM wiki" pattern — a knowledge substrate that agents read from *and write into* so context compounds across sessions instead of being re-pasted. Where Cognee/mem0 represent the vector-DB track of agent memory, wuphf represents a parallel "human-inspectable, agent-maintained" track using markdown files in a local git repo. The Show HN engagement (258 points) and the visible cluster of sibling implementations appearing in the same week suggest this pattern is crystallizing into a recognized sub-category.

## What stands out immediately
- Backend is a local git repo at `~/.wuphf/wiki/` (markdown default; `nex`, `gbrain`, `none` also supported as backends — claim, not verified)
- Two-tier memory model: per-agent **notebooks** (private scratch) → **wiki** (team-wide, promoted via "promotion hint" when content looks durable)
- Markdown files act as a "living knowledge graph": typed facts with triplets, per-entity append-only fact logs, LLM-synthesized briefs (claim from README)
- Includes a `/lint` suite that flags contradictions, orphans, stale claims, broken cross-references — quality gate that vector-DB memory tools typically lack
- Multi-agent collaboration framing: "Slack for AI employees with a shared brain" — Claude Code, Codex, OpenClaw all targeted as clients
- Architecture choices documented: fresh sessions per turn, push-driven agent wakes, scoped MCP tools (4 in DM mode vs 27 in full office) — claims to inspect
- 657 stars, 202 releases, latest v0.83.10 — high release velocity, primarily Go (72.7%) + TypeScript (17.4%)
- Distributed via `npx wuphf` for end users; Go 1.25+ for source builds; tmux for TUI mode

## Why clawfit should care
This strengthens an emerging Level 5 sub-pattern that clawfit has now seen four datapoints for: **human-inspectable, agent-maintained memory** as a distinct track from embedding/vector memory.

Datapoint accumulation:
1. **Beads** (22.2k★) — agent-maintained issue/state ledger
2. **Engram** (2.9k★) — markdown-first agent memory
3. **GBrain** (Garry Tan) — markdown + git knowledge graph, autonomous enrichment
4. **wuphf** (this signal) — markdown + git wiki with notebook→wiki promotion flow and lint gates

Common shape: git-versioned, grep-able, no API key required, structured facts over embeddings, transparency over recall quality. This is a coherent enough pattern that clawfit's eventual L5 scoring should distinguish "vector memory" (Cognee, mem0, Letta) from "git-native wiki memory" (this cluster) as separate sub-types with different latency/cost/inspectability tradeoffs.

wuphf specifically adds the **multi-agent collaboration** dimension on top — notebook→wiki promotion is a contention/dedup pattern that single-agent tools (GBrain) don't need to solve. That makes it a candidate exemplar if the L5 sub-type ever needs a representative for "team-shared agent memory."

## Preliminary interpretation
Current best reading:
- **Level 5 — Memory / MCP / context layer** (primary)
- Sub-pattern: human-inspectable, agent-maintained memory (markdown + git track)
- Cross-cuts: Level 4 capability flavor (the wiki backend exposes itself via MCP tools — 4/27 tool count claim)
- Distinct from Cognee/mem0 (vector memory), distinct from cc-canary/MCP context routing

Differentiation summary:
- vs **GBrain**: GBrain is single-user personal knowledge base with autonomous enrichment crons; wuphf is multi-agent shared workspace with explicit notebook→wiki promotion flow
- vs **Cognee**: Cognee is vector + graph memory with embedding-based retrieval; wuphf is markdown+git with grep/cited-lookup and contradiction linting
- vs **Karpathy's original gist**: original was a description; wuphf operationalizes it with a backend-pluggable architecture and lint quality gates

## Status
- Tracking at 657★, 258 HN points; no registry entry (clawfit registry currently scopes runtimes/LLMs/hardware, not memory backends)
- No reference-levels.md change yet — but flagging that the human-inspectable agent-memory sub-pattern now has 4 named datapoints (Beads, Engram, GBrain, wuphf). If a 5th appears, consider promoting this to a documented L5 sub-type in reference-levels.md
- Items to validate on next pass: actual MCP tool surface (4 vs 27 claim), whether the `gbrain` backend integration is functional or aspirational, lint suite scope and false-positive rate
