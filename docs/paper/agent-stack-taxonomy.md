# The AI Agent Stack: A 7-Layer Taxonomy of Agent Runtime Infrastructure

**Hong Seung-won** (`hongsw`), Anthropic Claude Sonnet 4.6 (AI research assistant)  
*clawfit project — https://github.com/hongsw/clawfit*  
*Submitted: May 2026 · Draft v0.1*

---

## Abstract

The AI agent tooling ecosystem has grown faster than any accompanying conceptual framework. Practitioners who wish to select, compose, or evaluate agent infrastructure face a proliferating landscape of runtimes, harnesses, skill packs, memory systems, and hardware substrates that existing taxonomies inadequately distinguish. We present a **7-layer taxonomy** of agent runtime infrastructure derived from empirical daily monitoring of 210+ open-source signals over 43 days (2026-03-28 to 2026-05-10). The taxonomy characterizes each layer by *architectural role* rather than by adoption or maturity. We document seven recurring meta-patterns that emerged from continuous observation — including multi-layer vertical clustering, spec-first governance convergence, and the cost asymmetry between computer-use and structured-API interaction modalities — and identify four open problems at layer boundaries. Our primary contribution is an operationally grounded taxonomy that practitioners can use for tool selection, and researchers can use as a structured lens for ecosystem analysis.

---

## 1. Introduction

A developer asking "which AI coding agent should I use?" in early 2026 faces not one question but at least five: which *base runtime* to adopt, which *harness* (if any) to layer above it, whether a *team coordination layer* is needed, which *skills and tools* to compose into the agent's capability surface, and how to handle *memory, context, and human interfaces*. These are distinct architectural decisions, yet most surveys and recommender systems treat agent selection as a single-dimensional choice.

The pace of ecosystem growth compounds the problem. Our daily monitoring tracked over 5 new significant signals per day on average — a rate that outstrips any monthly or quarterly survey cycle. By the time a static survey reaches publication, its taxonomy is already partially obsolete.

This paper makes three contributions:

1. **A 7-layer taxonomy** (§3) that decomposes agent infrastructure by architectural role — what a component *does* in a system, not how popular or mature it is.

2. **A continuous monitoring methodology** (§4) for tracking ecosystem signals at daily resolution, including quality criteria, deduplication, and promotion thresholds.

3. **Seven empirical meta-patterns** (§5) observed across 210+ signals, which are not predictable from any single tool's documentation but emerge from cross-signal analysis.

The taxonomy is not a maturity ladder: a Level 4 capability plug-in is not "more advanced" than a Level 1 base runtime. It is a map of *co-existing architectural roles* that must all be addressed in a production agent system.

---

## 2. Related Work

**Agent surveys.** Several surveys cover LLM-based agents from an NLP/ML perspective [CITATION], focusing on reasoning, tool use, and planning capabilities. These surveys classify agents by *task type* or *model architecture* rather than by the infrastructure layers in which they operate.

**Harness formalization.** Most directly related is Awesome-Agent-Harness [Meng 2026], which formalizes the execution harness layer as a 6-component model H = (E, T, C, S, L, V): execution loop, tool registry, context manager, state store, lifecycle hooks, and valuation interface. This work defines what sits at our Level 2 with precision. Our taxonomy is complementary: we treat the harness as one of seven layers, connecting it above (to governance and capability layers) and below (to the base runtime and inference substrate).

**Agent benchmarks.** SWE-Bench Verified [Jimenez et al. 2024] and its successors evaluate coding agent *capability*. Our taxonomy is orthogonal: it characterizes *infrastructure role*, not benchmark performance. Indeed, one of our empirical findings (§5.6) is that SWE-Bench Verified reached saturation as a frontier differentiator by April 2026.

**Recommender systems.** Several tools recommend LLMs for specific tasks (vLLM Recipes, llm.report). clawfit, the software artifact accompanying this paper, recommends (agent, LLM, hardware) triples using the taxonomy as its classification backbone.

---

## 3. The 7-Layer Taxonomy

**Design principle.** Layers are defined by *architectural role* — the primary function a component performs in a working agent system — not by implementation language, license, or deployment mode. A component's primary layer is determined by where the majority of its behavior lives; secondary layer assignments are recorded when a component genuinely operates at a second layer.

