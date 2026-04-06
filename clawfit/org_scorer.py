"""
Organization-level tool scorer.

Takes an org_profile (derived from questionnaire answers) and scores
ecosystem tools across all L1–L7 layers, returning a prioritized
multi-layer recommendation stack.
"""

from __future__ import annotations

import json
import pathlib
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional, Tuple

# Layer label map
LAYER_LABELS = {
    "L1": "Base runtime",
    "L2": "Meta wrapper / harness",
    "L3": "Team harness / SSOT",
    "L4a": "Memory / persistent context",
    "L4b": "Skill packs & managers",
    "L4c": "Tool-use / action infra",
    "L5": "Research / evaluation",
    "L6": "Data / knowledge infra",
    "L7": "Human interface / computer use",
}

# Maturity stage → recommended layers
MATURITY_LAYER_MAP: Dict[int, List[str]] = {
    1:  ["L1", "L7"],
    2:  ["L1", "L7"],
    3:  ["L1", "L4c"],
    4:  ["L1", "L4b", "L4c"],
    5:  ["L1", "L2", "L4b", "L4c"],
    6:  ["L1", "L2", "L3", "L4a", "L4b"],
    7:  ["L2", "L3", "L5"],
    8:  ["L1", "L2", "L3", "L5"],
    9:  ["L1", "L6", "L5"],
    10: ["L3", "L5", "L6"],
    11: ["L3", "L5", "L6"],
}


@dataclass
class OrgProfile:
    """Derived from questionnaire answers."""
    team_size: int = 1
    roles: List[str] = field(default_factory=lambda: ["developer"])
    maturity_stage: int = 3
    future_maturity_stage: int = 4
    task: str = "code-gen"
    latency: str = "medium"
    network: str = "online"
    statefulness: str = "stateless"
    budget_tier: str = "medium"   # free / low / medium / high
    budget: float = 0.01           # max cost_per_1k_tokens
    offline_required: bool = False
    governance_need: bool = False
    sharing: bool = False
    hardware_hint: Optional[str] = None
    layer_weights: Dict[str, float] = field(default_factory=lambda: {
        "L1": 0.3, "L2": 0.2, "L3": 0.1,
        "L4a": 0.1, "L4b": 0.1, "L4c": 0.1,
        "L5": 0.05, "L6": 0.05, "L7": 0.0,
    })


@dataclass
class LayerRecommendation:
    layer: str
    layer_label: str
    tools: List[Dict[str, Any]]
    why: str
    priority: str          # "primary" / "secondary" / "future"


@dataclass
class OrgRecommendation:
    org_profile: Dict[str, Any]
    maturity_stage: int
    maturity_label: str
    stack: List[Dict[str, Any]]    # one entry per relevant layer
    core_agent_fit: List[Dict[str, Any]]   # from clawfit recommend()
    next_step_hint: str


def _load_tools_registry() -> List[Dict]:
    path = pathlib.Path(__file__).parent / "data" / "tools_registry.json"
    with open(path) as f:
        return json.load(f)


def _maturity_label(stage: int) -> str:
    labels = {
        1: "Chatbot user",
        2: "Multi-chatbot user",
        3: "Automation beginner",
        4: "Tool-using agent user",
        5: "Sub-agent operator",
        6: "Personal harness builder",
        7: "Self-improvement loop",
        8: "Agent system publisher",
        9: "sLLM / ML practitioner",
        10: "Org SSOT architect",
        11: "Frontier researcher",
    }
    return labels.get(stage, f"Stage {stage}")


