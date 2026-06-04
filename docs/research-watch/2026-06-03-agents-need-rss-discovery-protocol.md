# Research Watch: "RSS Is Back. AI Agents Are Reading It." — Julien Reszka

- Repo/Link: https://julienreszka.com/blog/rss-is-back-ai-agents-are-reading-it/
- Source: Hacker News

## Why this is worth watching
The essay argues that AI agents have an unsolved structured discovery problem — they need deterministic, rate-limit-free, authentication-free feeds of new information, and RSS already satisfies all four requirements while social platform APIs satisfy none. This is a thought-leadership signal, not a tool, but it names a gap in agent infrastructure that is currently unrepresented in the clawfit ecosystem map. If the argument gains traction, it predicts a wave of tooling that treats feed consumption as a first-class agent capability rather than a scraping afterthought.

## What stands out immediately
- Four explicit requirements for agent-suitable content discovery: (1) a deterministic list of what is new, (2) a structured format parseable without guessing, (3) no rate limits tied to an advertising relationship, (4) no authentication wall protecting public content
- The core claim is that social platform APIs are structurally incompatible with agent consumption — they were designed to maximize human engagement via algorithmic inconsistency, which is exactly what agents cannot use
- Podcasting is cited as proof of protocol durability: RSS has run the entire podcast industry since 2002 with no disruption because it is open, free, and has no middleman to negotiate access with
- The proposed solution is publisher-side: "Publish an RSS feed if you don't have one" — this is a call to instrument the web for agent readability, not a new agent protocol
- No code, no repo, no specific implementation — this is framing, not tooling

## Why clawfit should care
The essay surfaces a discovery-layer gap that sits above clawfit's current scope but shapes what agents can autonomously consume. Agents in clawfit's registry that perform research, monitoring, or competitive intelligence tasks (profiles with `task: qa` or `task: research`) implicitly depend on structured feed availability — but the current schema has no field representing whether an agent can consume RSS/Atom feeds as a native capability vs. requiring scraping. If feed-native agent tooling emerges as a category (e.g., MCP servers that wrap RSS, agent plugins that subscribe to topic feeds), it would land in L4 (capability/tool-use layer) and affect scoring for online research profiles. The companion signal `feed-mcp` (noted in web search results) is an early indicator this tooling category may already be forming.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capability / skill / plugin / tool-use layer** (if and when feed-consumption tooling materializes as installable agent plugins or MCP servers)
- The essay itself is a thought-leadership signal with no level assignment — analogous to the Tunguz harness essay (L2/L3 conceptual anchor); it names a pattern, not a product
- A companion signal — `feed-mcp` (Richard Wooding, Medium, 2026) — suggests an MCP server wrapping RSS/Atom/JSON feeds for agent consumption may already exist; not yet assessed for the registry

## Status
- Watching: first signal for "structured feed consumption" as an agent capability gap; no map mutation warranted; monitor for MCP servers or agent plugins that treat RSS/Atom as a native tool-use surface; `feed-mcp` is a candidate for a follow-on research-watch doc
