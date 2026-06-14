# Research Watch: apple/container — Lightweight VM Container Runtime for Agent Isolation on Mac

- Repo/Link: https://github.com/apple/container
- Source: GitHub Trending (1,487 stars today, 36,273 total)

## Why this is worth watching
Apple open-sourced a Swift tool for creating and running Linux containers via lightweight virtual machines on Mac, optimized for Apple silicon. Unlike Docker Desktop (which runs a full Linux VM with a shared kernel), apple/container spawns one VM per container, providing hypervisor-level isolation. This is structurally significant for agent execution: an AI coding agent running in a per-VM container cannot escape to the host filesystem or network by default, eliminating a class of containment failures that affect Docker-level isolation.

## What stands out immediately
- One VM per container — hypervisor isolation rather than shared-kernel namespace isolation
- Optimized for Apple silicon (M-series); leverages Virtualization.framework
- Swift implementation; official Apple open-source release (not a third-party tool)
- 36.3k stars at launch; 1,487 today — highest single-day star velocity in this scan
- Directly comparable to lima (Lima: Linux on Mac), which is already used by Goose for its sandbox mode

## Why clawfit should care
This is a **hardware-axis signal** for the Mac execution environment. Current clawfit hardware entries treat `hardware: mac_local` as a monolithic category. apple/container introduces a meaningful distinction: agents running inside apple/container VMs have a qualitatively different isolation model from agents running in Docker, Devcontainers, or bare processes on Mac. This is relevant for `data_sensitivity: confidential` and `governance_need: hard` profiles where containment guarantees matter. It also directly impacts Goose's Mac-local deployment story (Goose uses Lima for sandboxing; apple/container is a first-party Apple alternative to Lima).

## Preliminary interpretation
Current best reading:
- **Hardware/infrastructure axis annotation** — Mac-local isolation layer, not a standalone Level 1–7 tool
- Relevant to the `hardware-deployment-axis.md` reference note as a new Mac isolation primitive

## Status
- 36.3k stars exceeds threshold, but this is not an agent tool — it is execution infrastructure
- No registry entry warranted (not a tool a developer selects via clawfit's recommend flow)
- Map mutation deferred: add as an annotation to `docs/reference-notes/hardware-deployment-axis.md` when Mac isolation distinctions become a clawfit scoring axis
- Monitor: Goose, OpenHands, or any L1 agent adopting apple/container as their default sandbox on Mac
