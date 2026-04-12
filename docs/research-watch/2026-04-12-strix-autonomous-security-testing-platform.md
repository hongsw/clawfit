# Research Watch: Strix — Autonomous AI Security Testing Platform

- Repo/Link: https://github.com/usestrix/strix
- Source: GeekNews (26 points)

## Why this is worth watching
Strix is an open-source multi-agent security testing platform with 23k+ stars that validates vulnerabilities through actual proof-of-concept execution, not just static analysis. This differentiates it from traditional SAST tools and from Shannon (KeygraphHQ), which focuses on attack-surface identification. Strix positions as a developer-facing CI/CD security layer — closer to a testing harness than a pentesting agent.

## What stands out immediately
- "Teams of agents that collaborate and scale" — multi-agent architecture for security assessment
- Dynamic execution in sandboxed environments + PoC validation reduces false positives
- HTTP proxy analysis, browser automation, terminal access, code analysis, reconnaissance — broad surface coverage
- CI/CD integration pattern: runs on pull requests via GitHub Actions
- Python (91.6%); installable via `pip install strix-agent`
- PyPI package availability signals ecosystem-friendly distribution

## Why clawfit should care
Shannon is already tracked as a domain-specialized pentester. Strix occupies adjacent space but with a distinct deployment model: developer self-service CI/CD integration vs. expert pentester workflow. The two tools are not substitutes — Strix is the "shift-left security testing" variant. As the `security-testing` task type discussion noted (reference-levels.md), `qa` is too broad for security agents; Strix further reinforces this gap in the current task taxonomy. Registry entry warranted as a Level 1 domain-specialized agent alongside Shannon.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base runtime**, domain-specialized for security (parallel to Shannon, distinct deployment model)

## Status
- New entry, 23k+ stars. Add to registry alongside Shannon. Evaluate whether a distinct `security-testing` task type is needed in the scoring system.
