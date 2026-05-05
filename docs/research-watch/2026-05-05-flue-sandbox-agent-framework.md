# Research Watch: Flue — The Sandbox Agent Framework

- Repo/Link: https://github.com/withastro/flue
- Source: GitHub Trending (TypeScript #4, ~290 stars today)

## Why this is worth watching
Flue comes from the Astro organization (withastro), which carries real ecosystem credibility — the team has already demonstrated an ability to define a developer-facing framework standard (Astro itself). The "agent harness" framing is explicit in their own words: "think Astro or Next.js, but for agents." The two-tier sandbox model (virtual-by-default, container-on-demand) is a design choice that directly addresses the cost/scale tradeoff in coding agent infrastructure, which is a currently contested problem space.

## What stands out immediately
- Self-described as "The Agent Harness Framework" — deliberately not a base runtime, not a skills pack
- Two-tier sandbox: virtual (just-bash, in-memory, no container overhead) as default; full Linux container via providers like Daytona as opt-in
- Connectors model installs third-party sandbox adapters via markdown recipes, not npm packages — unusual distribution pattern
- AGENTS.md-driven: behavior, skills, and context live in Markdown; minimal code required
- Deployment targets span Node.js, Cloudflare Workers, GitHub Actions, GitLab CI — runtime-agnostic claim appears structural, not rhetorical
- LLM provider abstraction covers Anthropic, OpenAI, OpenRouter, custom gateways — not locked to one vendor
- CLI offers `flue dev`, `flue run`, `flue build` — lifecycle mirrors standard web toolchain conventions (claim from repo; verify in practice)

## Why clawfit should care
The `withastro` org origin means Flue could standardize AGENTS.md the way Astro standardized `astro.config.mjs` — a governance artifact that clawfit's Level 3 tracking should watch. The connector model is also novel: if adapters for sandbox providers proliferate (Daytona, Freestyle, E2B), Flue becomes an orchestration layer sitting above those execution substrates, which is a Level 2 position that narrows clawfit's current registry gap for TypeScript harnesses targeting CI/headless workflows. The cost-latency tradeoff built into the sandbox tier selection maps directly onto clawfit's `latency` and `budget` scoring axes.

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta wrapper / harness / orchestration layer** (TypeScript, headless, CI-native agent harness)
- Secondary signal: **Level 3** — AGENTS.md as executable SSOT if the governance-via-Markdown pattern matures
- The sandbox infrastructure (virtual vs. container) is borrowed from Level 7 substrates but Flue itself does not own that layer

## Status
- New entry, moderate-high signal. ~290 stars/day from GitHub Trending. Withastro org authorship elevates credibility above typical new-framework noise. Watch for AGENTS.md standardization activity and community connector submissions.
