# clawfit Reference Levels v0.4

This document organizes external tools and projects that clawfit should compare against, learn from, or use as supporting references.

## Role of this document
This file is the **canonical ecosystem map** for clawfit's current reference taxonomy.

It is meant to answer questions like:
- what kind of thing is this repo/product/project?
- which major layer of the ecosystem does it belong to?
- what neighboring systems should it be compared against?

It is **not** the adoption/maturity ladder (that lives separately), and it is also **not** the raw discovery log.

### Current scope
- primary focus: AI coding agents, LLM agent runtimes, harnesses, workflows, capabilities, interfaces, and closely related infrastructure
- includes: open-source projects, references, and selected commercial products when they are structurally important to the map
- excludes: full standalone LLM model catalogs, general cloud infrastructure, general-purpose developer tools (unless structurally important to the agent layer)
- region/language: global by default; local ecosystem items may appear when strategically relevant

### How to read the numbered levels

**Layers and lenses, not a maturity ladder.** A tool at Level 4 is not "more advanced" than a tool at Level 1. The levels describe *architectural role*:
- L1–L2: what runs and wraps the agent
- L3: what governs the agent's behavior
- L4: what capabilities the agent has access to
- L5: how the agent evaluates and learns
- L6–L7: where the agent interacts with users and data

**Primary + secondary classification.** Many tools span multiple levels. Each tool has one *primary* level (where it does most of its work) and may carry *secondary* levels (where its features genuinely operate). Example: `deepagents` is primary L2 (harness/SDK) with secondary L1 (CLI mode as a base runtime). Appearing in a dated scan note does not constitute level membership.

**Discovery logs vs. canonical taxonomy.** The "New signals as of YYYY-MM-DD" sections below are dated discovery logs — high-velocity research notes that may or may not graduate to stable taxonomy entries. They are preserved here for continuity but will progressively move to `docs/scans/` and `docs/research-watch/`. Only the named Level sections (L1–L7) and the companion axis notes represent the stable canonical taxonomy.

### Companion reference notes

These documents expand on specific axes that cut across the 7-level stack:

| Document | Addresses |
|----------|-----------|
| [`inference-runtime-substrate.md`](reference-notes/inference-runtime-substrate.md) | How LLMs actually run on hardware (vLLM, Ollama, llama.cpp, MLX, etc.) |
| [`hardware-deployment-axis.md`](reference-notes/hardware-deployment-axis.md) | Hardware categories, governance, isolation model |
| [`missing-recommendation-axes.md`](reference-notes/missing-recommendation-axes.md) | Model governance, autonomy level, task expansion, org profile |
| [`evidence-schema.md`](reference-notes/evidence-schema.md) | Structured evidence fields for registry entries |
| [`ontology-hardening-roadmap.md`](reference-notes/ontology-hardening-roadmap.md) | 6-phase roadmap toward a stable comparison model |
| [`ecosystem-layers-diagram.md`](reference-notes/ecosystem-layers-diagram.md) | Visual reference: layer stack, axes, multi-layer collapse patterns |

### Scan log location

New daily scan summaries: `docs/scans/` · Individual tool deep-dives: `docs/research-watch/`
See [`docs/scans/README.md`](scans/README.md) for the separation policy.

The older 1–6 structure was useful, but the ecosystem has shifted.
In particular, recent patterns such as:
- `oh-my-openagent`
- `oh-my-claudecode`
- `oh-my-codex`
- `oh-my-gemini-cli`
- `oh-my-agent`
- router / harness / skills-pack systems

show that the market is no longer only about choosing a **base agent**.
It is increasingly about choosing:
1. a **base runtime**,
2. a **meta wrapper / harness**,
3. a **team workflow / executable SSOT layer**,
4. a **capability layer**,
5. and sometimes a **human interface layer**.

So this document now uses a more explicit **7-level structure**.

## 🗓 New patterns as of 2026-05 (v0.4 update)
- **L6 taxonomy split — L6a / L6b formalised:** L6 now has two named sub-layers. L6a = retrieval-native (embed → index → retrieve → inject; LLM is consumer). L6b = LLM-native KB (LLM maintains the knowledge artifact directly; no retrieval pipeline). Anchored by Karpathy LLM Wiki gist (2026-04-04) and confirmed implementation `wuphf` (L4a primary, L6b secondary). Operational definition: write-authority determines classification — LLM writes → L6b; pipeline/human writes → L6a.
- **Operational definition added (L4a vs L6b boundary):** Resolves the ambiguity between agent-memory tools (L4a) and LLM-native knowledge bases (L6b). Tools that support both roles are classified by their primary write-authority and carry cross-references.

## 🗓 New patterns as of 2026-04 (v0.3 update)
- **Institutional harness entry:** LangChain/LangGraph entered Level 2 directly with `deepagents` — a production-ready, batteries-included open-source harness explicitly positioned against proprietary coding assistants
- **Memory layer productization:** `claude-mem` (45k★) proves Level 4 memory tooling has crossed from research into mainstream plugin adoption
- **Skill layer maturation:** Level 4 is fragmenting into distinct subtypes — skill managers (lifecycle tools), domain skill packs, and tool-use extensions. `Chops`, `skills-cleaner`, `Impeccable`, `K-Skill`, `Expect` are simultaneous signals of this split
- **Git-native agent standard:** `gitagent` proposes Git as the distribution and versioning layer for agent definitions — a Level 3 SSOT pattern distinct from plugin registries
- **Collective memory pattern:** Mozilla AI's `cq` introduces multi-agent shared knowledge commons — a Level 5 subtype not previously represented
- **Anthropic's canonical harness patterns:** The Anthropic engineering article on long-running app harness design (dual-agent, sprint contracts, context reset) is now a reference for Level 2 architecture
- **Agentic AI Foundation governance shift:** MCP donated to Linux Foundation-backed consortium (Microsoft + Google + OpenAI + Anthropic). 97M monthly downloads. AGENTS.md (OpenAI) is a new cross-platform SSOT spec alongside CLAUDE.md
- **Harness reliability as new axis:** `oh-my-pi` Hashline approach and Anthropic sprint-contracts both address the same problem — agent workflow coherence over long sessions. "Harness reliability" is an emerging evaluation criterion beyond latency/cost
- **Skill marketplace formalization:** claudemarketplaces.com (150+ skills with ratings) + 277k installs on a single Anthropic-published skill signal that skill distribution is at app-store scale
- **Computer use collapses Level 1/7 boundary:** Claude Computer Use (first-party) and understudy (demo-based) both operate the full desktop — the Layer 7 definition needs to expand to include computer-use agents
- **Adaptive base agents emerging:** NousResearch Hermes Agent (27k★) positions itself as "grows with you" — signals a new subtype of Level 1 base runtimes that blur into Level 4a memory; adaptive session behavior at the base runtime layer
- **On-device LLM runtime race:** Google AI Edge LiteRT-LM (1.8k★, +487 today) brings Google's engineering weight to edge/ARM inference, joining llama.cpp and Ollama; offline profiles now have three credible runtime substrates
- **L4b skill packs cross into knowledge-work:** kepano/obsidian-skills (20k★) is a first-party Obsidian skill pack — the first major L4b entry for knowledge workers (researchers, PMs) beyond pure code-gen contexts
- **Offline multimodal threshold crossed:** Real-time audio/video-in + voice-out agents now run on consumer Apple Silicon (M3 Pro, Gemma E2B) with no cloud dependency — Level 7 offline multimodal is no longer research-only
- **Domain-specialized security agents emerging:** Shannon (36k★, KeygraphHQ) is an autonomous AI pentester that generates and executes exploits — the first high-signal Level 1 agent specialized for a single non-coding domain (security/pentest); signals that `qa` as a clawfit task label is too broad and a `security-testing` task type may be needed
- **Offline voice input fills a gap:** Ghost Pepper (HN front page) — local hold-to-talk STT for macOS — is the first offline-native voice input tool in this taxonomy; differentiates from Superwhisper on `network: offline` and `data_sensitivity: confidential` suitability
- **Agent-sandboxed VM execution productizing:** Freestyle (HN front page, 192 points) — full Linux VMs with sub-700ms boot, live fork, and pause/resume billing — signals that cloud-side execution substrate is becoming a product category distinct from the agent itself (see Level 2)

### 📡 New signals as of 2026-05-05
- **agency-agents — 144-agent cross-tool persona pack added to L4b (92.4k★, promotion criteria met):** msitarzewski/agency-agents (92,398★, MIT license, 15.2k forks) ships 144 agents across 12 professional divisions with an automated conversion pipeline that generates tool-specific install formats for Claude Code, Cursor, Copilot, Aider, Windsurf, and Gemini CLI from a single Markdown SSOT. Star count (92.4k) is 3.7x the previous largest L4b entry by stars (caveman at 48.1k); community-origin provenance (Reddit thread) adds independent credibility. First L4b entry spanning non-technical professional verticals (Sales, Legal, Healthcare, Finance) at high star count alongside software/knowledge-work packs. Classified L4b primary (cross-tool-portable skill pack sub-type); weak secondary L3 read (12-division org chart structure) noted but insufficient — no governance workflow or sprint lifecycle present. **Added to L4b domain skill packs (top position by star count).**
- **dexter — autonomous financial research agent (23k★, L1 domain-specialized) — deferred:** virattt/dexter (23,024★) is a clear L1 domain-specialized agent (vertical-domain CLI, not a harness). Research-watch doc explicitly holds for schema extension: no `task` field in current clawfit taxonomy maps cleanly to `financial-research`; evaluate after schema extension discussion. Structural signal noted (SKILL.md pattern convergence with clawfit vocabulary). No map change today.
- **Rapid-MLX — Apple Silicon inference runtime (1k★, substrate axis) — below threshold:** raullenchai/Rapid-MLX (1,002★) sits below the 5k-star registry threshold. Research-watch doc explicitly defers: re-evaluate at 3k stars or when an independent benchmark confirms the Ollama comparison claim. No map change today.
- **Kimi K2.6 — Moonshot open-weight LLM (LLM signal, no map change):** moonshotai/Kimi-K2.6 (SWE-Bench 80.2%, 256K context, Modified MIT, $0.95/$4.00 per 1M) maps to `llms.json`, not to any ecosystem layer. Hold pending full Modified MIT license text review and one independent SWE-Bench confirmation. No reference-levels.md change warranted.
- **Scoring audit 2026-05-05:** Four research-watch signals assessed. **One map mutation applied:** agency-agents added to L4b domain skill packs (92.4k★, cross-tool-portable skill pack sub-type). Three signals held: dexter (schema blocker per research-watch doc), Rapid-MLX (below 5k threshold), Kimi K2.6 (LLM registry candidate only).
- **L6 taxonomy split — L6a (retrieval-native) / L6b (LLM-native KB) formalised 2026-05-05:** Anchored by Karpathy LLM Wiki gist (2026-04-04) and research-watch doc `2026-05-05-llm-wiki-knowledge-layer-paradigm.md`. Split criteria: L6a = retrieve-inject loop (LLM is consumer, pipelines maintain store); L6b = LLM-maintained knowledge artifact (LLM is maintainer, no retrieval pipeline). wuphf (L4a primary) and GBrain (L4a primary) are the first confirmed L6b implementations; cross-references added to both. Promotion threshold for standalone L6b entries: ≥5k stars with L6b as clear primary classification.

**조작적 정의 — L4a vs L6b 구분 기준 (2026-05-05):**
- **쓰기 주체가 LLM** → L6b: LLM이 지식 저장소를 생성·유지보수하며 사람은 읽기만 한다 (wuphf, GBrain)
- **읽기 주체가 LLM** → L4a: 파이프라인·사람이 저장소를 유지하고 LLM이 조회·소비한다 (cognee, claude-mem)
- 도구가 두 역할을 모두 지원하면 primary 역할이 더 큰 쪽으로 분류, 나머지는 cross-reference로 표기 Ecosystem map SVGs updated to show L6a/L6b sub-cells.

