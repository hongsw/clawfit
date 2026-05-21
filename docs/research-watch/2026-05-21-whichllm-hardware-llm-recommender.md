# Research Watch: whichllm — Hardware-Based LLM Recommender CLI

- Repo/Link: https://github.com/Andyyyy64/whichllm
- Source: GeekNews front page

## Why this is worth watching

whichllm is a Python CLI that auto-detects local hardware (NVIDIA, AMD, Apple Silicon, CPU-only) and recommends the best-performing open-weight LLMs that will actually run, ranked by merged benchmark data (LiveBench, Artificial Analysis, Chatbot Arena) rather than raw parameter count. It uses evidence-graded benchmark tagging (direct match, variant, interpolated, self-reported) and accounts for VRAM consumption including weights, KV cache, activations, and overhead.

## What stands out immediately

- Hardware autodetection: NVIDIA/AMD/Apple Silicon/CPU-only paths
- Benchmark-first ranking: recency-aware dampening on frozen leaderboards, direct source merging
- Evidence confidence grades on each benchmark data point — unusual methodological transparency
- 1.6k★, MIT, Python 100% — below the 5k registry threshold
- Directly solves the same problem as clawfit's hardware + LLM dimension, but for local-first open-weight model selection rather than agent-stack recommendation

## Why clawfit should care

whichllm is a **direct functional analog to clawfit's local LLM selection layer** — it answers "given this hardware, which open-weight LLM should I run?" which is a sub-problem of clawfit's (agent, LLM, hardware) triple recommendation. Two design decisions are worth examining for clawfit: (1) evidence grading — confidence tiers on each benchmark data point, not just a single score; (2) hardware consumption decomposition — VRAM estimate splits weights, KV cache, activations, and overhead separately. Neither pattern currently exists in clawfit's `hardware.json` or `scoring.py`. If clawfit expands into local LLM hardware-fit scoring, whichllm's methodology is the first articulation of this approach in open source.

## Preliminary interpretation

Current best reading:
- Not an ecosystem layer entry — this is a **clawfit-class tool** for the LLM × hardware sub-domain
- No L1–L7 classification applicable; closest analogy is the inference-runtime-substrate companion axis

## Status

- 1.6k★, MIT — below threshold; not a registry candidate
- Flagged as methodology signal: evidence grading + VRAM decomposition are candidate design patterns for clawfit's hardware scoring axis
- Revisit if crosses 5k★ or if clawfit adds a hardware-fit sub-scorer
