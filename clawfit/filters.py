"""Hard filters that eliminate incompatible options before scoring."""

from __future__ import annotations

from typing import List, Optional, Union

from .schemas import Agent, LLM, Hardware

LATENCY_RANK = {"low": 1, "medium": 2, "high": 3}

# Vertical task tags and their generic parent.
# An agent/LLM with the parent tag satisfies a vertical-tag query (fallback).
# An agent/LLM with the exact vertical tag is preferred (scored higher).
TASK_PARENTS: dict[str, str] = {
    "financial-research": "research",
    "security-testing":   "research",
    "legal-review":       "research",
    "medical-assistance": "qa",
    "content-creation":   "summarization",
    "sales-automation":   "summarization",
}

# Budget tiers: absolute cost-per-1k-tokens ceiling for each tier.
# "high" imposes no ceiling (passes all models).
BUDGET_CEILINGS: dict[str, float] = {
    "free":   0.0,           # offline/local only
    "low":    0.001,         # < $0.001/1k  (DeepSeek Flash, GPT-4o-mini)
    "medium": 0.005,         # < $0.005/1k  (GPT-4o, Claude Sonnet, Mistral Medium)
    "high":   float("inf"),  # no constraint
}


def _task_matches(item_tasks: List[str], requested: str) -> bool:
    """Return True if requested task matches directly or via parent fallback."""
    if requested in item_tasks:
        return True
    parent = TASK_PARENTS.get(requested)
    return parent is not None and parent in item_tasks


def _resolve_budget(budget: Optional[Union[str, float]]) -> Optional[float]:
    """Convert budget tier string or raw float to an absolute ceiling.

    Accepts:
        None         → no budget filter
        "free" / "low" / "medium" / "high" → tier-based ceiling
        0.001 (float) → absolute ceiling, backward-compatible
    """
    if budget is None:
        return None
    if isinstance(budget, str):
        if budget not in BUDGET_CEILINGS:
            valid = ", ".join(BUDGET_CEILINGS)
            raise ValueError(f"Unknown budget tier {budget!r}. Valid tiers: {valid}")
        return BUDGET_CEILINGS[budget]
    return float(budget)


def filter_agents(
    agents: List[Agent],
    *,
    task: Optional[str] = None,
    latency: Optional[str] = None,
    network: Optional[str] = None,
    statefulness: Optional[str] = None,
    maturity_stage: Optional[int] = None,
) -> List[Agent]:
    out = list(agents)
    if task:
        out = [a for a in out if _task_matches(a.tasks, task)]
    if latency:
        max_rank = LATENCY_RANK.get(latency, 3)
        out = [a for a in out if LATENCY_RANK.get(a.latency, 3) <= max_rank]
    if network:
        out = [a for a in out if a.network == network or a.network == "hybrid"]
    if statefulness:
        out = [a for a in out if a.statefulness == statefulness]
    if maturity_stage is not None:
        out = [a for a in out if a.maturity_min <= maturity_stage <= a.maturity_max]
    return out


def filter_llms(
    llms: List[LLM],
    *,
    task: Optional[str] = None,
    latency: Optional[str] = None,
    budget: Optional[Union[str, float]] = None,
    network: Optional[str] = None,
) -> List[LLM]:
    out = list(llms)
    if task:
        out = [m for m in out if _task_matches(m.tasks, task)]
    if latency:
        max_rank = LATENCY_RANK.get(latency, 3)
        out = [m for m in out if LATENCY_RANK.get(m.latency, 3) <= max_rank]
    ceiling = _resolve_budget(budget)
    if ceiling is not None:
        out = [m for m in out if m.cost_per_1k_tokens <= ceiling]
    if network:
        out = [m for m in out if m.network == network]
    return out


def filter_hardware(
    hardware: List[Hardware],
    *,
    hw_type: Optional[str] = None,
    latency: Optional[str] = None,
    budget: Optional[Union[str, float]] = None,
) -> List[Hardware]:
    out = list(hardware)
    if hw_type:
        out = [h for h in out if h.type == hw_type]
    if latency:
        max_rank = LATENCY_RANK.get(latency, 3)
        out = [h for h in out if LATENCY_RANK.get(h.latency, 3) <= max_rank]
    if budget is not None:
        # hardware budget remains absolute (cost_per_hour), tiers don't apply here
        out = [h for h in out if h.cost_per_hour <= float(budget)]
    return out
