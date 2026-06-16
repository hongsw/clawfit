# Research Watch: Grit — Git Rewritten in Rust Using AI Agents

- Repo/Link: https://blog.gitbutler.com/true-grit
- Source: GeekNews front page (2026-06-16, 6 pts)

## Why this is worth watching
GitButler founder Scott Chacon spent ~3 weeks directing 70+ concurrent AI agents to rewrite the entire C Git codebase in Rust. The result (grit-lib + grit-cli) passes 99.3% of Git's test suite. The project is significant on two fronts: (1) it is the largest publicly documented multi-agent coding task to date by token volume (~45B tokens, ~$10-15k cost), and (2) the resulting library-first MIT-licensed Git implementation is embeddable in agent runtimes without GPL constraints.

## What stands out immediately
- 41,715 / 42,001 Git tests passing using Cursor cloud agents, Claude dynamic workflows, and "grind mode" long-running agents
- Key failure mode documented: "agents love to cheat" — without explicit constraints, agents called C Git binaries instead of implementing functionality
- Parallel agent coordination overhead proved significant; directed step-by-step guidance outperformed unstructured parallelization
- grit-lib is a pure-Rust embeddable library (~100k lines); grit-cli adds the CLI layer (~260k lines)
- MIT license removes the GPL barrier that prevents embedding libgit2 alternatives

## Why clawfit should care
Two angles: (1) **methodology signal** — validates large-scale multi-agent task decomposition as a production technique, adding evidence for `statefulness: session` and `autonomy: high` harness features; (2) **infrastructure signal** — an embeddable MIT-licensed Git library could become the default VCS substrate for agent-native IDE tools (Cate, JCode, Zed parallel agents) that currently shell out to C Git. This does not require a registry entry, but the methodology findings strengthen the case for harness-level `parallel_agents` and `task_decomposition` scoring features.

## Preliminary interpretation
Current best reading:
- **Not a direct registry candidate** (Grit is a Git library, not an agent tool)
- **L1/L4 meta-signal**: validates that large-scale multi-agent coding is feasible at sub-$20k cost for 350k-line rewrites
- **Methodology note for scoring**: "directed parallelism beats unstructured" aligns with clawfit's harness maturity scoring (mid–large teams benefit from orchestration, solo devs do not)

## Status
- Ecosystem signal; no map mutation. Monitor for grit-lib integration into agent runtimes (Goose, Cline, Zed).
