# Research Watch: cc-switch — Multi-CLI Provider Switcher for Claude Code, Codex, Gemini, OpenCode, OpenClaw

- Repo: https://github.com/farion1231/cc-switch
- Also see:
  - CLI fork: https://github.com/saladday/cc-switch-cli
  - Web fork: https://github.com/Laliet/CC-Switch-Web
  - Vendor write-up: https://www.newapi.ai/en/docs/apps/cc-switch
- Source: GitHub Trending Daily Rust (2026-04-28)

## Why this is worth watching
cc-switch is a Tauri 2 / Rust desktop app that unifies provider/config management across **five** distinct AI coding CLIs — Claude Code, Codex, Gemini CLI, OpenCode, and OpenClaw — with 52,802 stars total and roughly +892 stars in a single day. The velocity is significant on its own, but the more important signal is the explicit multi-CLI scope: cc-switch's existence and reception is evidence that "user runs more than one coding agent and actively switches between them" has crossed from edge case into mainstream workflow assumption.

## What stands out immediately
- **52,802★ total, +892 today** — among the strongest single-day deltas in the Claude Code adjacency this week
- **Five CLIs supported in one app**: Claude Code, Codex, Gemini CLI, OpenCode, OpenClaw — this is the broadest cross-CLI surface seen so far
- **50+ built-in provider presets**, including AWS Bedrock, NVIDIA NIM, and "community relay services" (i.e. third-party Anthropic-compatible gateways)
- **Local proxy** with hot-switching, auto-failover, and circuit breaker — this is infrastructure-grade reliability tooling for vendor swapping, not just a config picker
- **Unified MCP server management** with bidirectional sync across the five CLIs (claim to inspect — implementation depth matters)
- **Cross-app prompts and skills** management — treats prompts/skills as portable assets across vendors rather than per-CLI artifacts
- **Usage dashboard** tracking spend, requests, tokens across providers
- **38 releases / 1,601 commits / Tauri 2.8 + Rust + SQLite** stack — sustained development, not a flash repo
- Has spawned a CLI fork (cc-switch-cli) and a web fork (CC-Switch-Web), suggesting genuine demand across delivery surfaces

## Why clawfit should care
This is the third multi-vendor signal in roughly one week, and the pattern is now hard to ignore:
- **2026-04-28 morning**: cmux (15K★, multi-agent terminal orchestrator)
- **2026-04-28 morning**: Sub2API (16K★, multi-vendor subscription gateway)
- **2026-04-28 round 2**: cc-switch (52K★, multi-CLI provider switcher) — this doc

The meta-signal: users are actively *tooling around* vendor lock-in. They are not picking one CLI and committing — they are buying infrastructure (proxies, gateways, switchers) so they can move between Claude Code, Codex, and Gemini CLI per-task or per-session.

For clawfit's recommendation engine this has direct implications:
- **Cost weight (0.25)**: today's weighting assumes a stable cost frontier per LLM. If users routinely fail over between providers (Anthropic → Bedrock → community relay), the effective cost is the *frontier across providers*, not a single LLM's listed cost. The current single-cost model under-represents what cost-conscious users actually pay.
- **LLM preference weight (0.15)**: assumes preference is sticky. cc-switch's adoption suggests preference is increasingly *task-scoped* rather than user-scoped. A `--prefer-llm` flag may need a `--prefer-llm-for <task>` companion.
- **Vendor-portability as a fit dimension**: nothing in the current registry schema captures "this agent runs cleanly under a multi-CLI switcher." If multi-CLI usage is the new default for power users, agent recommendations should at minimum surface whether an agent has a clean configuration footprint for switchers like cc-switch.

cc-switch itself is a utility/infrastructure tool — it does not fit the agent / LLM / hardware schema in `clawfit/registry/`. **No registry entry recommended.** The signal it carries is what matters.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capability / skill / plugin / tool-use layer** (provider-switching utility, MCP server orchestration sub-category)
- Secondary: **Level 3 — executable SSOT / governance** (atomic-write config management with audit-trail-friendly export/import)
- Adjacent meta-pattern: **Level 2 wrapper-of-wrappers** — cc-switch is not itself a harness, but it composes over the five CLI runtimes, hinting at a future "switcher" sub-layer between L1 base runtimes and L2 harnesses

Not strong enough to add a new layer to `docs/reference-levels.md` yet, but flag if a fourth multi-vendor tool of similar caliber appears within the next two weeks. Three signals in one week + a sustained Rust/Tauri implementation argues this is structural, not noise.

## Status
- Tracking. 52,802★ / +892 today. No registry entry (utility tool, off-schema). Third data point in a multi-vendor / vendor-portability meta-trend; revisit clawfit cost and preference scoring assumptions if a fourth comparable signal lands within ~14 days.
