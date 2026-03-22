"""Load registry JSON files into typed dataclass lists."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List

from .schemas import Agent, LLM, Hardware

_REGISTRY_DIR = Path(__file__).parent / "registry"


def _load_json(filename: str) -> list:
    with open(_REGISTRY_DIR / filename) as f:
        return json.load(f)


def load_agents() -> List[Agent]:
    return [Agent(**r) for r in _load_json("agents.json")]


def load_llms() -> List[LLM]:
    return [LLM(**r) for r in _load_json("llms.json")]


def load_hardware() -> List[Hardware]:
    return [Hardware(**r) for r in _load_json("hardware.json")]
