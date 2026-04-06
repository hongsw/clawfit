# Ecosystem Classification Axes

This document explains **how and why** clawfit classifies tools into the 7-level taxonomy.  
For the tool list itself, see [`docs/reference-levels.md`](../reference-levels.md).

---

## How to read this document

Each level has:
1. **Defining question** — the single question that determines if a tool belongs here
2. **Classification criterion** — the rule used in `Preliminary interpretation` sections of research-watch docs
3. **Sub-axes** — finer dimensions within the level used to distinguish tools from each other
4. **Boundary rules** — how to separate this level from adjacent levels
5. **Example classifications** with rationale

---

## Level 1 — Base runtimes / primary agent surfaces

### Defining question
> Is this the tool a user installs as their primary development environment — the base layer everything else sits on top of?

### Classification criterion
The tool must be **self-contained and user-facing**: no separate L1 agent is required underneath it. Users choose it the way they choose an IDE or a shell.

### Sub-axes

| Axis | Values | Examples |
|------|--------|---------|
| **Interface type** | CLI · IDE (editor fork) · browser extension · desktop app | Aider=CLI, Cursor=IDE, Gemma Gem=browser ext |
| **Model coupling** | cloud-API only · local-only · hybrid · any | Claude Code=cloud-API, Aider=hybrid |
| **Autonomy mode** | autocomplete · interactive · agentic (autonomous) | Continue=autocomplete, OpenHands=agentic |
| **Task domain** | code-gen · research · computer-use · general | understudy=computer-use, Aider=code-gen |

### Boundary rules
- If it **requires another L1 tool underneath**, it is L2 — not L1.
- If it **embeds L2/L3 behaviors** but is still the primary install surface, it stays L1 (see Modo).
- If it primarily **operates a UI layer** (clicks, types, screenshots), start with L7 and check if L1 also applies.

### Example classifications
| Tool | Why L1 |
|------|--------|
| Claude Code | Users install it as their primary coding agent; no prior agent required |
| deepagents (CLI mode) | When used as CLI, it is the primary runtime; SDK mode shifts it to L2 |
| Modo | Full IDE (VS Code fork); no separate L1 beneath it despite embedding L2/L3 features |

---

## Level 2 — Meta wrappers / harnesses / orchestration layers

### Defining question
> Does this tool sit on top of an existing L1 agent and transform how it operates — without being the primary runtime itself?

### Classification criterion
The tool **requires a base agent** (L1) to function. It adds orchestration, routing, defaults, multi-agent coordination, or workflow conventions on top of that base.

### Sub-axes

| Axis | Values | Examples |
|------|--------|---------|
| **Orchestration pattern** | multi-agent · routing · UI wrapper · defaults/conventions | oh-my-claudecode=multi-agent, claude-code-router=routing |
| **Dependency scope** | single-agent specific · cross-agent compatible | SuperClaude=Claude-specific, Aperant=cross-agent |
| **Reliability mechanism** | none · content-hash (Hashline) · sprint-contract · session reset | oh-my-pi=Hashline, Anthropic harness=sprint-contract |
| **Distribution** | config files · npm package · CLI install · fork | SuperClaude=config files, oh-my-claudecode=npm |

### Boundary rules
- If the tool works **without any L1 agent underneath**, it is L1.
- If it defines **team-wide workflow rules stored in the repo** (not just runtime orchestration), it overlaps with L3.
- Single-function configurations (one skill, one rule file) belong in L3 or L4b — not L2.

### Example classifications
| Tool | Why L2 |
|------|--------|
| oh-my-claudecode | Wraps Claude Code with multi-agent coordination; requires Claude Code underneath |
| claude-code-router | Routes between LLM backends on top of Claude Code; no standalone function |
| deepagents (SDK mode) | LangGraph-based orchestration SDK; wraps an LLM runtime |

---

## Level 3 — Team harness / executable SSOT / governance layer

### Defining question
> Is this a file, convention, or system that both humans read as a workflow guide **and** agents read as executable instructions — governing how an agent operates across an entire project?

### Classification criterion
**Executable SSOT** (Single Source of Truth): the artifact must serve as project-wide governance that survives across sessions, not a per-invocation capability addition.

### Sub-axes

| Axis | Values | Examples |
|------|--------|---------|
| **SSOT type** | workflow/operational · design/visual · governance/cross-platform · git-native | CLAUDE.md=workflow, DESIGN.md=design, AGENTS.md=governance, gitagent=git-native |
| **Scope** | single-agent · cross-agent runtime · cross-platform | CLAUDE.md=Claude-specific, AGENTS.md=multi-runtime |
| **Distribution mechanism** | file-in-repo · git clone · registry | CLAUDE.md=file-in-repo, gitagent=git clone |
| **Governance authority** | individual project · team · foundation-level standard | CLAUDE.md=project, AGENTS.md=foundation (Agentic AI Foundation) |

