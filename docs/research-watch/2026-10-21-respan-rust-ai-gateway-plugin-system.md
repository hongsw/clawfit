# Research Watch: Respan (YC W24)

- Repo/Link: https://github.com/respan-ai/respan (YC W24)
- Source: Hacker News (41 points, 16 comments)

## Why this is worth watching
An open-source AI gateway written in Rust, designed around a plugin architecture. Unlike Python-based gateways (LiteLLM, OpenRouter), Respan targets high-performance, low-latency proxy routing with extensibility through plugins. YC W24 backing indicates commercial traction.

## What stands out immediately
- Rust implementation: lower latency, lower memory overhead than Python gateways
- Plugin-first architecture: routers, transformers, and auth layers as plugins
- Open source with commercial backing (YC W24)
- Competes with LiteLLM proxy, Kong AI Gateway, and similar tools

## Why clawfit should care
Respan sits at the LLM gateway layer — a level between raw API access and agent harnesses. Relevant for organizations needing self-hosted, high-performance LLM routing with governance controls. Could serve as infrastructure recommendation for `governance_need: hard` profiles in clawfit.

## Preliminary interpretation
Current best reading:
- **Level 3 — LLM Gateway / Router**

## Status
- Tracking: Rust-native AI gateway, plugin-based routing, self-hosted governance use case
