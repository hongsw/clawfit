# Research Watch: Unreal Agent — Async Tool Management Harness

- Repo/Link: https://github.com/unreallabsai/unreal-agent
- Source: Hacker News (115 points, 68 comments)

## Why this is worth watching
Unreal Agent targets a specific production waste pattern: agents burn tokens waiting for tool calls to complete. By decoupling tool dispatch from model invocation — firing calls as in-progress and resuming once results arrive — it claims 40% cost reduction on GPT-6 Astra benchmark runs vs Codex, without performance regression. Sequoia + First Round backed, with founders from CERN, Meta, Snap, DeepMind.

## What stands out immediately
- **Async tool management**: model issues tool call, moves on; results appended when ready; no token burn on waiting
- **Benchmark results on three evals**: Terminal-Bench 4.0 (57.9% at $1,428), SWE-Atlas Codebase QnA (65.8% at $936), DeepSWE 1.1 (72.4% at $1,367) — cost numbers are meaningful for production cost comparisons
- **Open-source** (GitHub: unreallabsai/unreal-agent), Apache-style license
- **Critique of existing SDKs**: "carry assumptions unsuitable for production environments" — positions itself against LangChain/Codex SDK maintenance overhead

## Why clawfit should care
This is a direct L2 competitor entry with a concrete cost claim and benchmark evidence — rare in the harness category. The async tool dispatch pattern could be registered as a `feature` attribute distinguishing it from synchronous-loop harnesses (AutoGen, CrewAI, Codex). If the cost-savings claim holds across LLMs, it strengthens the case for a `tool_parallelism` scoring dimension that clawfit currently lacks.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / SDK layer** (primary)

## Status
- New signal (2026-09-23): first research-watch doc; 115 HN points, VC-backed open-source; above monitoring threshold; registry candidate — needs confirmed star count and license verification before adding
