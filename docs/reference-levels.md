# clawfit Reference Levels v0.3

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
- excludes for now: a full standalone ontology of LLM models/providers themselves (those may need a separate map/registry)
- region/language: global by default; local ecosystem items may still appear when strategically relevant

### Important note
The numbered levels below should be read as **ecosystem layers / lenses**, not as a sequential maturity ladder.
Date-stamped scans and discovery notes support this map, but they should increasingly live in separate scan documents over time.

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

### New patterns as of 2026-04 (v0.3 update)
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

### New signals as of 2026-04-08
- **Claude Mythos Preview — new Anthropic model tier:** Three simultaneous HN front-page entries (1,584 pts combined) covering system card, cybersecurity capability assessment, and Project Glasswing. Introduces explicit long-horizon and security-domain capabilities; may warrant a new LLM registry tier above current Opus/Sonnet. Glasswing is the first Anthropic-branded AI security governance framework.
- **GLM-5.1 "long-horizon tasks":** ZhipuAI's new model (z.ai, 401 HN pts) explicitly positions around multi-step agentic task completion — "long-horizon" as primary framing signals a new evaluation axis for LLM selection in clawfit beyond latency/cost.
- **NVIDIA PersonaPlex enters persona layer:** NVIDIA (github.com/NVIDIA/personaplex, 662 trending stars) publishing a persona-based AI application library signals hardware vendors moving up-stack into agent identity configuration — potential Level 4c entrant.
- **Production skill packs reach senior practitioners:** Addy Osmani (Google Chrome DevRel) published `agent-skills` — production-grade engineering skills for AI coding agents. First high-credibility Level 4b entry from a named Google engineer.

### New signals as of 2026-04-11
- **"Harness Engineering" named as a paradigm:** A four-year retrospective (bits-bytes-nn.github.io, GeekNews front page) documents the progression "Prompt Engineering → Context Engineering → Harness Engineering (2025–2026)." When practitioners name a paradigm, vocabulary has matured. Validates clawfit's Level 2–3 emphasis; suggests increasing harness-layer weight in recommendations for orgs at maturity stages 5–7.
- **obra/superpowers crosses 145k stars:** Shell-based agentic skills framework + development methodology reaches the largest star count of any harness/SSOT repo in this taxonomy. Explicit "that works" framing targets reliability, not novelty. Spans Level 3 (methodology) and Level 4b (skills). First Level 3 entry with mainstream adoption evidence.
- **Archon: harness-builder as tool type:** coleam00/Archon (15k★, GitHub Trending) explicitly calls itself a "harness builder" — a meta-tool that generates harness configurations. "Deterministic and repeatable" framing targets governance/reliability axis. New Level 2 sub-type: harness generator vs. harness runtime.
- **rowboat: memory-native AI coworker:** rowboatlabs/rowboat (11.7k★, GitHub Trending) frames memory as first-class, not a plugin. "Coworker" framing implies persistent task ownership. Adds a memory-native Level 1 sub-type alongside stateless base agents.
- **Twill.ai (YC S25): async cloud agent delegation:** HN Launch HN front page — "delegate to cloud agents, get back PRs." Async fire-and-forget model with PR output is a new deployment topology for Level 1: no interactive session, no local setup. First managed cloud agent service in this taxonomy.
- **multica: open-source managed agents platform:** multica-ai/multica (6k★, GitHub Trending) — "turn coding agents into real teammates — assign tasks, track progress." Team-oriented multi-agent management platform enters Level 2.

