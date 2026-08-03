# Research Watch: NixOS-DGX-Spark — Reproducible Local AI on NVIDIA DGX Spark

- Repo/Link: https://github.com/graham33/nixos-dgx-spark
- Source: Hacker News (Show HN, 88 points)

## Why this is worth watching
NixOS running on the NVIDIA DGX Spark (GB10 Grace Blackwell Superchip, ~1 PFLOP, ~$3,000) enables fully reproducible, declarative local AI deployments. NixOS's configuration-as-code model means the entire host OS, driver stack, and inference tooling can be pinned in a flake.nix — no configuration drift across machines or deploys. For teams requiring confidential AI (data never leaves premise) with infrastructure-as-code discipline, this is a new viable path.

## What stands out immediately
- DGX Spark is distinct from RTX Spark (tracked 2026-06-02) — Grace Blackwell vs. consumer desktop GPU; ~1 PFLOP unified memory vs. gaming-class VRAM
- NixOS integration means agent sandboxes and inference runtimes can be reproduced deterministically from source
- 88 HN points is meaningful community signal for a narrow hardware+OS combination
- Addresses the `governance_need: hard` + `network: offline` segment with enterprise-class local compute

## Why clawfit should care
The hardware layer (L6) currently tracks NVIDIA RTX Spark, AMD Ryzen AI Halo, and Apple Silicon in the `hardware.json` registry. DGX Spark is a new tier: above consumer-desktop (RTX Spark) and below cluster-scale. If teams start deploying DGX Sparks with NixOS for air-gapped agentic workflows, clawfit needs a "grace-blackwell-desktop" hardware entry with appropriate pricing and PFLOP spec. The NixOS angle also opens a `deployment_model: nix-reproducible` attribute not currently modeled.

## Preliminary interpretation
Current best reading:
- **Level 6 — Local hardware substrate, Grace Blackwell desktop tier**
- Secondary: cross-cutting governance signal (offline + reproducible infra)

## Status
- First signal for DGX Spark + NixOS combination. Hardware hardware.json entry pending until verified pricing and availability are stable. No registry entry today.
