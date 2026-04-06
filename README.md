# clawfit

> Agent + LLM + hardware recommendation engine and evidence hub.

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](pyproject.toml)
[![Tests](https://img.shields.io/badge/tests-pytest-informational)](tests/)
[![Status](https://img.shields.io/badge/status-early%20public-green)](https://github.com/hongsw/clawfit)

**Read in:** [한국어 🇰🇷](README.ko.md)

`clawfit` helps answer a practical question:

**Given a task, latency target, budget, network conditions, and statefulness requirements, what combination of agent pattern, model, and hardware is the best fit?**

It started as a lightweight recommendation CLI and is evolving toward a broader **comparison + evidence hub** for AI coding tools, agent runtimes, orchestration frameworks, and supporting infrastructure.

> [!IMPORTANT]
> **START HERE — ECOSYSTEM MAP**
>
> If you want to understand what `clawfit` is really mapping, comparing, and tracking, **click this first**:
>
> ## **[Jump directly to the ecosystem map: `docs/reference-levels.md`](https://github.com/hongsw/clawfit/blob/main/docs/reference-levels.md)**
>
> This is the fastest way to see the current landscape of:
> - base agent runtimes
> - harness / wrapper layers
> - research-loop systems
> - MCP / memory / tool ecosystems
> - vibe-coding / agent-tool / meta-wrapper trends
>
> **If you only click one link in this repo, click this one.**

---

## 🔥 What's hot right now (2026-04)

The ecosystem is moving fast. Here are the signals worth watching this week:

| Signal | Why it matters | Level |
|--------|---------------|-------|
| **[claude-mem](https://github.com/thedotmack/claude-mem) ⭐45k** | Cross-session memory for Claude Code via hooks + SQLite + Chroma. Install with `npx claude-mem install`. | L4a Memory |
| **[deepagents](https://github.com/langchain-ai/deepagents) ⭐19k** | LangChain's batteries-included open-source agent harness. Direct competitor to Claude Code CLI. | L1/L2 |
| **Agentic AI Foundation** | MCP donated to Linux Foundation consortium (Microsoft + Google + OpenAI + Anthropic). 97M monthly SDK downloads. OpenAI's AGENTS.md is a new cross-platform spec. | Governance |
| **[oh-my-claudecode](https://github.com/yeachan-heo/oh-my-claudecode) ⭐24k** | Star count doubled — multi-agent Claude Code orchestration gaining serious traction. | L2 |
| **[everything-claude-code](https://github.com/affaan-m/everything-claude-code) ⭐140k** | Largest known Claude Code resource hub. | L3 |
| **Claude Computer Use** | First-party desktop control (mouse/keyboard/screen) via Claude Code Desktop + Cowork. Collapses L1/L7 boundary. | L1/L7 |
| **Skill layer maturing** | [Chops](https://github.com/Shpigford/chops), [skills-cleaner](https://github.com/amebahead/skills-cleaner), [caveman](https://github.com/JuliusBrussee/caveman) ⭐1.7k (716 HN pts) — token compression as a skill. L4 fragmenting into skill managers / domain packs / tool infra. | L4b |
| **[awesome-design-md](https://github.com/VoltAgent/awesome-design-md) ⭐15.9k** | 55+ DESIGN.md files for AI agents — extends SSOT pattern to visual/UI design. New L3 sub-pattern alongside CLAUDE.md and AGENTS.md. | L3 |
| **[mdarena](https://github.com/HudsonGri/mdarena)** | First tool to empirically benchmark CLAUDE.md instruction variants. Finding: per-directory targeted instructions beat monolithic files by ~27%. | L5 |
| **[rtk](https://github.com/rtk-ai/rtk)** | Rust CLI proxy compressing shell output 60–90% before agent reads it. Changes the cost curve for session-heavy workflows. | L4c |
| **[Mozilla cq](https://blog.mozilla.ai/cq-stack-overflow-for-agents/)** | "Stack Overflow for agents" — multi-agent shared knowledge commons. New statefulness pattern: *collective*. | L5 |

Full analysis in [`docs/research-watch/`](docs/research-watch/) · Full map in [`docs/reference-levels.md`](docs/reference-levels.md)

---

## Changelog

| Date | What changed |
|------|-------------|
| 2026-04-06 | 6 additional research-watch docs: apex-protocol, awesome-design-md, caveman, gemma-gem, mdarena, modo |
| 2026-04-06 | `reference-levels.md` updated: awesome-design-md → L3, caveman → L4b, rtk → L4c, mdarena → L5 |
| 2026-04-06 | Star counts verified via GitHub API across all 50+ tracked repos |
| 2026-04-06 | 13 new research-watch docs: deepagents, claude-mem, Agentic AI Foundation, Codex plugins, Claude Computer Use, oh-my-pi Hashline, cq, gitagent, skill layer cluster, understudy |
| 2026-04-06 | `reference-levels.md` → v0.3: Level 4 split into 4a/4b/4c subtypes; new L3 AGENTS.md entry; L7 expanded with computer-use agents |
| 2026-04-06 | Harness team added: `.claude/agents/` with 5 specialized sub-agents |
| 2026-03-31 | Ecosystem map v0.2: 7-layer taxonomy, research-watch scan launch |

---

## New here?

- **Canonical intro:** [`Introducing clawfit`](https://github.com/hongsw/clawfit/blob/main/docs/posts/2026-03-28-introducing-clawfit.md)
- **Ecosystem overview:** [`docs/pages/ecosystem-overview.md`](https://github.com/hongsw/clawfit/blob/main/docs/pages/ecosystem-overview.md)

## Why this exists

The AI tooling landscape is fragmented.

People compare:
- agent frameworks
- coding assistants
- model providers
- local vs cloud hardware
- memory / MCP / plugin ecosystems
- workflow wrappers and orchestration layers

But most comparisons are either:
- anecdotal,
- marketing-heavy,
- too narrow,
- or disconnected from real execution constraints.

`clawfit` is an attempt to make those tradeoffs more explicit.

---

## What clawfit does today

### 1) Recommends combinations
It ranks candidate combinations of:
- **agent pattern**
- **LLM**
- **hardware**

based on constraints like:
- task type
- latency
- budget
- hardware preference
- online/offline network requirement
- statefulness requirement

### 2) Encodes tradeoffs in structured registries
Instead of burying assumptions in prose, clawfit stores comparison inputs in machine-readable data files.

### 3) Organizes the ecosystem into reference levels
The repo also includes an expanding evidence map for AI agent and coding-tool ecosystems.

---

## Quick start

### Install

```bash
git clone https://github.com/hongsw/clawfit.git
cd clawfit
pip install -e .
```

### Run a recommendation

```bash
clawfit recommend --task qa --latency low --budget 0.01
```

### More detailed example

```bash
clawfit recommend \
  --task code-gen \
  --latency medium \
  --budget 0.01 \
  --hardware cloud \
  --network online \
  --statefulness session \
  --top 5
```

### Inspect the registry

```bash
clawfit list agents
clawfit list llms
clawfit list hardware
clawfit profile
```

---

## Example output

`clawfit recommend` returns JSON:

```json
[
  {
    "agent": "react-agent",
    "llm": "claude-sonnet",
    "hardware": "aws-cpu-medium",
    "architecture": "cloud-api",
    "fit_score": 0.85,
    "why": [
      "Good task match for QA workloads",
      "Latency target aligns with available agent + model profile"
    ],
    "risk": [
      "Higher per-token cost than smaller alternatives"
    ]
  }
]
```

---

## Supported task categories

Current task labels include:

- `classification`
- `code-gen`
- `data-analysis`
- `qa`
- `research`
- `summarization`

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

## How it works

The current pipeline is intentionally simple and inspectable:

1. **Registry loading**
   - load structured agent / LLM / hardware definitions
2. **Constraint filtering**
   - eliminate incompatible options
3. **Scoring**
   - rank remaining combinations by fit
4. **Recommendation output**
   - return top candidates with rationale and risks

This makes the system easy to extend, audit, and benchmark.

---

## Repository structure

```text
clawfit/
├─ clawfit/
│  ├─ cli.py
│  ├─ filters.py
│  ├─ loader.py
│  ├─ recommend.py
│  ├─ scoring.py
│  └─ schemas.py
├─ data/
│  ├─ feature_matrix.json
│  ├─ feature_matrix.schema.json
│  └─ tools_registry.json
├─ docs/
│  └─ reference-levels.md
├─ tests/
│  ├─ test_filters.py
│  └─ test_recommend.py
└─ pyproject.toml
```

---

## Ecosystem research layer

clawfit is evolving beyond a narrow recommender into a broader comparison framework for AI tooling.

Important repo documents:
- [`docs/reference-levels.md`](docs/reference-levels.md) — classification of comparison targets and ecosystem layers
- `data/tools_registry.json` — initial structured registry
- `data/feature_matrix.json` — early feature verification matrix
- `data/feature_matrix.schema.json` — schema for feature data

### Reference levels overview

The current map uses a **7-layer structure**. These are best read as ecosystem layers/lenses, not a sequential maturity ladder.

| Level | Focus |
|---|---|
| 1 | Base runtimes / primary agent surfaces |
| 2 | Meta wrappers / harnesses / orchestration layers |
| 3 | Team harness / executable SSOT / governance layer |
| 4 | Capability extension layer (MCP / memory / plugins / tools) |
| 5 | Research / evaluation / benchmark / autoresearch patterns |
| 6 | Data / evidence / knowledge infrastructure |
| 7 | Human interface / voice / input-output layer |

See full details in [`docs/reference-levels.md`](docs/reference-levels.md) · [한국어 맵](docs/reference-levels.ko.md) and the overview hub at [`docs/pages/ecosystem-overview.md`](docs/pages/ecosystem-overview.md).

---

## Running tests

```bash
python -m pytest tests/ -v
```

---

## Roadmap

Planned directions include:

- richer scoring criteria
- clearer evidence provenance for registry claims
- benchmark-aware recommendation logic
- more agent runtime profiles
- better hardware taxonomy
- public comparison dashboards / docs
- stronger integration with ecosystem research workflows

---

## Who this is for

clawfit is useful if you are:
- comparing agent stacks
- deciding between local and cloud execution
- designing a coding-agent workflow
- mapping AI tool ecosystems
- building an evidence-backed recommendation layer

---

## Contributing

Contributions are welcome, especially around:
- registry expansion
- feature verification
- scoring logic
- benchmark references
- documentation cleanup

If you want to contribute, open an issue or PR with:
- what you are adding,
- what evidence supports it,
- and how it should fit into the comparison model.

---

## License

MIT
