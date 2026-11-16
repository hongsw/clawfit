# Research Watch: Lovable Apps — Vibe-Coded App Data Exposure

- Repo/Link: https://www.crissyfield.de/research/lovable-en/
- Source: Hacker News

## Why this is worth watching
Security researcher crissyfield published research showing that apps built with the Lovable vibe-coding platform exposed passport details and over 200,000 private messages. The root cause: Lovable generated frontend code that embedded raw Supabase credentials in client-side JavaScript, bypassing row-level security. This is not a Lovable-specific bug — it is an architecture pattern problem that any LLM code generator can produce when it prioritizes working demos over secure credential handling.

## What stands out immediately
- 200K+ private messages and passport scans exposed from real user apps
- Generated code embedded service-role Supabase keys client-side
- Pattern is repeatable across any AI code generator that lacks a security review gate
- No governance or credential audit in the generation pipeline

## Why clawfit should care
This event crystallizes why clawfit's `governance_need` dimension matters. Orgs building user-facing apps with AI agents require tools that include security review gates or at minimum warn against credential embedding. When `governance_need: "hard"` is set, clawfit should weight tools with explicit security review steps higher and flag vibe-coding platforms (Lovable, Bolt, etc.) as `min_maturity: 3+` with a governance caveat. The finding also supports adding a "security-review" feature flag to the registry.

## Preliminary interpretation
Current best reading:
- **Ecosystem signal — governance/security gap in L3 vibe-coding platforms**

## Status
- Active — high-impact disclosure; watch for Lovable response and similar disclosures from Bolt/Replit Agent
