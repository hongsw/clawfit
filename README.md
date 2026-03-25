# clawfit

AI agent + LLM + hardware recommendation engine.

Given a task description and constraints (latency, budget, network, statefulness),
clawfit recommends the best agent pattern, LLM, and hardware combination.

## Install

```bash
pip install -e .
```

## CLI Usage

### Get a recommendation

```bash
clawfit recommend --task qa --latency low --budget 0.01
```

With all options:

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

### List registry entries

```bash
clawfit list agents
clawfit list llms
clawfit list hardware
```

### Show registry summary

```bash
clawfit profile
```

## Output

`recommend` returns JSON:

```json
[
  {
    "agent": "react-agent",
    "llm": "claude-sonnet",
    "hardware": "aws-cpu-medium",
    "architecture": "cloud-api",
    "fit_score": 0.85,
    "why": ["ReAct Agent supports 'qa' with medium latency", ...],
    "risk": ["High per-token cost — monitor usage"]
  }
]
```

## Python API

```python
from clawfit.recommend import recommend

results = recommend(task="research", latency="high", network="online")
```

## Tasks

Supported task categories: `classification`, `code-gen`, `data-analysis`, `qa`, `research`, `summarization`.

## Architecture

1. **Registry** — JSON files define available agents, LLMs, and hardware.
2. **Filters** — Hard constraints eliminate incompatible options.
3. **Scoring** — Remaining candidates are scored on latency fit, cost, and preference alignment.
4. **Recommendation** — Top-N results returned with architecture label, rationale, and risks.

## Ecosystem research

clawfit is evolving beyond a simple recommender into a comparison and evidence hub for AI coding tools.

Reference classification document:
- `docs/reference-levels.md`

Initial structured registry:
- `data/tools_registry.json`

Initial feature verification dataset:
- `data/feature_matrix.json`
- `data/feature_matrix.schema.json`

It currently organizes references into six levels:
- Level 1 — core comparison targets
- Level 2 — workflow wrappers and orchestration tools
- Level 3 — architecture and benchmark references
- Level 4 — memory, context, MCP, and plugin ecosystem
- Level 5 — data hub, RAG, and evidence infrastructure
- Level 6 — productivity, input, and human-agent interface tools

## Tests

```bash
python -m pytest tests/ -v
```