### Layer 1 — Base Runtimes

**Definition.** The primary agent surface: the component that runs the agent loop, manages tool calls, and presents the LLM's actions to the user or downstream system.

**Discriminating question.** *If you remove this component, can the agent still execute tasks?* If no, it is Level 1.

**Representative entries.** Claude Code (Anthropic, ~250k★), opencode (anomalyco, 157k★, MIT, terminal-first, provider-agnostic), pi/earendil-works (46.5k★, MIT, coding CLI + unified LLM API), Aider (35k★), Cline (59k★, VS Code), OpenManus (56.2k★, Python, general-purpose), Goose (Block Inc.), Roo Code (23k★, VS Code multi-role).

**Sub-types observed.** Terminal-native (opencode, pi, Aider), IDE-threaded (Cline, Roo Code, Continue), provider-agnostic (opencode, pi — support 30+ LLM providers), model-specialized (DeepSeek-TUI, targeting a single model vendor), domain-specialized (TradingAgents 67k★ for finance, Shannon 36k★ for security).

**Companion axis.** Inference runtime substrates (Ollama, llama.cpp, vLLM, MLX, antirez/ds4) are not Level 1 agents — they provide the model execution layer *beneath* L1 but have no agent UX. We document these in a companion reference note rather than as taxonomy members.

### Layer 2 — Meta Wrappers / Harnesses

**Definition.** A component that wraps, orchestrates, or supervises one or more Level 1 agents without itself *being* the primary user-facing agent surface.

**Discriminating question.** *Does this component add orchestration, lifecycle management, or multi-agent coordination above the base runtime?* If yes, it is Level 2.

**Formalization.** Consistent with Awesome-Agent-Harness [Meng 2026], a harness provides some subset of: **E**xecution loop management, **T**ool registry, **C**ontext management, **S**tate store, **L**ifecycle hooks, **V**aluation interface. Unmapped component: *valuation interface* (V) has no current representation in our L1–L7 taxonomy — an open gap noted in §6.

**Representative entries.** helmor (dohooo, 1k★, macOS-native multi-agent workbench, full dev loop via git-worktree), ruflo (38.8k★, Claude Code swarm orchestrator), deepagents (LangChain/LangGraph, production harness), Microsoft Agent Framework v1.0 (graph-based, AutoGen+SK consolidation), DureClaw (multi-machine orchestration), Mendral (harness-outside-sandbox topology), Vibe-Trading (HKUDS, 6.2k★, 29-team swarm for finance).

**Named topology.** "Harness-outside-sandbox" — the agent control loop lives outside the execution environment; credentials never enter the sandbox; stateless execution is cattle. First named by Mendral/Docker co-founders [Luzzardi & Alba 2026]; independently instantiated by OpenAI Agents SDK and Freestyle.

### Layer 3 — Team Workflow / Executable SSOT

**Definition.** A component that governs *what* agents do — their roles, behavioral specs, sprint contracts, or operational constraints — as a human-readable, version-controlled source of truth.

**Discriminating question.** *Does this component define agent behavior rules that apply across multiple sessions or multiple agents?* If yes, it is Level 3.

**Representative entries.** OpenSpec (Fission-AI, 46.2k★, spec-first development framework generating proposal+spec+design+tasks artifacts), acai.sh (ACID-tagged requirement SSOT), ouroboros (AI-generated convergence specs via elicitation), DureClaw (cross-machine team SSOT), gsd/get-shit-done (52k★, prose spec-driven), gitagent (git as agent definition distribution layer).

**Emerging sub-type.** Three independent signals in six days (acai.sh, ouroboros, OpenSpec) define a "pre-execution spec layer" pattern: structured artifacts *produced before any coding begins* that govern agent behavior across 25+ tools. A fourth signal is required for formal sub-type promotion per our protocol.

### Layer 4 — Capability / Skill / Plugin

**Definition.** A component that extends what an agent *can do* — skills, tools, MCP servers, or plug-ins that add capabilities to an existing L1 agent without changing its core loop.

