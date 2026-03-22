"""Score candidate combinations and produce ranked recommendations."""

from __future__ import annotations

from typing import List, Tuple

from .schemas import Agent, LLM, Hardware, Recommendation

LATENCY_RANK = {"low": 1, "medium": 2, "high": 3}


def _latency_score(target: str, actual: str) -> float:
    """1.0 if exact match, 0.5 if one step away, 0.0 if two steps."""
    diff = abs(LATENCY_RANK.get(target, 2) - LATENCY_RANK.get(actual, 2))
    return max(1.0 - diff * 0.5, 0.0)


def _preferred_llm_bonus(agent: Agent, llm: LLM) -> float:
    return 0.15 if llm.id in agent.preferred_llms else 0.0


def _cost_score(llm: LLM, hw: Hardware) -> float:
    """Lower cost => higher score, normalized 0-1."""
    combined = llm.cost_per_1k_tokens * 1000 + hw.cost_per_hour
    if combined <= 0:
        return 1.0
    if combined < 1:
        return 0.9
    if combined < 10:
        return 0.6
    if combined < 50:
        return 0.3
    return 0.1


def _infer_architecture(agent: Agent, llm: LLM, hw: Hardware) -> str:
    if hw.type == "edge":
        return "edge-local"
    if llm.network == "offline":
        return "on-prem-rag" if "qa" in agent.tasks else "on-prem-batch"
    if agent.statefulness == "persistent":
        return "cloud-orchestrated"
    return "cloud-api"


def _identify_risks(agent: Agent, llm: LLM, hw: Hardware) -> List[str]:
    risks = []
    if llm.network == "online" and hw.type == "edge":
        risks.append("Edge hardware with cloud LLM requires stable network")
    if llm.cost_per_1k_tokens >= 0.01:
        risks.append("High per-token cost — monitor usage")
    if hw.cost_per_hour >= 20:
        risks.append("Expensive hardware — consider auto-scaling")
    if agent.statefulness == "persistent" and hw.type == "cloud":
        risks.append("Persistent state on ephemeral cloud — add durable storage")
    return risks


def _build_why(agent: Agent, llm: LLM, hw: Hardware, task: str) -> List[str]:
    reasons = []
    reasons.append(f"{agent.name} supports '{task}' with {agent.latency} latency")
    reasons.append(f"{llm.name} ({llm.provider}) fits the task and cost profile")
    if llm.id in agent.preferred_llms:
        reasons.append(f"{llm.name} is a preferred LLM for {agent.name}")
    reasons.append(f"{hw.name} ({hw.type}) matches deployment needs")
    return reasons


def score_combination(
    agent: Agent, llm: LLM, hw: Hardware, *, target_latency: str = "medium"
) -> float:
    lat = (
        _latency_score(target_latency, agent.latency) * 0.2
        + _latency_score(target_latency, llm.latency) * 0.2
        + _latency_score(target_latency, hw.latency) * 0.1
    )
    cost = _cost_score(llm, hw) * 0.25
    pref = _preferred_llm_bonus(agent, llm)
    base = 0.1  # baseline
    return round(min(lat + cost + pref + base, 1.0), 3)


def rank(
    agents: List[Agent],
    llms: List[LLM],
    hardware: List[Hardware],
    *,
    task: str,
    target_latency: str = "medium",
) -> List[Tuple[float, Recommendation]]:
    results = []
    for a in agents:
        for m in llms:
            for h in hardware:
                score = score_combination(a, m, h, target_latency=target_latency)
                rec = Recommendation(
                    agent=a.id,
                    llm=m.id,
                    hardware=h.id,
                    architecture=_infer_architecture(a, m, h),
                    fit_score=score,
                    why=_build_why(a, m, h, task),
                    risk=_identify_risks(a, m, h),
                )
                results.append((score, rec))
    results.sort(key=lambda x: x[0], reverse=True)
    return results
