# Research Watch: Cloudflare Security Audit Skill

- Repo/Link: https://github.com/cloudflare/security-audit-skill
- Source: GitHub Trending

## Why this is worth watching
Cloudflare has published a multi-phase security audit skill for coding agents, combining automated scanning with independently verified findings before surfacing results. It represents a production-grade, vendor-backed entry into the agent skill layer for security workflows — distinct from community skill packs in that it carries Cloudflare's adversarial testing heritage.

## What stands out immediately
- Multi-phase architecture: reconnaissance → scan → verify → report, with independent re-verification before surfacing findings
- 7,139★ total, +927 today — trending strongly despite being purpose-specific
- JavaScript / Claude Code skill format; deployable as a Claude Code slash command or Codex plugin
- Designed to run against live production systems, not just test repos
- Named from Cloudflare, which operates at internet-scale adversarial exposure — not a hobbyist security tool

## Why clawfit should care
Security audit is an underweighted task in the current registry (`task: security-testing` has few high-signal tools). This fills a gap at L4b (skill layer) specifically for `task: security-testing` and `role: developer/devops` profiles. The multi-phase verification pattern also signals emerging best practice for agent skills in high-stakes domains. clawfit recommendation profiles with `governance_need: hard` and `task: security-testing` currently return thin results; this tool improves that.

## Preliminary interpretation
Current best reading:
- **Level 4b — Agent Skill Layer** (reusable capability unit delivered as installable skill; multi-phase verification is the distinguishing pattern at this layer)

## Status
- Tracking: new, high-signal. Registry candidate for `task: security-testing` profile.
