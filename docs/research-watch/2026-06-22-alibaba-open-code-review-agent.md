# Research Watch: alibaba/open-code-review

- Repo/Link: https://github.com/alibaba/open-code-review
- Source: GeekNews / GitHub Trending

## Why this is worth watching
Alibaba open-sourced an AI code review agent with 2 years of internal production use at scale, identifying millions of code defects. At 8.2k★ and Apache-2.0 it is immediately deployable — not a research artifact. The tool ships as a CLI, a Claude Code skill, and a Codex plugin, making it the first Alibaba-origin entry in this taxonomy.

## What stands out immediately
- Reads git diffs; sends changed files to an LLM with tool-use capabilities
- Line-level structured review comments with precision annotations
- Built-in rule set: NPE, thread-safety, XSS, SQL injection
- Multi-model support: OpenAI and Anthropic compatible
- Concurrent file review with smart bundling for large PRs
- Deployment options: CLI, Skill, Claude Code plugin, Codex plugin

## Why clawfit should care
Fills the code review agent cell in the registry — no existing entry covers automated PR/commit review as a primary task. Directly relevant to `task: qa` + `role: developer` profiles. Third independent signal for AI code review tooling (after SkillSpector's code-scanning capability and the Osmani agentic-code-review benchmark article 2026-06-21). `setup_complexity: low` via NPM install positions it well for `solo_dev_codegen` and `offline_mid_codegen` developer profiles where automated QA improves output quality.

## Preliminary interpretation
Current best reading:
- **Level 1 — Specialized code review agent** (agent with tool-use loop targeting git diffs as input surface; not a general coding agent)
- **Level 5 secondary** — produces structured evaluation artifacts (line-level review comments with severity classification)

## Status
- Registry entry added (8.2k★ threshold met, Apache-2.0, deployable tool, production-validated)