**Discriminating question.** *Does this component add new task capabilities to an existing agent?* If yes, and it does not provide its own agent loop, it is Level 4.

**Sub-layers observed.**

- **L4a — Memory & context tools.** Components that manage the agent's knowledge during or across sessions: cognee, claude-mem, mem0, Engram (MCP-native structured memory), wuphf (agent-maintained markdown wiki), memvid (portable-binary single-file memory).

- **L4b — Domain skill packs.** Curated collections of skills targeting specific professional domains: agency-agents (92.4k★, 144 agents across 12 professional verticals), marketingskills (23.7k★), obsidian-skills (20k★, knowledge workers), claude-plugins-official (Anthropic 1st-party, 18.9k★), VoltAgent/awesome-agent-skills (1,000+ skills).

- **L4c — Tool-use extensions / MCP servers.** Infrastructure tools that connect agents to external systems: n8n-mcp (19.5k★, 1,650+ integration nodes), browser-harness (self-healing CDP automation), codegraph (colbymchenry, 1.1k★, code knowledge graph — 94% tool-call reduction claim), Sub2API (subscription pooling gateway), context-mode (context window sandboxing).

**Maturation signal.** The skill marketplace has reached app-store scale: claudemarketplaces.com reports 150+ skills with ratings and 277k installs on a single Anthropic-published skill.

### Layer 5 — Memory, Research Loops & Observability

**Definition.** Cross-session or cross-agent systems for persistence, evaluation, and observability that are not task-specific (contrast with L4a memory *plugins* which are capability extensions for a specific agent).

**Representative entries.** Langfuse (25k★, production LLM observability — tracing, evals, prompt versioning), CC-Canary (per-session behavioral health monitoring), CocoIndex (7.7k★, incremental data pipeline engine for vector/graph DBs), local-deep-research (6.6k★, privacy-first LLM research tool, 10+ search engines).

**Inspectable memory sub-pattern.** Five independent implementations of agent-maintained human-readable memory emerged: (i) markdown+git (wuphf, GBrain), (ii) SQLite+MCP-native (Engram, Beads), (iii) portable-binary single-file (memvid). The pattern is now stable as a named L5 sub-type.

### Layer 6 — Human Interface / Multimodal

**Definition.** The surface through which humans interact with agents, or through which agents process and produce non-text modalities.

**L6a / L6b split (formalized 2026-05-05).** The previous unified L6 was split:

- **L6a — Retrieval-native knowledge stores.** Embed → index → retrieve → inject pipeline; the LLM is a *consumer* of the store (LightRAG, MinerU, RAG-Anything). Operational marker: the pipeline or human writes to the store.
- **L6b — LLM-native knowledge bases.** The LLM *writes and maintains* the knowledge artifact; no retrieval pipeline (wuphf, GBrain, Karpathy LLM Wiki pattern). Operational marker: the LLM writes to the store.
- **L6a structural sub-type.** PageIndex (28.2k★) rejects embedding entirely; an LLM reasons over a hierarchical TOC tree — neither classical L6a nor L6b. Candidate for L6c (reasoning-native retrieval); one signal, not yet promoted.

**Human interface sub-types.** IDE-threaded parallel agents (Zed 1.0, cmux), terminal-native (Warp, opencode), mobile-remote (Happy), voice I/O (Ghost Pepper for offline STT, VibeVoice for TTS/STT, Superwhisper), desktop document workspace (helmor, craft-agents-oss).

### Layer 7 — Infrastructure / Hardware

**Definition.** The compute substrate: cloud instances, edge devices, local hardware, and the inference engines that run on them.

**Representative entries.** AWS GPU Large, AWS CPU Medium, cloud-serverless (per-request), on-device Apple Silicon (M-series, DeepSeek V4-Flash offline), Google 8th-gen TPUs (agent-inference-specific), NVIDIA OpenShell (K3s-in-Docker sandbox runtime).

**Boundary note.** Level 1/Level 7 boundary collapse: computer-use agents (Claude Computer Use, trycua/cua, understudy) operate the full desktop stack — L1 agent behavior and L7 hardware interaction are fused. Empirical cost penalty: Reflex.dev benchmark reports vision-driven computer-use ≈45× more input tokens and ≈51× more wall-clock time than structured-API agents on identical tasks [Reflex 2026]. Recommendation: structured-API should be preferred wherever task structure permits; computer-use should carry an explicit cost caveat in any recommendation.

