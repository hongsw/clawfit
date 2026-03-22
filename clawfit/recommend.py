"""Top-level recommend API: filter then score."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List, Optional

from .loader import load_agents, load_llms, load_hardware
from .filters import filter_agents, filter_llms, filter_hardware
from .scoring import rank
from .schemas import Recommendation


def recommend(
    *,
    task: str,
    latency: str = "medium",
    budget: Optional[float] = None,
    hardware: Optional[str] = None,
    network: Optional[str] = None,
    statefulness: Optional[str] = None,
    top_n: int = 3,
) -> List[Dict[str, Any]]:
    agents = filter_agents(
        load_agents(),
        task=task,
        latency=latency,
        network=network,
        statefulness=statefulness,
    )
    llms = filter_llms(
        load_llms(),
        task=task,
        latency=latency,
        budget=budget,
        network=network,
    )
    hw = filter_hardware(
        load_hardware(),
        hw_type=hardware,
        latency=latency,
        budget=None,  # budget arg is per-1k-tokens for LLM; hw filtered by type/latency
    )

    if not agents:
        return [{"error": "No agents match the given constraints."}]
    if not llms:
        return [{"error": "No LLMs match the given constraints."}]
    if not hw:
        return [{"error": "No hardware matches the given constraints."}]

    ranked = rank(agents, llms, hw, task=task, target_latency=latency)
    return [asdict(rec) for _, rec in ranked[:top_n]]
