# Research Watch: Software After AI — Tom Tunguz Harness-Era Thesis

- Repo: https://www.tomtunguz.com/harnessing-ai/
- Also see: GeekNews front page #20 (35 points); no associated code repo — this is a VC thesis post

## Why this is worth watching

Tom Tunguz (Redpoint, Theory Ventures) has published a structured 7-component breakdown of what he calls "the harness" — the layer that converts a raw LLM into a reliable production agent — and frames it as the primary competitive moat in post-model software. This is not a tool announcement; it is a mainstream VC articulation of an architectural category that clawfit's taxonomy independently arrived at as Level 2. The framing gaining VC-endorsed language signals that harness infrastructure is entering the enterprise investment thesis cycle, not merely the developer-community discovery phase.

## What stands out immediately

- Tunguz names 7 discrete harness components: (1) Context & Memory — bespoke retrieval plus a "context database" of business SOPs; (2) Tools & Action — external capability registry with argument validation and approval gates; (3) Orchestration & Loop — the think-act-observe-repeat cycle including planning, decomposition, and learning; (4) State & Persistence — checkpoints and artifact storage for failure resilience; (5) Sandbox & Compute — isolated workspaces with controlled network access and credential management; (6) Observability & Governance — tracing, logging, evaluation-as-regression-testing, and human oversight gates; (7) Cost & Workflow Optimization — model selection and knowledge distribution decisions
- The competitive framing is explicit: "What happens when every company has access to the same model? The best riders win." Model access is not the moat; harness engineering is
- Only one tool is cited by name: MCP (Model Context Protocol), described as "the connective tissue" for tool exposure. No specific harness vendors or open-source projects are named, which is notable — the market is framed as open, not settled
- The argument structure maps the "thousands of separate markets" framing: major labs dominate prioritized verticals; startups win by building superior harness infrastructure for the rest
- This is a thesis post, not a product announcement. Claims here are analytical, not empirically validated by a shipped system

## Why clawfit should care

Tunguz's 7 components map almost directly onto clawfit's taxonomy split between L2 (orchestration and loop), L3 (governance and SSOT), L4 (tools and capabilities), and L5 (memory and context). The fact that a prominent VC collapses these into a single "harness" category is both a validation signal and a potential distortion risk: if the market starts using "harness" as an undifferentiated term, clawfit's more granular L2/L3/L4/L5 split becomes a differentiated analysis asset rather than an academic exercise.

More immediately: the Observability & Governance component (#6) is under-represented in the current registry. No current registry agent carries a validated `governance_need: hard` flag with an associated tracing/evaluation backend. The Cost & Workflow Optimization component (#7) is the closest to clawfit's scoring model (model selection weights), but the "knowledge distribution" framing — deciding what should be in prompts vs. fine-tuned weights vs. retrieved context — is not a current scoring axis.

The MCP citation as "connective tissue" confirms that L5/L4 boundary via MCP is now VC-legible, not just community-legible. This raises the salience of MCP-native tool registries as a scoring consideration.

## Preliminary interpretation

Current best reading:
- **Level 2 — Meta wrappers / harness / orchestration layers (primary):** The thesis is fundamentally about the orchestration-and-loop layer (component #3) and what wraps it. The other six components are either sub-layers (L4: tools, L5: memory/context, L3: governance) or cross-cutting concerns (L7: observability, L7: compute isolation) that Tunguz bundles under a single "harness" abstraction for a VC audience
- This is a **meta-signal** (ecosystem thesis), not a tool, so it does not receive a registry entry and does not trigger a map mutation. It is evidence that the L2 category is being named and invested in at the capital layer

## Status

- Ecosystem-thesis signal, no registry candidate. No map mutation warranted.
- Confirms Level 2 harness classification as the current primary competitive layer in the VC investment thesis; accelerates the case for formalizing the L2 sub-type taxonomy (orchestration-only harnesses vs. full 7-component harness stacks).
- Flag for schema analyst: Tunguz's component #6 (Observability & Governance with evaluation-as-regression-testing) is the most underdeveloped area in the current registry. If a tool emerges that implements this component as a standalone L2 module, it would be the first signal for a dedicated "harness observability" sub-type. Watch for harness products naming these 7 components in their own documentation — VC-thesis language propagates into product marketing within 6–12 months of publication.