### New signals as of 2026-04-15
- **Claude Code Routines — first-party serverless agent execution:** (HN front page, code.claude.com/docs/en/routines) — Anthropic launches Routines in research preview: saved Claude Code configurations triggered by schedule, HTTP API, or GitHub events (PRs, pushes, issues, 18 event types), running autonomously on Anthropic-managed cloud infrastructure. Introduces `managed_hosted` + `event_driven` statefulness mode — distinct from interactive sessions or sprint-loop harnesses. GitHub event triggers encode org workflows as automation, enabling PM/exec initiation of agent runs without CLI access. First Anthropic-native serverless runner in this taxonomy. Enters Level 2.
- **shanraisshan/claude-code-best-practice crosses 43.7k stars as #1 trending:** (GitHub Trending #1) — comprehensive agentic engineering curriculum with explicit three-abstraction model (Commands/Agents/Skills). 69 curated tips from Boris Cherny (Claude Code creator). Comparative analysis of 10 major frameworks. "Agentic engineering" vocabulary now independently named by three major guides (obra/superpowers, gsd/get-shit-done, this). The Level 3 SSOT layer has three confirmed entry points: code harnesses, methodology guides, and behavioral spec files (CLAUDE.md). clawfit's registry `claude_code_best_practice` min_maturity lowered to 2 (accessible to beginners), pm+researcher roles added.
- **virattt/ai-hedge-fund at 54k stars — domain-specialized multi-agent finance system:** (GitHub Trending) — 19 specialized agents modeling investor personas (Buffett, Munger, Lynch, Wood, Burry + analytics agents); multi-LLM (OpenAI/Anthropic/Groq/DeepSeek/Ollama). Educational but highest-starred domain-specialized multi-agent application in taxonomy. Validates `research` + `data-analysis` tasks beyond software development contexts. Not added to registry (too domain-specific for generic scoring).
- **kontext-cli — credential broker for AI coding agents:** (HN Show HN, 98★) — Go binary replacing long-lived API keys with ephemeral OIDC+RFC 8693 token-exchanged credentials injected at Claude Code session start, expired on exit. Governance telemetry streams hook events (PreToolUse, PostToolUse, UserPromptSubmit) to audit backend. First dedicated credential broker + audit tool for AI agents. Signals a sub-layer below harnesses for infrastructure-level security governance. Level 4c early signal; revisit at 1k★.

### New signals as of 2026-04-14
- **gsd/get-shit-done: meta-prompting + spec-driven dev at 52k stars:** (GitHub Trending, gsd-build/get-shit-done) — "light-weight meta-prompting, context engineering and spec-driven development system." Three-layer vocabulary convergence in one project; 52k stars is mainstream adoption signal. Enters Level 3 alongside `obra/superpowers`. "Spec-driven" framing may become a governance filter dimension for compliance-conscious orgs.
- **forrestchang/andrej-karpathy-skills: CLAUDE.md behavioral spec hits 25k stars:** (GitHub Trending) — a single CLAUDE.md derived from Karpathy's public observations. 25k stars for a pure Markdown file signals that CLAUDE.md behavioral specifications are becoming a de-facto standard layer independent of code harnesses. Three major CLAUDE.md guides now have 25k+ stars; the Level 3 SSOT layer is fragmenting into: (a) code harnesses, (b) workflow methodology guides, and (c) behavioral specification files.
- **pgmicro: in-process PostgreSQL explicitly designed for AI agents:** (GeekNews, glommer/pgmicro) — compiles PostgreSQL SQL to SQLite bytecode; zero-dependency, in-process, full Postgres SQL compat. First database project with explicit AI agent environment framing. Adds SQL-native sub-type to Level 4a memory layer alongside key-value stores (cipher) and markdown bases (GBrain).
- **AMD GAIA: hardware vendor enters local agent execution:** (HN, 89 pts, amd-gaia.ai) — AMD's dedicated local AI agent platform for Ryzen/Radeon hardware. First x86 CPU/GPU vendor with named agent execution product alongside Apple Silicon + Ollama. Expands addressable hardware surface for `network: offline` profiles beyond the current Apple Silicon reference stack.
- **SnapState: workflow execution state persistence productizing:** (HN Show HN, snapstate.dev) — persistent state for AI agent workflows. Early signal of a new Level 4a sub-category: execution state checkpointing (distinct from knowledge memory). As ralph-style loops and sprint-contract sessions grow longer, workflow state persistence is separating from memory/knowledge tooling.

