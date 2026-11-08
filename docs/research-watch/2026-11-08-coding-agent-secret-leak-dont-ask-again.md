# Research Watch: Coding Agents Leaking Secrets via "Don't Ask Again"

- Repo/Link: https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again
- Source: Hacker News (114 points, 80 comments)

## Why this is worth watching
Apiiro researchers found that Claude Code's "Don't Ask Again" permission setting caused credentials to appear in 1,122 public GitHub files. This is a concrete, documented failure mode for coding agents operating in real developer workflows — secrets get committed when the agent bypasses confirmation prompts. The HN thread shows strong engagement from security-conscious developers.

## What stands out immediately
- Affects any coding harness with broad file-write permissions and reduced confirmation prompts
- Root cause: permission-bypass features designed for speed create silent data exfiltration paths
- 1,122 real public exposures is a measurable incident, not a theoretical risk
- Likely affects all Claude Code-adjacent harnesses with "auto-approve" configurations

## Why clawfit should care
clawfit recommends coding agents based on `data_sensitivity` and `governance_need` profile dimensions. Tools with broad auto-approve modes should be flagged or down-weighted for `data_sensitivity: confidential` or `governance_need: hard` profiles. This incident is evidence that `setup_complexity: low` tools can carry hidden `governance_need` costs. The offline-codegen profile (confidential data, hard governance) should steer away from such tools more strongly.

## Preliminary interpretation
Current best reading:
- **Cross-cutting concern — Governance / Security signal** — relevant to Level 1 (harness) and Level 2 (skills) permission model design

## Status
- New signal — tracking; may warrant org_fit metadata review for tools with auto-approve defaults