### SSOT sub-types (emerging)

```
CLAUDE.md   — workflow rules: how the agent should behave and execute tasks
AGENTS.md   — cross-platform governance: runtime-agnostic agent specification
DESIGN.md   — visual output norms: design system constraints for UI generation
gitagent    — git-native distribution: agent definition stored and versioned in Git
```

### Boundary rules
- If the artifact **adds a new invocable capability** (slash command, tool call), it is L4b — not L3.
- If it **governs output norms project-wide** (not per-session), it is L3 even if distributed like a skill.
- If it **evaluates** SSOT quality rather than defining it, it is L5 (see mdarena).

### Example classifications
| Tool | Why L3 |
|------|--------|
| CLAUDE.md | Humans read as workflow guide; Claude reads as executable instructions; governs all sessions |
| awesome-design-md | Agents read DESIGN.md before all UI generation; persistent design-system governance |
| gitagent | Git repo = agent definition; `git clone` = agent instantiation; team-scale distribution |

---

## Level 4 — Capability extension layer

### Defining question
> Does this add a specific capability to an agent without replacing the base runtime?

### Classification criterion
The tool **augments an existing agent** — the agent functions without it, but the tool adds memory, skills, or tool-call infrastructure.

Level 4 has split into three observable subtypes:

---

### 4a — Memory / persistent context

**Defining question:** Does this make the agent remember things across sessions or across the project?

| Axis | Values | Examples |
|------|--------|---------|
| **Memory scope** | session · project · cross-session · collective (multi-agent) | cipher=session, claude-mem=cross-session, cq (→ L5)=collective |
| **Storage backend** | SQLite · vector DB (Chroma, Zilliz) · graph · in-memory | claude-mem=SQLite+Chroma |
| **Integration mechanism** | hooks · MCP server · SDK wrapper | claude-mem=hooks, cipher=MCP |

**Boundary with L6:** L4a is agent-facing memory (the agent reads/writes it during a session). L6 is data infrastructure for knowledge retrieval (RAG pipelines, document extraction). L4a plugs into an agent; L6 builds the knowledge store.

---

### 4b — Skill packs & skill managers

**Defining question:** Does this add a specific, discrete, invocable capability to an agent — packaged as an installable skill?

| Axis | Values | Examples |
|------|--------|---------|
| **Skill type** | lifecycle manager · platform-native (official) · domain pack · cost-optimization | Chops=lifecycle, claude-plugins-official=platform-native, K-Skill=domain, caveman=cost-opt |
| **Distribution** | `npx skills add` · npm · config file · manual copy | caveman=npx skills, Impeccable=manual copy |
| **Activation** | slash command · natural language · always-on hook | caveman=/caveman, Impeccable=slash |
| **Scope** | single-agent · multi-agent runtime | Chops=multi-runtime (Claude/Cursor/Codex/Windsurf) |

**Boundary with L3:** A skill adds one invocable capability (per-session). An SSOT governs all agent output across the project (persistent). If you could remove the file and the agent still functions but loses a command → L4b. If you remove the file and the agent loses project-wide behavioral governance → L3.

**Boundary with L4c:** Skills modify agent *behavior* via prompt convention. L4c tools modify how *tool calls* work — they are infrastructure, not behavior.

---

### 4c — Tool-use / action infrastructure

**Defining question:** Does this mediate how an agent calls or connects to external systems — MCP servers, shell proxies, platform connectors?

| Axis | Values | Examples |
|------|--------|---------|
| **Infrastructure type** | MCP server · shell proxy · browser connector · domain-profile MCP | rtk=shell proxy, MCP servers=MCP, Expect=browser connector, APEX=domain-profile MCP |
| **Safety model** | passive (no safety controls) · safety-critical (kill switches, limits) | most MCP=passive, APEX=safety-critical |
| **Governance** | open-source · foundation-backed standard | most=open-source, MCP=foundation-backed (Agentic AI Foundation) |

**Domain-profile MCP** (emerging sub-type): MCP extended with domain-specific safety constraints and conformance tests (e.g., APEX Protocol for financial trading). Distinguished from generic MCP servers by mandatory safety controls and protocol conformance requirements.

---

## Level 5 — Research / evaluation / benchmark / autoresearch

### Defining question
> Does this measure, evaluate, or autonomously research — rather than acting in production?

### Classification criterion
The tool's **output is measurement or knowledge**, not code, UI, or tool calls.

### Sub-axes

