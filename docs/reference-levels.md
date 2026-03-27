# clawfit Reference Levels v0.1

This document organizes external tools and projects that clawfit should compare against, learn from, or use as supporting references.

## Level 1 — Core comparison targets
These are the highest-priority products for clawfit's first comparison matrix.

- OpenClaw — https://github.com/openclaw/openclaw
- ZeroClaw — https://github.com/zeroclaw-labs/zeroclaw
- Claude Code — https://github.com/anthropics/claude-code
- OpenCode — https://github.com/anomalyco/opencode
- Goose — https://github.com/block/goose
- Crush — https://github.com/charmbracelet/crush
- Aider — https://github.com/paul-gauthier/aider
- OpenHands — https://github.com/All-Hands-AI/OpenHands
- Cline — https://github.com/cline/cline
- Continue — https://github.com/continuedev/continue
- Cursor — https://cursor.com/
- Superwhisper — https://superwhisper.com/

## Level 2 — Workflow wrappers and orchestration tools
These matter for multi-agent execution, automation wrappers, and remote operation.

- oh-my-openagent — https://github.com/code-yeongyu/oh-my-openagent
- oh-my-claudecode — https://github.com/Yeachan-Heo/oh-my-claudecode
- Aperant — https://github.com/AndyMik90/Aperant
- ralph-claude-code — https://github.com/frankbria/ralph-claude-code
- open-ralph-wiggum — https://github.com/Th0rgal/open-ralph-wiggum
- SuperClaude Framework — https://github.com/SuperClaude-Org/SuperClaude_Framework
- claudecodeui — https://github.com/siteboon/claudecodeui
- agentapi — https://github.com/coder/agentapi
- autoresearch — https://github.com/karpathy/autoresearch

## Level 3 — Architecture and benchmark references
These are especially useful when designing clawfit's abstraction layer and benchmark system.

- any-agent — https://github.com/mozilla-ai/any-agent
- any-llm — https://github.com/mozilla-ai/any-llm
- opencode-bench — https://github.com/anomalyco/opencode-bench
- lm-evaluation-harness — https://github.com/EleutherAI/lm-evaluation-harness
- Prometheus — https://github.com/prometheus-eval/prometheus
- Ko-AgentBench — https://github.com/Hugging-Face-KREW/Ko-AgentBench
- agent-lightning — https://github.com/microsoft/agent-lightning
- hoyeon — https://github.com/team-attention/hoyeon

## Level 4 — Memory, context, MCP, and plugin ecosystem
These shape the real compatibility matrix beyond marketing checkboxes.

- OpenMemory — https://github.com/CaviraOSS/OpenMemory
- cipher — https://github.com/campfirein/cipher
- claude-context — https://github.com/zilliztech/claude-context
- serena — https://github.com/oraios/serena
- claude-plugins-official — https://github.com/anthropics/claude-plugins-official
- plugins-for-claude-natives — https://github.com/team-attention/plugins-for-claude-natives
- mcp-for-beginners — https://github.com/microsoft/mcp-for-beginners
- mcp-context-forge — https://github.com/IBM/mcp-context-forge

## Level 5 — Data hub, RAG, and evidence infrastructure
These references are useful when clawfit evolves into an evidence hub and simulation system.

- LightRAG — https://github.com/HKUDS/LightRAG
- RAG-Anything — https://github.com/HKUDS/RAG-Anything
- airweave — https://github.com/airweave-ai/airweave
- agentset — https://github.com/agentset-ai/agentset
- PageIndex — https://github.com/VectifyAI/PageIndex
- MinerU — https://github.com/opendatalab/MinerU

## Level 6 — Productivity, input, and human-agent interface tools
These are not always the main coding engine, but they strongly influence practical developer productivity.

- Superwhisper — https://superwhisper.com/
- claude-code-voice — https://github.com/channprj/claude-code-voice
- cc-telegram — https://github.com/hada0127/cc-telegram
- ouroboros — https://github.com/Q00/ouroboros
- OpenClaw talkmode improvement reference — https://github.com/openclaw/openclaw/pull/53553#issuecomment-4124082023

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
  https://github.com/Yeachan-Heo/oh-my-claudecode
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

**clawfit mapping:** supporting references; usually Level 2, 3, or 6 context rather than Level 1 comparison targets.

### E. Platform / SDK layer
These help developers build their own vibe-coding products rather than directly serving as end-user comparison targets.

- vibesdk — platform for building vibe-coding systems  
  https://github.com/cloudflare/vibesdk
- ruler — cross-agent rule layer / policy consistency  
  https://github.com/intellectronica/ruler

**clawfit mapping:** Level 3 or Level 4 depending on whether the emphasis is architecture or capability extension.

## Provisional classification guidance for clawfit
When a new repo appears in the vibe-coding ecosystem, classify it by asking:

1. Is this a **primary product choice** for users?
   - Then consider Level 1.
2. Is it mainly a **wrapper, orchestrator, or multi-agent shell**?
   - Then consider Level 2.
3. Is it mainly an **architecture / benchmark / platform abstraction**?
   - Then consider Level 3.
4. Is it mainly **memory, MCP, retrieval, context, or plugin support**?
   - Then consider Level 4.
5. Is it mainly **evidence/data infrastructure**?
   - Then consider Level 5.
6. Is it mainly **interface / productivity / input-layer support**?
   - Then consider Level 6.

Important: **do not treat the GitHub topic `vibe-coding` itself as a category system.**
It is only a discovery signal. clawfit should reclassify discovered repos using its own reference-level model.

## Research-loop signal note
`karpathy/autoresearch` is an especially important reference because it is not merely another coding assistant. It represents a **research-native autonomous loop**: modify code, run a bounded experiment, evaluate, keep/discard, and repeat. This makes it relevant to clawfit not only as a tool entry, but as an origin point for a broader autoresearch pattern and its growing fork ecosystem.

## Notes
- Level 1 should become clawfit's first public comparison matrix.
- Levels 2–6 provide the surrounding ecosystem needed for a realistic recommendation engine.
- Feature claims should be stored with evidence links and verification dates, not just yes/no flags.
- The GitHub topic `vibe-coding` is useful for discovery, but not sufficient as a canonical taxonomy.