---

## 4. Methodology

### 4.1 Daily Signal Collection

We monitored six primary sources daily (Table 1) and four secondary sources when bandwidth permitted.

**Table 1. Tier 1 monitoring sources.**

| Source | Target | Cutoff |
|--------|--------|--------|
| GitHub Trending — All languages | Top 25, daily | ≥50 stars/day |
| GitHub Trending — Python | Top 15, daily | AI/agent-related |
| GitHub Trending — TypeScript | Top 15, daily | AI/agent-related |
| GeekNews (news.hada.io) | Top 30 stories | Korean AI/tool signals |
| Hacker News | Top 30 stories | ≥50 points |
| User GitHub stars (hongsw) | All new stars | Personal curation |

### 4.2 Quality Thresholds

A signal must satisfy at least one of:

- **Stars.** GitHub repository with ≥100 stars (research-watch entry) or ≥5,000 stars (registry entry).
- **Velocity.** ≥50 new stars/day as a proxy for active community interest.
- **Source trust.** Academic authors (arXiv, institutional affiliation), tier-1 engineering blogs (Brex, Cloudflare, Anthropic), or Hacker News ≥50 points.
- **Personal curation.** Explicitly starred by the monitoring author.
- **Novelty.** ≤6 months since first public release, or a significant release within the prior 14 days.

Signals not meeting any criterion are excluded without documentation. "Awesome-list" aggregators are excluded unless they introduce a new category.

### 4.3 Deduplication

Before processing a signal, we grep all existing `docs/research-watch/*.md` files for the repository URL. A match terminates processing; star-count updates on existing canonical entries are applied in-place without creating a new document.

### 4.4 Layer Classification Protocol

For each passing signal, a research-watcher agent reads the repository, classifies the primary and secondary layers, and writes a structured analysis. Layer assignment uses the discriminating questions in §3. Ambiguous cases are assigned to the layer where the component does *most* of its work; secondary assignments are recorded explicitly.

### 4.5 Promotion Thresholds

The taxonomy distinguishes three levels of evidence:

- **Research-watch document.** A new signal that passes quality thresholds. Does not modify the canonical taxonomy.
- **Scan note.** A signal that reveals a possible new pattern. Recorded as a dated discovery note in `reference-levels.md` with an explicit promotion threshold.
- **Canonical taxonomy entry.** A signal or pattern that meets the promotion threshold: ≥5,000 stars for a tool entry, or ≥2 independent signals for a new named pattern or sub-type.

The **single-signal promotion prohibition** is the key discipline mechanism: no new sub-layer, sub-type, or pattern is added to the stable taxonomy on the basis of one signal alone.

---

## 5. Empirical Meta-Patterns

The following patterns were not predicted by the taxonomy design; they emerged from observing 210+ signals over 43 days.

### 5.1 Multi-Layer Vertical Clustering

**Observation.** Domain-specialized tools tend to appear simultaneously at multiple layers within a short time window, not one layer at a time.

**Case study — Finance vertical.** Five independent finance-domain signals surfaced within one week (2026-05-01 to 2026-05-06): TradingAgents (L1, 67k★), virattt/dexter (L1, 23k★), agency-agents Finance division (L4b, within 92.4k★ pack), anthropics/financial-services (L4b, 8.5k★, 1st-party), Kronos (LLM axis, financial markets foundation model). The cluster spans ≥3 layers simultaneously.

**Implication.** Once a vertical cluster forms at ≥3 layers, new task types (e.g., `financial-research`, `financial-modeling`) should be added to recommendation schemas. Cluster detection is a leading indicator of schema extension needs.

**Other clusters observed.** Security/pentesting (Shannon + Strix), game development (Claude-Code-Game-Studios), marketing (marketingskills).

### 5.2 Multi-Vendor Anti-Lockin as a User Response Pattern

**Observation.** As LLM vendors converge on usage-based pricing (Anthropic Pro-tier removal April 2026, GitHub Copilot moving to token-metered AI Credits June 2026), the user-side response is a coordinated cluster of portability tools.

