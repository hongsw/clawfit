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


def _cmd_tui(args: argparse.Namespace) -> None:
    from .tui import run_tui
    from .diagnose import print_recommendation
    result = run_tui()
    if result and not args.quiet:
        print_recommendation(result)


def _cmd_serve(args: argparse.Namespace) -> None:
    from .server import serve
    serve(port=args.port, open_browser=not args.no_browser)


def _cmd_diagnose(args: argparse.Namespace) -> None:
    import json as _json
    from .diagnose import run_diagnosis, print_recommendation

    prefilled = _json.loads(args.answers) if args.answers else None
    interactive = prefilled is None or len(prefilled) < 10

    result = run_diagnosis(answers=prefilled, interactive=interactive, top_per_layer=args.top)

    if args.output_json:
        print(_json.dumps(result, indent=2))
    else:
        print_recommendation(result)


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

    # tui
    tui_p = sub.add_parser("tui", help="Interactive TUI questionnaire with live results")
    tui_p.add_argument("--quiet", action="store_true", help="Don't print summary after exit")
    tui_p.set_defaults(func=_cmd_tui)

    # serve
    srv = sub.add_parser("serve", help="Launch web UI with live results (localhost:7771)")
    srv.add_argument("--port", type=int, default=7771, help="Port (default 7771)")
    srv.add_argument("--no-browser", action="store_true", help="Don't open browser automatically")
    srv.set_defaults(func=_cmd_serve)

    # diagnose
    diag = sub.add_parser("diagnose", help="Interactive org-fit questionnaire → tool stack recommendation")
    diag.add_argument(
        "--answers", metavar="JSON", default=None,
        help='Pre-filled answers as JSON, e.g. \'{"team_size":"solo","primary_task":"code-gen"}\'',
    )
    diag.add_argument("--top", type=int, default=3, help="Tools per layer (default 3)")
    diag.add_argument("--json", action="store_true", dest="output_json", help="Output raw JSON")
    diag.set_defaults(func=_cmd_diagnose)

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
