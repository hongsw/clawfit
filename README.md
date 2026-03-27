# clawfit

> Agent + LLM + hardware recommendation engine and evidence hub.

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](pyproject.toml)
[![Tests](https://img.shields.io/badge/tests-pytest-informational)](tests/)
[![Status](https://img.shields.io/badge/status-early%20public-green)](https://github.com/hongsw/clawfit)

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

| Level | Focus |
|---|---|
| 1 | Core comparison targets |
| 2 | Workflow wrappers and orchestration tools |
| 3 | Architecture and benchmark references |
| 4 | Memory, context, MCP, and plugin ecosystem |
| 5 | Data hub, RAG, and evidence infrastructure |
| 6 | Productivity, input, and human-agent interface tools |

See full details in [`docs/reference-levels.md`](docs/reference-levels.md).

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
