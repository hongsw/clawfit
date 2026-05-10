# Research Watch: Awesome-Agent-Harness — Formal Survey of LLM Agent Execution Harnesses

- Repo: https://github.com/Gloriaameng/Awesome-Agent-Harness
- Also see: https://www.preprints.org/manuscript/202604.0428 (preprint v2, DOI 10.20944/preprints202604.0428.v2); https://arxiv.org/abs/2603.25723 (companion: Natural-Language Agent Harnesses, Pan et al., March 2026); https://arxiv.org/abs/2604.25850 (companion: Agentic Harness Engineering, observability-driven evolution, April 2026); `docs/research-watch/2026-04-11-harness-engineering-paradigm-shift.md` (adjacent signal); `docs/research-watch/2026-04-06-langchain-deepagents.md` (L2 peer surveyed in the matrix)

## Why this is worth watching

This is the first preprint-backed, peer-reviewed survey to formalize agent harnesses as a named discipline with LTS (labeled-transition-system) semantics rather than treating them as engineering folklore. The paper covers 110+ papers and 23 production systems, producing a six-component compositional model (E, T, C, S, L, V) that is structurally distinct from any taxonomy this project currently uses. It arrives at the same moment as two sibling arXiv preprints on the same problem — Natural-Language Agent Harnesses (2603.25723) and Agentic Harness Engineering (2604.25850) — which together constitute the first multi-paper academic cluster around harness engineering, not agent benchmarking. The thesis is load-bearing for clawfit's L2 classification: "The agent execution harness — not the model — is the primary determinant of agent reliability at scale."

## What stands out immediately

- **Star count and license.** 187 stars, CC-BY-4.0. Below the 5k registry threshold by a wide margin. This is an academic survey repo, not a deployable tool; the relevance is definitional and taxonomic, not as a registry candidate.

- **Six-component formal model: H = (E, T, C, S, L, V).** The tuple is:
  - **E — Execution Loop:** observe-think-act cycles, termination conditions, error recovery
  - **T — Tool Registry:** typed tool catalog, routing, schema validation, monitoring
  - **C — Context Manager:** what enters the context window, compaction strategy, retrieval layer
  - **S — State Store:** cross-turn and cross-session persistence, crash recovery
  - **L — Lifecycle Hooks:** auth, logging, policy enforcement, instrumentation
  - **V — Evaluation Interface:** action trajectories, intermediate states, success signal detection
  The model applies a completeness matrix (✓ / ≈ / ✗) across 23 systems including Claude Code, OpenHands, MetaGPT, LangChain, LangGraph, SWE-agent, MemGPT, AutoGen, and PRISM/OpenClaw.

- **Production evidence is specific and verifiable.** Three concrete data points are cited:
  - Grok Code Fast 1: improved from 6.7% to 68.3% on SWE-bench through harness modifications alone (claim to inspect — methodology not detailed in the GitHub README; requires preprint access for the ablation design).
  - Stripe Minions: 1,300 PRs weekly with zero hand-written code — cited as a deployed harness case.
  - METR finding: benchmark-passing PRs show 24.2 pp lower human merge rates — cited as an evaluation-harness gap signal.
  These figures are the strongest production-evidence citations seen in a harness-domain survey in this taxonomy to date. They should be treated as claims to inspect pending independent confirmation of methodology.

- **Five-category system taxonomy.** The survey classifies the 23 systems as: Full-stack (PRISM/OpenClaw, AIOS, OpenHands, SWE-agent); Multi-agent (MetaGPT, AutoGen, ChatDev, CAMEL); General frameworks (LangChain, LangGraph, LlamaIndex); Specialized (MemGPT, Voyager); Capability modules and evaluation infra (HAL, AgentBench). This taxonomy partially overlaps with clawfit's L1–L5 stack but draws different cuts: LangChain is a "General Framework" here vs. L2 in the clawfit map; MemGPT is a "Specialized harness" here vs. L5 in the clawfit map.

- **Nine open challenges are named, not vague.** Concretely: (1) security/sandboxing — 15–35% container escape rates observed; (2) evaluation standardization; (3) protocol interoperability (MCP, A2A); (4) runtime context management; (5) tool registry design; (6) memory architecture; (7) planning/reasoning integration; (8) multi-agent coordination; (9) compute economics — 1M tokens/task average cited. The container escape rate figure (15–35%) is the most alarming specific figure and warrants citing if clawfit adds security posture as a scoring axis.

- **Author affiliation and preprint status.** Authors include affiliations at Dalian University of Technology (Wang), Xiaohongshu/Little Red Book (Chen). Preprint on Preprints.org as v2, described as "under review." Not yet peer-reviewed or arXiv-indexed; Preprints.org is a non-peer-reviewed preprint server. This matters for citing specific figures as validated facts.

- **Harness explicitly distinguished from orchestration and agent.** The survey frames harness as orthogonal to both: agent = model + reasoning capability; orchestration = multi-agent coordination pattern; harness = execution infrastructure that wraps both. This tripartite distinction is not made anywhere in clawfit's current reference documentation.

- **Companion preprints form a cluster.** arXiv:2603.25723 (Natural-Language Agent Harnesses, March 2026) proposes externalizing harness logic as portable natural-language artifacts executed by an Intelligent Harness Runtime — which is architecturally similar to the CLAUDE.md + AGENTS.md patterns clawfit already tracks. arXiv:2604.25850 (Agentic Harness Engineering, April 2026) proposes observability-driven automatic evolution of coding-agent harnesses and reports +7.3 pp on Terminal-Bench 2 with transfer gains of 5.1–10.1 pp on SWE-bench-verified. Together these three papers constitute a nascent academic sub-field forming around harness engineering — a field that clawfit's L2 classification is implicitly about.

