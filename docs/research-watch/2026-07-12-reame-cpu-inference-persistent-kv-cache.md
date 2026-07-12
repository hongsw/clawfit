# Research Watch: Reame

- Repo/Link: https://github.com/swellweb/reame
- Source: Hacker News

## Why this is worth watching
Reame is an llama.cpp-based inference server with a distinctive property: it gets faster with each request rather than resetting state. It persists KV-cache prefixes to disk (zstd-compressed), maintains an on-disk n-gram archive fed by every completed generation, and uses grammar-based speculation to propose tokens for free on novel content. The result is that free-tier cloud vCPUs and ARM edge devices become viable long-term inference hosts — cost collapses as the cache warms.

## What stands out immediately
- Persistent shared-prefix KV cache: system prompts are paid for once, reused forever
- Palimpsest archive: completed generations contribute n-grams to future speculation at zero cost
- Self-regulating speculative decoding: draft model or n-gram lookup, automatically selected
- Targets shared vCPUs and free cloud tiers — the lowest-end hardware segment
- Philosophy: "never compute the same thing twice"

## Why clawfit should care
This is a strong signal for the `network=offline` + `monthly_budget=low` profile. The `offline_mid_codegen` scorer already surfaces ATLAS and ZeroClaw; Reame fits the same niche but with a different angle — it doesn't require expensive GPU hardware, only persistence across sessions. A future `hardware.json` entry for "CPU-only inference host" would need a Reame-style tag. The cost curve inversion (gets cheaper over time) is unlike any current registry entry.

## Preliminary interpretation
Current best reading:
- **Level 5 — Hardware / Execution Layer** (CPU-optimized inference runtime with persistent state)

## Status
- Tracking; high potential for `budget=low` / `network=offline` hardware dimension