def _score_tool(tool: Dict, profile: OrgProfile) -> float:
    """Score a single ecosystem tool against the org profile (0–1)."""
    score = 0.0
    org_fit = tool.get("org_fit", {})

    # Layer weight contribution
    level_key = f"L{tool.get('level', 1)}"
    score += profile.layer_weights.get(level_key, 0.0) * 0.4

    # Maturity fit
    min_m = org_fit.get("min_maturity", 1)
    max_m = org_fit.get("max_maturity", 11)
    opt_m = org_fit.get("optimal_maturity", 6)
    if min_m <= profile.maturity_stage <= max_m:
        dist = abs(profile.maturity_stage - opt_m)
        half = max(opt_m - min_m, max_m - opt_m, 1)
        score += max(0.3 - (dist / half) * 0.2, 0.1) * 0.3
    else:
        score -= 0.1  # out of range penalty

    # Feature matching
    features = org_fit.get("features", [])
    if profile.governance_need and "governance" in features:
        score += 0.1
    if profile.sharing and "team-sharing" in features:
        score += 0.1
    if profile.offline_required and "offline" in features:
        score += 0.15
    elif profile.offline_required and "offline" not in features and tool.get("level") == 1:
        score -= 0.2  # penalize online-only tools when offline required

    # Budget compatibility
    budget_tier = org_fit.get("pricing_tier", "paid")
    if profile.budget_tier == "free" and budget_tier != "free":
        score -= 0.15
    elif profile.budget_tier in ("medium", "high") and budget_tier in ("paid", "free"):
        score += 0.05

    return round(max(min(score, 1.0), 0.0), 3)


def _next_step_hint(profile: OrgProfile) -> str:
    stage = profile.maturity_stage
    if stage <= 2:
        return (
            "Start with a base runtime (L1). Learn one tool deeply before adding layers. "
            "Your next milestone: integrate your first MCP tool (L4c)."
        )
    if stage <= 4:
        return (
            "You're ready for a meta-wrapper or harness (L2). "
            "Try oh-my-claudecode or SuperClaude to add orchestration on top of your base agent."
        )
    if stage <= 6:
        return (
            "You're in the harness zone. "
            "Consider formalizing team conventions into a SSOT layer (L3): CLAUDE.md, AGENTS.md, or gitagent. "
            "Add persistent memory (L4a) to reduce repeated context loading."
        )
    if stage <= 8:
        return (
            "You should be running self-improvement loops (L5). "
            "Use autoresearch or cq to let agents learn from prior runs. "
            "Consider publishing your harness as a reusable component (L1→L2)."
        )
    return (
        "You operate at the frontier. "
        "Focus on benchmarking your systems (L5) and building knowledge infrastructure (L6). "
        "Your SSOT layer (L3) should be the canonical input for org-wide AI governance."
    )


def build_profile_from_answers(answers: Dict[str, str]) -> OrgProfile:
    """
    Convert raw questionnaire answers {question_id: option_value} into an OrgProfile.
    Merges all signals from selected options.
    """
    path = pathlib.Path(__file__).parent / "data" / "org_questions.json"
    with open(path) as f:
        qbank = json.load(f)

    profile = OrgProfile()
    layer_w: Dict[str, float] = {
        "L1": 0.3, "L2": 0.2, "L3": 0.1,
        "L4a": 0.05, "L4b": 0.1, "L4c": 0.1,
        "L5": 0.05, "L6": 0.05, "L7": 0.05,
    }
    future_delta = 0

    for q in qbank["questions"]:
        qid = q["id"]
        if qid not in answers:
            continue
        chosen_value = answers[qid]
        for opt in q["options"]:
            if opt["value"] == chosen_value:
                sigs = opt["signals"]
                # Apply each signal
                for k, v in sigs.items():
                    if k == "layer_weights":
                        for lk, lv in v.items():
                            layer_w[lk] = layer_w.get(lk, 0.0) + lv
                    elif k == "future_maturity_delta":
                        future_delta += v
                    elif k == "roles":
                        profile.roles = v
                    elif hasattr(profile, k):
                        setattr(profile, k, v)
                break

    # Normalize layer weights
    total = sum(layer_w.values()) or 1.0
    profile.layer_weights = {k: round(v / total, 3) for k, v in layer_w.items()}
    profile.future_maturity_stage = min(profile.maturity_stage + future_delta, 11)

    return profile