**Case study.** On 2026-04-28, three simultaneous high-signal tools appeared: cc-switch (52.8k★, CLI configuration switcher across Claude Code/Codex/Gemini/OpenCode), Sub2API (16.1k★, subscription-pooling gateway), cmux (15.6k★, terminal-multiplexed concurrent agents). A fourth tool, ComposioHQ/awesome-codex-skills, extended the cross-vendor skill schema to Codex CLI.

**Implication.** Provider lock-in is decreasing as a constraint. `vendor_lock_in` should be modeled as a near-zero cost for power users; cost and capability weights become more dominant.

### 5.3 Spec-First Governance Convergence

**Observation.** Three structurally distinct tools producing pre-execution specification artifacts emerged within six days (2026-05-03 to 2026-05-09):

- **acai.sh** — ACID-tagged requirement IDs embedded in code and tests
- **ouroboros** — AI-generated convergence specs via structured elicitation
- **OpenSpec** (46.2k★) — Human-authored delta artifacts (proposal + spec + design + tasks) portable to 30 tools

**Shared structure.** All three produce *governance artifacts before any code is written*, which then guide agent behavior across multiple tools and sessions. This distinguishes them from runtime prompt templates (L2 harness level) and from post-execution audit logs.

**Status.** Pattern named "pre-execution spec layer" as a candidate L3 sub-type. Promotion to canonical taxonomy awaits a fourth independent signal.

### 5.4 Layer 4 Skill Pack Domain Fragmentation

**Observation.** The L4b skill pack sub-layer, initially dominated by software-engineering skills, has fragmented across professional verticals at high adoption velocity.

**Data.** L4b packs observed: agency-agents (92.4k★, 12 professional verticals), marketingskills (23.7k★), obsidian-skills (20k★, knowledge workers), claude-plugins-official (18.9k★, Anthropic 1st-party general), anthropics/financial-services (8.5k★, 1st-party finance), Claude-Code-Game-Studios (10k★, game dev), mattpocock/skills (20k★, practitioner TypeScript engineering).

**Implication.** `task: code-gen` and `task: qa` are insufficient as task labels. Vertical-specific task types (`task: financial-research`, `task: game-dev`, `task: marketing-copy`) are needed in recommendation schemas.

### 5.5 L1/L7 Boundary Collapse — Computer Use

**Observation.** Computer-use agents (Claude Computer Use, trycua/cua, understudy) operate the full desktop — combining L1 agent UX with L7 hardware/OS interaction — in a way that cannot be cleanly classified at either layer.

**Empirical cost.** Reflex.dev (2026-05-06) measured identical tasks: vision-driven computer-use consumed 45× more input tokens and took 51× longer wall-clock than structured-API agents [Reflex 2026]. Quality also diverged (1 of 4 items found due to visible-fold blindness).

**Implication.** Any recommendation involving computer-use agents should carry an explicit cost caveat. We add `interaction_modality ∈ {structured_api, vision_computer_use, hybrid_dom_vision, terminal_text}` as a candidate scoring dimension.

### 5.6 Benchmark Saturation as a Taxonomy Signal

**Observation.** SWE-Bench Verified reached capability-saturation (multiple frontier models at ceiling) by April 2026 [OpenAI 2026]. A separate exploit-based invalidation was documented by Berkeley RDI (2026-04-12). Terminal-Bench 2.0 is emerging as a successor.

**Implication.** LLM preference weights based on SWE-Bench scores should carry lower confidence for frontier-tier models. Recommender systems should not treat benchmark parity as equivalent to capability parity until new benchmarks stabilize.

### 5.7 Institutional Entry Pattern at L1

**Observation.** The base runtime layer (L1) has historically been dominated by Anthropic, OpenAI, and open-source community projects. In April–May 2026, three institutional entrants appeared: NVIDIA OpenShell (NVIDIA, Apache-2.0, K3s-in-Docker sandbox runtime), OpenManus (FoundationAgents, from MetaGPT contributors, 56.2k★), and earendil-works/pi (Earendil Inc., 46.5k★, after org migration from solo developer badlogic).

