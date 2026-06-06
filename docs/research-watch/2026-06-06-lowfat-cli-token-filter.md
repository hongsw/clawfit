# Research Watch: Lowfat — Pluggable CLI Token Filter

- Repo/Link: https://github.com/zdk/lowfat
- Source: Hacker News (Show HN)
- Stars: Unknown (Show HN, no star count in source)

## Why this is worth watching
Lowfat is a CLI-level pluggable filter that intercepts stdin/stdout pipes to reduce token volume before content reaches an LLM — claims 91.8% token reduction in the author's workflow. Unlike Headroom (which is a Python/TypeScript library that deploys as a proxy or MCP server and uses ML-based compression), Lowfat operates as a Unix pipe filter with no language SDK dependency. The architectural layer is different: Headroom is middleware inside an agent pipeline; Lowfat is a shell-level composition primitive.

## What stands out immediately
- `91.8% token savings` claimed on the author's own workflow — not a cross-benchmark figure
- CLI pipe-based: `cat file.txt | lowfat | llm` — no SDK, no Python, no config
- "Pluggable" design: custom rules/filters loadable per project
- Very low installation friction (single binary if distributed as such)
- HN Show HN format: community project, star count unknown at scan time
- Architecturally distinct from Headroom: operates at the shell layer, not the agent SDK layer

## Why clawfit should care
A second signal (after Headroom) for token-volume reduction as a first-class pipeline concern. The shell-level approach is more accessible for non-Python/TS stacks and may be more relevant for the `offline_mid_codegen` profile where developers pipe tool outputs to their agent. The different architectural layer (CLI pipe vs. library/proxy) confirms this is becoming a named sub-category at L5 rather than a single-tool phenomenon. However, the unverified benchmark claim (single-workflow result, no cross-tool replication) warrants caution.

## Preliminary interpretation
Current best reading:
- **Level 5 — Context-compression sub-type (CLI-pipe variant)**: operates between tool output and LLM surface, compressing content before it reaches the model. Different deployment model from Headroom (ML model + proxy) but same functional layer.

## Status
- **Early watch — no map mutation**: no confirmed star count; benchmark is single-workflow result; functional verification needed (does it install cleanly? does it handle binary/structured output correctly?). Second L5 context-compression signal confirms sub-type status for Headroom. Revisit if GitHub star count crosses 2k or HN thread shows independent replication of the token savings claim.
