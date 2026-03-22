"""Hard filters that eliminate incompatible options before scoring."""

from __future__ import annotations

from typing import List, Optional

from .schemas import Agent, LLM, Hardware

LATENCY_RANK = {"low": 1, "medium": 2, "high": 3}


def filter_agents(
    agents: List[Agent],
    *,
    task: Optional[str] = None,
    latency: Optional[str] = None,
    network: Optional[str] = None,
    statefulness: Optional[str] = None,
) -> List[Agent]:
    out = list(agents)
    if task:
        out = [a for a in out if task in a.tasks]
    if latency:
        max_rank = LATENCY_RANK.get(latency, 3)
        out = [a for a in out if LATENCY_RANK.get(a.latency, 3) <= max_rank]
    if network:
        out = [a for a in out if a.network == network or a.network == "hybrid"]
    if statefulness:
        out = [a for a in out if a.statefulness == statefulness]
    return out


def filter_llms(
    llms: List[LLM],
    *,
    task: Optional[str] = None,
    latency: Optional[str] = None,
    budget: Optional[float] = None,
    network: Optional[str] = None,
) -> List[LLM]:
    out = list(llms)
    if task:
        out = [m for m in out if task in m.tasks]
    if latency:
        max_rank = LATENCY_RANK.get(latency, 3)
        out = [m for m in out if LATENCY_RANK.get(m.latency, 3) <= max_rank]
    if budget is not None:
        out = [m for m in out if m.cost_per_1k_tokens <= budget]
    if network:
        out = [m for m in out if m.network == network]
    return out


def filter_hardware(
    hardware: List[Hardware],
    *,
    hw_type: Optional[str] = None,
    latency: Optional[str] = None,
    budget: Optional[float] = None,
) -> List[Hardware]:
    out = list(hardware)
    if hw_type:
        out = [h for h in out if h.type == hw_type]
    if latency:
        max_rank = LATENCY_RANK.get(latency, 3)
        out = [h for h in out if LATENCY_RANK.get(h.latency, 3) <= max_rank]
    if budget is not None:
        out = [h for h in out if h.cost_per_hour <= budget]
    return out
