# Research Watch: OpenScience — Open-Source AI Workbench for Scientific Research

- Repo: https://github.com/synthetic-sciences/openscience (⭐1,453+)
- Source: MarkTechPost (2026-07-05); GitHub trending; positioned as open alternative to Anthropic Claude Science
- Alt repo: https://github.com/ai4s-research/open-science (related project, same pattern)

## Why this is worth watching

OpenScience is an open-source AI workbench for scientific research that runs the full research loop — literature review, hypothesis generation, code, experiment, analysis, write-up — as a continuous agentic session. It is explicitly framed as an open alternative to Anthropic's Claude Science (launched late June 2026) and runs locally on user infrastructure.

The structural pattern is important: OpenScience is an L3 "research orchestration system" — a layer above a coding agent (L2) that governs the research workflow through a structured plan-and-execute loop, not just a single agent invocation. It includes a local server hosting the workspace UI, agent runtime, and tool layer, with specialist sub-agents for biology, physics, and ML domains. This represents the first open-source signal for "scientific research agent orchestration" as a distinct category.

1,453 stars in approximately 3 weeks of existence suggests substantive uptake in the academic/research community.

## What stands out immediately

- **Continuous research session model:** OpenScience runs a single session from goal to write-up, treating the research loop (hypothesis → experiment → analysis → revision) as the atomic unit of work, not individual LLM calls.
- **Domain specialist sub-agents:** separate agent personas for biology, physics, and ML research — plus a critique sub-agent and literature-review sub-agent with read-only plan mode. Multi-agent specialization within a single scientific domain context.
- **MCP + skills architecture:** tool layer is MCP-native with scientific connectors (literature databases, code execution, lab data ingestion), allowing third-party MCP servers to extend the platform.
- **Local server architecture:** not a cloud service; runs on user hardware with a workspace UI. Designed for institutional or individual use without vendor data access.
- **Model-agnostic by design:** supports Claude, GPT family, Gemini, and local models — no hardcoded dependency on any provider.
- **Explicit Claude Science alternative framing:** the project positions itself as the open-source counterpart to Anthropic's Claude Science, signalling awareness of the commercial competitor landscape.
- **Apache 2.0 license:** permissive; institutional adoption not gated by commercial agreements.

## Why clawfit should care

clawfit's current task taxonomy includes `code-gen`, `qa`, `orchestration`, and `research`. The `research` task is currently underspecified — it maps to a single class of agents rather than distinguishing "search/synthesis research" from "scientific research with experiment execution."

OpenScience surfaces a distinction: general research agents (Perplexity-like, Deep Research) perform retrieval and synthesis; scientific research agents run code, execute experiments, and produce reproducible artifacts. These have different requirements:
- Scientific research needs code execution sandboxing (L7) and data provenance, not just web search
- The latency constraint is different: scientific experiments run over hours/days, not seconds
- The cost model is dominated by experiment execution compute, not LLM token cost

If scientific research agent orchestration becomes a stable category (needs a second signal), clawfit would benefit from a `task: scientific-research` dimension distinct from `task: research`.

Additionally, OpenScience's MCP-native tool layer and domain-specialist sub-agent architecture is a concrete example of the L3/L4 interaction that clawfit's taxonomy models but has few examples of in the registry.

## Preliminary interpretation

Current best reading:
- **Level 3 — Team workflow / Research orchestration** (primary): governs the full research workflow with structured planning, specialist sub-agents, and a continuous session model
- **Level 5 secondary:** critique sub-agent functions as an evaluation layer within the session

Not L2: OpenScience orchestrates agent workflows rather than simply wrapping a single coding agent. The presence of sub-agents, a planning layer, and structured workflow phases places it above the L2 harness tier.

Cross-watch: Claude Science (Anthropic commercial product, June 2026) — OpenScience is the open-source counterpart. Also: Prime-RL (2026-07-15) — reinforcement learning for agentic research; different approach to the same "agents doing science" problem.

## Claims to verify

- Whether OpenScience's "continuous session" model actually maintains coherent research state across multi-hour experiments, or whether it loses context and requires manual re-prompting
- Whether the domain specialist sub-agents have meaningfully different system prompts / tool access, or whether they are superficially persona-differentiated versions of the same agent
- Whether results are reproducible: does the "write-up" output cite the experiments run in the session with sufficient detail for independent reproduction?
- Star velocity: 1,453 stars in ~3 weeks may plateau if the scientific research community engagement doesn't sustain beyond initial launch interest

## Status

- First signal for "open-source scientific research agent orchestration." 1,453 stars above minimum threshold (100). Launched July 5, 2026 (within 6-month window).
- Registry consideration: deferred — no deterministic cost/latency data; scientific research task has no current clawfit scoring dimension.
- Pattern watch: if a second "scientific research workbench" signal appears, `task: scientific-research` and `harness_type: research-orchestration` become eligible for taxonomy addition.
- Open question: how does OpenScience handle experiment failure modes and recovery? A research workbench that requires manual intervention on every failed code execution is an L2 harness, not an L3 orchestrator.
