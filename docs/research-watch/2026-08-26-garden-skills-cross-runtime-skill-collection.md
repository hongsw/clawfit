# Research Watch: ConardLi/garden-skills — Cross-Runtime Production Skill Collection for Six Agent Runtimes

- Repo: https://github.com/ConardLi/garden-skills (⭐10,847)
- Source: GitHub Trending (daily, all languages)

## Why this is worth watching

garden-skills ships five production-ready agent skills targeting web design, image generation, knowledge retrieval, and document production — with explicit support for six agent runtimes simultaneously: Claude Code, Claude.ai (web), Cursor, Codex CLI, Gemini CLI, and OpenCode. The cross-runtime commitment at launch is structurally significant: it means the skills are tested against each runtime's actual execution environment, not just theoretically compatible.

The skill categories cover output types that agents produce for human consumption (web pages, presentations, images, articles, knowledge summaries), not internal computation steps. This positions garden-skills at the intersection of L4 (capabilities the agent has) and L6 (artifacts consumed by humans).

## What stands out immediately

- **Six runtime targets on launch**: Claude Code, Claude.ai web, Cursor, Codex CLI, Gemini CLI, OpenCode — covers both Anthropic-centric and multi-provider agent ecosystems; notably includes Claude.ai web (the consumer interface, not just the developer CLI)
- **Five distinct output-category skills**: web-video-presentation (16:9 web decks with 23 themes), web-design-engineer (web pages + dashboards, 25 style recipes), gpt-image-2 (image generation, 79 structured prompt templates), kb-retriever (local knowledge base retrieval without context flooding), beautiful-article (source-to-article transformation, 11 theme profiles)
- **Version discipline per skill**: each skill maintains independent versioning (v0.1.0 through v1.3.0) — signals that skills are maintained as discrete components, not a monolithic repo
- **`kb-retriever` addresses a real agent failure mode**: "local knowledge base retrieval without flooding context" is a precise response to the problem where naive RAG dumps too much retrieved content into context, degrading generation quality
- **79 structured prompt templates for image generation**: templates in a skill are deterministic quality levers — they reduce prompt-engineering variance for a use case where result quality is highly prompt-sensitive
- **10,847 stars** at time of scan — substantial traction for a skill collection, suggesting user demand for curated, tested cross-runtime skills vs. rolling-your-own

## Why clawfit should care

garden-skills and archify (also tracked today) are two signals for the "production-tested cross-runtime agent skill collection" format. The pattern — curated skills with multi-runtime installation and versioned maintenance — is now appearing repeatedly in the top GitHub trending repos. This is not a new taxonomy category (awesome-agent-skills tracked April 2026, scientific-agent-skills tracked August 2026), but the volume and quality signal suggest the format is maturing from early-adopter to mainstream practice.

The `kb-retriever` skill is specifically relevant to clawfit's `statefulness` and `network` filter dimensions. If agents using garden-skills' kb-retriever can query local knowledge bases without network calls, that shifts what's feasible for `network: offline` configurations — a local knowledge base becomes a capability substitute for some types of `network: online` document retrieval.

Also notable: garden-skills' inclusion of Claude.ai web (consumer interface) alongside Claude Code (developer CLI) acknowledges that non-developer users are deploying agent skills through the web interface. This has no current analogue in clawfit's agent registry, which focuses on developer-facing runtimes.

## Preliminary interpretation

Current best reading:
- **Level 4 — Capabilities / Skills / MCP**: primary. garden-skills adds bounded, well-defined capabilities to existing agent runtimes — it does not itself orchestrate agents, manage memory, or define workflows.
- **Level 6 secondary** (weak): skills that produce web presentations, articles, and designed web pages for human viewing operate at the human interface layer. The output is a human-facing artifact, even though the skill itself lives at L4.

Cross-signal: garden-skills (10.8k★, Aug 26) + archify (17.4k★, Aug 26) = two same-day signals for "cross-runtime portable agent skill." The pattern is already recognized in the taxonomy; no canonical section change required. The two-signal rule for a new sub-type is not met because this sub-type already has documented entries.

## Claims to verify

- Whether each runtime's installation path has been actively tested and maintained, or whether "six runtimes" is aspirational documentation that deteriorates as runtimes update
- Whether the `kb-retriever` skill's "no context flooding" guarantee relies on a fixed retrieval budget or adapts to available context window size — the distinction matters for large-context models (Qwen3.8-Flash-Next at 262k context vs. GPT-4o at 128k)
- Whether the 79 image prompt templates are Claude-specific or provider-agnostic — if they embed Claude-specific syntax, the cross-runtime claim for gpt-image-2 may be nominal for non-Claude runtimes
- Star growth curve: 10.8k total at time of scan — whether this reflects a trending spike or sustained growth; issue resolution rate and PR merge cadence as quality signals

## Status

- Tracking: first signal 2026-08-26
- Stars: 10,847 — above 100-star threshold; above 5k threshold in principle
- Registry decision: skip this cycle. Skill collections do not map to current agents.json/llms.json/hardware.json schema. The registry tracks agent runtimes, models, and hardware, not skill libraries.
- Schema watch: `skill_output_types: [code | prose | diagram | web-page | image | presentation]`; `runtime_coverage: [single | multi-runtime | all-major]`; knowledge retrieval capability field
- Watch: whether kb-retriever spawns a standalone MCP server variant; whether Gemini CLI and OpenCode support is actively tested across skill updates; whether garden-skills contributes to or references the Agent Plugins v1.0 format
