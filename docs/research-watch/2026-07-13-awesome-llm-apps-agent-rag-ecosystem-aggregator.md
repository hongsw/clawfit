# Research Watch: awesome-llm-apps — Runnable Agent & RAG Pattern Gallery

- Repo/Link: https://github.com/Shubhamsaboo/awesome-llm-apps
- Source: GitHub Trending Daily #4

## Why this is worth watching
At 119k stars with 408 new stars in a single trending window, awesome-llm-apps is the highest-velocity community pattern gallery for LLM application development currently tracked here. Its 15 categories span clawfit's L2–L6 layers simultaneously — multi-agent orchestration, MCP integrations, RAG pipelines, memory systems, voice agents, and generative UI — making it a broad ecosystem adoption signal rather than a single-layer tool.

## What stands out immediately
- 100+ runnable templates; Python 54.6%, TypeScript 21.6%, JavaScript 16.4%; Apache 2.0
- Frameworks featured: CrewAI, AG2, Google ADK, OpenAI Agents SDK — all L2 harnesses
- Provider-agnostic across Claude, Gemini, OpenAI, xAI, Qwen, Llama; model-switch via config
- Categories map across layers: Starter/Advanced Agents (L1/L2), Multi-agent Teams (L2), MCP Agents (L4c), RAG Systems + Memory-enabled Apps (L5), Voice AI + Generative UI Agents (L6)
- **Always-on Agents** category (background/scheduled execution) represents a `statefulness: persistent` deployment pattern underrepresented in clawfit's current agents.json
- **LLM Optimization Tools** category covers cost and token reduction — directly adjacent to clawfit's cost scoring axis
- No per-app latency or cost metadata present; scoring signals are qualitative, not structured

## Why clawfit should care
The collection is a practitioner adoption signal: categories that attract runnable templates reveal which ecosystem layers are maturing in actual use. The LLM Optimization Tools section is worth a follow-up pass for discrete tools that could surface cost-axis signals. The Always-on Agents category warrants a check against clawfit's `statefulness` filter — if common patterns there require persistent state, the filter coverage gap is real. The mix of local and cloud deployments aligns with clawfit's `hardware` and `network` dimensions but carries no structured metadata to extract directly.

## Preliminary interpretation
Current best reading:
- **Cross-layer discovery artifact (L2–L6 coverage)** — does not cleanly map to a single level

The preliminary L3 suggestion misapplies the layer definition: L3 is "team harness / executable SSOT / governance layer," describing tools that govern agent behavior at runtime. awesome-llm-apps is a discovery and reference surface, not a governance mechanism. Its dominant example content (CrewAI, AG2, ADK orchestration) is L2, but the repo itself spans all relevant levels simultaneously and belongs outside the per-level taxonomy as a pattern library.

## Status
- Watching as ecosystem breadth signal; not a registry candidate (no single deployable tool). Follow up: audit LLM Optimization Tools sub-category for cost-axis entries; revisit Always-on Agents for `statefulness: persistent` gap coverage.
