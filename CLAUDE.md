# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install in editable mode (required before using CLI)
pip install -e .

# Run all tests
python -m pytest tests/ -v

# Run a single test file
python -m pytest tests/test_filters.py -v

# Run a single test by name
python -m pytest tests/test_recommend.py::TestRecommend::test_basic_recommendation -v

# CLI usage
clawfit recommend --task qa --latency low --budget 0.01
clawfit recommend --task code-gen --latency medium --budget 0.01 --hardware cloud --network online --statefulness session --top 5
clawfit list agents
clawfit list llms
clawfit list hardware
clawfit profile
```

## Architecture

The recommendation pipeline is: **load → filter → score → rank → output**

```
clawfit/
├── cli.py          # argparse CLI; subcommands: recommend, list, profile
├── schemas.py      # dataclasses: Agent, LLM, Hardware, Recommendation
├── loader.py       # loads registry/*.json into dataclass instances
├── filters.py      # hard constraint elimination (task, latency, budget, network, statefulness)
├── scoring.py      # cartesian product scoring; weights: latency 0.5, cost 0.25, LLM preference 0.15, baseline 0.1
├── recommend.py    # public API: recommend() → list[dict]
└── registry/       # JSON truth: agents.json (4), llms.json (7), hardware.json (5)
```

**Entry points:**
- CLI: `clawfit.cli:main`
- Python API: `from clawfit.recommend import recommend`

**Registry data** lives in `clawfit/registry/*.json`. To add a new agent/LLM/hardware option, edit the relevant JSON file — no code changes needed.

**Scoring** (`scoring.py`) assigns fit_score 0–1 per (agent, llm, hardware) triple. `rank()` does the cartesian product over all filtered candidates and sorts descending.

**Filters** (`filters.py`) are hard constraints — a candidate that doesn't pass a filter is never scored. Filters use `LATENCY_RANK` (low=1, medium=2, high=3) for ordering: a requested "low" latency allows low only; "medium" allows low and medium.

## Ecosystem Context

`clawfit` tracks a broader AI tooling landscape documented in `docs/reference-levels.md` — a 7-layer taxonomy covering base agent runtimes, harness/wrapper layers, research-loop systems, MCP ecosystems, and vibe-coding trends. The `docs/research-watch/` directory contains named signals tracking emerging tools. This context informs how new registry entries and scoring criteria are added.

## No External Dependencies

The package is intentionally stdlib-only (argparse, dataclasses, json, unittest). Do not introduce third-party dependencies without explicit discussion.
