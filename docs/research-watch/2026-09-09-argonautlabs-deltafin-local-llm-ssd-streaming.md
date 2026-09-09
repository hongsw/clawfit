# Research Watch: deltafin — Local LLM SSD-Streaming Inference

- Repo/Link: https://github.com/argonautlabsai/deltafin
- Source: Hacker News (195 pts)

## Why this is worth watching
deltafin runs Kimi K3 (2.8 trillion parameter model) at 1 token/second on a MacBook Pro by streaming weights from four SSDs rather than keeping them in RAM. This is a meaningful architectural breakthrough: it decouples model size from VRAM/RAM constraints, enabling enterprise-grade models to run fully offline on consumer hardware.

## What stands out immediately
- 2.8T parameter model on a laptop — no cloud, no GPU cluster
- Streams from 4 SSDs; ~1 tok/s is slow but usable for batch tasks
- Direct threat to the "large models require cloud" assumption in clawfit's current latency scoring
- Implies offline_mid_codegen profiles could soon access much larger models locally

## Why clawfit should care
clawfit's `latency` and `network` metadata for local hardware assumes a firm ceiling on local model size. SSD streaming breaks this ceiling. The `offline_mid_codegen` profile today scores ZeroClaw and Goose at the top; with deltafin-style inference, a new hardware tier ("local-ssd-cluster") would change recommendations substantially.

## Preliminary interpretation
Current best reading:
- **Level 6 — Infrastructure / Runtime Layer** (local inference substrate)

## Status
- New — high signal; warrants hardware registry entry discussion