| Axis | Values | Examples |
|------|--------|---------|
| **Evaluation target** | model capability · agent behavior · SSOT quality · collective knowledge | lm-eval=model, opencode-bench=agent, mdarena=SSOT, cq=collective |
| **Research mode** | human-directed benchmark · autonomous research loop · knowledge commons | SWE-bench=directed, autoresearch=autonomous, cq=commons |
| **Output format** | scores/rankings · research reports · shared knowledge base | benchmarks=scores, autoresearch=reports, cq=knowledge base |

**SSOT evaluation** (new sub-type, 2026-04): Tools like mdarena that evaluate L3 SSOT artifacts (CLAUDE.md files) using L5 methods. The subject is L3; the function is L5.

**Collective knowledge** (new sub-type, 2026-04): Mozilla cq — agents query a shared knowledge commons before acting, contribute findings after. Statefulness pattern: *collective* (vs. session / project).

### Boundary with L4a
cq is L5 (collective knowledge commons) rather than L4a (per-agent memory) because its scope is cross-agent and cross-organization — it is a shared public commons, not a memory layer for a single agent's sessions.

---

## Level 6 — Data / evidence / knowledge infrastructure

### Defining question
> Does this provide the data pipeline or knowledge retrieval infrastructure that agents draw from?

### Sub-axes

| Axis | Values | Examples |
|------|--------|---------|
| **RAG pattern** | graph-based · vector · document extraction · hybrid | LightRAG=graph, RAG-Anything=hybrid |
| **Knowledge scope** | general · code-specific · domain-specific | MinerU=general (document extraction) |
| **Integration** | MCP server · SDK · standalone service | airweave=SDK |

### Boundary with L4a
L6 builds and maintains knowledge stores (pipelines, indexes, extraction). L4a plugs into those stores from the agent side (session memory, context injection). L6 is the infrastructure; L4a is the agent-facing adapter.

---

## Level 7 — Human interface / voice / computer use

### Defining question
> Does this define how a human communicates with an agent, or how an agent operates a UI on behalf of a human?

### Sub-axes

| Axis | Values | Examples |
|------|--------|---------|
| **Modality** | voice input · computer-use · web UI · terminal UI · messaging relay | Superwhisper=voice, Claude Computer Use=computer-use, claudecodeui=web UI, cc-telegram=messaging |
| **Execution scope** | full desktop · browser-scoped · app-scoped | Claude Computer Use=full desktop, Gemma Gem=browser-scoped |
| **Inference location** | cloud · local · browser (WebGPU) | Superwhisper=cloud, Gemma Gem=browser |
| **Dependency** | requires L1 agent · self-contained | claudecodeui=requires Claude Code, Gemma Gem=self-contained |

### L1/L7 boundary collapse (2026-04 pattern)
Tools that **operate the full UI layer** (computer-use, browser control) AND are self-contained base runtimes get dual classification L1+L7. The collapse happens when the UI operation is the agent's primary function, not a side-effect. Both Claude Computer Use and Gemma Gem demonstrate this pattern.

---

## Cross-level patterns

### Synthesis products (L1 + L2 + L3 features in one tool)
Some tools (e.g., Modo) embed L2 orchestration and L3 SSOT features inside a L1 IDE surface. Classification rule: **the primary level is determined by whether the tool requires a separate L1 underneath**. If not — it is L1, with L2/L3 features noted as embedded behaviors.

### Token efficiency interventions (L4b + L4c)
Two complementary tools: rtk (L4c) compresses *inputs* to the LLM (shell output); caveman (L4b) compresses *outputs* from the LLM (prose). Together they form a "token efficiency layer" that reduces cost without changing the model or task. Future scoring in clawfit may need a `token_efficiency_modifier` axis.

### Governance layer expansion (L3)
L3 originally meant CLAUDE.md (workflow rules). As of 2026-04 it now includes three SSOT sub-types:
- **Workflow**: CLAUDE.md, AGENTS.md
- **Design**: DESIGN.md
- **Distribution**: gitagent

If this continues, L3 may need formal sub-axes (3a workflow, 3b design, 3c governance standard) analogous to L4's 4a/4b/4c split.

---

## Quick classification checklist

```
1. Does it require a separate L1 agent underneath?
   YES → consider L2, L3, L4
   NO  → consider L1, L7

2. Does it govern project-wide agent behavior persistently?
   YES → L3 (SSOT / governance)
   NO  → continue

3. Does it add a discrete invocable capability (skill/command)?
   YES → L4b

4. Does it mediate external tool calls or system connections?
   YES → L4c

5. Does it persist or retrieve context across sessions?
   YES → L4a

6. Does it measure / evaluate / benchmark?
   YES → L5

7. Does it build or maintain knowledge infrastructure?
   YES → L6

8. Does it define human↔agent interaction modality, or operate a UI?
   YES → L7 (check L1 overlap if also self-contained)
```
