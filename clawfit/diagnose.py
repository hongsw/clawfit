"""
Interactive org-fit diagnosis CLI.

Asks a series of questions, builds an OrgProfile, and returns a
layered tool-stack recommendation for the organization.
"""

from __future__ import annotations

import json
import pathlib
import sys
from dataclasses import asdict
from typing import Any, Dict, List, Optional


def _load_questions() -> List[Dict[str, Any]]:
    path = pathlib.Path(__file__).parent.parent / "data" / "org_questions.json"
    with open(path) as f:
        return json.load(f)["questions"]


def _ask(question: Dict[str, Any], answers: Dict[str, str]) -> str:
    """Prompt user for one question and return the chosen option value."""
    print(f"\n{'─' * 60}")
    print(f"[{question['phase'].upper()}] {question['text']}")
    opts = question["options"]
    for i, opt in enumerate(opts, 1):
        print(f"  {i}. {opt['label']}")

    while True:
        raw = input("Choose (1-{}): ".format(len(opts))).strip()
        if raw.isdigit():
            idx = int(raw) - 1
            if 0 <= idx < len(opts):
                return opts[idx]["value"]
        print(f"  Please enter a number between 1 and {len(opts)}.")


def run_diagnosis(
    answers: Optional[Dict[str, str]] = None,
    interactive: bool = True,
    top_per_layer: int = 3,
) -> Dict[str, Any]:
    """
    Run the org-fit diagnosis.

    Parameters
    ----------
    answers
        Pre-filled answers dict {question_id: option_value}.
        If None and interactive=True, prompts the user.
    interactive
        Whether to prompt for missing answers interactively.
    top_per_layer
        Number of tool recommendations per layer.

    Returns
    -------
    dict
        OrgRecommendation serialized as a dict.
    """
    questions = _load_questions()
    filled: Dict[str, str] = dict(answers or {})

    if interactive:
        print("\n╔══════════════════════════════════════════════════╗")
        print("║   clawfit  —  Org-Fit Diagnosis                 ║")
        print("║   Answer 10 questions to get your tool stack.  ║")
        print("╚══════════════════════════════════════════════════╝")

        for q in questions:
            if q["id"] not in filled:
                filled[q["id"]] = _ask(q, filled)

    from .org_scorer import build_profile_from_answers, org_recommend

    profile = build_profile_from_answers(filled)
    result = org_recommend(profile, top_per_layer=top_per_layer)
    return asdict(result)


def print_recommendation(rec: Dict[str, Any]) -> None:
    """Pretty-print an OrgRecommendation dict to stdout."""
    print(f"\n{'═' * 60}")
    print(f"  Org-Fit Recommendation")
    print(f"  Maturity: Stage {rec['maturity_stage']} — {rec['maturity_label']}")
    print(f"{'═' * 60}")

    print("\n🔷 Your Tool Stack\n")
    for layer_entry in rec["stack"]:
        pri = layer_entry["priority"].upper()
        label = layer_entry["layer_label"]
        layer = layer_entry["layer"]
        why = layer_entry["why"]
        print(f"  [{pri}] {layer} — {label}")
        print(f"    Why: {why}")
        print(f"    Tools:")
        for t in layer_entry["tools"]:
            score_pct = int(t["score"] * 100)
            print(f"      • {t['name']:<30s} score={score_pct:3d}%  {t['url']}")
        print()

    print("🔶 Core Agent + LLM Fit\n")
    for fit in rec["core_agent_fit"]:
        print(f"  {fit.get('agent','?')} + {fit.get('llm','?')} + {fit.get('hardware','?')}")
        score_pct = int(fit.get("fit_score", 0) * 100)
        print(f"    Fit score : {score_pct}%")
        if fit.get("maturity_note"):
            print(f"    Stage fit : {fit['maturity_note']}")
        for w in fit.get("why", []):
            print(f"    ✓ {w}")
        print()

    print("📌 Next Step\n")
    print(f"  {rec['next_step_hint']}")
    print()


def main(argv=None) -> None:
    import argparse

    parser = argparse.ArgumentParser(
        prog="clawfit diagnose",
        description="Interactive org-fit questionnaire and tool-stack recommendation",
    )
    parser.add_argument(
        "--answers",
        metavar="JSON",
        default=None,
        help='Pre-filled answers as JSON string, e.g. \'{"team_size":"solo","primary_task":"code-gen"}\'',
    )
    parser.add_argument(
        "--top", type=int, default=3, help="Tools to show per layer (default 3)"
    )
    parser.add_argument(
        "--json", action="store_true", dest="output_json",
        help="Output raw JSON instead of formatted text",
    )
    args = parser.parse_args(argv)

    prefilled = json.loads(args.answers) if args.answers else None
    interactive = prefilled is None or len(prefilled) < 10

    result = run_diagnosis(answers=prefilled, interactive=interactive, top_per_layer=args.top)

    if args.output_json:
        print(json.dumps(result, indent=2))
    else:
        print_recommendation(result)