## Why clawfit should care

**1. The ETCSLV model is a rigorous alternative vocabulary for clawfit's L2/L4/L5 boundary decisions.** The current taxonomy assigns tools to L2 (harness/orchestration), L4 (capability/tool), and L5 (memory/context) using heuristics derived from observation. The ETCSLV decomposition maps those heuristics onto formal components: C (context management) is the L5 boundary; T (tool registry) is the L4 boundary; E + L (execution loop + lifecycle hooks) are L2 core; S (state store) spans L4a and L5; V (evaluation) is an unmapped component. Specifically, tools like Ruflo and Vibe-Trading that collapse L2/L4/L5 simultaneously can now be analyzed as "high ETCSLV completeness" rather than described as multi-layer collapses. This is more precise language for the notes in reference-levels.md.

**2. The five-category harness taxonomy diverges from clawfit's layer map in analytically useful ways.** The survey puts LangChain in "General Frameworks" while clawfit calls it L2. The survey puts MemGPT in "Specialized harnesses" while clawfit calls it L5. These divergences are not errors in either taxonomy — they reflect different classification axes. The survey classifies by architectural completeness (how many of ETCSLV are present); clawfit classifies by architectural role (where in the stack does the tool primarily operate). A tool with full ETCSLV completeness (like OpenHands) would be L1 in clawfit (it IS the base runtime, not a harness over something else). A tool with E + L only (like a minimal lifecycle hook library) would be L2 in clawfit despite limited ETCSLV coverage. Neither axis is wrong; they answer different questions. clawfit's current docs do not acknowledge this axis difference.

**3. The V component (evaluation interface) is not modeled anywhere in clawfit.** The survey treats evaluation infrastructure — action trajectory logging, intermediate state capture, success signal detection — as a first-class harness component. clawfit's registry has no evaluation axis. The METR finding (24.2 pp merge-rate gap between benchmark-passing and human-merge-rate PRs) is precisely the kind of signal that an evaluation component would surface. If clawfit ever adds an `evaluation_support` dimension to the recommendation engine, the V component definition from this survey is the cleanest available prior art.

**4. The 15–35% container escape rate figure is the most alarming security signal in the current watch queue.** If this figure is validated, it means a non-trivial fraction of sandboxed agent deployments have observable boundary violations. clawfit's `governance_need: hard` profile currently has no way to surface sandboxing reliability as a filter dimension. The S (state store) and L (lifecycle hooks) components in the ETCSLV model map most directly to where these failures originate.

**5. The harness-vs-orchestration-vs-agent tripartite distinction clarifies a recurring ambiguity in clawfit research notes.** Several prior entries (Ruflo, OpenManus, Vibe-Trading) describe multi-layer collapses where it is unclear whether the tool is "a harness that includes memory" or "an agent that includes a harness." The survey's vocabulary resolves this: a system is a harness to the extent it provides ETCSLV infrastructure around a model; it is an agent to the extent the model's reasoning is the primary product. Ruflo and Vibe-Trading are harnesses (ETCSLV-heavy, model-agnostic at the infrastructure layer) even though they include memory (S component). OpenManus is closer to an agent (E is central; T is accessory; S and L are thin; V is absent).

## Preliminary interpretation

Current best reading:

- **Level 2 — Meta wrappers / harnesses / orchestration layers** (primary, as a definitional reference). The survey does not itself deploy as a tool, but it defines, formalizes, and benchmarks the L2 layer. Its completeness matrix is the first tool-independent rubric for evaluating how much of the harness surface any specific L2 candidate implements. Categorizing the survey itself as L2 reflects its role: it is the academic definition layer for the harness concept, the same way a language specification sits at the layer it defines rather than at the layer that implements it.

- **Level 5 — Memory / MCP / context layer** (secondary, via C and S components). The survey's treatment of context management (C) and state persistence (S) as first-class harness components overlaps directly with clawfit's L5 definition. Several L5 entries in the clawfit map (MemGPT, AgentDB, claude-mem) appear in the survey's completeness matrix as "specialized" — the survey provides the first structured comparison of these against each other within a shared component rubric.

- Notable: The V (evaluation) component has no clawfit-level equivalent. It is not L1–L7. This may signal that an eighth layer — or a cross-cutting evaluation axis — is missing from the clawfit taxonomy. Too early to act on this; single-survey signal.

- The companion preprint arXiv:2603.25723 (Natural-Language Agent Harnesses) maps to L3 in clawfit's taxonomy — it proposes externalizing harness logic as portable natural-language governance artifacts, which is structurally identical to the CLAUDE.md / AGENTS.md SSOT pattern clawfit already tracks at L3. The connection between natural-language harness specifications and L3 SSOT governance files is worth documenting explicitly in the L3 section notes.

## Status

- 187 stars, CC-BY-4.0, Preprints.org v2 (under review, not yet peer-reviewed). Well below the registry promotion threshold — this is definitional/taxonomic reference material, not a deployable tool. Track the preprint for peer-review acceptance or arXiv cross-listing as the primary promotion signal. No reference-levels.md modification warranted from this single survey. The ETCSLV vocabulary should be considered when the L2 sub-type naming project (swarm-orchestration harness, GUI desktop harness, template-driven swarm harness) reaches a consolidation cycle — the model provides a principled axis for distinguishing sub-types by component completeness rather than by UX or deployment form factor alone.
