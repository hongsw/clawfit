# Research Watch: Pu.sh — Full Coding-Agent Harness in 400 Lines of Shell

- Repo/Link: https://pu.dev
- Source: Hacker News (Show HN, 59 points, 16 comments)

## Why this is worth watching
Pu.sh is a complete coding-agent harness implemented in approximately 400 lines of shell script. The "400 lines" framing deliberately echoes mini-swe-agent (100-line minimal coding agent, 2026-04-27) — both are explicit counter-statements to the "batteries-included" harness trend. A usable harness in 400 lines means the core harness loop (prompt → tool call → observe → loop) has minimal irreducible complexity, which is a useful calibration anchor for evaluating heavier frameworks.

## What stands out immediately
- 400-line single-file shell implementation — auditable, forkable, zero dependencies
- "Full harness" claim implies the loop is complete, not a toy demo
- Shell provenance: no Node/Python runtime requirement; runs anywhere bash runs
- HN traction (59 pts) confirms practitioner interest in minimal harness alternatives

## Why clawfit should care
This is a second "minimal harness" signal in five days (mini-swe-agent + Pu.sh). If the minimal-harness pattern reaches a third data point, it qualifies as a confirmed sub-type at Level 2 alongside heavyweight harnesses (LangGraph, DureClaw) and methodology harnesses (obra/superpowers). For `offline_mid_codegen` and `solo_dev_codegen` profiles prioritizing low setup complexity, a shell-only harness has near-zero onboarding cost. Current `setup_complexity: low` harnesses in the registry could reference this as the minimal-viable baseline.

## Preliminary interpretation
Current best reading:
- **Level 2 — Minimal harness sub-type** — complete loop implementation; contrasts with Level 3 methodology harnesses and Level 2 heavyweight orchestration systems

## Status
- Early signal (59 HN pts). Tracking. Revisit when GitHub star count is available.
