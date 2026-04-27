# Research Watch: trycua/cua — Open-Source Computer-Use Agent Infrastructure

- Repo/Link: https://github.com/trycua/cua
- Source: GitHub Trending (182 stars/day today)

## Why this is worth watching
trycua/cua provides open-source sandboxes and SDKs explicitly designed for computer-use agents — giving the ecosystem an independent, non-proprietary alternative to Anthropic's first-party Computer Use implementation. As CUA moves from demo to production use, infrastructure for sandboxed agent execution becomes a prerequisite for any org that needs reproducibility, security isolation, or offline capability.

## What stands out immediately
- Full CUA infrastructure stack: sandboxes + SDKs + training tooling in one repo
- Distinct positioning from Claude Computer Use: open-source, provider-agnostic
- SDKs suggest it targets agent *developers*, not just end-users
- "Training AI agents" framing implies gym-style environments, not just deployment sandboxes
- Language: HTML-heavy (possibly rich documentation or UI components)
- Trending with 182 stars/day — sustained interest signal

## Why clawfit should care
This fills a gap between Level 1 base runtimes (Claude Computer Use, understudy) and the Level 4c tool infrastructure layer. A purpose-built open-source CUA sandbox could be the backbone for orgs with `data_sensitivity: confidential` who want computer-use capabilities without routing desktop actions through Anthropic's cloud. Relevant to any profile where computer-use is the task modality rather than text/code output.

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool-use / action infrastructure (open-source CUA sandbox and SDK layer)**
- Possible Level 1 entry if SDK provides a standalone base runtime, not just infrastructure

## Status
- Tracking: new entry, medium-high signal. 182 stars/day puts it in same momentum band as browser-harness (77 HN pts) and libretto (80 HN pts) at time of initial tracking. Revisit at 5k total stars for registry entry consideration.