def org_recommend(profile: OrgProfile, top_per_layer: int = 3) -> OrgRecommendation:
    """
    Score all ecosystem tools against the org profile and return a layered stack.
    """
    tools = _load_tools_registry()

    # Score all tools
    scored: List[Tuple[float, Dict]] = []
    for t in tools:
        s = _score_tool(t, profile)
        scored.append((s, t))
    scored.sort(key=lambda x: x[0], reverse=True)

    # Group by layer, take top N per relevant layer
    relevant_layers = MATURITY_LAYER_MAP.get(profile.maturity_stage, ["L1", "L2", "L4c"])
    # Also include future layers
    future_layers = MATURITY_LAYER_MAP.get(profile.future_maturity_stage, [])
    future_only = [l for l in future_layers if l not in relevant_layers]

    stack: List[Dict] = []
    seen_layers: Dict[str, List] = {}

    for s, t in scored:
        layer_key = f"L{t.get('level', 1)}"
        seen_layers.setdefault(layer_key, [])
        if len(seen_layers[layer_key]) < top_per_layer:
            seen_layers[layer_key].append({
                "id": t["id"],
                "name": t["name"],
                "url": t.get("url", ""),
                "score": s,
                "notes": t.get("notes", ""),
                "layer": layer_key,
                "priority": "primary" if layer_key in relevant_layers else (
                    "future" if layer_key in future_only else "secondary"
                ),
            })

    # Build ordered stack: primary layers first, then future
    for layer in relevant_layers:
        items = seen_layers.get(layer, [])
        if items:
            why = _layer_why(layer, profile)
            stack.append({
                "layer": layer,
                "layer_label": LAYER_LABELS.get(layer, layer),
                "priority": "primary",
                "why": why,
                "tools": items,
            })

    for layer in future_only:
        items = seen_layers.get(layer, [])
        if items:
            stack.append({
                "layer": layer,
                "layer_label": LAYER_LABELS.get(layer, layer),
                "priority": "future",
                "why": f"Not needed now, but relevant as you grow toward stage {profile.future_maturity_stage}.",
                "tools": items,
            })

    # Run the core agent+LLM+hw recommendation
    from .recommend import recommend
    core_fit = recommend(
        task=profile.task,
        latency=profile.latency,
        budget=profile.budget if profile.budget > 0 else None,
        network=profile.network if profile.offline_required else None,
        # Only enforce statefulness as a hard filter when persistent storage is required;
        # "session" and "stateless" profiles should still see persistent-capable agents.
        statefulness=profile.statefulness if profile.statefulness == "persistent" else None,
        maturity_stage=profile.maturity_stage,
        top_n=2,
    )

    return OrgRecommendation(
        org_profile=asdict(profile),
        maturity_stage=profile.maturity_stage,
        maturity_label=_maturity_label(profile.maturity_stage),
        stack=stack,
        core_agent_fit=core_fit,
        next_step_hint=_next_step_hint(profile),
    )


def _layer_why(layer: str, profile: OrgProfile) -> str:
    whys = {
        "L1": f"You need a base runtime for stage {profile.maturity_stage} work — this is the foundation everything runs on.",
        "L2": "A meta-wrapper lets your team apply consistent conventions and orchestration on top of the base agent.",
        "L3": f"With {'governance requirements and ' if profile.governance_need else ''}team size {profile.team_size}, a shared SSOT layer prevents drift and standardizes how agents operate.",
        "L4a": "Persistent memory reduces repeated context loading across sessions — valuable for teams sharing knowledge.",
        "L4b": "Skill packs extend your agent's capabilities for your specific domain without custom code.",
        "L4c": "Tool-use infrastructure connects your agent to external systems and APIs.",
        "L5": "Evaluation and self-improvement loops help agents get better over time — essential at your maturity level.",
        "L6": "Knowledge infrastructure enables your agent to access and reason over large bodies of internal data.",
        "L7": "Human interface tooling improves how your team interacts with agents (voice, UI, computer use).",
    }
    return whys.get(layer, f"Relevant at stage {profile.maturity_stage}.")