### New signals as of 2026-04-13
- **Meta HyperAgents — self-referential agent improvement:** (GeekNews, cobusgreyling.medium.com) — agents that modify their own improvement *mechanisms*, not just task outputs. Distinct from adaptive runtimes (Hermes Agent) — the modification loop targets the meta-level improvement process. Research-stage; may require a new top-end maturity stage if it productizes. Challenges static LLM capability scoring.
- **Anthropic Advisor Strategy — named multi-LLM pairing pattern:** (GeekNews, claude.com/blog) — Opus as strategic advisor + Sonnet as executor; officially endorsed cost-optimization architecture. Formalizes "planner/executor dual-model" as a named pattern. Signals clawfit needs a `multi_llm_pattern` dimension beyond single-LLM selection.
- **Anthropic Managed Agents — hosted stable interfaces:** (GeekNews, anthropic.com/engineering/managed-agents) — long-running hosted agents with interface contracts that survive model version upgrades. Governance-relevant: interface stability as a reliability primitive. Distinct from harness-design-long-running-apps (sprint contracts). Suggests a `managed_hosted` statefulness value for the scoring model.
- **snarktank/ralph crosses 15k stars:** (GitHub Trending, +463/day) — TypeScript autonomous agent loop for PRD-driven iterative execution. Now the highest-starred implementation in the ralph methodology family (above ralph-claude-code 8k and open-ralph-wiggum 1.4k). Validates PRD-driven loops crossing mainstream developer adoption.
- **VoxCPM: tokenizer-free TTS for multilingual voice agents:** (OpenBMB, 11k★, GitHub Trending) — voice output infrastructure with tokenizer-free architecture; lower latency and broader language coverage than tokenized TTS. Fills the Level 7 voice *output* gap alongside Ghost Pepper (voice input). First high-signal multilingual TTS for agent pipelines.
- **Claudraband: Claude Code for power users:** (HN, 85 pts) — explicit "power user" positioning for a Claude Code harness; targets senior developers needing more than default Claude Code but less than full team orchestration. New Level 2 segment between simple wrappers and enterprise orchestrators.

