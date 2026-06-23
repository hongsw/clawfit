# Research Watch: Prompt Injection as Role Confusion (ICML 2026)

- Repo/Link: https://role-confusion.github.io
- Source: Hacker News (136 pts, 75 comments)

## Why this is worth watching
ICML 2026 paper by Ye, Cui, and Hadfield-Menell reframes prompt injection attacks as a structural LLM flaw — role perception driven by writing style, not architectural tags — and introduces CoT Forgery, which raises jailbreak success from ~0% to ~60% across tested models. This is a methodology paper with direct scoring implications for agent governance.

## What stands out immediately
- **Role probes** measure how strongly an LLM perceives a token as belonging to a role (User, System, CoT) — finding: roles are inferred from style, not tags
- **CoT Forgery attack**: injecting fake reasoning text into prompts exploits the model's trust in its own thinking (ChainOfThought role), achieving ~60% jailbreak across models tested
- Removing all role tags does **not** eliminate role perception if the text *sounds like* that role — style bleeds across boundaries
- Prepending "User:" to injected data is sufficient to shift model perception toward user-command trust
- Recommendation: separate competing objectives into distinct roles by architectural redesign, not memorized defense patterns

## Why clawfit should care
The `governance_need: hard` scoring dimension in clawfit currently maps to network isolation and audit trails. This paper argues that *model-level role architecture* is a governance variable independent of deployment setup. Tools that expose agents to external data (web browsing, email, file reading) carry structural injection risk that sandboxing does not fully address. The CoT Forgery attack is especially relevant to reasoning-mode models (Fable 5, Claude 3.7 extended thinking, Gemini 2.5 Flash thinking) — all of which are increasingly used in high-stakes agent loops. **Scoring implication**: `governance_need: hard` profiles should weight against tools that pass raw external content into LLM context without intermediate sanitization.

## Preliminary interpretation
Current best reading:
- **Level 5 — Evaluation & Provenance methodology signal** (security evaluation framework for LLM agents)
- **Level 3 secondary — Governance** (new attack surface affects `governance_need` scoring weight)

## Status
- ICML 2026 peer-reviewed paper; 136 HN points; high-credibility signal
- No registry entry: methodology paper, not a tool
- Watch: whether any harness (Claude Code, Goose, Cursor) ships a mitigation for CoT Forgery specifically
