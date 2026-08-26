# Research Watch: Macchiato — iPhone Remote Control for Local Agents

- Repo/Link: https://macchiato.chat
- Source: GeekNews (Show GN)

## Why this is worth watching
Local coding agents (Claude Code, Goose, Aider) are increasingly powerful but require a desktop session to operate. Macchiato extends that session to the iPhone — letting users submit commands, review outputs, and approve actions remotely without opening a laptop. This is an emerging L6 human interface pattern: the desktop remains the executor, the mobile becomes the controller.

## What stands out immediately
- Bridges the gap between local agent execution and mobile approval workflows
- Remote control paradigm: agent runs locally on the user's machine, app relays commands over the local network or secure tunnel
- Positions as an "agentic remote" rather than a full mobile client — thin UI, not an agent runtime itself
- Addresses a real friction point: leaving a long-running agent task unattended at the desk

## Why clawfit should care
Represents a new L6 interface sub-type: **mobile remote control** distinct from (a) native mobile agents and (b) cloud agent dashboards. If mobile remote control becomes a standard harness feature, clawfit may need an `interface_modes: [desktop | mobile-native | mobile-remote | web]` axis to distinguish deployment patterns for governance-sensitive orgs where remote approval matters.

## Preliminary interpretation
Current best reading:
- **Level 6 — Human Interface Layer** (mobile remote approval surface)
- Secondary: Level 2 (acts as a thin client wrapper over any local agent runtime)

## Status
- First-signal; below 1,000-star threshold — tracking for follow-up if adoption reported by major harness maintainers