### New signals as of 2026-04-12
- **Strix: second high-signal security agent enters Level 1:** usestrix/strix (23k★, GeekNews 26 pts) — open-source autonomous security testing platform using teams of agents with PoC validation. Distinct from Shannon (expert pentester tool): Strix is developer self-service, CI/CD-integrated, shift-left. Reinforces the need for a `security-testing` task type beyond `qa` in the scoring taxonomy.
- **GBrain: personal knowledge compounding as Level 4a pattern:** garrytan/gbrain — MIT-licensed personal knowledge base by YC CEO Garry Tan; markdown+PGLite backend, agents read-before/write-after. OpenClaw+Hermes Agent native. Local-first, human-inspectable, MCP support incoming. Adds a "compounding personal knowledge" sub-pattern to Level 4a distinct from session-memory tools.
- **🔥 DureClaw: 크로스 머신 멀티 에이전트 오케스트레이션 (hongsw 직접 제작):** [DureClaw/dureclaw](https://github.com/DureClaw/dureclaw) — Claude Code 오케스트레이터 + Phoenix WebSocket 서버 + oah-agent 워커 3층 아키텍처. 이종 AI 백엔드(claude/opencode/gemini/aider) 지원. MCP 플러그인 정식 배포. Mac/Linux/Windows/Raspberry Pi. claude-peers-mcp가 머신 내 피어 메시라면 DureClaw는 머신 간 크루 오케스트레이션. Level 2/4c 하이브리드. **clawfit 레지스트리 카테고리(이종 백엔드 오케스트레이션, 크로스 머신 에이전트 크루) 설계 방향의 원점.**
- **Berkeley RDI: all major agent benchmarks are exploitable:** "How We Broke Top AI Agent Benchmarks" (rdi.berkeley.edu, 171 HN pts) — UC Berkeley team demonstrates that every major benchmark (SWE-bench, WebArena, OSWorld, etc.) can be exploited to achieve near-perfect scores without solving a single task. Seven recurring vulnerability classes identified. Directly undermines LLM selection decisions based on published benchmark scores; clawfit's LLM preference weights may need an evidence-quality caveat. Agent-Eval Checklist proposed as a future Level 5 reference standard.

---

## Level 1 — Base runtimes / primary agent surfaces
These are the main user-facing agent runtimes or primary product choices.
They are the tools users most directly choose as their base environment.

- <img src="https://github.com/openclaw.png" alt="OpenClaw" width="18" /> [OpenClaw](https://github.com/openclaw/openclaw) — ⭐ 349,119
- <img src="https://github.com/zeroclaw-labs.png" alt="ZeroClaw" width="18" /> [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) — ⭐ 29,526
- <img src="https://github.com/anthropics.png" alt="Claude Code" width="18" /> [Claude Code](https://github.com/anthropics/claude-code) — ⭐ 109,423
- <img src="https://github.com/anomalyco.png" alt="OpenCode" width="18" /> [OpenCode](https://github.com/anomalyco/opencode) — ⭐ 137,788
- <img src="https://github.com/block.png" alt="Goose" width="18" /> [Goose](https://github.com/block/goose) — ⭐ 37,129
- <img src="https://github.com/charmbracelet.png" alt="Crush" width="18" /> [Crush](https://github.com/charmbracelet/crush) — ⭐ 22,543
- <img src="https://github.com/paul-gauthier.png" alt="Aider" width="18" /> [Aider](https://github.com/paul-gauthier/aider) — ⭐ 42,869
- <img src="https://github.com/All-Hands-AI.png" alt="OpenHands" width="18" /> [OpenHands](https://github.com/All-Hands-AI/OpenHands) — ⭐ 70,632
- <img src="https://github.com/cline.png" alt="Cline" width="18" /> [Cline](https://github.com/cline/cline) — ⭐ 59,924
- <img src="https://github.com/continuedev.png" alt="Continue" width="18" /> [Continue](https://github.com/continuedev/continue) — ⭐ 32,309
- Cursor — https://cursor.com/
- Kiro CLI — https://kiro.dev/
- <img src="https://github.com/langchain-ai.png" alt="deepagents" width="18" /> [deepagents](https://github.com/langchain-ai/deepagents) — ⭐ 19,379 *(also Level 2; CLI mode = base runtime, SDK mode = harness)*
- <img src="https://github.com/understudy-ai.png" alt="understudy" width="18" /> [understudy](https://github.com/understudy-ai/understudy) — ⭐ 410 — demonstration-based local desktop agent (GUI + browser + shell + filesystem)
- Claude Computer Use — direct mouse/keyboard/screen control via Claude Code Desktop + Cowork + Dispatch; macOS first *(also Level 7)*
- <img src="https://github.com/NousResearch.png" alt="Hermes Agent" width="18" /> [Hermes Agent](https://github.com/NousResearch/hermes-agent) — ⭐ 27,234 — adaptive open-source agent from NousResearch; "grows with you" — signals session-persistent adaptation at the base runtime layer
- <img src="https://github.com/google-ai-edge.png" alt="LiteRT-LM" width="18" /> [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) — ⭐ 1,813 — Google AI Edge on-device LLM inference runtime; ARM-first, mobile + edge; companion to google-ai-edge/gallery
- <img src="https://github.com/KeygraphHQ.png" alt="Shannon" width="18" /> [Shannon](https://github.com/KeygraphHQ/shannon) — ⭐ 36,485 — autonomous AI pentester; reads source code, identifies attack surfaces, generates and executes exploits; first high-signal domain-specialized security agent in this taxonomy
- <img src="https://github.com/rowboatlabs.png" alt="rowboat" width="18" /> [rowboat](https://github.com/rowboatlabs/rowboat) — ⭐ 11,716 — open-source AI coworker with native memory; persistent task ownership across sessions; memory-native Level 1 sub-type
- [Twill.ai](https://twill.ai) — YC S25 — async cloud agent delegation; "delegate tasks, get back PRs"; fire-and-forget model with PR output; first managed cloud agent service in this taxonomy
- <img src="https://github.com/usestrix.png" alt="Strix" width="18" /> [Strix](https://github.com/usestrix/strix) — ⭐ 23,536 — open-source autonomous security testing platform; teams of agents run code dynamically, find vulnerabilities, validate via PoC; CI/CD integration; developer self-service shift-left variant alongside Shannon's expert-pentester model

---

## Level 2 — Meta wrappers / harnesses / orchestration layers
These projects sit on top of existing base agents and transform how they operate.
They provide orchestration, better defaults, compatibility layers, workflows, routing, multi-agent teams, or opinionated operating conventions.

- <img src="https://github.com/code-yeongyu.png" alt="oh-my-openagent" width="18" /> [oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) — ⭐ 48,590
- <img src="https://github.com/Yeachan-Heo.png" alt="oh-my-claudecode" width="18" /> [oh-my-claudecode](https://github.com/yeachan-heo/oh-my-claudecode) — ⭐ 24,538
- <img src="https://github.com/Yeachan-Heo.png" alt="oh-my-codex" width="18" /> [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) — ⭐ 16,703
- <img src="https://github.com/Joonghyun-Lee-Frieren.png" alt="oh-my-gemini-cli" width="18" /> [oh-my-gemini-cli](https://github.com/Joonghyun-Lee-Frieren/oh-my-gemini-cli) — ⭐ 103
- <img src="https://github.com/first-fluke.png" alt="oh-my-agent" width="18" /> [oh-my-agent](https://github.com/first-fluke/oh-my-agent) — ⭐ 565
- <img src="https://github.com/AndyMik90.png" alt="Aperant" width="18" /> [Aperant](https://github.com/AndyMik90/Aperant) — ⭐ 13,816
- <img src="https://github.com/frankbria.png" alt="ralph-claude-code" width="18" /> [ralph-claude-code](https://github.com/frankbria/ralph-claude-code) — ⭐ 8,477
- <img src="https://github.com/Th0rgal.png" alt="open-ralph-wiggum" width="18" /> [open-ralph-wiggum](https://github.com/Th0rgal/open-ralph-wiggum) — ⭐ 1,421
- <img src="https://github.com/SuperClaude-Org.png" alt="SuperClaude Framework" width="18" /> [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) — ⭐ 22,161
- <img src="https://github.com/siteboon.png" alt="claudecodeui" width="18" /> [claudecodeui](https://github.com/siteboon/claudecodeui) — ⭐ 9,503
- <img src="https://github.com/coder.png" alt="agentapi" width="18" /> [agentapi](https://github.com/coder/agentapi) — ⭐ 1,338
- <img src="https://github.com/musistudio.png" alt="claude-code-router" width="18" /> [claude-code-router](https://github.com/musistudio/claude-code-router) — ⭐ 31,571
- <img src="https://github.com/langchain-ai.png" alt="deepagents" width="18" /> [deepagents](https://github.com/langchain-ai/deepagents) — ⭐ 19,379 *(LangGraph-based SDK; also Level 1 as CLI)*
- <img src="https://github.com/can1357.png" alt="oh-my-pi" width="18" /> [oh-my-pi](https://github.com/can1357/oh-my-pi) — ⭐ 2,681 — Hashline approach: content-hash verification for concurrent multi-agent file safety; see ["The Harness Problem"](https://blog.can.ac/2026/02/12/the-harness-problem/)
- Anthropic engineering: [Harness design for long-running applications](https://www.anthropic.com/engineering/harness-design-long-running-apps) — canonical dual-agent + sprint-contract architecture from Anthropic
- <img src="https://github.com/coleam00.png" alt="Archon" width="18" /> [Archon](https://github.com/coleam00/Archon) — ⭐ 15,583 — "first open-source harness builder for AI coding"; makes AI coding deterministic and repeatable; harness-generator sub-type
- <img src="https://github.com/multica-ai.png" alt="multica" width="18" /> [multica](https://github.com/multica-ai/multica) — ⭐ 6,029 — open-source managed agents platform; "turn coding agents into real teammates — assign tasks, track progress"
- <img src="https://github.com/snarktank.png" alt="ralph" width="18" /> [ralph](https://github.com/snarktank/ralph) — ⭐ 15,908 — TypeScript autonomous agent loop for PRD-driven iterative execution; highest-starred ralph-family implementation; solo/small team target
- [Claudraband](https://github.com/halfwhey/claudraband) — Claude Code harness for power users; explicit senior-developer positioning; Level 2 mid-range segment
- Anthropic engineering: [Managed Agents](https://www.anthropic.com/engineering/managed-agents) — hosted long-running agents with stable interfaces independent of model version upgrades; governance/reliability primitive
- [Claude Code Routines](https://claude.ai/code/routines) — *(research preview, 2026-04)* — first-party Anthropic managed cloud runner; schedule / API / GitHub-event triggers; autonomous sessions on Anthropic infrastructure; `/schedule` CLI; Pro/Max/Team/Enterprise plans — first serverless execution-as-a-service runner native to Claude Code
- <img src="https://github.com/DureClaw.png" alt="DureClaw" width="18" /> [DureClaw](https://github.com/DureClaw/dureclaw) — ⭐ 1 🔥 **크로스 머신 멀티 에이전트 오케스트레이션** — Claude Code 오케스트레이터 + Phoenix WebSocket 메시지 버스 + oah-agent 워커 3층 아키텍처; 이종 AI 백엔드(claude/opencode/gemini/aider) 지원; Mac/Linux/Windows/Raspberry Pi; MCP 플러그인 정식 배포(`@dureclaw/mcp`); 한국 두레(협동 농경) 철학 기반; **hongsw 직접 제작** — clawfit 레지스트리 설계 방향에 직접적 영향

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
- <img src="https://github.com/first-fluke.png" alt="oh-my-agent" width="18" /> [oh-my-agent](https://github.com/first-fluke/oh-my-agent) — ⭐ 565
- <img src="https://github.com/Joonghyun-Lee-Frieren.png" alt="oh-my-gemini-cli" width="18" /> [oh-my-gemini-cli](https://github.com/Joonghyun-Lee-Frieren/oh-my-gemini-cli) — ⭐ 103
- <img src="https://github.com/affaan-m.png" alt="everything-claude-code" width="18" /> [everything-claude-code](https://github.com/affaan-m/everything-claude-code) — ⭐ 140,708
- <img src="https://github.com/gotalab.png" alt="cc-sdd" width="18" /> [cc-sdd](https://github.com/gotalab/cc-sdd) — ⭐ 3,026
- <img src="https://github.com/open-gitagent.png" alt="gitagent" width="18" /> [gitagent](https://github.com/open-gitagent/gitagent) — Git-native open standard for agent definition and lifecycle management; `git clone` = agent instantiation
- **AGENTS.md** — OpenAI's cross-platform agent specification format; part of Agentic AI Foundation (Microsoft + Google + OpenAI + Anthropic + Linux Foundation); competes with / complements CLAUDE.md as executable SSOT
- <img src="https://github.com/VoltAgent.png" alt="awesome-design-md" width="18" /> [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) — ⭐ 15,900 🔥 55+ DESIGN.md files extracted from popular sites; extends SSOT pattern into visual/UI domain — agents read design system rules before generating UI
- <img src="https://github.com/obra.png" alt="superpowers" width="18" /> [superpowers](https://github.com/obra/superpowers) — ⭐ 145,706 🔥🔥 agentic skills framework + software development methodology; Shell-first; "that works" reliability framing; largest-starred harness/SSOT repo in this taxonomy; spans Level 3 + Level 4b
- [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) — ⭐ 43,721 🔥 — agentic engineering curriculum by shanraisshan; Commands/Agents/Skills three-abstraction model; 69 tips from Claude Code creator Boris Cherny; comparative analysis of 10 frameworks; #1 GitHub Trending 2026-04-15; accessible from beginner to advanced

---

## Level 4 — Capability extension layer (MCP / memory / plugins / tools)
These systems add capabilities to agents rather than replacing the base runtime.
This is where context, memory, tools, MCP, plugins, and action-enabling systems live.

Level 4 is splitting into three observable subtypes:
- **4a. Memory / persistent context** — session or project-level memory systems
- **4b. Skill packs & skill managers** — domain-specific skill collections and lifecycle tools
- **4c. Tool-use / action infrastructure** — MCP servers, toolkits, platform connectors

### 4a. Memory / persistent context
- <img src="https://github.com/thedotmack.png" alt="claude-mem" width="18" /> [claude-mem](https://github.com/thedotmack/claude-mem) — ⭐ 45,600 🔥 hooks-based persistent memory with SQLite + Chroma, `npx claude-mem install`
- <img src="https://github.com/CaviraOSS.png" alt="OpenMemory" width="18" /> [OpenMemory](https://github.com/CaviraOSS/OpenMemory) — ⭐ 3,871
- <img src="https://github.com/campfirein.png" alt="cipher" width="18" /> [cipher](https://github.com/campfirein/cipher) — ⭐ 4,178
- <img src="https://github.com/zilliztech.png" alt="claude-context" width="18" /> [claude-context](https://github.com/zilliztech/claude-context) — ⭐ 5,850
- <img src="https://github.com/garrytan.png" alt="GBrain" width="18" /> [GBrain](https://github.com/garrytan/gbrain) — MIT — personal knowledge base for agents by YC CEO Garry Tan; markdown+PGLite backend; agents read-before/write-after; OpenClaw+Hermes native; CLI via bun; "compounding personal knowledge" sub-pattern

### 4b. Skill packs & skill managers
**Skill managers (lifecycle/discovery):**
- <img src="https://github.com/Shpigford.png" alt="Chops" width="18" /> [Chops](https://github.com/Shpigford/chops) — macOS skill manager across Claude Code, Cursor, Codex, Windsurf, Amp simultaneously
- <img src="https://github.com/amebahead.png" alt="skills-cleaner" width="18" /> [skills-cleaner](https://github.com/amebahead/skills-cleaner) — Claude plugin for listing, deduplication, and lifecycle management of `.claude/plugin/` skills
- [claudemarketplaces.com](https://claudemarketplaces.com/) — 150+ skills with ratings (March 2026); first rated marketplace for Claude skills
- [claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) — 340 plugins + 1,367 agent skills catalog

**Platform-native plugin systems:**
- OpenAI Codex plugin system — Skills + Apps + MCP bundles; official plugins for GitHub, Linear, Vercel, Netlify, Slack, Figma, Notion, Gmail
- <img src="https://github.com/anthropics.png" alt="claude-plugins-official" width="18" /> [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) — ⭐ 16,063

**Domain skill packs:**
- <img src="https://github.com/pbakaus.png" alt="Impeccable" width="18" /> [Impeccable](https://github.com/pbakaus/impeccable) — 20 design commands across 7 domains (layout, spacing, color, typography…) for Claude Code + Cursor
- <img src="https://github.com/NomaDamas.png" alt="K-Skill" width="18" /> [K-Skill](https://github.com/NomaDamas/k-skill) — Korean-localized skill pack (SRT, Seoul subway, KBO, lottery)
- <img src="https://github.com/kepano.png" alt="obsidian-skills" width="18" /> [obsidian-skills](https://github.com/kepano/obsidian-skills) — ⭐ 20,148 — first-party agent skill pack from Obsidian CEO; teaches agents Markdown, Bases, JSON Canvas, and Obsidian CLI; signals L4b maturation beyond coding into knowledge-work
- <img src="https://github.com/team-attention.png" alt="plugins-for-claude-natives" width="18" /> [plugins-for-claude-natives](https://github.com/team-attention/plugins-for-claude-natives) — ⭐ 722
- <img src="https://github.com/JuliusBrussee.png" alt="caveman" width="18" /> [caveman](https://github.com/JuliusBrussee/caveman) — ⭐ 1,700 🔥 output token compression skill (65–75% prose reduction); three intensity levels (Lite/Full/Ultra); install via `npx skills add`

### 4c. Tool-use / action infrastructure
- <img src="https://github.com/rtk-ai.png" alt="rtk" width="18" /> [rtk](https://github.com/rtk-ai/rtk) — Rust CLI token proxy; sits between agent and shell, compresses git/ls/test output 60–90% before the LLM reads it; zero-dependency single binary
- <img src="https://github.com/millionco.png" alt="Expect" width="18" /> [Expect](https://github.com/millionco/expect) — CLI that auto-generates and executes browser-based test plans from code changes (Claude/Codex backend)
- <img src="https://github.com/oraios.png" alt="serena" width="18" /> [serena](https://github.com/oraios/serena) — ⭐ 22,504
- <img src="https://github.com/modelcontextprotocol.png" alt="MCP Servers" width="18" /> [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — ⭐ 83,039 *(governance: donated to Agentic AI Foundation Dec 2025; 97M monthly SDK downloads)*
- <img src="https://github.com/microsoft.png" alt="mcp-for-beginners" width="18" /> [mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) — ⭐ 15,804
- <img src="https://github.com/IBM.png" alt="mcp-context-forge" width="18" /> [mcp-context-forge](https://github.com/IBM/mcp-context-forge) — ⭐ 3,526
- <img src="https://github.com/ComposioHQ.png" alt="Composio" width="18" /> [Composio](https://github.com/ComposioHQ/composio) — ⭐ 27,650
- <img src="https://github.com/withoneai.png" alt="Pica" width="18" /> [Pica](https://github.com/withoneai/pica) — ⭐ 1,470

---

## Level 5 — Research / evaluation / benchmark / autoresearch patterns
These are especially useful when designing clawfit's abstraction layer and long-term research model.
They include evaluation harnesses, benchmark references, autonomous research loops, and **collective agent knowledge systems**.

- <img src="https://github.com/mozilla-ai.png" alt="cq" width="18" /> [cq](https://blog.mozilla.ai/cq-stack-overflow-for-agents/) — Mozilla AI shared knowledge commons for agents; query before acting, contribute after — "Stack Overflow for agents"
- <img src="https://github.com/karpathy.png" alt="autoresearch" width="18" /> [autoresearch](https://github.com/karpathy/autoresearch) — ⭐ 66,534
- <img src="https://github.com/mozilla-ai.png" alt="any-agent" width="18" /> [any-agent](https://github.com/mozilla-ai/any-agent) — ⭐ 1,138
- <img src="https://github.com/mozilla-ai.png" alt="any-llm" width="18" /> [any-llm](https://github.com/mozilla-ai/any-llm) — ⭐ 1,862
- <img src="https://github.com/anomalyco.png" alt="opencode-bench" width="18" /> [opencode-bench](https://github.com/anomalyco/opencode-bench) — ⭐ 60
- <img src="https://github.com/EleutherAI.png" alt="lm-evaluation-harness" width="18" /> [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — ⭐ 12,017
- <img src="https://github.com/prometheus-eval.png" alt="Prometheus" width="18" /> [Prometheus](https://github.com/prometheus-eval/prometheus) — ⭐ 312
- <img src="https://github.com/Hugging-Face-KREW.png" alt="Ko-AgentBench" width="18" /> [Ko-AgentBench](https://github.com/Hugging-Face-KREW/Ko-AgentBench) — ⭐ 65
- <img src="https://github.com/microsoft.png" alt="agent-lightning" width="18" /> [agent-lightning](https://github.com/microsoft/agent-lightning) — ⭐ 16,545
- <img src="https://github.com/team-attention.png" alt="hoyeon" width="18" /> [hoyeon](https://github.com/team-attention/hoyeon) — ⭐ 131
- <img src="https://github.com/HudsonGri.png" alt="mdarena" width="18" /> [mdarena](https://github.com/HudsonGri/mdarena) — empirical benchmarking of CLAUDE.md instruction variants; mines merged PRs, runs agent with/without instruction files, grades by test pass rate + diff overlap; SWE-bench-compatible export

---

## Level 6 — Data / evidence / knowledge infrastructure
These references are useful when clawfit evolves into an evidence hub and simulation system.
They help answer how agents access, structure, retrieve, and reason over external knowledge.

- <img src="https://github.com/HKUDS.png" alt="LightRAG" width="18" /> [LightRAG](https://github.com/HKUDS/LightRAG) — ⭐ 32,300
- <img src="https://github.com/HKUDS.png" alt="RAG-Anything" width="18" /> [RAG-Anything](https://github.com/HKUDS/RAG-Anything) — ⭐ 15,200
- <img src="https://github.com/airweave-ai.png" alt="airweave" width="18" /> [airweave](https://github.com/airweave-ai/airweave) — ⭐ 6,200
- <img src="https://github.com/agentset-ai.png" alt="agentset" width="18" /> [agentset](https://github.com/agentset-ai/agentset) — ⭐ 1,928
- <img src="https://github.com/VectifyAI.png" alt="PageIndex" width="18" /> [PageIndex](https://github.com/VectifyAI/PageIndex) — ⭐ 24,200
- <img src="https://github.com/opendatalab.png" alt="MinerU" width="18" /> [MinerU](https://github.com/opendatalab/MinerU) — ⭐ 58,200

---

## Level 7 — Human interface / voice / input-output layer
These are not always the main coding engine, but they strongly influence how humans actually operate agents.
This includes voice input, talk mode, speech interruption, remote relays, terminals, and interaction loops.

- <img src="https://github.com/langchain-ai.png" alt="deep-agents-ui" width="18" /> [deep-agents-ui](https://github.com/langchain-ai/deep-agents-ui) — ⭐ 1,500 — Next.js web UI for deepagents; chat + file monitor + step-through debug (companion to Level 1/2 deepagents)
- Claude Computer Use — first-party Anthropic desktop control (mouse + keyboard + screen) via Claude Code Desktop + Cowork *(also Level 1)*
- [Ghostmeet](https://github.com/Higangssh/ghostmeet) — ⭐ 32 — self-hosted Chrome extension for real-time meeting transcription (Whisper) + AI summary (Claude API); fully local, no audio leaves device
- Superwhisper — https://superwhisper.com/
- <img src="https://github.com/channprj.png" alt="claude-code-voice" width="18" /> [claude-code-voice](https://github.com/channprj/claude-code-voice) — ⭐ 8
- <img src="https://github.com/hada0127.png" alt="cc-telegram" width="18" /> [cc-telegram](https://github.com/hada0127/cc-telegram) — ⭐ 15
- <img src="https://github.com/Q00.png" alt="ouroboros" width="18" /> [ouroboros](https://github.com/Q00/ouroboros) — ⭐ 2,000
- OpenClaw talkmode improvement reference — https://github.com/openclaw/openclaw/pull/53553#issuecomment-4124082023
- [Ghost Pepper](https://github.com/matthartman/ghost-pepper) — local hold-to-talk STT for macOS (Whisper-based); fully offline, no audio leaves device; privacy-first alternative to Superwhisper for confidential environments
- <img src="https://github.com/OpenBMB.png" alt="VoxCPM" width="18" /> [VoxCPM](https://github.com/OpenBMB/VoxCPM) — ⭐ 11,260 — tokenizer-free TTS for multilingual speech generation; lower latency voice output layer for agent pipelines; fills Level 7 voice output gap alongside Ghost Pepper (input)

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
