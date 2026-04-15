# Research Watch: virattt/ai-hedge-fund — Domain-Specialized Multi-Agent System

- Repo/Link: https://github.com/virattt/ai-hedge-fund
- Source: GitHub Trending

## Why this is worth watching
54.1k stars (9.4k forks) for an educational multi-agent system built around 19 specialized agents modeling famous investor personas (Buffett, Munger, Lynch, Wood, Burry, etc.) plus analytical agents for valuation, sentiment, fundamentals, technicals, risk management, and portfolio management. It is not a reusable framework but a concrete domain application — the first high-signal example of a domain-specialized multi-agent application in the finance/research space crossing mainstream adoption in this taxonomy.

## What stands out immediately
- **19 specialized agents** with distinct roles; demonstrates how persona-based division of labor scales to complex analytical tasks
- **Multi-LLM support**: OpenAI, Anthropic, Groq, DeepSeek, Ollama (local) — configurable per agent or globally
- Web UI + CLI interfaces; Python backend, TypeScript frontend
- Explicitly educational: no live trading; safe for demonstration and study
- 9.4k forks suggests active adaptation/remixing for other domains

## Why clawfit should care
The multi-LLM support pattern (different models for different agents in a single workflow) is becoming structurally significant — it's what the `advisor_strategy` pattern (Opus + Sonnet pairing) generalizes to. The finance domain application demonstrates that clawfit's `research` and `data-analysis` task labels are increasingly relevant beyond software development contexts. The 19-agent persona decomposition also validates that `role` in org_fit should encompass analyst/researcher personas, not just developer/exec.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base runtimes** (standalone multi-agent application with its own orchestration)
- Domain: finance/research; taxonomy entry for non-coding domain-specialized agents

## Status
- Tracking as domain-specialized multi-agent pattern; 54k stars signals mainstream; not adding to registry (too domain-specific to score generically)
