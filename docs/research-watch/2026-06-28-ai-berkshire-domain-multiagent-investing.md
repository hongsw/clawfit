# Research Watch: ai-berkshire — Claude Code Multi-Agent Value Investing Framework

- Repo/Link: https://github.com/xbtlin/ai-berkshire
- Source: GitHub Trending

## Why this is worth watching
A domain-specific multi-agent harness for value investing that uses Claude Code as the execution substrate. At 4,091★ with +685 in a single day it is the fastest-rising agent harness with a financial domain focus seen in recent scans. It signals the "vibe trading" pattern (tracked 2026-05-09 for TradingAgents) maturing into the Claude Code harness format.

## What stands out immediately
- Explicitly built on Claude Code as the base harness (not LangChain/AutoGPT)
- Multi-agent decomposition: separate sub-agents for macro, fundamental, and technical analysis
- Positioned as "Berkshire Hathaway style" analysis — long-term value investing lens over day trading
- +685 today suggests a social-media trigger (likely a high-profile tweet or newsletter)
- No enterprise governance or offline mode; cloud/online assumption throughout

## Why clawfit should care
Confirms the pattern that coding-agent harnesses are spawning domain clones (finance, legal, biotech). The task profile (`research`, `data-analysis`) and role profile (`exec`, `researcher`) differ from the typical `code-gen` / `developer` pair that dominates the registry. A registry entry would represent the first finance-domain harness with Claude Code provenance (distinct from TradingAgents which is LangChain-based).

## Preliminary interpretation
Current best reading:
- **Level 2 primary — agent harness / orchestration framework** (multi-agent orchestration over financial data sources with role-specialized sub-agents)
- **Level 4c secondary — tool integration** (market data APIs, financial statement fetchers as action surfaces)

## Status
- First signal. 4,091★. GitHub Trending (all languages). Held pending second independent signal.
- Promotion criterion: 8k★ OR a second Claude Code-native multi-agent financial analysis harness.
- Registry candidate: `tasks: [research, data-analysis]`, `roles: [exec, researcher]`, `network: online`, `setup_complexity: medium`, `latency: high`.
