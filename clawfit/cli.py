"""CLI entry point for clawfit."""

from __future__ import annotations

import argparse
import json
import sys

from . import __version__


def _cmd_recommend(args: argparse.Namespace) -> None:
    from .recommend import recommend

    results = recommend(
        task=args.task,
        latency=args.latency,
        budget=args.budget,
        hardware=args.hardware,
        network=args.network,
        statefulness=args.statefulness,
        maturity_stage=args.maturity,
        top_n=args.top,
    )
    print(json.dumps(results, indent=2))


def _cmd_list(args: argparse.Namespace) -> None:
    from .loader import load_agents, load_llms, load_hardware

    loaders = {
        "agents": load_agents,
        "llms": load_llms,
        "hardware": load_hardware,
    }
    items = loaders[args.registry]()
    for item in items:
        print(f"  {item.id:24s} {item.name}")


def _cmd_profile(args: argparse.Namespace) -> None:
    from .loader import load_agents, load_llms, load_hardware

    agents = load_agents()
    llms = load_llms()
    hw = load_hardware()
    tasks = sorted({t for a in agents for t in a.tasks})
    print(f"clawfit v{__version__}")
    print(f"  Agents   : {len(agents)}")
    print(f"  LLMs     : {len(llms)}")
    print(f"  Hardware : {len(hw)}")
    print(f"  Tasks    : {', '.join(tasks)}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="clawfit",
        description="AI agent + LLM + hardware recommendation engine",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command")

    # recommend
    rec = sub.add_parser("recommend", help="Get a recommendation")
    rec.add_argument("--task", required=True, help="Task category (e.g. qa, research, code-gen)")
    rec.add_argument("--latency", default="medium", choices=["low", "medium", "high"])
    rec.add_argument("--budget", type=float, default=None, help="Max cost per 1k tokens")
    rec.add_argument("--hardware", default=None, choices=["cloud", "edge", "on-prem"])
    rec.add_argument("--network", default=None, choices=["online", "offline"])
    rec.add_argument("--statefulness", default=None, choices=["stateless", "session", "persistent"])
    rec.add_argument("--top", type=int, default=3, help="Number of results (default 3)")
    rec.add_argument(
        "--maturity", type=int, default=None, choices=range(1, 12),
        metavar="1-11",
        help="User maturity stage (1=chatbot user → 11=frontier researcher). "
             "Filters and weights agents by fit for that stage.",
    )
    rec.set_defaults(func=_cmd_recommend)

    # list
    ls = sub.add_parser("list", help="List registry entries")
    ls.add_argument("registry", choices=["agents", "llms", "hardware"])
    ls.set_defaults(func=_cmd_list)

    # profile
    prof = sub.add_parser("profile", help="Show registry summary")
    prof.set_defaults(func=_cmd_profile)

    return parser


def main(argv=None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == "__main__":
    main()