### 📡 New signals as of 2026-05-04
- **n8n-mcp — workflow-platform MCP bridge added to L4c (19.5k★, promotion criteria met):** czlonkowski/n8n-mcp (19,481★, TypeScript 91.8%, v2.50.0, 201 releases, 541+ tests) exposes the full n8n node library (1,650+ integrations, 2,352 templates) to any MCP-compatible Claude surface via 7 zero-credential discovery tools + 13 management tools. Pre-indexed SQLite cache rather than live API passthrough is architecturally distinct from all existing L4c entries. Meets promotion criteria: ≥5k stars with clear single-layer L4c fit (workflow-platform MCP bridge sub-type). Research-watch doc deferred on naming a new sub-type pending a second workflow-platform entry; the tool itself qualifies on its own merit. Secondary L2 surface (management tools enable workflow lifecycle) noted but insufficient to displace L4c primary classification. **Added to L4c.**
- **CocoIndex — incremental data pipeline engine added to L6 (7.7k★, promotion criteria met):** cocoindex-io/cocoindex (7,655★, v1.0.2 stable April 2026, Apache-2.0) is a Rust-core incremental ingestion engine that keeps vector DBs, graph DBs, and data warehouses populated with delta-only reprocessing from live sources. Meets promotion criteria: ≥5k stars with clear single-layer L6 fit; write-side ingestion counterpart to airweave (read-side sync). Research-watch doc is cautious about independent production confirmation, but v1.0.2 stable tag, Apache-2.0 license, and 12 confirmed connectors are sufficient for canonical L6 entry. No credible secondary classification (no agent-side interface, no MCP server). **Added to L6.**
- **Ruflo (38.8k★, L2 primary) — deferred, research-watch doc explicit hold:** Incomplete federation implementation (issue #1669), SWE-Bench 84.8% claim unverified in primary docs, rebrand incomplete as of v3.5–v3.6. Research-watch doc says "Do NOT modify reference-levels.md at this time"; re-evaluate at v4.0 stable or confirmed 50k stars. Multi-layer collapse (L2+L5+L4c) also means no clean single-level insertion. No change.
- **ouroboros (3.2k★, L2 primary) — already in map:** Entry at L2 confirmed existing (line 317). No duplicate action required.
- **browserbase/skills (1.8k★, L4b primary) — below 5k threshold:** No registry entry today; institutional provenance and +322/day velocity noted. Promote if crosses 5k or a second major infrastructure vendor ships a comparable first-party skill pack this quarter.
- **DeepSeek-TUI (2.1k★, L1 model-specialized terminal agent) — below 5k threshold:** Hmbown/DeepSeek-TUI (Rust, 2,140★, +343/day, GitHub Trending #4) — terminal TUI coding agent purpose-built for DeepSeek models. Mirrors jcode in Rust stack but adds model-vendor specialization as a new dimension. Signals a potential **model-vendor-locked terminal agent** sub-type at L1. Pattern watch: if Gemini-TUI, Grok-TUI, or similar appear in next 60 days, L1 is fragmenting along the model-vendor axis. Below threshold; tracked in research-watch.
- **DeepClaude (HN #3, 114 pts, L2 cost-optimization adapter) — single signal, unverified claim:** aattaran/DeepClaude routes the Claude Code agentic loop through DeepSeek V4-Pro with a 17x cost reduction claim. Third cost-arbitrage signal in 12 days (after Sub2API 2026-04-28 and GoModel 2026-04-22). Structural insight: treats Claude Code's loop as a portable execution primitive separable from Anthropic's model backend — same anti-lockin meta-pattern but at the model-backend substitution layer. **Map mutation deferred**: cost claim requires independent verification; confirm Claude Code behaviors (hooks, skills, tool use) survive the backend substitution. Revisit at 5k★ or second independent implementation.
- **Scoring audit 2026-05-04 (updated):** Seven research-watch signals assessed (five prior + two new). **Two map mutations applied:** (i) n8n-mcp added to L4c; (ii) CocoIndex added to L6. Five held: Ruflo (defer), ouroboros (already in map), browserbase/skills (below threshold), DeepSeek-TUI (below threshold), DeepClaude (unverified claim). Three-profile spot-check: **no regressions from 2026-05-01 baseline** — solo_dev_codegen 94% ceiling tie, large_exec_research Routines(90%)/OpenClaw(89%)/Refly(87%)/Superset+Crystal(86%), offline_mid_codegen Goose(88%)/Aider+Continue(84%)/ZeroClaw(80%)/ATLAS(77%). No metadata fixes required.

### 📡 New signals as of 2026-05-03
- **Mendral — loop-outside-sandbox as named L2 harness topology (single signal, Docker/Dagger provenance):** Andrea Luzzardi and Sam Alba (Docker co-founders, Dagger alumni) published an architectural opinion formalizing the "agent control loop lives outside the execution sandbox" split. The post is notable for provenance weight and precision: LLM credentials never enter the sandbox; sandboxes are stateless cattle with 25ms suspend/resume (Blaxel/Firecracker claim); durable execution is inherited from Inngest step-checkpoints rather than built custom; `/skills/*` and `/memory/*` path routing to Postgres makes multi-user statefulness a database property, not a sandbox property. Production claims: 16,000+ CI investigations/month, 1.18 billion log lines from one customer, ClickHouse for log ingestion at 35:1 compression. The Freestyle signal (2026-04-24) and OpenAI Agents SDK sandbox update (2026-04-16) converge on the same topology, but those are L7-infra / L1-SDK signals rather than independent named endorsements of the harness-outside-sandbox pattern specifically. **Classified L2 primary (harness topology), L7 secondary (Blaxel microVM substrate), L5 adjacent (filesystem-virtualised /skills/+/memory/ path routing).** Map mutation deferred: the pattern deserves a named entry in L2 alongside Anthropic sprint-contracts and Hashline, but the rule requires a second independent source naming "harness-outside-sandbox" as a design principle (not just using it implicitly). Watch for this vocabulary to spread to non-Mendral sources.
- **Microsoft Agent Framework v1.0 — graph-based multi-agent harness, AutoGen+SK consolidation (single signal, conditional L2 candidate):** Microsoft shipped a production-stable v1.0 unified SDK (10k★, seven weeks post-GA) that formally retires AutoGen and Semantic Kernel as independent development targets. Graph-based workflow engine with checkpointing, time-travel state hydration, human-in-the-loop approvals, and streaming; dual-language Python/C# API symmetry; declarative YAML agent definitions; MCP + A2A protocol support listed as first-class integrations; pluggable memory backends (Mem0, Redis, Neo4j); Azure Durable Functions + OpenTelemetry built-in. L2 primary; secondary L3 (YAML agent specs with version control); secondary L5 (pluggable memory). **Map mutation deferred pending**: (a) independent validation that MCP and A2A work at full client+server depth, not client-only; (b) confirmation that non-Azure LLM providers (Anthropic, Bedrock, Gemini) function outside Azure-hosted infrastructure. Watch: whether the Semantic Kernel community migrates, stalls, or forks — fragmentation would reduce effective ecosystem coverage. Re-evaluate at 2026-06 scan cycle.
- **acai.sh / specsmaxxing — ACID-tagged requirement SSOT for agents (single signal, L3 candidate sub-type):** YAML `feature.yaml` specs with stable greppable requirement IDs (ACIDs, e.g. `animated-terminal.FRAME.1-1`) embedded in generated code comments and test assertions. HN 158 pts / 171 comments (2026-05-02). Dashboard tracks requirement lifecycle (No status → Assigned → Completed → Accepted/Rejected). `acai skill` CLI injects the ACID process as an agent skill (L4b secondary). Closest prior art: gsd/get-shit-done (L3, prose spec-driven, 52k★). The ACID pattern introduces a distinct L3 sub-type — **requirement-tagged SSOT** — alongside (a) methodology guides (gsd, obra/superpowers), (b) behavioral spec files (CLAUDE.md), and (c) git-native definitions (gitagent). **Map mutation deferred**: single signal only; pattern requires a second independent tool adopting stable-ID requirement tagging for agent traceability before promotion. Revisit if acai.sh crosses 2k★ or a second ACID-style tool surfaces.
- **craft-agents-oss — document-centric desktop agent surface (single signal, L6 candidate sub-type):** lukilabs/craft-agents-oss (5.7k★, v0.9.0 tagged 2026-04-30, Apache-2.0); Electron+React desktop + CLI + headless WebSocket server; Claude Agent SDK + Pi SDK dual-backend (multi-vendor anti-lockin pattern, 3rd datapoint at L6); three-tier permission model (Explore / Ask to Edit / Auto); 32+ MCP server tools for Craft document operations; cron + label-triggered automations; headless TLS server mode enabling thin-client deployment. L6 primary (document-workspace desktop agent, distinct sub-type from IDE-threaded Zed/Roo Code and terminal-multiplexed cmux/Warp); L2 secondary (event-driven automation, session-state management, headless server mode); L4c tertiary (MCP document-layer consumer). **Map mutation deferred**: document-centric desktop agent sub-type is new to L6 and requires a second independent document-workspace desktop agent before adding as a named sub-type. Revisit at 10k★ or v1.0 tag.
- **DeepSeek V4-Pro — open-weight frontier model at SWE-Bench parity (LLM signal, no map change):** 1.6T total / 49B active MoE, 1M-token context, SWE-Bench Verified 80.6 (parity with Claude Opus 4.6 at 80.8), MIT license, $0.435/M input. V4-Flash companion: 284B/13B active, $0.14/M input, quantized offline path via Unsloth/M5. OpenRouter: 43.4B prompt tokens processed. No reference-levels.md change warranted — this is an LLM registry entry, not an ecosystem layer. Recommend adding both `deepseek-v4-pro` and `deepseek-v4-flash` to `llms.json`; schema is fully compatible with existing entries.
- **xAI Grok 4.3 — pricing/agentic-benchmark pressure signal (LLM signal, no map change):** Released 2026-04-30; 37–83% price cut vs. Grok 4.20; blended ~$1.56/M; GDPval-AA ELO 1500 (+321 from 4.20), above Claude Sonnet 4.6 on that index; always-on reasoning (~44% output token inflation, no opt-out); 1M-token context; native video input; server-side tools at $5/1,000 calls. Always-on reasoning constrains to `latency: medium` or higher profiles. No reference-levels.md change warranted — maps to `llms.json`. Hold for one independent benchmark confirmation cycle before adding to registry; clarify 200k-token tier-escalation pricing and OpenAI-compatible tool-call conformance first.
- **Scoring audit 2026-05-03:** Six research-watch signals scanned. **Zero map mutations applied.** All six entries are single-signal or explicitly flagged for deferred validation in their respective research-watch documents. Two LLM signals (DeepSeek V4-Pro, Grok 4.3) remain llms.json candidates only. Four ecosystem-layer candidates (Mendral L2 topology, Microsoft Agent Framework L2, acai.sh L3 sub-type, craft-agents-oss L6 sub-type) each require a second independent corroborating signal before promotion to the map. No scoring-model changes today.

### 📡 New signals as of 2026-05-01
- **TauricResearch/TradingAgents — highest-starred financial multi-agent framework (57.7k★):** (GitHub Trending #2, +2,023 today) — Multi-agent LLM financial trading framework with role-specialized agents (analyst, risk, execution). Overtakes virattt/ai-hedge-fund (54k★, tracked 2026-04-15) as the largest domain-specialized financial multi-agent repo. Second high-signal confirmation (with ai-hedge-fund) that `research` + `data-analysis` tasks extend into finance as a primary domain. Same Level 1/2 structure as Claude-Code-Game-Studios (role-hierarchy domain harness). Not added to registry (too domain-specific); tracking as evidence that domain-specialized multi-agent systems are a durable cluster. If `financial-analysis` recurs as a distinct task type request, add to `primary_task` enum.
- **spawn-agent — Vercel AI SDK adapter for local coding agents:** (GeekNews, github.com/millionco/spawn-agent) — Makes local coding agents (Claude Code, Codex CLI) behave as Vercel AI SDK models, enabling zero-rebind integration for Vercel-ecosystem developers. Extends the multi-vendor anti-lockin cluster (cc-switch, Sub2API, cmux, awesome-codex-skills, 2026-04-28) into the SDK↔CLI boundary. Level 4c adapter sub-type; complements GoModel (gateway) and cc-switch (CLI config switcher). Early signal; no confirmed star count yet.
- **Pu.sh — full coding-agent harness in 400 lines of shell:** (Hacker News Show HN, 59 pts) — Complete coding-agent loop implemented in ~400 lines of shell. Explicit minimal-harness framing echoes mini-swe-agent (100-line minimal agent, 2026-04-27). Two "minimal" counter-signals in five days is a weak trend; a third would confirm a named minimal-harness sub-type at Level 2 opposing the batteries-included trend (LangGraph deepagents, obra/superpowers). Zero-dependency shell provenance is relevant for `setup_complexity: low` profiles. Early signal.
- **Microsoft VibeVoice open-sourced:** (GeekNews, github.com/microsoft/VibeVoice) — Microsoft released an official open-source speech AI with both TTS and STT capabilities. Builds on the VibeVoice signal tracked 2026-03-28; Microsoft provenance and official open-source release represent a significant maturity upgrade for the voice I/O layer. Joins jamiepine/voicebox (19k★) and VoxCPM (11k★) in Level 7 voice output; adds Level 7 voice input alongside Ghost Pepper. No registry entry yet; revisit at 5k★ with confirmed feature benchmark data.
- **Scoring audit 2026-05-01:** Three-profile spot-check shows healthy distributions — no regressions from 2026-04-29 baseline. solo_dev_codegen: five-way tie at 94% (Claude Code, OpenCode, Goose, Crush, Cline — consistent with ceiling behavior). large_exec_research: Claude Code Routines (90%), OpenClaw (89%), Refly (87%), Superset+Crystal (86%) — correct. offline_mid_codegen: Goose (88%), Aider+Continue (84%), ZeroClaw (80%), ATLAS (77%) — correct. Bottom entries (marketingskills, korean-law-mcp, Polysona) appropriately low for all three profiles. No metadata fixes required. No new registry entries added (all new signals pre-threshold or domain-specific).
### 📡 New signals as of 2026-04-30
- **Meta-pattern (a) Vendor cross-sponsorship of competing agent surfaces — generational signal:** Warp (warpdotdev/warp, Rust, AGPLv3 client + MIT UI framework) open-sourced its previously-closed multi-year terminal product on 2026-04-28 with **OpenAI as founding sponsor** and rebranded as "an agentic development environment." Repo gained **+11,955★ in a single day to reach 42,313★** — ~6× the previous clawfit-tracked velocity high (free-claude-code, 2026-04-24). First instance in this taxonomy of an LLM vendor sponsoring a third-party (non-vendor-built) agent-surface as named "founding sponsor." Distinct from Anthropic's first-party Claude Code (vendor builds) and from OpenAI's openai-agents-python (vendor publishes own framework). **Extends the 2026-04-28 multi-vendor anti-lockin meta-pattern**: vendor-side now actively underwrites cross-pollination, not just the user-side. Layer classification: L6 primary (terminal-native ADE / concurrent-agent surface, sibling to cmux and Zed parallel agents) + L2 (Oz cloud orchestration platform: triage → plan → code → PR lifecycle) + L1 (Warp's built-in coding agent). Multi-layer collapse pattern continues. No registry entry today (multi-layer product does not map cleanly onto agents/llms/hardware schemas; AGPLv3 affects governance_need: hard profiles); meta-note only. Re-evaluate the named pattern "vendor cross-sponsorship" if a second instance appears.
- **Meta-pattern (b) L5 inspectable agent memory — third architectural sub-track confirmed (portable-binary):** memvid (memvid/memvid, Rust, 15.3K★, Apache-2.0) ships a single-file `.mv2` container that bundles header + embedded WAL + HNSW vector index + Tantivy/BM25 full-text + temporal index + TOC into one append-only binary. v2.0 Python→Rust rewrite (March 2026); claimed 0.025ms P50 retrieval; downstream `memvid/claude-brain` Claude Code plugin at 477★. **Materially larger than other L5 memory signals tracked this month and inhabits a third sub-track** distinct from (1) vector/graph cluster (cognee, claude-mem, mem0, GitNexus) and (2) the inspectable-memory cluster previously tracked. The L5 inspectable / agent-maintained memory cluster now has three named architectural sub-tracks: **(i) markdown+git** (wuphf, GBrain), **(ii) SQLite+MCP-native** (Engram, Beads), **(iii) portable-binary single-file** (memvid). Five independent datapoints across the three sub-tracks; sub-pattern is stable. No new level; structure noted in L4a/L5 internal organization. Memvid added to L4a as a portable-binary memory entry.
- **Meta-pattern (c) Vendor mix at L1 expands — NVIDIA enters runtime substrate:** NVIDIA OpenShell (NVIDIA/OpenShell, Rust 86%, Apache-2.0, 5,424★, alpha) ships an embedded-K3s-in-Docker sandbox runtime with hot-reloadable network/inference policies and a privacy-routing credential layer. **First L1 entry from NVIDIA** — until now NVIDIA appeared only at L4c (PersonaPlex, 2026-04-08). Runtime-agnostic agent compatibility (Claude Code / OpenCode / Codex / GitHub Copilot CLI / OpenClaw / Ollama). L1 vendor mix shifts: previously dominated by Anthropic / OpenAI / open-source projects, now includes a hyperscaler GPU vendor with explicit "safe, private" + enterprise framing. Cross-references L4c (egress filtering, policy enforcement) similar to how some MCP gateways span L4c/L5. Single-signal — no registry entry today; tracked as vendor-positioning signal. Strengthens case for an `isolation_model` scoring dimension (none / process / container / microVM / k8s-in-docker) to compare cua/trycua, Freestyle, Daytona, OpenShell coherently.
- **Meta-pattern (d) "Vibe" crosses from community shorthand to vendor-canonical product naming:** Mistral simultaneously released Medium 3.5 (dense 128B, 256k context, $1.50/$7.50 per 1M, SWE-Bench Verified 77.6%, modified MIT open weights) and a managed async agent platform branded **"vibe remote agents"** (mistral.ai/news/vibe-remote-agents-mistral-medium-3-5). **First major model lab to formally adopt "vibe" in product naming.** Mistral becomes the fourth vendor-managed async remote agent runtime alongside Claude Code Routines (Anthropic), Agents SDK + Codex (OpenAI), and Gemini Enterprise Agent Platform (Google). Also surfaces a memory-portability framing ("teleport") that may emerge as a distinct L4a/L5 sub-pattern if other vendors adopt similar vocabulary. Implications: (i) "vibe coding" task framing in clawfit is now vendor-validated, not just community vocabulary; (ii) the four-vendor managed async runtime cluster is structurally complete across the major frontier-model labs; (iii) Mistral's open-weight + self-host-on-4-GPUs framing keeps the open-weight + offline tier (alongside DeepSeek V4, Qwen3.6) credible at frontier capability. No registry entry today (Medium 3.5 model would land in LLM registry once benchmark data is independently confirmed and pricing tier mapping is settled).
- **hongsw/harness — locale/voice overlay as a candidate third L4b axis (single signal, design-origin datapoint):** hongsw fork of revfactory/harness adds three localization skills (`korean-persona-search`, `korean-voice-adapter`, `korean-persona-harness`) on top of the unchanged six-phase team-architecture engine. Korean persona injection sources from NVIDIA Nemotron-Personas-Korea (1M rows, CC BY 4.0). Distinct from existing L4b sub-types: domain skill packs (marketingskills, obsidian-skills, Game Studios) **replace skill content**; this **parameterizes generated agent voice/manner** without restructuring teams. Together with DureClaw (cross-machine orchestration) and revfactory/harness (upstream meta-skill), the hongsw-authored stack forms a coherent two-layer design-origin reference for clawfit. Currently 6★ — single-signal under the registry threshold. Added as L2 entry alongside DureClaw with explicit "design origin" framing; **locale/voice overlay** flagged as candidate third L4b axis pending a second independent datapoint.
- **cc-connect — L7 messaging-bridge pattern consolidates multi-platform (3rd datapoint):** chenhg5/cc-connect (Go, 6.7k★, +171/day on GitHub Trending Daily Go) is a single Go binary + embedded web UI that bundles **11 chat platforms** (Feishu, DingTalk, Slack, Telegram, Discord, WeChat Work, Weibo, LINE, QQ, QQ Bot, Weixin) with **10+ agents** (Claude Code, Codex, Cursor Agent, Gemini CLI, Kimi CLI, Qoder CLI, OpenCode, iFlow CLI, Pi, Devin) plus any ACP-compatible agent. Bridge API exposes WebSocket + REST. Strong CN-region coverage distinguishes from cc-telegram (single-platform) and Happy (mobile-first). **Third datapoint in the L7 messaging-bridge sub-pattern**; the pattern is stable. ACP referenced again as the agent-side abstraction surface (parallel to Happy, cc-canary). cc-connect is a deployment utility, not an agent/LLM/hardware option — no registry entry; tracked under L7.
- **Zed 1.0 stable + Zed for Business (8 days after Parallel Agents launch):** zed.dev/blog/zed-1-0 (HN front page, 956 pts, top item 2026-04-30). Zed crossed 0.x → 1.0 with simultaneous Zed for Business SKU (centralized billing, RBAC, team management). Built-in ACP support multiplexes Claude Agent / Codex / OpenCode / Cursor inside one editor. **Enterprise eligibility threshold crossed**: previously recommending Zed for `team_size: large` + `governance_need: hard` required disclaimers; both resolved. Existing L7 entry updated with 1.0 stable + ACP multiplexing note.
- **Scoring audit 2026-04-30:** Seven research-watch signals scanned today. Two map mutations applied: (i) memvid added to L4a (portable-binary memory sub-track); (ii) hongsw/harness added to L2 alongside DureClaw (hongsw design-origin pair). Five signals reflected as meta-notes only (Warp cross-sponsorship, NVIDIA OpenShell vendor entry, Mistral vibe-canonical, cc-connect L7 3rd datapoint, Zed 1.0 enterprise threshold). No scoring-model changes today; cost weight (0.25) and LLM preference weight (0.15) re-evaluation deferred to 2026-05 calibration cycle pending continued multi-vendor anti-lockin pressure.

### 📡 New signals as of 2026-04-29
- **Warp open-sourced under AGPL-3.0 — agent-centric terminal enters Level 6:** (GitHub Trending + HN + GeekNews, warpdotdev/warp) — Warp creator Zach Lloyd open-sourced the terminal client with explicit "agentic development environment" framing. Rust-based; block output model + inline AI assistance remains proprietary cloud service (BYOAI mode for local inference). High simultaneous reach: HN + GeekNews front page on the same day. Extends Level 6 fragmentation into three distinct terminal sub-types: IDE-threaded (Zed), terminal-multiplexed (cmux using libghostty), and agent-native terminal (Warp, own renderer). For `primary_role: developer` profiles, terminal choice is now an explicit agent-environment selection dimension. No registry entry (terminal UI).
- **OpenAI models on Amazon Bedrock — cloud inference platform consolidation signal:** (Hacker News, stratechery.com) — OpenAI integrating GPT-series models into Amazon Bedrock removes the only remaining Anthropic-exclusive governance surface on AWS. Previously, `hardware: cloud` + `governance_need: hard` + `network: online` effectively required Anthropic models via Bedrock. Now all frontier models are available on the same managed surface with VPC, IAM, and data residency. Implication: clawfit's `hardware: cloud` dimension may need a `managed_platform` sub-field (Bedrock / Azure AI / Vertex AI) to capture governance-surface availability by model. No registry change today; flag for schema review.
- **Browser automation sub-cluster reaches 3 entries (Libretto + browser-harness + Obscura):** Third headless browser tool explicitly designed for AI agent automation surfaced (GeekNews, github.com/h4ckf0r0day/obscura, V8-based). With Libretto (deterministic, 2026-04-16), browser-harness (self-healing, 2026-04-25), and now Obscura (agent-first design), **browser automation for AI agents** is a confirmed named Level 4c sub-cluster. Axis: deterministic/compliance (Libretto) vs. self-healing/agentic (browser-harness) vs. agent-first/scraping (Obscura). Relevant for `task: research` + `task: qa` profiles where web interaction is a hard requirement.
- **HyperFrames by HeyGen — HTML/CSS-to-MP4 pipeline designed for AI agent workflows:** (GeekNews, github.com/heygen-com/hyperframes) — HeyGen (AI video company) releases a programmatic video production tool that takes HTML/CSS markup as input and renders to MP4, explicitly designed to be called from within agent pipelines. Signals expansion of agent task scope into media production — current `primary_task` taxonomy (`code-gen`, `qa`, `research`, `data-analysis`, `writing`) does not cover `media-production` or `content-creation`. Candidate for a new task type if additional signals confirm this axis. Level 4c tool-use extension; medium signal.
- **Scoring audit 2026-04-29:** Three-profile spot-check shows healthy distributions — no regressions. solo_dev_codegen: seven-way tie at 94% (Claude Code, OpenCode, Goose, Crush, Cline, vercel-labs/open-agents, Roo Code — known ceiling behavior, consistent with 2026-04-26 audit). large_exec_research: Claude Code Routines (90%), OpenClaw (89%), Refly (87%), Superset+Crystal (86%) — correct. offline_mid_codegen: Goose (88%), Aider+Continue (84%), ZeroClaw (80%), ATLAS (77%) — correct. Superwhisper investigated: `code-gen` task retained (notes explicitly justify voice-dictated coding use case; different from ghost_pepper/voicebox fixes); rank 43/76 at 74% confirms it is not causing false positives. No metadata fixes required. No new registry entries added (today's signals — Warp, OpenAI+Bedrock, HyperFrames, Obscura — are all pre-threshold or non-registry-fit).

### 📡 New signals as of 2026-04-28
- **Education axis confirmed (3rd datapoint):** `shareAI-lab/claw0` (2,385★ in ~2 months, trilingual en/zh/ja) is a 10-section "from-scratch" curriculum that walks readers through building an OpenClaw-style agent gateway in ~7,000 lines of progressive Python — anchored to a specific production codebase rather than to generic agent patterns. Joins the Maryam Miradi pattern-teaching post and the Claude Architect certification guide as the third independent education-track signal in ~30 days. **"Structured agent-internals literacy" now meets the threshold for a recurring axis** (not noise) alongside harnesses, methodology guides, and behavioral specs. No new level needed; tracked as a sub-pattern of Level 3 SSOT/methodology.
- **Skill aggregator pattern crosses vendor boundary (cross-vendor meta-pattern):** `ComposioHQ/awesome-codex-skills` (+637/day, ~50 skills across 5 categories) is the first non-Anthropic L4b skill aggregator with traction — targeting OpenAI Codex CLI with the same SKILL.md + YAML frontmatter format used in the Anthropic ecosystem, installed at `$CODEX_HOME/skills/` symmetrically to `.claude/skills/`. Adds a third **curator archetype** at L4b: integration-vendor-curated (Composio) — distinct from platform-vendor (Vercel), community-curated (VoltAgent), and practitioner-curated (mattpocock). Cross-cutting implication: SKILL.md may be drifting toward a de facto cross-vendor schema, partially decoupling the runtime axis (Claude Code vs Codex CLI vs Gemini CLI) from the skill-pack axis. Worth tracking as a `skill_portability` / `vendor_lock_in` consideration if portability is empirically confirmed.
- **Industry pricing convergence (2nd datapoint, trend confirmed):** GitHub Copilot announces transition from PRUs (premium request units) to token-metered AI Credits effective 2026-06-01 (HN 490 pts). Combined with Anthropic's Claude Code Pro-tier removal on 2026-04-22, the two largest paid coding-agent vendors are converging on usage-based billing within a six-week window. **`pricing_tier: paid` as a coarse label is losing predictive power**; `cost_per_1k_tokens` becomes the dominant cost signal, and team-size segmentation (solo favors usage-based; large teams face budget variance) may need to enter the scoring model. Not a level-specific signal — affects products across Levels 1–3.
- **cmux — terminal-multiplexed multi-agent UX (15.6k★, Swift/macOS):** Native macOS terminal built on libghostty with vertical tabs, OSC-driven per-pane notifications, and explicit `cmux claude-teams` integration. Terminal-multiplexed counterpart to Zed Parallel Agents' IDE-threaded pattern — same problem (managing concurrent coding agents), different surface. Reinforces Level 6 fragmentation along workflow surfaces (IDE-threaded / terminal-multiplexed / mobile-remote / web-control). UX/notification-focused, not orchestration-focused — does not displace harnesses the way Zed does. Tracked here, no registry entry (terminal UI doesn't map onto agent/llm/hardware schemas).
- **dirac — OSS Cline-fork tops Terminal-Bench 2.0 agent leaderboard:** (HN Show HN 282 pts) Apache-2.0 fork of Cline reports 65.2% on TB2 using `gemini-3-flash-preview` (vs. 64.3% Junie CLI, 47.6% Google baseline). Three orthogonal signals: (1) Terminal-Bench 2.0 emerging as a candidate successor to saturated SWE-bench Verified (extends the 2026-04-27 benchmark-saturation note); (2) small/fast model tier viable as production agent substrate; (3) OSS agent leadership on Gemini, not Anthropic/OpenAI — relevant to LLM preference weighting. Notable design stance: native tool-calling only, **explicit non-adopter of MCP**. Single-signal, claim-to-inspect — no registry entry, no map mutation; revisit when TB2 leaderboard is independently confirmed.
- **GitNexus — code-specialized graph-RAG with WASM client-side mode (31.5k★, +1,074/day):** TypeScript project that fuses L4a graph memory and L4c MCP tool surface (16 tools) in one codebase, with a fully client-side WASM/WebGPU mode (no backend service required). Code-aware graph schema (CALLS/IMPORTS/EXTENDS/IMPLEMENTS) distinguishes it from generic memory tools (cognee, claude-mem, mem0). PolyForm Noncommercial license affects enterprise registry inclusion. Velocity is anomalous for a mature 31.5k★ repo — possible re-discovery event; needs validation. Single-signal aggregation candidate: flag for L4a code-graph-RAG sub-cluster if 2+ more entries appear. No map mutation today.
- **cc-switch — multi-CLI provider switcher at 52.8k★ (+892 today, single-day high):** Cross-CLI configuration switcher unifying Claude Code, Codex, Gemini, OpenCode, and OpenClaw under one provider-preset model (50+ presets out of the box). Atomic-write SSOT for `~/.claude/`, `~/.codex/`, `~/.gemini/` etc. — primarily a Level 4 provider-switching utility, with a secondary Level 3 SSOT character because of the atomic-write/rollback pattern. Strongest single GitHub signal of the day. Combined with Sub2API and cmux (same day), this is a coordinated **multi-vendor anti-lockin** signal cluster — see meta-pattern note below.
- **Sub2API — subscription-pooling gateway at 16.1k★ (+454 today):** Pools multiple paid CLI subscriptions (Claude Pro/Max, Copilot, Gemini Advanced, etc.) behind one OpenAI-compatible API, presenting unified access without per-vendor account juggling. Sits primarily at Level 4c (gateway/proxy sub-type) with a Level 7 cross-cut because it changes the substrate's economic profile (subscription pooling instead of usage-metered API). Direct counter-pattern to the industry pricing convergence noted in this same scan: vendors are moving to usage-based billing while users are responding with subscription pooling. License/ToS posture needs verification before any registry inclusion.
- **wuphf — agent-maintained markdown wiki (HN Show, 258 pts):** A wiki whose contents are written and curated by agents, kept under git, intended to be human-inspectable. Fourth datapoint in the human-readable agent-memory pattern (after Beads, Engram, GBrain). Level 5 memory layer; sub-pattern note below.
- **Engram — coding-agent persistent memory at 2.9k★ (+50 today):** MCP-native structured memory for coding agents — protocol-endpoint shape rather than runtime-layer shape. Differentiates from Beads (Go runtime providing retention infra) on the interface axis: Engram exposes memory through MCP tool calls, Beads exposes it through a process boundary. Both can coexist; Level 5 primary, Level 4c MCP secondary.
- **hiclaw — Matrix-federated multi-agent OS at 4.3k★:** Open-protocol federated coordination layer for multiple agents using the Matrix protocol as transport. First high-signal Level 3 entry on the **OSS/federated branch** of multi-agent coordination, distinct from the enterprise/closed branch (Microsoft Teams BYOA, Gemini Enterprise Agent Platform, Anthropic Managed Agents). Level 3 is now visibly forking into "enterprise-platform-coordinated" and "open-protocol-coordinated" sub-branches.
- **Memanto — typed semantic memory paper (HF, 6 upvotes):** Academic work proposing typed schemas + information-theoretic retrieval as a counter-thesis to graph/embedding-only memory architectures (Beads, Engram, wuphf, cognee, claude-mem). Weak signal in adoption terms but useful as the theoretical pole opposite the implementation cluster. Level 5 academic reference; track for citation traction, not adoption velocity.
- **Meta-pattern (a) Multi-vendor anti-lockin — same-day cluster of 3 ≥15k★ signals:** cc-switch (52.8k★, CLI switcher), Sub2API (16.1k★, subscription pooling), and cmux (15.6k★, terminal-multiplexed concurrent agents) all surfaced 2026-04-28. Add awesome-codex-skills (cross-vendor skill schema, 2026-04-28 morning) as a fourth, lower-weight datapoint. The cluster forms the user-side response to the vendor-side pricing convergence noted earlier in this same scan: as vendors move toward usage-metered billing, power users are normalizing **multi-vendor portability as the default workflow** rather than the exception. Implication for clawfit: cost weight (0.25) and LLM preference weight (0.15) may both be under-weighted for power-user profiles where vendor switching cost is now near-zero. No scoring change today (single-day cluster, needs ≥1 more day of confirmation), but flagged for re-evaluation in the 2026-05 calibration cycle.
- **Meta-pattern (b) Agent-maintained inspectable memory — 5-datapoint sub-pattern at L5:** Beads (22.2k★, retention runtime, 2026-04-27) + Engram (2.9k★, MCP-native memory, today) + wuphf (Show HN, agent-maintained markdown wiki, today) + GBrain (existing reference, markdown+PGLite, agents read-before/write-after) + Memanto (academic counter-thesis, today). Common shape: human-readable, version-controllable, agent-maintained, low or zero vector-DB dependency. Distinct from the embedding/graph-RAG memory cluster (cognee, claude-mem, mem0, GitNexus). Promoting to a named L5 sub-pattern: **"inspectable agent memory"** alongside the existing embedding/graph cluster. No new level introduced — extending L5 internal structure as the existing taxonomy guidance prescribes.
- **Scoring audit 2026-04-28 (round 2 update):** Twelve total research-watch signals scanned today across two rounds. No new registry entries added — single-day cluster (a) and 5-datapoint sub-pattern (b) are reflected as map-level meta-notes only, not as scoring-model changes. Three-profile spot-check unchanged from 2026-04-27 — no regressions, no metadata fixes required. Re-evaluate cost/LLM-preference weights in the 2026-05 calibration cycle if multi-vendor anti-lockin pattern persists.

### 📡 New signals as of 2026-04-27
- **trycua/cua — open-source CUA sandbox + SDK infrastructure:** (GitHub Trending, 182 stars/day) — Purpose-built open-source infrastructure stack for Computer-Use Agents: sandboxes, SDKs, and training environments. Provider-agnostic; distinct from Anthropic's first-party Computer Use. First independent CUA infrastructure in this taxonomy. Relevant to `data_sensitivity: confidential` profiles that need computer-use capability without cloud routing. Level 4c candidate; revisit at 5k total stars.
- **gastownhall/beads — Go-native memory enhancement for coding agents:** (GitHub Trending, 152 stars/day) — Context retention memory system for coding agents, implemented in Go. Adds to the fragmenting Level 4a memory cluster (cognee, hippo-memory, claude-mem, GBrain). Go provenance distinguishes it from Python-heavy alternatives. Relevant to offline/low-dependency profiles. Early signal; revisit at 5k total stars.
- **mini-swe-agent — 100-line minimal coding agent from SWE-agent team:** (GeekNews) — Princeton + Stanford researchers strip the full SWE-agent framework to ~100 lines of Python while preserving GitHub issue resolution capability. Simultaneously a research artifact (minimal baseline) and a practical signal that agentic coding loops don't require framework overhead. Not a production recommendation target; valuable as Level 1 calibration reference and Level 5 benchmark companion.
- **SWE-bench Verified saturation — benchmark no longer measures frontier capabilities:** (Hacker News, openai.com) — OpenAI statement that SWE-bench Verified can no longer differentiate frontier models (saturation). Follows Berkeley RDI exploit-based invalidation (2026-04-12). Two distinct benchmark failure modes now documented: exploit-inflation and capability-saturation. Direct implication for clawfit: LLM preference weights citing SWE-bench performance should carry lower confidence for frontier-tier models until a successor benchmark is established. See also: `2026-04-27-swebench-verified-no-longer-frontier.md`.
- **free-claude-code velocity update:** 1,701 stars/day (up from ~1,962/day peak on 2026-04-24) — pricing pressure signal from Anthropic's Pro tier removal persists one week later. Continued developer interest validates `pricing_tier` as a material selection axis for solo/small profiles.
- **Scoring audit 2026-04-27:** Three-profile spot-check shows healthy distributions — no regressions. solo_dev_codegen five-way tie at 94% visible (expected ceiling behavior; seven-way tie when all entries counted; known calibration item). large_exec_research correctly surfaces Claude Code Routines (90%), OpenClaw (89%), Refly (87%), Superset+Crystal (86%). offline_mid_codegen correctly surfaces Goose (88%), Aider+Continue (84%), ZeroClaw (80%), ATLAS (77%). No metadata fixes required today. No new registry entries added (all new signals below 5k-star registry threshold).

### 📡 New signals as of 2026-04-26
- **RooCodeInc/Roo-Code — multi-role VS Code team agent at 23k stars:** (GitHub Trending #8, TypeScript, 23,503★) — "A whole dev team of AI agents in your code editor." Multi-persona role model (architect, developer, reviewer) in a single VS Code session. Distinct from Cline and Continue: those are single-assistant models; Roo Code frames the IDE session as a coordinated team of role-specific agents. Direct Level 1 competitor to Cline (59k★) in the IDE coding agent slot. Added to registry.
- **mattpocock/skills — practitioner skill directory at 20k stars confirms L4b dotfile pattern:** (GitHub Trending #2, Shell, 19,986★) — Matt Pocock's personal `.claude` skill directory. Third high-credibility practitioner to publish their skill directory at 10k+ stars (after Karpathy autoresearch, Addy Osmani agent-skills). Confirms **practitioner dotfile as distribution** as a stable L4b sub-type distinct from marketplaces (claudemarketplaces.com) and aggregators (awesome-agent-skills). No registry entry (content resource).
- **davila7/claude-code-templates — Claude Code config+monitor CLI at 25k stars:** (GitHub Trending #5, Python, 25,340★) — "CLI tool for configuring and monitoring Claude Code." Dual positioning: template/SSOT (Level 3) + monitoring UI (Level 7). Feature verification needed before registry entry.
- **Gemini Enterprise Agent Platform — Google Cloud enterprise agent orchestration:** (GeekNews front page) — Named enterprise agent platform extending Vertex AI with A2A (Agent-to-Agent) + MCP dual-protocol support. First named "Enterprise Agent Platform" product from a hyperscaler. Competes with Claude Code Routines and Anthropic Managed Agents for `team_size: large` + `governance_need: hard` profiles. Tracking; no registry entry pending documentation stabilization.
- **vLLM Recipes — model+hardware configuration recommendation engine:** (GeekNews front page, recipes.vllm.ai) — Interactive platform from the vLLM team for recommending model+hardware configs for inference serving. Adjacent to clawfit's domain but distinct: vLLM Recipes targets serving-side optimization; clawfit targets org-fit. Complementary positioning — no registry entry (serving infrastructure guide, not an agent tool).
- **Scoring audit 2026-04-26:** Three-profile spot-check shows healthy distributions — no regressions. solo_dev_codegen now a seven-way tie at 94% (Roo Code joins the ceiling cluster — expected behavior). large_exec_research correctly surfaces Claude Code Routines (90%), OpenClaw (89%), Refly (87%), Superset+Crystal (86%). offline_mid_codegen correctly surfaces Goose (88%), Aider+Continue (84%), ZeroClaw (80%), ATLAS (77%). Metadata audit found `devops` as non-standard role in DureClaw and hermes-paperclip-adapter — harmless since both also carry `developer`; no fix required. One new registry entry added: Roo Code (Level 1, IDE multi-role team agent).

### 📡 New signals as of 2026-04-25
- **browser-use/browser-harness — anti-framework browser automation via raw CDP:** (Hacker News Show HN, 77 pts) — From the browser-use team, but reversed: instead of wrapping CDP with Playwright APIs, gives the LLM a raw Chrome DevTools Protocol connection + `helpers.py`. When steps fail the LLM reads errors, self-edits helpers.py, and retries mid-task. Self-healing by design. Anchors a new Level 4c sub-type axis: **deterministic automation** (Libretto) vs. **self-healing/agentic automation** (browser-harness). Relevant for QA + research profiles where full LLM autonomy over browser state is acceptable. Added to registry.
- **CC-Canary — Claude Code per-session behavioral health monitor:** (Hacker News, 37 pts) — Stdlib-only Python tool from delta-hq that reads `~/.claude/projects/**/*.jsonl` session logs and measures tool-mix, read:edit ratio, reasoning-loop phrases, self-admitted errors, stop hook violations, token usage, and thinking depth. Composite health score with argmax regression date detection. Used to document the Claude Code thinking-redaction quality regression (17,871 thinking blocks, 6,852 sessions). First tool in taxonomy for **quantitative monitoring of agent behavioral quality across sessions** — distinct from capability benchmarks and trace observability (Langfuse). Enters Level 5 as a "per-session health monitor" sub-type. Zero dependencies (stdlib only).
- **DeepSeek V4 — 1M-token context MoE at #1 HN:** (Hacker News, 1,786 pts / 1,392 comments — highest score on front page today; GeekNews 6 pts) — MoE model with 1M-token context window. If SWE-bench scores confirm coding quality, adds an open-weight + offline + 1M-context tier to the LLM registry above current Qwen3-35B-A3B (tracked 2026-04-20). Key implication: 1M context potentially eliminates RAG/chunking overhead for medium-to-large codebases on local hardware. Revisit once benchmark data and quantized inference requirements are confirmed.
- **zilliztech/claude-context star count update:** GitHub Trending today at 9,004★ (+706/day) — up from 5,850★ in last map update. Updated in Level 4a entry below.
- **Scoring audit 2026-04-25:** Three-profile spot-check shows healthy distributions — no regressions. solo_dev_codegen five-way tie at 94% (expected ceiling behavior, known calibration item). large_exec_research top-5 correctly surfaces Claude Code Routines (90%), OpenClaw (89%), Refly (87%), Superset+Crystal (86%). offline_mid_codegen correctly surfaces Goose (88%), Aider+Continue (84%), ZeroClaw (80%), ATLAS (77%). No metadata fixes required today.

### 📡 New signals as of 2026-04-24
- **coreyhaines31/marketingskills — first mainstream L4b marketing domain skill pack:** (GitHub Trending #14, +285/day, 23,796★) — Marketing skills for Claude Code and AI agents: CRO, copywriting, ad copy, campaign analysis. Largest-starred non-developer domain skill pack in this taxonomy. With obsidian-skills (knowledge work, 20k★), Claude-Code-Game-Studios (game dev, 10k★), and now marketingskills (marketing, 23.7k★), L4b domain fragmentation is accelerating beyond software engineering into every professional vertical. Added to registry.
- **VoltAgent/awesome-agent-skills — 1,000+ curated agent skills from official dev teams:** (GitHub Trending #16, +228/day, 18,060★) — Curated collection of 1,000+ skills from official developer teams. Signals that skill aggregation at scale is becoming its own product layer distinct from individual packs and platform-native marketplaces. L4b discovery hub sub-type; tracking at 18k★.
- **mksglu/context-mode — context window sandboxing for AI coding agents:** (GitHub Trending #13, +238/day, 9,419★) — "Context window optimization for AI coding agents. Sandboxes tool output." TypeScript. Distinct from token compression (rtk/caveman) and session memory (claude-mem): output sandboxing prevents tool results from polluting the context window. New L4c sub-type for governance-conscious profiles. Tracking at 9.4k★.
- **Alishahryar1/free-claude-code — pricing pressure signal, highest daily velocity on trending:** (GitHub Trending #7, +1,962/day, 5,544★) — "Use claude-code for free in the terminal, VSCode extension or via discord." Highest daily velocity on today's trending list — a direct community response to Anthropic's Pro tier removal (2026-04-22). Not adding to registry (ToS status unclear); tracking as pricing elasticity signal validating `pricing_tier: paid` as a material selection axis in solo/small profiles.
- **huggingface/ml-intern — HuggingFace open-source ML research loop agent:** (GitHub Trending #1, +720/day, 3,258★) — Open-source ML engineer that reads papers and runs training experiments. HuggingFace provenance gives access to Hub, datasets, and model cards natively. First institutional entry in L5 research-loop space from a major AI infrastructure company (vs. Karpathy autoresearch from a solo researcher). Tracking at 3.2k★; revisit at 10k★.
- **Agent Vault — open-source credential proxy and vault for agents:** (Hacker News front page) — Second HN-prominent credential infrastructure tool for AI agents in 10 days (after kontext-cli, 2026-04-15). "Vault" framing implies broader secrets management than kontext-cli's ephemeral OIDC rotation. Confirms L4c credential proxy as a stable product category. Tracking pending confirmed GitHub URL.
- **GeekNews unreachable today (503):** Could not scan GeekNews front page. Check tomorrow for any missed Korean ecosystem signals.
- **Scoring audit 2026-04-24:** Three-profile spot-check shows healthy distributions — no regressions. solo_dev_codegen five-way tie at 94% (expected ceiling behavior, known calibration item). large_exec_research top-5 includes Claude Code Routines (90%), OpenClaw (89%), Refly (87%), Superset+Crystal (86%) — coherent. offline_mid_codegen correctly surfaces Goose (88%), Aider (84%), Continue (84%), ZeroClaw (80%), ATLAS (77%) — all offline-capable code-gen tools. No metadata fixes required. One new registry entry added: marketingskills (L4b marketing domain skill pack).

### 📡 New signals as of 2026-04-23
- **vercel-labs/skills — platform-vendor skill manager via `npx skills`:** (GitHub Trending, 15,469★) — Vercel Labs' second consecutive high-signal agent infrastructure entry (after `open-agents` 2026-04-16). Standalone skill manager accessible via `npx skills`. TypeScript-first; targets the frontend/fullstack developer segment already in the Vercel ecosystem. Signals that Level 4b is splitting further: community skill managers (Chops, skills-cleaner) vs. platform-vendor-native skill distribution channels. Monitor for registry addition once feature scope is confirmed.
- **langfuse/langfuse — production LLM observability at 25k stars enters Level 5:** (GitHub Trending, 25,601★) — Open-source LLM engineering platform: tracing, metrics, evals, prompt versioning, datasets, playground. MIT + managed cloud; self-hostable. Native integrations across LangChain, LlamaIndex, OpenAI, Anthropic, LiteLLM. Fills a gap in the taxonomy: **production observability for deployed agent systems** — distinct from pre-deployment benchmark harnesses (lm-evaluation-harness) and research loops (autoresearch). Most-adopted tool for this use case; added to registry at Level 5.
- **Zed Parallel Agents — IDE absorbs multi-agent orchestration (released 2026-04-22):** (Hacker News) — Zed editor ships Threads Sidebar: multiple simultaneous agent threads per window, per-thread AI backend mixing, filesystem scope isolation, and worktree isolation. First high-signal IDE to absorb Level 2 multi-agent orchestration as a native editor feature — bypasses the need for standalone harnesses (Crystal, ccpm, claude-squad) for solo/small teams. Signals an IDE-harness convergence pattern worth watching. Added to registry at Level 7.
- **Google 8th gen TPUs for the agentic era:** (Hacker News) — Google explicitly branded new TPU generation around agent workloads, with two separate chips: one for training, one for agent inference serving. First hyperscaler to position server-side inference hardware as agent-specific. Expands cloud inference hardware context alongside AMD GAIA (local x86) and Apple Silicon (local ARM). No registry entry (no direct user-facing product).
- **Microsoft Teams BYOA — enterprise agent distribution via three-line adapter:** (Hacker News) — Teams SDK `bring-your-agent-to-teams` allows any existing HTTP agent (LangChain, Azure AI Foundry, Slack bots) to plug into Teams. Zero-rebuild integration with auto Azure AD registration. Signals a new enterprise deployment surface: `output_destination: enterprise_collab_platform` — a dimension clawfit doesn't model yet. Relevant to `team_size: large` + `governance_need: hard` profiles where Teams reach is a hard requirement.
- **Scoring audit 2026-04-23:** Two metadata issues identified and fixed: (1) `ghost_pepper.tasks` had `code-gen` incorrectly (Ghost Pepper is a voice input tool, same fix pattern as voicebox 2026-04-21); removed, now `["research", "summarization"]`. (2) `ralph_claude_code.roles` was missing `pm` despite being PRD-driven — added `pm` for consistency with snarktank/ralph. Two new registry entries added: Langfuse (Level 5, LLM observability) and Zed (Level 7, parallel-agent IDE).

### 📡 New signals as of 2026-04-22
- **CrabTrap — LLM-as-a-judge HTTP proxy for agent production security:** (Brex engineering blog, HN 55 pts) — HTTP proxy that intercepts agent tool/API calls in real time and routes each through an LLM judge (allow/deny/rewrite). Fintech provenance (Brex). Fills a missing Level 4c sub-type: **agent output/action guardrails** — distinct from input-side guardrails (system prompts), audit logging (kontext-cli), and offline evaluation harnesses. Relevant to `governance_need: hard` profiles where agents have write access to production systems. Revisit when public repo is available.
- **GoModel — AI gateway in Go (enterpilot/gomodel, 333★, HN Show HN 155 pts):** Open-source LiteLLM alternative in Go; OpenAI-compatible API for OpenAI/Anthropic/Gemini/Groq/xAI/Ollama; dual-layer caching (exact-match + semantic), built-in guardrails pipeline, Prometheus metrics, admin dashboard. First Go-native gateway in this taxonomy alongside Python-first LiteLLM. Early signal; revisit at 2k★.
- **Claude Code removed from Pro tier — pricing escalation signal:** (HN, 185 pts) — Anthropic removed Claude Code from the $20/month Pro plan; now requires Max ($100+), Team, or Enterprise. The `claude_code` registry entry's `pricing_tier: paid` no longer aligns with medium-budget solo/small profiles. Metadata fix applied: `optimal_maturity` corrected from 5 to 4 (Claude Code is equally optimal for daily solo/small developers at maturity 4 as for stage 5), and `team_size` updated to include `"large"` (Claude Code has always supported enterprise-scale organizations). Consider adding `premium` pricing tier to schema to distinguish $100+/month tools from $20/month tools in future.
- **Scoring audit 2026-04-22:** Three-profile spot-check shows two metadata issues resolved: (1) `claude_code.optimal_maturity` corrected 5→4 — Claude Code now correctly surfaces in top-5 for `solo_dev_codegen` (was incorrectly penalized as sub-optimal for maturity-4 daily users); (2) `claude_code.team_size` updated to include `large` — corrects under-representation in enterprise profiles. No new tools added to registry today (CrabTrap and GoModel are early signals below registry threshold).

### 📡 New signals as of 2026-04-21
- **Kimi vendor verifier — inference provider integrity verification:** (HN front page, 2026-04-21) — Moonshot AI (Kimi) released a tool for verifying that inference API providers (Together.ai, Fireworks, Groq, etc.) are actually running the model they claim, not a quantized/modified variant. This introduces a new evaluation sub-category at Level 5: **inference supply-chain integrity verification** — distinct from LLM capability benchmarks. Relevant to clawfit: provider-agnostic model scoring may need a "verified provider" axis if reseller accuracy variance becomes a material selection factor. Revisit when a public verification suite is available.
- **Scoring audit 2026-04-21:** Spot-checks across three profiles show healthy distributions. One metadata fix applied: `voicebox` had `code-gen` incorrectly in tasks (it is a voice synthesis studio, not a code generator); corrected to `["summarization", "research"]`. No other regressions found. Thunderbolt confirmed at 2,810★ (+27% since Apr-20 tracking entry). openai-agents-python confirmed at 23,922★ (+2,119★ since Apr-18 tracking entry).

### 📡 New signals as of 2026-04-20
- **Thunderbolt (thunderbird/thunderbolt) — privacy-first multi-model AI client from Mozilla ecosystem:** (GitHub Trending, +695 today, 2,205★) — Cross-platform AI client (web, iOS, Android, macOS, Linux, Windows) with "choose your models, own your data, eliminate vendor lock-in" framing. MPL 2.0; compatible with Ollama/llama.cpp/OpenAI-compatible APIs. Under security audit for enterprise production readiness. From the Thunderbird (email client) organization — ~20M user install base. Fills a gap for `data_sensitivity: confidential` and `governance_need: hard` profiles that need AI interfaces without SaaS data exposure. First privacy-first general AI client with Mozilla provenance in this taxonomy. Enters Level 7 as an "on-premises AI client" sub-type distinct from coding-specific interfaces.
- **OpenMythos — looped transformer reconstruction signals new LLM capability tier:** (GeekNews front page) — PyTorch reconstruction of the suspected Claude Mythos architecture as a Recurrent-Depth Transformer with sparse MoE routing. Reasoning depth controlled by loop count at inference time — a new capability axis beyond parameter count or benchmark score. Amazon Bedrock now offers Claude Mythos Preview (gated). If Mythos-class reasoning becomes API-accessible, clawfit's LLM registry needs a new tier above Opus. Level 5 research signal; revisit when Mythos API is generally available.
- **Qwen3.6-35B-A3B — first explicit "agentic coding" MoE open-weight model:** (GeekNews front page) — Alibaba's 35B-total/3B-active MoE model positioned explicitly for agentic coding. Open-weight; Hugging Face available. Competes with Mistral/DeepSeek in efficient open-weight segment. Relevant for `network: offline` + `budget: low` profiles needing capable agentic coding without cloud API costs. Track for SWE-bench/LiveCodeBench benchmark data before adding to LLM registry.
- **Scoring audit 2026-04-20:** Spot-checks across three profiles (solo_dev_codegen, large_exec_research, offline_mid_codegen) show healthy distribution. Top-5 results are coherent and appropriate. No new metadata fixes required. Five-way tie at 94% for solo_dev_codegen reflects ceiling behavior when multiple tools match all constraints equally — known calibration item, not a regression.

### 📡 New signals as of 2026-04-18
- **ChromeDevTools/chrome-devtools-mcp — first-party MCP server for browser debugging at 35k stars:** (GitHub Trending, +196 today, 35,846★) — Official MCP server from the Chrome DevTools team. Exposes DOM, network, console, performance, and storage via MCP to any coding agent. 35,846★ is the highest star count for any MCP server in this taxonomy. Enables agents to do live browser QA without leaving the agent session — closes the gap between coding agents and browser-based debugging. Enters Level 4c as a "browser-native MCP server" sub-type. Strengthens case for a `web-qa` sub-task type distinct from general `qa`.
- **openai/openai-agents-python — vendor-published official multi-agent framework at 21k stars:** (GitHub Trending, +625 today, 21,803★) — OpenAI's official "lightweight, powerful framework for multi-agent workflows" in Python. Handoffs, routing, tool calling, async execution. Same provenance class as Claude Code Routines and Anthropic Managed Agents. Competes with LangGraph/deepagents at Level 2; "lightweight" framing targets developers who found LangGraph too complex. Signals that "vendor-published harness" is solidifying as a named sub-type at Level 2. Added to registry.
- **BasedHardware/omi — passive ambient multimodal AI at 9.8k stars:** (GitHub Trending, +824 today, 9,824★) — Dart/Flutter AI that continuously watches screen and listens to audio, proactively surfacing suggestions ("tells you what to do"). Distinct from Ghost Pepper (hold-to-talk) and Superwhisper (explicit dictation) — omi is passive/always-on, not push-to-activate. First entry in taxonomy for "proactive ambient AI advisor" sub-type at Level 7. For exec/PM personas who want AI presence without managing sessions.
- **SimoneAvogadro/android-reverse-engineering-skill — mobile security skill pack at 2.7k stars:** (GitHub Trending, +538 today, 2,737★) — Shell Claude Code skill for Android APK reverse engineering (decompilation, smali, manifest audit). First Level 4b skill pack for mobile security/RE — extends the security skill cluster (Shannon, Strix) into mobile. Reinforces argument for `security-testing` as a distinct clawfit task type.
- **Tracer-Cloud/opensre — AI SRE agent toolkit at 1.4k stars:** (GitHub Trending, +184 today, 1,441★) — Python toolkit for building AI SRE agents combining incident response, runbook execution, and monitoring. First infrastructure/operations domain (SRE/DevOps) to surface a dedicated agent toolkit in this taxonomy alongside AI coding agents. Signals that `sre`/`devops` may warrant an explicit role in clawfit's org_fit model.
- **Scoring fix — cognee removed from code-gen task bucket:** cognee (knowledge graph memory, Level 4a) was surfacing in top-5 for solo_dev_codegen and offline_mid_codegen profiles due to incorrect `code-gen` task inclusion. Fixed: removed `code-gen` from cognee tasks (cognee is memory infrastructure, not a code generator); setup_complexity corrected from `low` to `medium`.

### 📡 New signals as of 2026-04-17
- **topoteretes/cognee — graph-native agent memory crosses 15k stars:** (GitHub Trending, +170 today, 15,788★) — "Knowledge Engine for AI Agent Memory in 6 lines of code." Builds knowledge graphs over documents, code, and conversations rather than pure vector similarity. MCP-compatible; integrates with LangChain, LlamaIndex, CrewAI, OpenHands. Joins Level 4a memory layer as a graph-native sub-type alongside claude-mem (session-centric) and GBrain (markdown-native). Added to registry.
- **Cloudflare triple-launch: agent-specific infrastructure stack:** (HN front page, three simultaneous entries) — AI Platform (inference layer for agents, edge-native), Artifacts (Git-compatible versioned blob storage for agent outputs, beta), Email Service (SMTP/IMAP abstraction for autonomous agents). A major CDN/platform vendor entering agent infrastructure simultaneously on three axes signals agent cloud infrastructure is commoditizing. AI Platform → Level 2 cloud inference sub-layer; Artifacts → Level 4a artifact-versioning sub-type; Email → Level 4c agent communication surface.
- **jamiepine/voicebox — open-source voice synthesis studio at 19k stars:** (GitHub Trending, +880 today, 19,049★) — TypeScript-first voice synthesis studio with voice cloning, style transfer, and multi-speaker management. Surpasses VoxCPM (11,260★) in star count. Natural pairing for TypeScript-first orgs (Vercel ecosystem). Adds TypeScript-native sub-type to Level 7 voice output layer alongside VoxCPM (Python/multilingual). Added to registry.
- **lsdefine/GenericAgent — self-evolving agent with skill tree:** (GitHub Trending, +872 today, 2,753★) — Seeds itself with 3,300-line Python codebase and grows a skill tree autonomously. Claims 6× less token consumption. Represents a "skill-acquisition-native" Level 1 sub-type distinct from Hermes Agent (adaptive) and rowboat (memory-native). Early signal; revisit at 10k★.
- **EvoMap/evolver — GEP-powered agent evolution engine:** (GitHub Trending, +812 today, 3,141★) — Applies Gene Expression Programming (Genome Evolution Protocol) to evolve AI agent behavioral programs. JavaScript; add-on engine, not standalone. Converges with Meta HyperAgents (2026-04-13) and GenericAgent (today) as a cluster of self-improvement agent signals. May warrant a Level 4 behavioral-evolution sub-type if pattern stabilizes; revisit at 10k★.

### 📡 New signals as of 2026-04-16
- **vercel-labs/open-agents — platform vendor enters cloud agent template space:** (GitHub Trending, +915 today, 2,611★) — Vercel Labs' official open-source template for building cloud agents. TypeScript-first, production-oriented. Vercel's entry means cloud agent deployment is becoming commodity infrastructure rather than an engineering challenge — directly lowering activation energy for `network: online` + `solo/small` profiles. Enters Level 1 alongside Twill.ai as a "cloud-first agent" sub-type.
- **Claude-Code-Game-Studios — domain-specialized harness reaches 10k stars:** (GitHub Trending, Donchitos/Claude-Code-Game-Studios, +612 today, 10,395★) — 49 AI agents + 72 workflow skills organized as a game studio hierarchy; Shell-based, Claude Code native. First high-signal Level 2/3 harness specialized for a non-software-engineering domain (game development). Signals that domain-specialized harnesses are fragmenting from the generic harness layer: the next wave of Level 2/3 tooling will be industry-vertical, not just generic productivity. May indicate a need for `domain` as a new dimension alongside `task` in the scoring model.
- **Libretto — deterministic AI browser automation enters Level 4c:** (HN, 80 pts, saffron-health/libretto) — "Making AI Browser Automations Deterministic." Health-tech provenance implies production/compliance requirements. Extends Level 4c in a reliability direction — distinct from capability-focused tool infrastructure (serena, rtk). Aligns with the "harness reliability" axis; revisit at 1k★.
- **Happy — open-source cross-platform mobile client for Claude Code + Codex:** (GeekNews) — iOS/Android/web remote control client via CLI wrapper. First open-source mobile-native Level 7 entry with explicit dual-agent (Claude Code + Codex) support. Introduces `mobile` as a Level 7 sub-type distinct from web-based (claudecodeui) and desktop-based (pi-generative-ui) interfaces.

### 📡 New signals as of 2026-04-15
- **Claude Code Routines — first-party serverless agent execution:** (HN front page, code.claude.com/docs/en/routines) — Anthropic launches Routines in research preview: saved Claude Code configurations triggered by schedule, HTTP API, or GitHub events (PRs, pushes, issues, 18 event types), running autonomously on Anthropic-managed cloud infrastructure. Introduces `managed_hosted` + `event_driven` statefulness mode — distinct from interactive sessions or sprint-loop harnesses. GitHub event triggers encode org workflows as automation, enabling PM/exec initiation of agent runs without CLI access. First Anthropic-native serverless runner in this taxonomy. Enters Level 2.
- **shanraisshan/claude-code-best-practice crosses 43.7k stars as #1 trending:** (GitHub Trending #1) — comprehensive agentic engineering curriculum with explicit three-abstraction model (Commands/Agents/Skills). 69 curated tips from Boris Cherny (Claude Code creator). Comparative analysis of 10 major frameworks. "Agentic engineering" vocabulary now independently named by three major guides (obra/superpowers, gsd/get-shit-done, this). The Level 3 SSOT layer has three confirmed entry points: code harnesses, methodology guides, and behavioral spec files (CLAUDE.md). clawfit's registry `claude_code_best_practice` min_maturity lowered to 2 (accessible to beginners), pm+researcher roles added.
- **virattt/ai-hedge-fund at 54k stars — domain-specialized multi-agent finance system:** (GitHub Trending) — 19 specialized agents modeling investor personas (Buffett, Munger, Lynch, Wood, Burry + analytics agents); multi-LLM (OpenAI/Anthropic/Groq/DeepSeek/Ollama). Educational but highest-starred domain-specialized multi-agent application in taxonomy. Validates `research` + `data-analysis` tasks beyond software development contexts. Not added to registry (too domain-specific for generic scoring).
- **kontext-cli — credential broker for AI coding agents:** (HN Show HN, 98★) — Go binary replacing long-lived API keys with ephemeral OIDC+RFC 8693 token-exchanged credentials injected at Claude Code session start, expired on exit. Governance telemetry streams hook events (PreToolUse, PostToolUse, UserPromptSubmit) to audit backend. First dedicated credential broker + audit tool for AI agents. Signals a sub-layer below harnesses for infrastructure-level security governance. Level 4c early signal; revisit at 1k★.

### 📡 New signals as of 2026-04-14
- **gsd/get-shit-done: meta-prompting + spec-driven dev at 52k stars:** (GitHub Trending, gsd-build/get-shit-done) — "light-weight meta-prompting, context engineering and spec-driven development system." Three-layer vocabulary convergence in one project; 52k stars is mainstream adoption signal. Enters Level 3 alongside `obra/superpowers`. "Spec-driven" framing may become a governance filter dimension for compliance-conscious orgs.
- **forrestchang/andrej-karpathy-skills: CLAUDE.md behavioral spec hits 25k stars:** (GitHub Trending) — a single CLAUDE.md derived from Karpathy's public observations. 25k stars for a pure Markdown file signals that CLAUDE.md behavioral specifications are becoming a de-facto standard layer independent of code harnesses. Three major CLAUDE.md guides now have 25k+ stars; the Level 3 SSOT layer is fragmenting into: (a) code harnesses, (b) workflow methodology guides, and (c) behavioral specification files.
- **pgmicro: in-process PostgreSQL explicitly designed for AI agents:** (GeekNews, glommer/pgmicro) — compiles PostgreSQL SQL to SQLite bytecode; zero-dependency, in-process, full Postgres SQL compat. First database project with explicit AI agent environment framing. Adds SQL-native sub-type to Level 4a memory layer alongside key-value stores (cipher) and markdown bases (GBrain).
- **AMD GAIA: hardware vendor enters local agent execution:** (HN, 89 pts, amd-gaia.ai) — AMD's dedicated local AI agent platform for Ryzen/Radeon hardware. First x86 CPU/GPU vendor with named agent execution product alongside Apple Silicon + Ollama. Expands addressable hardware surface for `network: offline` profiles beyond the current Apple Silicon reference stack.
- **SnapState: workflow execution state persistence productizing:** (HN Show HN, snapstate.dev) — persistent state for AI agent workflows. Early signal of a new Level 4a sub-category: execution state checkpointing (distinct from knowledge memory). As ralph-style loops and sprint-contract sessions grow longer, workflow state persistence is separating from memory/knowledge tooling.

### 📡 New signals as of 2026-04-13
- **Meta HyperAgents — self-referential agent improvement:** (GeekNews, cobusgreyling.medium.com) — agents that modify their own improvement *mechanisms*, not just task outputs. Distinct from adaptive runtimes (Hermes Agent) — the modification loop targets the meta-level improvement process. Research-stage; may require a new top-end maturity stage if it productizes. Challenges static LLM capability scoring.
- **Anthropic Advisor Strategy — named multi-LLM pairing pattern:** (GeekNews, claude.com/blog) — Opus as strategic advisor + Sonnet as executor; officially endorsed cost-optimization architecture. Formalizes "planner/executor dual-model" as a named pattern. Signals clawfit needs a `multi_llm_pattern` dimension beyond single-LLM selection.
- **Anthropic Managed Agents — hosted stable interfaces:** (GeekNews, anthropic.com/engineering/managed-agents) — long-running hosted agents with interface contracts that survive model version upgrades. Governance-relevant: interface stability as a reliability primitive. Distinct from harness-design-long-running-apps (sprint contracts). Suggests a `managed_hosted` statefulness value for the scoring model.
- **snarktank/ralph crosses 15k stars:** (GitHub Trending, +463/day) — TypeScript autonomous agent loop for PRD-driven iterative execution. Now the highest-starred implementation in the ralph methodology family (above ralph-claude-code 8k and open-ralph-wiggum 1.4k). Validates PRD-driven loops crossing mainstream developer adoption.
- **VoxCPM: tokenizer-free TTS for multilingual voice agents:** (OpenBMB, 11k★, GitHub Trending) — voice output infrastructure with tokenizer-free architecture; lower latency and broader language coverage than tokenized TTS. Fills the Level 7 voice *output* gap alongside Ghost Pepper (voice input). First high-signal multilingual TTS for agent pipelines.
- **Claudraband: Claude Code for power users:** (HN, 85 pts) — explicit "power user" positioning for a Claude Code harness; targets senior developers needing more than default Claude Code but less than full team orchestration. New Level 2 segment between simple wrappers and enterprise orchestrators.

### 📡 New signals as of 2026-04-12
- **Strix: second high-signal security agent enters Level 1:** usestrix/strix (23k★, GeekNews 26 pts) — open-source autonomous security testing platform using teams of agents with PoC validation. Distinct from Shannon (expert pentester tool): Strix is developer self-service, CI/CD-integrated, shift-left. Reinforces the need for a `security-testing` task type beyond `qa` in the scoring taxonomy.
- **GBrain: personal knowledge compounding as Level 4a pattern:** garrytan/gbrain — MIT-licensed personal knowledge base by YC CEO Garry Tan; markdown+PGLite backend, agents read-before/write-after. OpenClaw+Hermes Agent native. Local-first, human-inspectable, MCP support incoming. Adds a "compounding personal knowledge" sub-pattern to Level 4a distinct from session-memory tools.
- **🔥 DureClaw: 크로스 머신 멀티 에이전트 오케스트레이션 (hongsw 직접 제작):** [DureClaw/dureclaw](https://github.com/DureClaw/dureclaw) — Claude Code 오케스트레이터 + Phoenix WebSocket 서버 + oah-agent 워커 3층 아키텍처. 이종 AI 백엔드(claude/opencode/gemini/aider) 지원. MCP 플러그인 정식 배포. Mac/Linux/Windows/Raspberry Pi. claude-peers-mcp가 머신 내 피어 메시라면 DureClaw는 머신 간 크루 오케스트레이션. Level 2/4c 하이브리드. **clawfit 레지스트리 카테고리(이종 백엔드 오케스트레이션, 크로스 머신 에이전트 크루) 설계 방향의 원점.**
- **Berkeley RDI: all major agent benchmarks are exploitable:** "How We Broke Top AI Agent Benchmarks" (rdi.berkeley.edu, 171 HN pts) — UC Berkeley team demonstrates that every major benchmark (SWE-bench, WebArena, OSWorld, etc.) can be exploited to achieve near-perfect scores without solving a single task. Seven recurring vulnerability classes identified. Directly undermines LLM selection decisions based on published benchmark scores; clawfit's LLM preference weights may need an evidence-quality caveat. Agent-Eval Checklist proposed as a future Level 5 reference standard.

---
### 📡 New signals as of 2026-04-11
- **"Harness Engineering" named as a paradigm:** A four-year retrospective (bits-bytes-nn.github.io, GeekNews front page) documents the progression "Prompt Engineering → Context Engineering → Harness Engineering (2025–2026)." When practitioners name a paradigm, vocabulary has matured. Validates clawfit's Level 2–3 emphasis; suggests increasing harness-layer weight in recommendations for orgs at maturity stages 5–7.
- **obra/superpowers crosses 145k stars:** Shell-based agentic skills framework + development methodology reaches the largest star count of any harness/SSOT repo in this taxonomy. Explicit "that works" framing targets reliability, not novelty. Spans Level 3 (methodology) and Level 4b (skills). First Level 3 entry with mainstream adoption evidence.
- **Archon: harness-builder as tool type:** coleam00/Archon (15k★, GitHub Trending) explicitly calls itself a "harness builder" — a meta-tool that generates harness configurations. "Deterministic and repeatable" framing targets governance/reliability axis. New Level 2 sub-type: harness generator vs. harness runtime.
- **rowboat: memory-native AI coworker:** rowboatlabs/rowboat (11.7k★, GitHub Trending) frames memory as first-class, not a plugin. "Coworker" framing implies persistent task ownership. Adds a memory-native Level 1 sub-type alongside stateless base agents.
- **Twill.ai (YC S25): async cloud agent delegation:** HN Launch HN front page — "delegate to cloud agents, get back PRs." Async fire-and-forget model with PR output is a new deployment topology for Level 1: no interactive session, no local setup. First managed cloud agent service in this taxonomy.
- **multica: open-source managed agents platform:** multica-ai/multica (6k★, GitHub Trending) — "turn coding agents into real teammates — assign tasks, track progress." Team-oriented multi-agent management platform enters Level 2.

### 📡 New signals as of 2026-04-08
- **Claude Mythos Preview — new Anthropic model tier:** Three simultaneous HN front-page entries (1,584 pts combined) covering system card, cybersecurity capability assessment, and Project Glasswing. Introduces explicit long-horizon and security-domain capabilities; may warrant a new LLM registry tier above current Opus/Sonnet. Glasswing is the first Anthropic-branded AI security governance framework.
- **GLM-5.1 "long-horizon tasks":** ZhipuAI's new model (z.ai, 401 HN pts) explicitly positions around multi-step agentic task completion — "long-horizon" as primary framing signals a new evaluation axis for LLM selection in clawfit beyond latency/cost.
- **NVIDIA PersonaPlex enters persona layer:** NVIDIA (github.com/NVIDIA/personaplex, 662 trending stars) publishing a persona-based AI application library signals hardware vendors moving up-stack into agent identity configuration — potential Level 4c entrant.
- **Production skill packs reach senior practitioners:** Addy Osmani (Google Chrome DevRel) published `agent-skills` — production-grade engineering skills for AI coding agents. First high-credibility Level 4b entry from a named Google engineer.


## Companion axis — Inference runtime substrate
The 7 levels below describe agent-facing tools. Underneath Level 1 sits a distinct layer: the **inference runtime substrate** — the software that actually executes LLMs on hardware. This axis is especially relevant for `network: offline` profiles where users must choose a local inference backend (Ollama, llama.cpp, MLX, vLLM, etc.). It is separate from the hardware filter (`laptop / workstation / cloud`) and from the agent runtime choices at Level 1.

Sub-types: **serving frameworks** (vLLM, FastChat, TensorRT-LLM) · **local runtime + UX** (Ollama, llama.cpp) · **hardware optimizers** (FlashAttention, MLX, MLC LLM) · **distributed home cluster** (exo) · **training substrate** (Unsloth, DeepSpeed, HF Transformers, PyTorch) · **domain-specific** (whisper.cpp)

Full analysis: [`docs/reference-notes/inference-runtime-substrate.md`](reference-notes/inference-runtime-substrate.md) *(addresses GitHub issue #9)*

---

## Level 1 — Base runtimes / primary agent surfaces
These are the main user-facing agent runtimes or primary product choices.
They are the tools users most directly choose as their base environment.

- <img src="https://github.com/openclaw.png" alt="OpenClaw" width="18" /> [OpenClaw](https://github.com/openclaw/openclaw) — ⭐ 365,342
- <img src="https://github.com/anomalyco.png" alt="OpenCode" width="18" /> [OpenCode](https://github.com/anomalyco/opencode) — ⭐ 150,654
- <img src="https://github.com/NousResearch.png" alt="Hermes Agent" width="18" /> [Hermes Agent](https://github.com/NousResearch/hermes-agent) — ⭐ 120,550 — adaptive open-source agent from NousResearch; "grows with you" — signals session-persistent adaptation at the base runtime layer
- <img src="https://github.com/anthropics.png" alt="Claude Code" width="18" /> [Claude Code](https://github.com/anthropics/claude-code) — ⭐ 118,485
- <img src="https://github.com/All-Hands-AI.png" alt="OpenHands" width="18" /> [OpenHands](https://github.com/All-Hands-AI/OpenHands) — ⭐ 72,201
- <img src="https://github.com/cline.png" alt="Cline" width="18" /> [Cline](https://github.com/cline/cline) — ⭐ 61,063
- <img src="https://github.com/paul-gauthier.png" alt="Aider" width="18" /> [Aider](https://github.com/paul-gauthier/aider) — ⭐ 44,022
- <img src="https://github.com/block.png" alt="Goose" width="18" /> [Goose](https://github.com/block/goose) — ⭐ 43,404
- <img src="https://github.com/KeygraphHQ.png" alt="Shannon" width="18" /> [Shannon](https://github.com/KeygraphHQ/shannon) — ⭐ 40,577 — autonomous AI pentester; reads source code, identifies attack surfaces, generates and executes exploits; first high-signal domain-specialized security agent in this taxonomy
- <img src="https://github.com/continuedev.png" alt="Continue" width="18" /> [Continue](https://github.com/continuedev/continue) — ⭐ 32,841
- <img src="https://github.com/zeroclaw-labs.png" alt="ZeroClaw" width="18" /> [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) — ⭐ 30,697
- <img src="https://github.com/usestrix.png" alt="Strix" width="18" /> [Strix](https://github.com/usestrix/strix) — ⭐ 24,627 — open-source autonomous security testing platform; teams of agents run code dynamically, find vulnerabilities, validate via PoC; CI/CD integration; developer self-service shift-left variant alongside Shannon's expert-pentester model
- <img src="https://github.com/RooCodeInc.png" alt="Roo Code" width="18" /> [Roo Code](https://github.com/RooCodeInc/Roo-Code) — ⭐ 23,697 — VS Code extension with multi-persona role model ("a whole dev team of AI agents in your code editor"); architect, developer, reviewer roles in one IDE session; direct Level 1 competitor to Cline with distinct multi-role framing; Apache-2.0
- <img src="https://github.com/charmbracelet.png" alt="Crush" width="18" /> [Crush](https://github.com/charmbracelet/crush) — ⭐ 23,571
- <img src="https://github.com/langchain-ai.png" alt="deepagents" width="18" /> [deepagents](https://github.com/langchain-ai/deepagents) — ⭐ 21,878 *(also Level 2; CLI mode = base runtime, SDK mode = harness)*
- <img src="https://github.com/rowboatlabs.png" alt="rowboat" width="18" /> [rowboat](https://github.com/rowboatlabs/rowboat) — ⭐ 13,143 — open-source AI coworker with native memory; persistent task ownership across sessions; memory-native Level 1 sub-type
- <img src="https://github.com/google-ai-edge.png" alt="LiteRT-LM" width="18" /> [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) — ⭐ 4,435 — Google AI Edge on-device LLM inference runtime; ARM-first, mobile + edge; companion to google-ai-edge/gallery
- <img src="https://github.com/vercel-labs.png" alt="open-agents" width="18" /> [open-agents](https://github.com/vercel-labs/open-agents) — ⭐ 4,202 — Vercel Labs' official open-source cloud agent template; TypeScript; production-oriented; platform-vendor-native deployment entry point for cloud agent architecture
- <img src="https://github.com/understudy-ai.png" alt="understudy" width="18" /> [understudy](https://github.com/understudy-ai/understudy) — ⭐ 422 — demonstration-based local desktop agent (GUI + browser + shell + filesystem)
- Cursor — https://cursor.com/
- Kiro CLI — https://kiro.dev/
- Claude Computer Use — direct mouse/keyboard/screen control via Claude Code Desktop + Cowork + Dispatch; macOS first *(also Level 7)*
- [Twill.ai](https://twill.ai) — YC S25 — async cloud agent delegation; "delegate tasks, get back PRs"; fire-and-forget model with PR output; first managed cloud agent service in this taxonomy

---

## Level 2 — Meta wrappers / harnesses / orchestration layers
These projects sit on top of existing base agents and transform how they operate.
They provide orchestration, better defaults, compatibility layers, workflows, routing, multi-agent teams, or opinionated operating conventions.

- <img src="https://github.com/code-yeongyu.png" alt="oh-my-openagent" width="18" /> [oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) — ⭐ 54,537
- <img src="https://github.com/musistudio.png" alt="claude-code-router" width="18" /> [claude-code-router](https://github.com/musistudio/claude-code-router) — ⭐ 33,100
- <img src="https://github.com/Yeachan-Heo.png" alt="oh-my-claudecode" width="18" /> [oh-my-claudecode](https://github.com/yeachan-heo/oh-my-claudecode) — ⭐ 31,602
- <img src="https://github.com/Yeachan-Heo.png" alt="oh-my-codex" width="18" /> [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) — ⭐ 26,371
- <img src="https://github.com/openai.png" alt="openai-agents-python" width="18" /> [openai-agents-python](https://github.com/openai/openai-agents-python) — ⭐ 25,420 — OpenAI's official lightweight Python multi-agent framework; handoffs, routing, tool calling, async execution; "lightweight" framing vs. LangGraph; vendor-published harness sub-type alongside Claude Code Routines
- <img src="https://github.com/SuperClaude-Org.png" alt="SuperClaude Framework" width="18" /> [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) — ⭐ 22,511
- <img src="https://github.com/multica-ai.png" alt="multica" width="18" /> [multica](https://github.com/multica-ai/multica) — ⭐ 21,999 — open-source managed agents platform; "turn coding agents into real teammates — assign tasks, track progress"
- <img src="https://github.com/langchain-ai.png" alt="deepagents" width="18" /> [deepagents](https://github.com/langchain-ai/deepagents) — ⭐ 21,878 *(LangGraph-based SDK; also Level 1 as CLI)*
- <img src="https://github.com/coleam00.png" alt="Archon" width="18" /> [Archon](https://github.com/coleam00/Archon) — ⭐ 19,916 — "first open-source harness builder for AI coding"; makes AI coding deterministic and repeatable; harness-generator sub-type
- <img src="https://github.com/snarktank.png" alt="ralph" width="18" /> [ralph](https://github.com/snarktank/ralph) — ⭐ 17,946 — TypeScript autonomous agent loop for PRD-driven iterative execution; highest-starred ralph-family implementation; solo/small team target
- <img src="https://github.com/AndyMik90.png" alt="Aperant" width="18" /> [Aperant](https://github.com/AndyMik90/Aperant) — ⭐ 14,093
- <img src="https://github.com/siteboon.png" alt="claudecodeui" width="18" /> [claudecodeui](https://github.com/siteboon/claudecodeui) — ⭐ 10,291
- <img src="https://github.com/frankbria.png" alt="ralph-claude-code" width="18" /> [ralph-claude-code](https://github.com/frankbria/ralph-claude-code) — ⭐ 8,878
- <img src="https://github.com/can1357.png" alt="oh-my-pi" width="18" /> [oh-my-pi](https://github.com/can1357/oh-my-pi) — ⭐ 3,541 — Hashline approach: content-hash verification for concurrent multi-agent file safety; see ["The Harness Problem"](https://blog.can.ac/2026/02/12/the-harness-problem/)
- <img src="https://github.com/Q00.png" alt="ouroboros" width="18" /> [ouroboros](https://github.com/Q00/ouroboros) — ⭐ 2,761 — "Agent OS: stop prompting, start specifying"; sits between user and AI runtime (Claude Code / Codex CLI / Hermes / OpenCode); Double-Diamond workflow (interview → seed → run → evaluate) + 9 specialist agents (Socratic Interviewer, Ontologist, Evaluator, …) + Ralph evolutionary loop + PAL cost-tier router + EventStore persistence; spec-driven harness sub-type; ralph-family sibling
- <img src="https://github.com/Th0rgal.png" alt="open-ralph-wiggum" width="18" /> [open-ralph-wiggum](https://github.com/Th0rgal/open-ralph-wiggum) — ⭐ 1,584
- <img src="https://github.com/coder.png" alt="agentapi" width="18" /> [agentapi](https://github.com/coder/agentapi) — ⭐ 1,372
- <img src="https://github.com/first-fluke.png" alt="oh-my-agent" width="18" /> [oh-my-agent](https://github.com/first-fluke/oh-my-agent) — ⭐ 856
- <img src="https://github.com/Joonghyun-Lee-Frieren.png" alt="oh-my-gemini-cli" width="18" /> [oh-my-gemini-cli](https://github.com/Joonghyun-Lee-Frieren/oh-my-gemini-cli) — ⭐ 155
- <img src="https://github.com/DureClaw.png" alt="DureClaw" width="18" /> [DureClaw](https://github.com/DureClaw/dureclaw) — ⭐ 2 🔥 **크로스 머신 멀티 에이전트 오케스트레이션** — Claude Code 오케스트레이터 + Phoenix WebSocket 메시지 버스 + oah-agent 워커 3층 아키텍처; 이종 AI 백엔드(claude/opencode/gemini/aider) 지원; Mac/Linux/Windows/Raspberry Pi; MCP 플러그인 정식 배포(`@dureclaw/mcp`); 한국 두레(협동 농경) 철학 기반; **hongsw 직접 제작** — clawfit 레지스트리 설계 방향에 직접적 영향 *(also Level 3 cross-machine team orchestration; also Level 4c via @dureclaw/mcp)*
- <img src="https://github.com/hongsw.png" alt="hongsw/harness" width="18" /> [hongsw/harness](https://github.com/hongsw/harness) — ⭐ 6 — Korean-localized fork of `revfactory/harness` team-architecture meta-skill; six-phase workflow (Domain Analysis → Team Architecture → Agent Definitions → Skill Generation → Integration → Validation) writing `.claude/agents/*.md` + `.claude/skills/*/SKILL.md` into consumer projects; adds three localization skills (`korean-persona-search`, `korean-voice-adapter`, `korean-persona-harness`) sourcing from NVIDIA Nemotron-Personas-Korea (1M rows, CC BY 4.0); distributed as Claude Code plugin marketplace entry (`/plugin marketplace add hongsw/harness`) and global skill copy; **hongsw 직접 제작** — second design-origin datapoint alongside DureClaw; **locale/voice overlay** as a candidate third L4b axis pending a second independent datapoint
- Anthropic engineering: [Harness design for long-running applications](https://www.anthropic.com/engineering/harness-design-long-running-apps) — canonical dual-agent + sprint-contract architecture from Anthropic
- [Claudraband](https://github.com/halfwhey/claudraband) — Claude Code harness for power users; explicit senior-developer positioning; Level 2 mid-range segment
- Anthropic engineering: [Managed Agents](https://www.anthropic.com/engineering/managed-agents) — hosted long-running agents with stable interfaces independent of model version upgrades; governance/reliability primitive
- [Claude Code Routines](https://claude.ai/code/routines) — *(research preview, 2026-04)* — first-party Anthropic managed cloud runner; schedule / API / GitHub-event triggers; autonomous sessions on Anthropic infrastructure; `/schedule` CLI; Pro/Max/Team/Enterprise plans — first serverless execution-as-a-service runner native to Claude Code

---

## Level 3 — Team harness / executable SSOT / governance layer
This is the level where LLM usage stops being just a personal tool habit and becomes a team operating system.

This level includes:
- shared skills / rules / commands
- workflow packs
- reproducible project conventions
- review / approval / governance rules
- executable documentation
- what Toss describes as a **Harness** for raising team productivity floors

A key idea here is **Executable SSOT**:
- humans read it as a workflow or operating guide,
- agents read it as executable instructions.

Representative references:
- Toss article — *Harness for team productivity*  
  https://toss.tech/article/harness-for-team-productivity
- <img src="https://github.com/obra.png" alt="superpowers" width="18" /> [superpowers](https://github.com/obra/superpowers) — ⭐ 169,893 🔥🔥 agentic skills framework + software development methodology; Shell-first; "that works" reliability framing; largest-starred harness/SSOT repo in this taxonomy; spans Level 3 + Level 4b
- <img src="https://github.com/affaan-m.png" alt="everything-claude-code" width="18" /> [everything-claude-code](https://github.com/affaan-m/everything-claude-code) — ⭐ 168,366
- <img src="https://github.com/VoltAgent.png" alt="awesome-design-md" width="18" /> [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) — ⭐ 66,752 🔥 55+ DESIGN.md files extracted from popular sites; extends SSOT pattern into visual/UI domain — agents read design system rules before generating UI
- [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) — ⭐ 48,595 🔥 — agentic engineering curriculum by shanraisshan; Commands/Agents/Skills three-abstraction model; 69 tips from Claude Code creator Boris Cherny; comparative analysis of 10 frameworks; #1 GitHub Trending 2026-04-15; accessible from beginner to advanced
- <img src="https://github.com/Donchitos.png" alt="Claude-Code-Game-Studios" width="18" /> [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) — ⭐ 16,381 — domain-specialized Claude Code harness for game development; 49 AI agents + 72 workflow skills; coordination system mirrors real studio hierarchy; Shell-based; first high-signal domain-vertical Level 2/3 harness outside software engineering
- <img src="https://github.com/gotalab.png" alt="cc-sdd" width="18" /> [cc-sdd](https://github.com/gotalab/cc-sdd) — ⭐ 3,217
- <img src="https://github.com/first-fluke.png" alt="oh-my-agent" width="18" /> [oh-my-agent](https://github.com/first-fluke/oh-my-agent) — ⭐ 856
- <img src="https://github.com/Joonghyun-Lee-Frieren.png" alt="oh-my-gemini-cli" width="18" /> [oh-my-gemini-cli](https://github.com/Joonghyun-Lee-Frieren/oh-my-gemini-cli) — ⭐ 155
- <img src="https://github.com/open-gitagent.png" alt="gitagent" width="18" /> [gitagent](https://github.com/open-gitagent/gitagent) — Git-native open standard for agent definition and lifecycle management; `git clone` = agent instantiation
- **AGENTS.md** — OpenAI's cross-platform agent specification format; part of Agentic AI Foundation (Microsoft + Google + OpenAI + Anthropic + Linux Foundation); competes with / complements CLAUDE.md as executable SSOT
- DureClaw — *(primary Level 2)* — cross-machine multi-agent team coordinator; Phoenix WebSocket message bus + oah-agent workers implement a multi-machine SSOT pattern across Mac/Linux/Windows/Raspberry Pi

---

## Level 4 — Capability extension layer (MCP / memory / plugins / tools)
These systems add capabilities to agents rather than replacing the base runtime.
This is where context, memory, tools, MCP, plugins, and action-enabling systems live.

Level 4 is splitting into three observable subtypes:
- **4a. Memory / persistent context** — session or project-level memory systems
- **4b. Skill packs & skill managers** — domain-specific skill collections and lifecycle tools
- **4c. Tool-use / action infrastructure** — MCP servers, toolkits, platform connectors

### 4a. Memory / persistent context
- <img src="https://github.com/thedotmack.png" alt="claude-mem" width="18" /> [claude-mem](https://github.com/thedotmack/claude-mem) — ⭐ 68,547 🔥 hooks-based persistent memory with SQLite + Chroma, `npx claude-mem install`
- <img src="https://github.com/topoteretes.png" alt="cognee" width="18" /> [cognee](https://github.com/topoteretes/cognee) — ⭐ 16,853 — graph-native knowledge engine for AI agent memory; builds knowledge graphs (not just vectors) over documents, code, and conversations; 6-line API; MCP-compatible; multi-LLM; graph-native sub-type for reasoning over relationships
- <img src="https://github.com/zilliztech.png" alt="claude-context" width="18" /> [claude-context](https://github.com/zilliztech/claude-context) — ⭐ 9,859
- <img src="https://github.com/campfirein.png" alt="cipher" width="18" /> [cipher](https://github.com/campfirein/cipher) — ⭐ 4,657
- <img src="https://github.com/CaviraOSS.png" alt="OpenMemory" width="18" /> [OpenMemory](https://github.com/CaviraOSS/OpenMemory) — ⭐ 4,029
- <img src="https://github.com/Gentleman-Programming.png" alt="Engram" width="18" /> [Engram](https://github.com/Gentleman-Programming/engram) — ⭐ 2,912 — Go binary persistent memory system for AI coding agents; agent-agnostic (Claude Code / OpenCode / Gemini CLI / Codex / Cursor / Windsurf via MCP); 17 MCP tools + What/Why/Where/Learned schema + session lifecycle hooks (`mem_session_start/end`); SQLite + FTS5; protocol-endpoint shape (Engram exposes memory through MCP) vs. Beads' runtime-layer shape; *(also Level 5 inspectable agent memory sub-pattern)*
- <img src="https://github.com/garrytan.png" alt="GBrain" width="18" /> [GBrain](https://github.com/garrytan/gbrain) — MIT — personal knowledge base for agents by YC CEO Garry Tan; markdown+PGLite backend; agents read-before/write-after; OpenClaw+Hermes native; CLI via bun; "compounding personal knowledge" sub-pattern
- [wuphf](https://github.com/nex-crm/wuphf) — Karpathy-style LLM wiki maintained by agents in Markdown + Git; multi-agent shared workspace with notebook → wiki promotion + lint gates; human-inspectable agent-maintained memory; vector-DB-free track alongside Beads / Engram / GBrain; *(also Level 5 inspectable agent memory sub-pattern; also Level 6b LLM-native KB — first confirmed implementation)*
- <img src="https://github.com/memvid.png" alt="memvid" width="18" /> [memvid](https://github.com/memvid/memvid) — ⭐ 15,283 — Rust-native single-file `.mv2` memory container; bundles header + embedded WAL + HNSW vector index + Tantivy/BM25 full-text + temporal index + TOC into one append-only binary; v2.0 Python→Rust rewrite (March 2026); claimed 0.025ms P50 retrieval; downstream `memvid/claude-brain` Claude Code plugin at 477★; **portable-binary memory** sub-track distinct from markdown+git (wuphf, GBrain) and SQLite+MCP (Engram, Beads); Apache-2.0; *(also Level 5 inspectable agent memory sub-pattern)*

### 4b. Skill packs & skill managers
**Skill managers (lifecycle/discovery):**
- <img src="https://github.com/Shpigford.png" alt="Chops" width="18" /> [Chops](https://github.com/Shpigford/chops) — macOS skill manager across Claude Code, Cursor, Codex, Windsurf, Amp simultaneously
- <img src="https://github.com/amebahead.png" alt="skills-cleaner" width="18" /> [skills-cleaner](https://github.com/amebahead/skills-cleaner) — Claude plugin for listing, deduplication, and lifecycle management of `.claude/plugin/` skills
- [claudemarketplaces.com](https://claudemarketplaces.com/) — 150+ skills with ratings (March 2026); first rated marketplace for Claude skills
- [claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) — 340 plugins + 1,367 agent skills catalog

**Platform-native plugin systems:**
- <img src="https://github.com/anthropics.png" alt="claude-plugins-official" width="18" /> [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) — ⭐ 18,040
- OpenAI Codex plugin system — Skills + Apps + MCP bundles; official plugins for GitHub, Linear, Vercel, Netlify, Slack, Figma, Notion, Gmail

**Domain skill packs:**
- <img src="https://github.com/msitarzewski.png" alt="agency-agents" width="18" /> [agency-agents](https://github.com/msitarzewski/agency-agents) — ⭐ 92,398 🔥🔥 144 agents across 12 professional divisions (Engineering, Marketing, Sales, Legal, Finance, Healthcare, Game Dev, and more); automated cross-tool conversion pipeline (`./scripts/convert.sh`) generates tool-specific formats from a single Markdown SSOT for Claude Code, Cursor, Copilot, Aider, Windsurf, Gemini CLI, and others; largest-starred persona skill pack in the taxonomy; first L4b pack spanning non-technical professional verticals at high star count; MIT license; community-origin (Reddit); 15.2k forks — *Primary L4b (cross-tool-portable skill pack sub-type); weak secondary L3 read (12-division org structure resembles an org chart SSOT but no governance workflow, approval chain, or sprint lifecycle present)*
- <img src="https://github.com/JuliusBrussee.png" alt="caveman" width="18" /> [caveman](https://github.com/JuliusBrussee/caveman) — ⭐ 48,120 🔥 output token compression skill (65–75% prose reduction); three intensity levels (Lite/Full/Ultra); install via `npx skills add`
- <img src="https://github.com/kepano.png" alt="obsidian-skills" width="18" /> [obsidian-skills](https://github.com/kepano/obsidian-skills) — ⭐ 26,818 — first-party agent skill pack from Obsidian CEO; teaches agents Markdown, Bases, JSON Canvas, and Obsidian CLI; signals L4b maturation beyond coding into knowledge-work
- <img src="https://github.com/coreyhaines31.png" alt="marketingskills" width="18" /> [marketingskills](https://github.com/coreyhaines31/marketingskills) — ⭐ 25,162 🔥 marketing domain skill pack for Claude Code and AI agents; CRO, copywriting, ad copy, campaign analysis; largest-starred non-developer domain skill pack in this taxonomy; signals L4b expansion beyond software/knowledge-work into all professional verticals
- <img src="https://github.com/team-attention.png" alt="plugins-for-claude-natives" width="18" /> [plugins-for-claude-natives](https://github.com/team-attention/plugins-for-claude-natives) — ⭐ 748
- <img src="https://github.com/pbakaus.png" alt="Impeccable" width="18" /> [Impeccable](https://github.com/pbakaus/impeccable) — 20 design commands across 7 domains (layout, spacing, color, typography…) for Claude Code + Cursor
- <img src="https://github.com/NomaDamas.png" alt="K-Skill" width="18" /> [K-Skill](https://github.com/NomaDamas/k-skill) — Korean-localized skill pack (SRT, Seoul subway, KBO, lottery)

### 4c. Tool-use / action infrastructure
- <img src="https://github.com/modelcontextprotocol.png" alt="MCP Servers" width="18" /> [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — ⭐ 84,644 *(governance: donated to Agentic AI Foundation Dec 2025; 97M monthly SDK downloads)*
- <img src="https://github.com/ChromeDevTools.png" alt="chrome-devtools-mcp" width="18" /> [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) — ⭐ 37,402 — official MCP server from Chrome DevTools team; exposes DOM, network, console, performance, and storage via MCP; highest-starred MCP server in this taxonomy; enables live browser QA and debugging inside any agent session; closes the gap between coding agents and web browser state
- <img src="https://github.com/ComposioHQ.png" alt="Composio" width="18" /> [Composio](https://github.com/ComposioHQ/composio) — ⭐ 27,933
- <img src="https://github.com/oraios.png" alt="serena" width="18" /> [serena](https://github.com/oraios/serena) — ⭐ 23,498
- <img src="https://github.com/czlonkowski.png" alt="n8n-mcp" width="18" /> [n8n-mcp](https://github.com/czlonkowski/n8n-mcp) — ⭐ 19,481 — MCP server exposing the full n8n node library (1,650+ integrations) to any MCP-compatible Claude surface; 7 zero-credential discovery/validation tools + 13 management tools requiring N8N API credentials; pre-indexed SQLite knowledge cache rather than live API passthrough; 541+ tests, 201 releases, TypeScript 91.8%; workflow-platform MCP bridge sub-type distinct from browser-automation and credential-proxy sub-clusters; relevant to `task: data-analysis` and `task: research` profiles with structured-workflow requirements
- <img src="https://github.com/microsoft.png" alt="mcp-for-beginners" width="18" /> [mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) — ⭐ 15,963
- <img src="https://github.com/IBM.png" alt="mcp-context-forge" width="18" /> [mcp-context-forge](https://github.com/IBM/mcp-context-forge) — ⭐ 3,620
- <img src="https://github.com/withoneai.png" alt="Pica" width="18" /> [Pica](https://github.com/withoneai/pica) — ⭐ 1,476
- <img src="https://github.com/rtk-ai.png" alt="rtk" width="18" /> [rtk](https://github.com/rtk-ai/rtk) — Rust CLI token proxy; sits between agent and shell, compresses git/ls/test output 60–90% before the LLM reads it; zero-dependency single binary
- <img src="https://github.com/millionco.png" alt="Expect" width="18" /> [Expect](https://github.com/millionco/expect) — CLI that auto-generates and executes browser-based test plans from code changes (Claude/Codex backend)
- [Libretto](https://github.com/saffron-health/libretto) — deterministic AI browser automation; "Making AI Browser Automations Deterministic"; health-tech provenance implies production/compliance requirements; first Level 4c entry with reliability (not capability) as primary value proposition; early signal, revisit at 1k★
- [browser-harness](https://github.com/browser-use/browser-harness) — from the browser-use team; gives LLM raw CDP access + `helpers.py`; self-healing (LLM edits helpers.py mid-task when steps fail); anti-framework stance; new Level 4c sub-type: **self-healing browser automation** distinct from deterministic (Libretto) and MCP-mediated (chrome-devtools-mcp) patterns; HN Show HN 77 pts (2026-04-25)

---

## Level 5 — Research / evaluation / benchmark / autoresearch patterns
These are especially useful when designing clawfit's abstraction layer and long-term research model.
They include evaluation harnesses, benchmark references, autonomous research loops, and **collective agent knowledge systems**.

- <img src="https://github.com/karpathy.png" alt="autoresearch" width="18" /> [autoresearch](https://github.com/karpathy/autoresearch) — ⭐ 77,236
- <img src="https://github.com/langfuse.png" alt="Langfuse" width="18" /> [Langfuse](https://github.com/langfuse/langfuse) — ⭐ 26,186 — open-source LLM engineering platform: observability, metrics, evals, prompt management, playground, datasets; MIT + managed cloud; self-hostable; integrates LangChain/LlamaIndex/OpenAI/Anthropic/LiteLLM; production observability for deployed agent systems (distinct from pre-deployment benchmarks)
- <img src="https://github.com/microsoft.png" alt="agent-lightning" width="18" /> [agent-lightning](https://github.com/microsoft/agent-lightning) — ⭐ 17,042
- <img src="https://github.com/EleutherAI.png" alt="lm-evaluation-harness" width="18" /> [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — ⭐ 12,342
- <img src="https://github.com/mozilla-ai.png" alt="any-llm" width="18" /> [any-llm](https://github.com/mozilla-ai/any-llm) — ⭐ 1,926
- <img src="https://github.com/mozilla-ai.png" alt="any-agent" width="18" /> [any-agent](https://github.com/mozilla-ai/any-agent) — ⭐ 1,156
- <img src="https://github.com/prometheus-eval.png" alt="Prometheus" width="18" /> [Prometheus](https://github.com/prometheus-eval/prometheus) — ⭐ 315
- <img src="https://github.com/team-attention.png" alt="hoyeon" width="18" /> [hoyeon](https://github.com/team-attention/hoyeon) — ⭐ 149
- <img src="https://github.com/anomalyco.png" alt="opencode-bench" width="18" /> [opencode-bench](https://github.com/anomalyco/opencode-bench) — ⭐ 64
- <img src="https://github.com/Hugging-Face-KREW.png" alt="Ko-AgentBench" width="18" /> [Ko-AgentBench](https://github.com/Hugging-Face-KREW/Ko-AgentBench) — ⭐ 64
- <img src="https://github.com/mozilla-ai.png" alt="cq" width="18" /> [cq](https://blog.mozilla.ai/cq-stack-overflow-for-agents/) — Mozilla AI shared knowledge commons for agents; query before acting, contribute after — "Stack Overflow for agents"
- <img src="https://github.com/HudsonGri.png" alt="mdarena" width="18" /> [mdarena](https://github.com/HudsonGri/mdarena) — empirical benchmarking of CLAUDE.md instruction variants; mines merged PRs, runs agent with/without instruction files, grades by test pass rate + diff overlap; SWE-bench-compatible export
- [CC-Canary](https://github.com/delta-hq/cc-canary) — stdlib-only Python; reads `~/.claude/projects/**/*.jsonl`; measures tool-mix, read:edit ratio, self-admitted errors, stop hook violations, thinking depth; composite health score with argmax regression date detection; **per-session behavioral health monitor** sub-type distinct from capability benchmarks and trace observability; HN 37 pts (2026-04-25)

---

## Level 6 — Data / evidence / knowledge infrastructure
These references are useful when clawfit evolves into an evidence hub and simulation system.
They help answer how agents access, structure, retrieve, and reason over external knowledge.

Two architectural sub-types formalised 2026-05-05, anchored by Karpathy LLM Wiki gist (2026-04-04):

### L6a — Retrieval-native knowledge infrastructure
Pre-process → embed → index → retrieve → inject. LLM is the *consumer* of the knowledge store; pipelines or humans maintain it. Entry point to L6 for large-corpus and multi-modal use cases.

- <img src="https://github.com/opendatalab.png" alt="MinerU" width="18" /> [MinerU](https://github.com/opendatalab/MinerU) — ⭐ 61,356
- <img src="https://github.com/HKUDS.png" alt="LightRAG" width="18" /> [LightRAG](https://github.com/HKUDS/LightRAG) — ⭐ 34,415
- <img src="https://github.com/VectifyAI.png" alt="PageIndex" width="18" /> [PageIndex](https://github.com/VectifyAI/PageIndex) — ⭐ 25,871
- <img src="https://github.com/HKUDS.png" alt="RAG-Anything" width="18" /> [RAG-Anything](https://github.com/HKUDS/RAG-Anything) — ⭐ 19,033
- <img src="https://github.com/cocoindex-io.png" alt="CocoIndex" width="18" /> [CocoIndex](https://github.com/cocoindex-io/cocoindex) — ⭐ 7,655 — incremental data pipeline engine for AI agents; Rust core with Python API; delta-only reprocessing (claimed 99.9% corpus cache reuse); declarative `Target = F(Source)` model; 12 connectors across vector DBs (LanceDB, Qdrant), graph DBs (FalkorDB, SurrealDB), relational DBs, data warehouses, message queues, and feature stores; end-to-end lineage; explicitly agent-framed ("continuously fresh context for your AI agents"); v1.0.2 stable (April 2026), Apache-2.0; write-side ingestion counterpart to read-side memory sync tools (airweave)
- <img src="https://github.com/airweave-ai.png" alt="airweave" width="18" /> [airweave](https://github.com/airweave-ai/airweave) — ⭐ 6,266
- <img src="https://github.com/agentset-ai.png" alt="agentset" width="18" /> [agentset](https://github.com/agentset-ai/agentset) — ⭐ 1,968

### L6b — LLM-native knowledge base
LLM is the *maintainer* of the knowledge store, not just the consumer. Sources → LLM reads and synthesises → LLM-maintained structured artifact (Markdown wiki, compendium) → LLM or human queries. No retrieval pipeline required; the LLM is the indexing and summarisation layer. Best fit for mid-sized corpora that fit in a large context window; grows in relevance as context windows expand.

Architectural reference: Karpathy LLM Wiki pattern — https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (2026-04-04)
Research-watch doc: `docs/research-watch/2026-05-05-llm-wiki-knowledge-layer-paradigm.md`

Promotion threshold: second independent ≥5k-star implementation explicitly adopting the LLM-maintains-KB pattern.

- [wuphf](https://github.com/nex-crm/wuphf) — Karpathy-style LLM wiki maintained by agents in Markdown + Git; multi-agent shared workspace with notebook → wiki promotion + lint gates; first confirmed L6b implementation *(also Level 4a memory — agent-memory primary read)*
- [GBrain](https://github.com/garrytan/gbrain) — personal knowledge base for agents by YC CEO Garry Tan; markdown+PGLite backend; agents read-before/write-after; compounding personal knowledge sub-pattern *(also Level 4a memory)*
- [찰떡AI (Chaltteok)](https://chaltteok-app.baryon.ai/) — (Baryon Labs, Seoul; MCP module MIT open-source: [`baryonlabs/chaltteok-app-mcp`](https://github.com/baryonlabs/chaltteok-app-mcp), Rust) Windows desktop AI assistant for SMB document generation (quotations, legal case files). Core L6b pattern: user's accumulated past documents (quotations, vendor notes, product lists) → LLM maintains local knowledge graph (nodes + edges, `GraphUpdate` field in MCP `Plan` output) → future documents auto-adapted to user's domain terminology, pricing, and practices. LLM routes between Codex and Claude via MCP abstraction. **Local-only** — all data stays on-device, no cloud sync; Korean privacy law compliant. Closed beta (v1.2.3). *(L4c secondary — host-protective MCP routing layer: "safety-first, host-defined actions only" — LLM cannot invoke arbitrary actions, only host-app-declared ones; distinct inward-protection variant not previously documented in L4c)*

---

## Level 7 — Human interface / voice / input-output layer
These are not always the main coding engine, but they strongly influence how humans actually operate agents.
This includes voice input, talk mode, speech interruption, remote relays, terminals, and interaction loops.

- <img src="https://github.com/jamiepine.png" alt="Voicebox" width="18" /> [Voicebox](https://github.com/jamiepine/voicebox) — ⭐ 23,680 — open-source voice synthesis studio; TypeScript-first; voice cloning, style transfer, multi-speaker management; surpasses VoxCPM in star count; natural pairing for TypeScript/Vercel-ecosystem orgs; TypeScript-native voice output sub-type
- <img src="https://github.com/OpenBMB.png" alt="VoxCPM" width="18" /> [VoxCPM](https://github.com/OpenBMB/VoxCPM) — ⭐ 16,083 — tokenizer-free TTS for multilingual speech generation; lower latency voice output layer for agent pipelines; fills Level 7 voice output gap alongside Ghost Pepper (input)
- <img src="https://github.com/BasedHardware.png" alt="omi" width="18" /> [omi](https://github.com/BasedHardware/omi) — ⭐ 12,266 — passive ambient AI; continuously watches screen and listens to audio; proactively surfaces suggestions without push-to-activate; Flutter/Dart, cross-platform; "advisor in the room" model for exec/PM personas; new passive-ambient sub-type distinct from hold-to-talk (Ghost Pepper) and dictation (Superwhisper)
- <img src="https://github.com/thunderbird.png" alt="Thunderbolt" width="18" /> [Thunderbolt](https://github.com/thunderbird/thunderbolt) — ⭐ 4,294 — privacy-first cross-platform AI client (web/iOS/Android/macOS/Linux/Windows); MPL 2.0; compatible with Ollama/llama.cpp/OpenAI-compatible APIs; "choose your models, own your data"; enterprise on-premises deployment; from Thunderbird/Mozilla ecosystem; first on-premises AI client sub-type in Level 7
- <img src="https://github.com/langchain-ai.png" alt="deep-agents-ui" width="18" /> [deep-agents-ui](https://github.com/langchain-ai/deep-agents-ui) — ⭐ 1,577 — Next.js web UI for deepagents; chat + file monitor + step-through debug (companion to Level 1/2 deepagents)
- [Ghostmeet](https://github.com/Higangssh/ghostmeet) — ⭐ 37 — self-hosted Chrome extension for real-time meeting transcription (Whisper) + AI summary (Claude API); fully local, no audio leaves device
- <img src="https://github.com/hada0127.png" alt="cc-telegram" width="18" /> [cc-telegram](https://github.com/hada0127/cc-telegram) — ⭐ 14
- <img src="https://github.com/channprj.png" alt="claude-code-voice" width="18" /> [claude-code-voice](https://github.com/channprj/claude-code-voice) — ⭐ 8
- Claude Computer Use — first-party Anthropic desktop control (mouse + keyboard + screen) via Claude Code Desktop + Cowork *(also Level 1)*
- Superwhisper — https://superwhisper.com/
- OpenClaw talkmode improvement reference — https://github.com/openclaw/openclaw/pull/53553#issuecomment-4124082023
- [Ghost Pepper](https://github.com/matthartman/ghost-pepper) — local hold-to-talk STT for macOS (Whisper-based); fully offline, no audio leaves device; privacy-first alternative to Superwhisper for confidential environments
- [Happy](https://github.com/happy-app/happy) — open-source cross-platform mobile client (iOS/Android/web) for Claude Code + Codex; CLI wrapper approach; first open-source mobile-native Level 7 entry with dual-agent support; introduces `mobile` sub-type for exec/PM users needing agent access without terminal
- [Zed](https://zed.dev) — GPU-accelerated code editor (Rust, 120fps); **Zed 1.0 stable released 2026-04-30** with simultaneous Zed for Business SKU (centralized billing, RBAC, team management); native parallel agents via Threads Sidebar (released 2026-04-22) — multiple simultaneous agent threads per window with per-thread AI backend mixing, filesystem scope isolation, and worktree isolation; built-in **ACP (Agent Client Protocol) multiplexing** for Claude Agent / Codex / OpenCode / Cursor inside one editor; first IDE to absorb Level 2 multi-agent orchestration as a first-class editor feature; Apache-2.0 open source; enterprise eligibility threshold crossed for `team_size: large` + `governance_need: hard` profiles

---

## Vibe coding topic scan (2026-03-27)
The GitHub topic `vibe-coding` is broad and noisy. It includes at least five different subfamilies that clawfit should not collapse into one bucket.

### A. Core engines / primary surfaces
These are tools people may directly choose as their main build surface.

- Onlook — AI-first visual app builder / design-to-code surface  
  https://github.com/onlook-dev/onlook
- Superset — multi-agent desktop IDE / orchestration surface  
  https://github.com/superset-sh/superset
- Kaku — terminal built for AI coding  
  https://github.com/tw93/Kaku
- Crystal (Nimbalyst) — desktop workflow manager for parallel AI coding sessions  
  https://github.com/stravu/crystal

**clawfit mapping:** usually Level 1 or Level 2 depending on whether the repo is a primary user-facing environment or mostly an orchestration shell.

### B. Workflow wrappers / orchestration / team execution
These are strongly relevant to clawfit because they shape practical multi-agent execution patterns.

- oh-my-claudecode — Claude Code multi-agent orchestration  
  https://github.com/yeachan-heo/oh-my-claudecode
- ccpm — GitHub Issues + worktree based parallel agent execution  
  https://github.com/automazeio/ccpm
- claude-squad — multi-terminal-agent management  
  https://github.com/smtg-ai/claude-squad
- refly — workflow/skills builder across Claude Code, Cursor, Codex, etc.  
  https://github.com/refly-ai/refly

**clawfit mapping:** mostly Level 2.

### C. Context / memory / MCP support infrastructure
These are not the main coding engine, but they materially affect agent quality and capability.

- Context7 — up-to-date documentation/context layer for AI coding tools  
  https://github.com/upstash/context7
- serena — semantic retrieval/editing toolkit for coding agents  
  https://github.com/oraios/serena
- cipher — memory layer for coding agents via MCP  
  https://github.com/campfirein/cipher
- claude-context — code search MCP for Claude Code  
  https://github.com/zilliztech/claude-context

**clawfit mapping:** mostly Level 4.

### D. Guidance / best practices / learning resources
These are important evidence sources for behavior, workflow norms, onboarding, and ecosystem understanding, but they are not usually recommendation endpoints by themselves.

- claude-code-best-practice — workflow and usage guidance  
  https://github.com/shanraisshan/claude-code-best-practice
- awesome-vibe-coding — curated reference list  
  https://github.com/filipecalegario/awesome-vibe-coding
- easy-vibe — learning/tutorial resource  
  https://github.com/datawhalechina/easy-vibe
- vibe-vibe — systematic learning/tutorial resource  
  https://github.com/datawhalechina/vibe-vibe

**clawfit mapping:** supporting references; usually Level 2, 3, or 7 context rather than Level 1 comparison targets.

### E. Platform / SDK layer
These help developers build their own vibe-coding products rather than directly serving as end-user comparison targets.

- vibesdk — platform for building vibe-coding systems  
  https://github.com/cloudflare/vibesdk
- ruler — cross-agent rule layer / policy consistency  
  https://github.com/intellectronica/ruler

**clawfit mapping:** Level 3 or Level 4 depending on whether the emphasis is architecture or capability extension.

## Meta-wrapper / harness-enhancement scan (2026-03-27)
A distinct pattern is emerging around repositories such as `oh-my-openagent`, `oh-my-claudecode`, `oh-my-codex`, `oh-my-gemini-cli`, `oh-my-agent`, `SuperClaude Framework`, routers, and other wrapper-style projects.

These projects are not usually new base agents from scratch. Instead, they sit **on top of existing agents** (Claude Code, OpenCode, Codex, Gemini CLI, etc.) and try to transform them through:
- better defaults
- orchestration layers
- curated skills / rules / prompts
- multi-agent coordination
- model routing
- compatibility layers
- project-level workflow conventions
- team productivity harnesses

This means clawfit should treat them as a separate ecosystem pattern: **meta wrappers / harness enhancers / meta transformation layers**.

### A. "Oh-my-*" style wrapper family
These repos explicitly package an opinionated upgraded experience around an existing agent stack.

- oh-my-openagent — agent harness / meta wrapper / orchestration layer  
  https://github.com/code-yeongyu/oh-my-openagent
- oh-my-claudecode — Claude Code oriented orchestration wrapper  
  https://github.com/yeachan-heo/oh-my-claudecode
- oh-my-codex — Codex enhancement / hooks / HUD / agent team layer  
  https://github.com/Yeachan-Heo/oh-my-codex
- oh-my-gemini-cli — context-engineering-powered workflow pack for Gemini CLI  
  https://github.com/Joonghyun-Lee-Frieren/oh-my-gemini-cli
- oh-my-agent — portable multi-agent harness across multiple base runtimes  
  https://github.com/first-fluke/oh-my-agent
- oh-my-opencode — OpenCode enhancement layer / curated tools / compatibility layer  
  https://github.com/opensoft/oh-my-opencode

**signal:** the naming pattern itself suggests an emerging family of "upgrade the base agent" projects rather than entirely new runtimes.

### A2. Multi-keyword scan signals
The following keyword bundle was used to probe for this ecosystem pattern:
`automation opencode multi-agent-systems ai-agents claude parallel-execution vibe-coding claude-code agentic-coding oh-my-opencode`

The direct combined query was noisy, but adjacent narrower searches revealed a wider family of related projects around the same axis.

Representative signals found:
- `yeachan-heo/oh-my-claudecode` — strong direct hit for Claude Code meta-orchestration
- `Yeachan-Heo/oh-my-codex` — explicit Codex-side expansion of the same pattern
- `Joonghyun-Lee-Frieren/oh-my-gemini-cli` — Gemini CLI adaptation of the same packaging logic
- `first-fluke/oh-my-agent` — runtime-agnostic portable harness form
- `code-yeongyu/oh-my-openagent` — direct hit and renamed lineage from `oh-my-opencode`
- `opensoft/oh-my-opencode` — OpenCode enhancement / compatibility layer
- `musistudio/claude-code-router` — routing wrapper around Claude Code
- `affaan-m/everything-claude-code` — skills/rules/harness optimization layer
- `can1357/oh-my-pi` — parallel evidence that the `oh-my-*` packaging pattern is spreading beyond Claude/OpenCode
- `gotalab/cc-sdd` — structured workflow layer across Claude Code, Codex, OpenCode, Cursor, Copilot, Gemini CLI, Windsurf
- `michaelshimeles/ralphy` — autonomous loop wrapper spanning Claude Code, Codex, OpenCode, Cursor agent, Qwen, Droid

**signal:** this is no longer one repo family; it is becoming a broader packaging pattern for turning base agents into more opinionated operating environments.

### B. Framework / router / optimization layer
These repos focus on shaping how an existing base agent behaves, routes, or operates.

- SuperClaude Framework — framework and behavior layer for Claude-centric workflows  
  https://github.com/SuperClaude-Org/SuperClaude_Framework
- claude-code-router — routing/infrastructure wrapper around Claude Code  
  https://github.com/musistudio/claude-code-router
- everything-claude-code — skill/rules/agent harness optimization system  
  https://github.com/affaan-m/everything-claude-code

**signal:** these are not merely prompts, but meta-level attempts to standardize or transform the operating envelope of a popular agent.

### C. Why this matters to clawfit
This pattern is strategically important because it indicates that users do not just pick a base agent anymore.
They increasingly pick:
1. a **base runtime** (Claude Code / OpenCode / Codex / Gemini CLI / etc.)
2. a **meta wrapper / enhancement layer** on top of it
3. often a **team harness / executable SSOT layer** to standardize behavior across an organization

That creates a second-order choice architecture.

In other words, the market is shifting from:
- "Which agent should I use?"

toward:
- "Which base agent should I use?"
- "Which enhancement layer / harness / wrapper should I add on top?"
- "How do I package that into a reproducible team workflow?"

### D. clawfit mapping
These wrapper-style projects usually belong near **Level 2** because they shape orchestration and workflow.
However, some of them also overlap with:
- **Level 3** when they function like a team productivity harness or executable SSOT
- **Level 4** when they add MCP/context/memory/plugin capability layers

### E. Meta-wrapper scan takeaway
The `oh-my-open*` family and similar projects should be recognized as a distinct pattern:

**meta transformation of existing agent systems**.

This is not the same as:
- building a new base agent
- building a tool for agents
- building a catalog of agents

Instead, it is about **repackaging, upgrading, routing, and orchestrating existing agents into a more opinionated operating system**.

That makes it an important independent axis in clawfit's ecosystem map.

## Agent tool scan (2026-03-27)
The GitHub topic/query space around `agent-tool`, `agent tools`, and `agent toolkit` is also noisy and should not be used as a canonical taxonomy.

Two patterns emerged:
1. The literal topic `agent-tool` is mostly too sparse / low-signal.
2. Broader search phrases such as `agent toolkit`, `agent tools`, and `tooling for agents` surface more meaningful repositories.

### A. Tooling platforms and tool-access infrastructure
These are platforms or tool layers that help agents actually take action.

- Composio — large tool-access / auth / sandbox platform for agents  
  https://github.com/ComposioHQ/composio
- Pica — agentic tooling platform  
  https://github.com/withoneai/pica
- strands-agents/tools — tools package for agent capabilities  
  https://github.com/strands-agents/tools
- modelcontextprotocol/servers — MCP server ecosystem reference  
  https://github.com/modelcontextprotocol/servers

**clawfit mapping:** usually Level 4 or Level 3 depending on whether the emphasis is capability extension or architectural abstraction.

### B. Agent orchestration / workflow / collaboration tooling
These are not merely tools used by agents, but systems for coordinating agent work.

- AutoGen — programming framework for agentic AI  
  https://github.com/microsoft/autogen
- CrewAI — orchestration framework for collaborative agents  
  https://github.com/crewAIInc/crewAI
- Sim — deploy/orchestrate AI agents  
  https://github.com/simstudioai/sim
- paperclip — orchestration for zero-human companies  
  https://github.com/paperclipai/paperclip
- ruflo — orchestration platform for Claude-centric swarms  
  https://github.com/ruvnet/ruflo

**clawfit mapping:** usually Level 2 or Level 3.

### C. Coding-agent-specific toolkits and wrappers
These are especially relevant to clawfit because they sit close to coding workflows.

- serena — semantic retrieval/editing toolkit for coding agents  
  https://github.com/oraios/serena
- pi-mono — AI agent toolkit with coding agent CLI / APIs / UIs  
  https://github.com/badlogic/pi-mono
- claude-code-router — infrastructure wrapper around Claude Code  
  https://github.com/musistudio/claude-code-router
- Dicklesworthstone/agentic_coding_flywheel_setup — bootstrapped multi-agent coding environment  
  https://github.com/Dicklesworthstone/agentic_coding_flywheel_setup

**clawfit mapping:** usually Level 2, 3, or 4 depending on whether the main value is orchestration, architecture, or tool augmentation.

### D. Catalogs / awesome lists / discovery layers
These help discovery but should not be treated as direct comparison endpoints.

- awesome-ai-agents  
  https://github.com/e2b-dev/awesome-ai-agents
- awesome_ai_agents  
  https://github.com/jim-schwoebel/awesome_ai_agents
- ai-agent-tools-catalog  
  https://github.com/GetStream/ai-agent-tools-catalog
- awesome-mcp-servers  
  https://github.com/appcypher/awesome-mcp-servers
- awesome-openclaw  
  https://github.com/SamurAIGPT/awesome-openclaw

**clawfit mapping:** support/discovery references, not primary product choices.

## Agent tool scan takeaway
As with `vibe-coding`, the phrase `agent tool` is better treated as a **discovery surface** than a stable category.

For clawfit, newly discovered repos in this area should be reclassified by asking:
- Is this a tool-access layer for agents?
- Is this an orchestration/workflow framework?
- Is this a coding-agent-specific augmentation layer?
- Is this only a catalog / discovery resource?

This prevents `agent tool` from collapsing platforms, wrappers, MCP servers, catalogs, and orchestration systems into one bucket.

## Notes
- Level 1 is the base runtime / primary product surface.
- Levels 2 and 3 are increasingly important because the market is clearly developing a harness layer above base agents.
- Feature claims should be stored with evidence links and verification dates, not just yes/no flags.
- Topics like `vibe-coding` and `agent-tool` are useful for discovery, but not sufficient as canonical taxonomy.
