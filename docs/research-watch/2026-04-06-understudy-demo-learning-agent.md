---
# Research Watch: understudy — local desktop agent that learns from demonstration

- Repo: <https://github.com/understudy-ai/understudy>

## Why this is worth watching
understudy inverts the typical agent interaction model: instead of the user writing prompts or config, **the user demonstrates the task once and the agent infers intent**. It controls GUI, browser, shell, and filesystem — a true local desktop agent. This "learn by showing" pattern is rare in the current harness ecosystem, which is dominated by prompt-based specification.

## What stands out immediately
- **Demonstration-based learning:** show once → agent repeats
- **Local-first:** runs entirely on-device, no cloud dependency
- **Cross-surface control:** GUI + browser + shell + filesystem simultaneously
- **No workflow builder required** — the demo IS the workflow definition
- Positions itself against traditional RPA (Robotic Process Automation) tools

## Why clawfit should care
understudy fits an unusual position in clawfit's taxonomy:
- **Level 1** (base runtime — it is the primary agent surface for desktop automation)
- **Level 6** (human interface — learns from human demonstration, not text prompts)
- **Statefulness:** `persistent` (learns and retains demonstrated workflows)
- **Network:** `offline` (local-first)

This is the closest thing to an **offline, demonstration-trained personal automation agent** in the current registry. Could be a candidate for clawfit's agent registry once mature.

## Preliminary interpretation
- Primary: **Level 1 — Base runtimes / primary agent surfaces** (desktop automation variant)
- Secondary: **Level 6 — Human interface** (demonstration as the input modality)

## Status
- Medium priority. Novel input modality (demonstration vs. prompt) worth watching.
- Registry candidate for `agents.json` once task coverage is clearer.
