# Research Watch: billion-context — Context Compression Plugin for Coding Agent Sessions

- Repo: https://github.com/ranxianglei/billion-context (⭐4.5k)
- Source: GitHub Trending (all languages), daily

## Why this is worth watching
billion-context is a context-window management plugin that sits between a coding agent and its model API. Rather than naively stuffing full conversation history into each request, it compresses prior turns into semantic summaries and restores detail on demand when the agent needs to revisit a specific decision. The key design choice: compression is transparent to the agent — the agent issues normal API calls; billion-context intercepts and rewrites the context payload. This is structurally different from memory MCP servers (which the agent actively queries) and from retrieval-augmented context (which prepends retrieved chunks at the front).

## What stands out immediately
- Transparent interception: agent code requires no modification; compression happens at the API proxy layer
- Semantic summary + on-demand restoration — compression is not lossy-only; detail is recoverable
- Self-reported ~5x token reduction (not independently verified — treat as a claim requiring benchmarking)
- 4.5k stars / 364 forks — meaningful adoption for a context-management tool, not purely a novelty repo
- Directly relevant to long-running coding agent sessions (Aider, Continue, Goose) where context window exhaustion causes session resets
- Orthogonal to latent memory approaches (Memorilla, today's other signal) — operates at the token level, not the model's internal representation
- MIT license

## Why clawfit should care
clawfit does not currently score tools on context-window strategy. billion-context represents a "transparent compression" pattern that is distinct from: (a) tools that expose a memory MCP server the agent queries, (b) tools that use RAG to prepend retrieved text, and (c) tools that simply truncate. The scoring implication: agents that accept a compression proxy mid-session would behave differently on `statefulness: persistent` profiles than agents that reset context on overflow. A `context_strategy: none | truncate | rag | compress | latent` axis would distinguish these. Second signal for context management as a first-class capability after Memorilla (also today, but architecturally different).

## Preliminary interpretation
Current best reading:
- **Level 4 — Capability Layer** (context-window management sub-type)
- Secondary: L2 (harness) — the interception proxy is functionally a thin harness wrapper

## Claims to verify
- The ~5x token reduction claim: needs independent benchmark on a standard coding session (not self-reported)
- Restoration fidelity: does restored detail match original or is there lossy drift in complex multi-turn sessions?
- Compatibility with specific coding agent harnesses: does it integrate with Aider, Continue, Goose, or only OpenAI-compatible endpoints?
- Star count: 4.5k total or current trending burst? If total, adoption is real; if trending, check forks/issues for active use evidence

## Status
- Second signal today for context management as a capability dimension (alongside Memorilla), but architecturally distinct (token-level proxy vs. latent-space)
- Together with Memorilla, may justify documenting a `context_strategy` scoring dimension — two-signal rule partially met; both signals are for "context management" broadly but different mechanisms; hold for a third signal before promoting to canonical taxonomy
- Registry action: candidate pending independent benchmark verification and harness compatibility confirmation; star threshold met (>5k); cost/latency data unavailable without benchmark
