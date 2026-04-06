"""Score candidate combinations and produce ranked recommendations."""

from __future__ import annotations

from typing import List, Optional, Tuple

from .schemas import Agent, LLM, Hardware, Recommendation

LATENCY_RANK = {"low": 1, "medium": 2, "high": 3}

# Maturity stage → clawfit tool layer description
MATURITY_LAYER_HINTS = {
    1: "L1 base runtime (chat interface)",
    2: "L1 multi-runtime + L7 interface",
    3: "L4a simple automation (Zapier-level MCP)",
    4: "L4 tool-use (MCP / Composio / Serena)",
    5: "L2 meta-wrapper (oh-my-*, multi-agent)",
    6: "L2 + L3 harness (personal → team SSOT)",
    7: "L5 self-improvement loop / autoresearch",
    8: "L1→L2 builder (own harness/runtime)",
    9: "L6 data / sLLM / knowledge infra",
    10: "L3 executable SSOT (org operating system)",
    11: "L5 + L6 frontier (benchmark / research producer)",
}


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


def _maturity_score(agent: Agent, maturity_stage: int) -> float:
    """
    1.0 at optimal stage, decays toward min/max, 0.0 outside range.
    Within range: score >= 0.3 (always worthwhile to show).
    """
    if maturity_stage < agent.maturity_min or maturity_stage > agent.maturity_max:
        return 0.0
    distance = abs(maturity_stage - agent.maturity_optimal)
    half_range = max(
        agent.maturity_optimal - agent.maturity_min,
        agent.maturity_max - agent.maturity_optimal,
        1,
    )
    return round(max(1.0 - (distance / half_range) * 0.7, 0.3), 3)


def _maturity_note(agent: Agent, maturity_stage: Optional[int]) -> str:
    """Generate a human-readable note about maturity fit."""
    if maturity_stage is None:
        return ""
    if maturity_stage < agent.maturity_min:
        return (
            f"Stage {maturity_stage} is below this agent's recommended range "
            f"({agent.maturity_min}–{agent.maturity_max}). "
            f"Consider starting with simpler patterns first."
        )
    if maturity_stage > agent.maturity_max:
        return (
            f"Stage {maturity_stage} has outgrown this agent's sweet spot "
            f"({agent.maturity_min}–{agent.maturity_max}). "
            f"You may benefit from more advanced orchestration."
        )
    if maturity_stage == agent.maturity_optimal:
        return f"Optimal match for stage {maturity_stage} users."
    return (
        f"Good fit for stage {maturity_stage} "
        f"(optimal: {agent.maturity_optimal}, range: {agent.maturity_min}–{agent.maturity_max})."
    )


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


def _build_why(
    agent: Agent, llm: LLM, hw: Hardware, task: str, maturity_stage: Optional[int]
) -> List[str]:
    reasons = []
    reasons.append(f"{agent.name} supports '{task}' with {agent.latency} latency")
    reasons.append(f"{llm.name} ({llm.provider}) fits the task and cost profile")
    if llm.id in agent.preferred_llms:
        reasons.append(f"{llm.name} is a preferred LLM for {agent.name}")
    reasons.append(f"{hw.name} ({hw.type}) matches deployment needs")
    if maturity_stage is not None:
        layer_hint = MATURITY_LAYER_HINTS.get(maturity_stage, "")
        if layer_hint:
            reasons.append(f"Stage {maturity_stage} user context: {layer_hint}")
    return reasons


def score_combination(
    agent: Agent,
    llm: LLM,
    hw: Hardware,
    *,
    target_latency: str = "medium",
    maturity_stage: Optional[int] = None,
) -> float:
    lat = (
        _latency_score(target_latency, agent.latency) * 0.2
        + _latency_score(target_latency, llm.latency) * 0.2
        + _latency_score(target_latency, hw.latency) * 0.1
    )
    cost = _cost_score(llm, hw) * 0.25
    pref = _preferred_llm_bonus(agent, llm)
    base = 0.1

    if maturity_stage is not None:
        mat = _maturity_score(agent, maturity_stage) * 0.15
        # Redistribute: reduce base weight to make room for maturity
        return round(min(lat + cost * 0.85 + pref + base * 0.67 + mat, 1.0), 3)

    return round(min(lat + cost + pref + base, 1.0), 3)


def rank(
    agents: List[Agent],
    llms: List[LLM],
    hardware: List[Hardware],
    *,
    task: str,
    target_latency: str = "medium",
    maturity_stage: Optional[int] = None,
) -> List[Tuple[float, Recommendation]]:
    results = []
    for a in agents:
        for m in llms:
            for h in hardware:
                score = score_combination(
                    a, m, h,
                    target_latency=target_latency,
                    maturity_stage=maturity_stage,
                )
                rec = Recommendation(
                    agent=a.id,
                    llm=m.id,
                    hardware=h.id,
                    architecture=_infer_architecture(a, m, h),
                    fit_score=score,
                    why=_build_why(a, m, h, task, maturity_stage),
                    risk=_identify_risks(a, m, h),
                    maturity_note=_maturity_note(a, maturity_stage),
                )
                results.append((score, rec))
    results.sort(key=lambda x: x[0], reverse=True)
    return results
