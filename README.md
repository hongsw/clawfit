# clawfit

> AI 에이전트 + LLM + 하드웨어 추천 엔진 — 76개 도구, 7레이어 에코시스템 맵, 10차원 조직 적합도 스코어링

> Agent + LLM + hardware recommendation engine and evidence hub.

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](pyproject.toml)
[![Tests](https://img.shields.io/badge/tests-pytest-informational)](tests/)
[![Status](https://img.shields.io/badge/status-early%20public-green)](https://github.com/hongsw/clawfit)

**Read in:** [한국어 🇰🇷](README.ko.md)

---

## What is clawfit?

`clawfit` answers a practical question:

**Given a task, latency target, budget, network conditions, and team maturity, what combination of agent pattern, model, and hardware is the best fit?**

It is three things in one:

1. **Recommendation engine** — 76 tools scored across 10 dimensions (task fit, maturity, role, layer relevance, team size, network, latency, features, complexity, budget). Hard multipliers penalize critical mismatches (offline required + online-only tool → x0.25).

2. **Ecosystem map** — A 7-layer taxonomy (L1 base runtimes → L7 human interfaces) with 150+ research-watch signal documents tracking GitHub Trending, GeekNews, and Hacker News daily via automated agents.

3. **Org-fit diagnosis** — A 10-question interactive questionnaire (TUI, CLI, or web) that builds an organization profile and recommends a prioritized multi-layer tool stack.

### Who is this for?

- Teams choosing between agent stacks (Claude Code vs OpenClaw vs Aider vs ...)
- DevOps deciding local vs cloud execution topology
- Executives evaluating AI tool adoption strategy
- Researchers mapping the AI agent ecosystem
- Anyone building an evidence-backed recommendation layer

> [!IMPORTANT]
> **START HERE — ECOSYSTEM MAP**
>
> If you want to understand what `clawfit` is really mapping, comparing, and tracking:
>
> ## **[Jump directly to the ecosystem map: `docs/reference-levels.md`](https://github.com/hongsw/clawfit/blob/main/docs/reference-levels.md)**
>
> This is the fastest way to see the current landscape of:
> - base agent runtimes (Claude Code, OpenClaw, Goose, Aider, pi-mono, ATLAS...)
> - harness / wrapper layers (oh-my-*, DureClaw, SuperClaude, Archon...)
> - research-loop systems (autoresearch, mdarena, cq...)
> - MCP / memory / tool ecosystems (claude-mem, korean-law-mcp, rtk...)
> - skill packs & persona layers (career-ops, caveman, Polysona...)
> - human interface / generative UI (pi-generative-ui, Ghost Pepper...)

---

## 🔥 What's hot right now (2026-05-04)

| Signal | Why it matters | Level |
|--------|---------------|-------|
| **[ruflo](https://github.com/ruvnet/ruflo) ⭐38.8k** | Multi-agent swarm orchestration for Claude Code — 100+ agents, SONA neural learning, HNSW vector memory, zero-trust federation (mTLS). +1,834★ today. v3.6.10 MIT. | L2 |
| **[TradingAgents](https://github.com/TauricResearch/TradingAgents) ⭐65.1k** | +3,315★ today (new daily record). Highest-starred domain-specialized multi-agent framework. Financial analyst→risk→execution role hierarchy. | L1 |
| **[n8n-mcp](https://github.com/czlonkowski/n8n-mcp) ⭐19.5k** | MCP server exposing 1,650+ n8n workflow nodes to Claude — bridges workflow automation platforms into agent tool-use. Added to L4c map today. | L4c |
| **[ouroboros](https://github.com/Q00/ouroboros) ⭐3.2k** | "Agent OS: Stop prompting. Start specifying." — Interview→Seed→Execute→Evaluate loop; ambiguity scoring ≤0.2 before any code runs; Ralph persistent runner. | L2/L3 |
| **[cocoindex](https://github.com/cocoindex-io/cocoindex) ⭐7.7k** | Incremental data-pipeline engine for long-horizon agents. Rust core, delta-only reprocessing (10× cost reduction), Apache 2.0, v1.0.2. Added to L6 map today. | L6 |
| **[DeepSeek V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)** | SWE-Bench Verified 80.6 (ties Opus 4.6), MIT, $0.44/M, 1M ctx. V4-Flash runs offline on M5 MacBook. Best open-weight coding model. | LLM |
| **[xAI Grok 4.3](https://x.ai/news)** | 37–83% price cut; GDPval-AA ELO 1500 (+321, largest single-release jump tracked); 1M ctx; always-on reasoning. | LLM |
| **[Microsoft Agent Framework v1.0](https://github.com/microsoft/agent-framework) ⭐10k** | AutoGen + Semantic Kernel consolidated. Graph-based multi-agent, YAML agent defs, MCP/A2A, Azure Durable Functions. First enterprise-stable multi-agent SDK. | L2 |
| **[cc-switch](https://github.com/hongsw/cc-switch) ⭐52.8k** | Cross-CLI provider switcher: Claude Code, Codex, Gemini, OpenCode unified under one SSOT. | L3/L4c |
| **[superpowers](https://github.com/obra/superpowers) ⭐145k** | Largest-starred harness/SSOT repo. Shell-first agentic skills + SSOT methodology. | L3/L4b |

Full analysis in [`docs/research-watch/`](docs/research-watch/) (150+ docs) · Full map in [`docs/reference-levels.md`](docs/reference-levels.md)

---

## Changelog

| Date | What changed |
|------|-------------|
| 2026-05-04 | Daily scan: ruflo ⭐38.8k L2 (Claude swarm orchestration), TradingAgents +3,315★/day now 65.1k, ouroboros Agent OS spec-first harness, cocoindex L6 incremental pipeline, n8n-mcp L4c (1,650+ nodes). n8n-mcp + CocoIndex added to reference-levels.md. 5 research-watch docs. scoring clean. |
| 2026-05-03 | Daily scan: DeepSeek V4-Pro (SWE-Bench 80.6, MIT, $0.44/M), xAI Grok 4.3 (83% cheaper, ELO +321), MS Agent Framework v1.0 (AutoGen+SK consolidated), acai.sh ACID spec-first, craft-agents-oss L6, TradingAgents 57.7k★. Scoring maturity weight bug fixed (was 1.0795, now exact 1.0). L6 diagram corrected. 9 research-watch docs. |
| 2026-04-30 | Daily scan: Warp open-source +11,955★/day record, Zed 1.0 stable, Mistral Medium 3.5 → llms.json, NVIDIA OpenShell L1, memvid L4a portable-binary, cc-connect L7 3rd datapoint, hongsw/harness L2. 7 research-watch docs. |
| 2026-04-28 | All GitHub star counts refreshed. All taxonomy bullet lists and tables sorted by star count (descending). Daily scans 04-21 through 04-28: cc-switch 52.8k★, cmux 15.6k★, GitNexus 31.5k★, dirac TB2 leader, Engram+wuphf L4a, DureClaw L3 SSOT confirmed. 12 research-watch docs. |
| 2026-04-20 | Thunderbolt Mozilla AI client L7, OpenMythos loop-transformer signal, Qwen3.6-35B-A3B open-weight agentic coding. |
| 2026-04-12 | DureClaw highlighted in reference-levels.md. 8 new tools added to registry (50→58). Task taxonomy expanded: +orchestration, +education, +legal-research. Exec role scoring fixed. |
| 2026-04-12 | Daily scan: Strix security agent, GBrain personal knowledge base added |
| 2026-04-11 | Daily scan: superpowers 145k★, Archon harness-builder, rowboat memory-native coworker, Twill.ai cloud delegation |
| 2026-04-08 | Claude Mythos Preview model tier, GLM-5.1 long-horizon, NVIDIA PersonaPlex, Addy Osmani agent-skills |
| 2026-04-07 | 8 repos from hongsw stars: career-ops, claude-peers-mcp, polysona, pi-generative-ui, dureclaw. Korean rewrites. Full numerical verification across all docs. |
| 2026-04-06 | reference-levels.md → v0.3: L4 split into 4a/4b/4c. 19 research-watch docs. Harness team (`.claude/agents/`). |
| 2026-03-31 | Ecosystem map v0.2: 7-layer taxonomy, research-watch scan launch |

---

## Quick start

### Install

**Option A — pipx (recommended, globally available, no venv needed)**

```bash
pipx install git+https://github.com/hongsw/clawfit
```

**Option B — editable install (for development / hacking)**

```bash
git clone https://github.com/hongsw/clawfit.git
cd clawfit
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
```

---

### Org-Fit Diagnosis — find your team's tool stack

Answer 10 questions about your team → get a prioritized multi-layer recommendation.

**TUI** (recommended — navigate with arrow keys, results update live in split pane):

```bash
clawfit tui
```

```
 ████████████░░░░░░  5/10  [USECASE]
 ──────────────────────────┬──────────────────────────────
 What is the main thing    │ Stage 4 — Tool-using agent
 you want AI to do?        │
                           │ [PRI] L1 Base runtime
  ○ Write or review code   │    45% Claude Code
  ● Research & summarize   │    39% Aider
  ○ Answer questions (QA)  │    38% Goose
  ○ Classify / route data  │
  ○ Analyze data           │ [PRI] L4c Tool-use infra
  ○ Summarize at scale     │    41% Serena
                           │    35% Context7
 ─ answered ─              │
  Team size: small team    │ NEXT STEP
  Role: developer          │ You're ready for a meta-wrapper...
 ──────────────────────────┴──────────────────────────────
  ↑/↓ Move   Space/Enter Select+Next   ← Back   → Next   q Quit
```

**CLI (non-interactive, pass answers as JSON):**

```bash
clawfit diagnose --answers '{
  "team_size": "small",
  "primary_role": "developer",
  "current_ai_usage": "coding_agent",
  "primary_task": "code-gen",
  "output_destination": "team",
  "frequency": "daily",
  "data_sensitivity": "internal",
  "monthly_budget": "medium",
  "governance_need": "soft",
  "growth_horizon": "deepen"
}'
```

**Web UI** (browser with live filtering):

```bash
clawfit serve          # opens http://localhost:7771
clawfit serve --port 8080
```

---

### Direct recommendation (if you already know your constraints)

```bash
clawfit recommend --task qa --latency low --budget 0.01
```

```bash
clawfit recommend \
  --task code-gen \
  --latency medium \
  --budget 0.01 \
  --hardware cloud \
  --network online \
  --statefulness session \
  --maturity 5 \
  --top 5
```

> `--maturity 5` = sub-agent user stage. See the [maturity × layer map](docs/pages/maturity-layer-map.md) for all 11 stages.

### Inspect the registry

```bash
clawfit list agents
clawfit list llms
clawfit list hardware
clawfit profile
```

---

## Scoring model

10-dimension weighted scoring with hard multipliers:

| Dimension | Weight | What it measures |
|-----------|--------|-----------------|
| task_fit | 0.22 | Does the tool's task list match the user's primary task? |
| maturity_fit | 0.18 | Is the tool appropriate for the user's AI maturity stage (1–11)? |
| role_fit | 0.15 | Does the tool target the user's role (developer/exec/researcher/devops)? |
| layer_relevance | 0.12 | Does the tool's ecosystem layer (L1–L7) match the profile's layer weights? |
| team_size_fit | 0.09 | Is the tool designed for the user's team size (solo/small/mid/large)? |
| network_fit | 0.08 | Does the tool work in the required network environment (online/offline/hybrid)? |
| latency_fit | 0.06 | Does the tool meet the required latency tier? |
| feature_fit | 0.05 | Does the tool support needed features (governance, team-sharing, offline)? |
| complexity_fit | 0.04 | Is setup complexity appropriate for the team's maturity? |
| budget_fit | 0.01 | Does the pricing tier match the budget? |

**Hard multipliers** (applied after weighted sum):
- Offline required + online-only tool → **x0.25**
- Role mismatch (no role overlap) → **x0.75**

---

## Supported task categories

| Task | Description |
|------|-------------|
| `code-gen` | Code generation, review, refactoring |
| `research` | Information gathering, literature review, deep analysis |
| `qa` | Question answering, document Q&A |
| `summarization` | Content summarization at scale |
| `data-analysis` | Data processing, visualization, statistical analysis |
| `orchestration` | Multi-agent coordination, cross-machine task distribution |
| `education` | Personalized learning, tutoring, quiz generation |
| `legal-research` | Legal document search, case law analysis, regulatory compliance |

---

## How it works

The pipeline is intentionally simple and inspectable:

1. **Registry loading** — load 58 tool definitions with 10-field org_fit metadata
2. **Profile building** — convert 10 questionnaire answers into an OrgProfile
3. **Scoring** — score each tool across 10 dimensions + hard multipliers
4. **Layer grouping** — group by ecosystem layer (L1–L7), prioritize by maturity stage
5. **Recommendation output** — return prioritized multi-layer stack with rationale

---

## Repository structure

```text
clawfit/
├─ .claude/agents/          ← harness team sub-agents (5)
├─ clawfit/
│  ├─ cli.py                ← argparse CLI (recommend, list, tui, serve, diagnose)
│  ├─ org_scorer.py         ← 10-dimension scoring engine
│  ├─ tui.py                ← curses TUI with split-pane live preview
│  ├─ server.py             ← stdlib HTTP server (localhost:7771)
│  ├─ diagnose.py           ← interactive CLI questionnaire
│  ├─ filters.py            ← hard constraint elimination
│  ├─ scoring.py            ← cartesian product scoring (agent × LLM × hardware)
│  ├─ recommend.py          ← public API: recommend() → list[dict]
│  ├─ schemas.py            ← dataclasses: Agent, LLM, Hardware, Recommendation
│  ├─ loader.py             ← loads registry/*.json
│  ├─ data/
│  │  ├─ tools_registry.json  ← 76 ecosystem tools with org_fit (10 fields each)
│  │  └─ org_questions.json   ← 10-question bank, 3 phases
│  └─ registry/             ← agents.json, llms.json, hardware.json
├─ docs/
│  ├─ reference-levels.md   ← ecosystem map v0.3 (7-layer taxonomy)
│  ├─ research-watch/       ← 150+ signal analysis docs (daily scan)
│  └─ pages/                ← ecosystem-overview, ecosystem-axes, maturity-layer-map
├─ data/
│  └─ tools_registry.json   ← mirror of clawfit/data/
├─ tests/
│  ├─ test_filters.py
│  └─ test_recommend.py
└─ pyproject.toml
```

---

## Ecosystem research layer

clawfit tracks a broader AI tooling landscape documented in:
- [`docs/reference-levels.md`](docs/reference-levels.md) — canonical 7-layer ecosystem map
- [`docs/pages/ecosystem-axes.md`](docs/pages/ecosystem-axes.md) — classification logic, boundary rules, worked examples
- [`docs/research-watch/`](docs/research-watch/) — 150+ individual tool/trend analysis documents (daily automated scan)
- [`docs/pages/maturity-layer-map.md`](docs/pages/maturity-layer-map.md) — how user maturity stages (1–11) map to tool layers (L1–L7)

### 7-layer structure

| Level | Focus | Examples |
|---|---|---|
| 1 | Base runtimes | Claude Code, OpenClaw, Aider, pi-mono, ATLAS, Hermes Agent |
| 2 | Meta wrappers / harnesses | oh-my-*, DureClaw, SuperClaude, Archon, multica |
| 3 | Team harness / SSOT | CLAUDE.md, AGENTS.md, DESIGN.md, gitagent, superpowers |
| 4a | Memory / persistent context | claude-mem, GBrain, Polysona |
| 4b | Skill packs & managers | career-ops, caveman, obsidian-skills, Chops |
| 4c | Tool-use / action infra | korean-law-mcp, rtk, claude-peers-mcp, serena |
| 5 | Research / evaluation | autoresearch, mdarena, Mozilla cq |
| 6 | Data / knowledge infra | DeepTutor, AnythingLLM |
| 7 | Human interface | pi-generative-ui, Ghost Pepper, ouroboros |

---

## Python API

```python
from clawfit.recommend import recommend

results = recommend(
    task="research",
    latency="high",
    network="online",
    top_n=3,
)

print(results[0])
```

---

## Running tests

```bash
python -m pytest tests/ -v
```

---

## Contributing

Contributions are welcome, especially around:
- registry expansion (new tools with complete org_fit metadata)
- scoring logic improvements
- benchmark references and evidence
- research-watch signal analysis

Open an issue or PR with: what you are adding, what evidence supports it, and how it fits into the comparison model.

---

## License

MIT