**Implication.** L1 vendor diversity is increasing. Recommendation systems that implicitly assume two or three dominant runtimes may produce over-concentrated recommendations.

---

## 6. Open Problems

**P1. Provider-agnostic cost estimation.** Tools like opencode and pi support 30–75 LLM providers. A (agent, LLM) fixed-pair scoring model cannot express "any-of-N-providers at the time of query." The taxonomy needs a second-pass LLM selection step or a `provider_agnostic: true` flag with associated scoring logic.

**P2. The unmapped V component.** Awesome-Agent-Harness's valuation interface (V) — the feedback and evaluation surface within the harness — has no representation in our L1–L7 taxonomy. Our L5 (observability) partially covers ex-post evaluation, but in-loop valuation during harness execution is uncharacterized. A candidate "L2v" or "L2-eval" sub-component may be needed.

**P3. L3/L4c boundary — MCP CLAUDE.md injection.** codegraph (L4c, MCP code intelligence server) auto-injects global `~/.claude/CLAUDE.md` instructions machine-wide — a behavior previously seen only at L3 (team workflow / SSOT layer). If this pattern spreads to other MCP servers, the L3/L4c boundary requires formal re-examination. Promotion threshold: three independent MCP servers adopting machine-wide config injection.

**P4. Interaction modality as a scoring dimension.** The L1/L7 computer-use collapse (§5.5) and the emergence of offline multimodal agents require `interaction_modality` as an explicit scoring axis. Current schemas treat all L1 agents as equivalent on the interaction surface; the 45×/51× cost gap makes this untenable for production recommendations.

---

## 7. Conclusion

We presented a 7-layer taxonomy of AI agent runtime infrastructure, a daily-resolution monitoring methodology, and seven empirical meta-patterns observed over 43 days. The taxonomy characterizes layers by architectural role, not maturity or adoption, making it stable across the rapid-release cycles that characterize this ecosystem. The monitoring methodology, with its explicit quality thresholds and single-signal promotion prohibition, provides a replicable framework for tracking ecosystems at the velocity they currently evolve.

Our most unexpected finding is the regularity of **multi-layer vertical clustering**: when a domain (finance, security, game development) becomes important to the agent ecosystem, it tends to appear simultaneously at ≥3 layers rather than penetrating one layer at a time. This pattern functions as an early-warning signal for schema extension in recommendation systems.

The taxonomy and all tracked signals are maintained as an open dataset at https://github.com/hongsw/clawfit.

---

## References

*[Formatted references to be completed in v0.2. Key cited works: Meng 2026 (Awesome-Agent-Harness), Jimenez et al. 2024 (SWE-Bench), Reflex 2026 (computer-use cost benchmark), Luzzardi & Alba 2026 (harness-outside-sandbox topology), OpenAI 2026 (SWE-Bench saturation statement).]*

---

## Appendix A — Taxonomy Quick Reference

| Layer | Role | Discriminating Question | Example |
|-------|------|------------------------|---------|
| L1 | Base runtime | Remove it → can the agent still run? | Claude Code, opencode, pi |
| L2 | Harness/wrapper | Orchestrates ≥1 L1 agent? | helmor, deepagents, DureClaw |
| L3 | Team / SSOT | Governs behavior across sessions? | OpenSpec, CLAUDE.md, ouroboros |
| L4a | Memory tool | Extends in-session or cross-session knowledge? | cognee, Engram, memvid |
| L4b | Domain skill pack | Adds professional-vertical capabilities? | agency-agents, marketingskills |
| L4c | MCP / tool-use | Connects agent to external systems? | n8n-mcp, codegraph, browser-harness |
| L5 | Observability / research | Cross-agent evaluation or observability? | Langfuse, CC-Canary, CocoIndex |
| L6a | Retrieval-native KB | Pipeline/human writes → LLM retrieves | LightRAG, MinerU |
| L6b | LLM-native KB | LLM writes and maintains | wuphf, GBrain |
| L7 | Infrastructure | Where does the model actually run? | AWS GPU, Apple Silicon, cloud-serverless |

---

*Draft v0.1 — May 2026. Feedback welcome via GitHub issues at hongsw/clawfit.*
