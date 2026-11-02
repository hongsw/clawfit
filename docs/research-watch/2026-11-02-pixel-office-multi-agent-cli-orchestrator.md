# Research Watch: Pixel Office — Multi-Agent CLI Orchestration Desktop App

- Repo/Link: https://news.hada.io/topic?id=36418
- Source: GeekNews

## Why this is worth watching
Pixel Office is a desktop application that assigns roles to multiple subscription AI CLIs (e.g., Claude Code, Cursor, Gemini CLI) and visualises their concurrent work as characters in a pixel-art office. It treats each AI CLI subscription as an "employee" with a defined task role, coordinating them from a single orchestration layer. This is one of the earliest consumer-facing attempts to make multi-agent CLI orchestration visually intuitive.

## What stands out immediately
- Assigns explicit roles (e.g., "backend dev", "reviewer", "tester") to separate AI CLI processes
- Progress visible in a shared pixel-art workspace UI
- Targets users who already hold multiple AI CLI subscriptions — no new model required
- Purely a coordination/UX layer on top of existing tools like Claude Code and Gemini CLI
- Desktop-native; no SaaS backend implied

## Why clawfit should care
This is a signal that multi-agent CLI orchestration is becoming a consumer workflow, not just a DevOps concern. It sits at **Level 3 / Orchestration**, bridging individual coding agents (Level 2) into a coordinated team workflow. For clawfit's scoring, it reinforces the `multi_agent` usage tier and suggests a `team_size: small–mid` fit for developers who want parallelism without enterprise tooling.

## Preliminary interpretation
Current best reading:
- **Level 3 — Orchestration / Harness Composition** (composes multiple Level 2 coding CLIs into coordinated roles)

## Status
- Early-stage signal; no GitHub repo found yet — watch for open-source release
