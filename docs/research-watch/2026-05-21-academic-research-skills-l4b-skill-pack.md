# Research Watch: academic-research-skills

- Repo/Link: https://github.com/Imbad0202/academic-research-skills
- Source: GitHub Trending (#2, 16,121★, Python)

## Why this is worth watching

A structured Claude Code skill pack covering the full academic research lifecycle — from literature review through peer review simulation and final publication. At 16,121★ it exceeds the 5k registry threshold, making it the first high-signal L4b domain skill pack explicitly targeting the academic research workflow. The pack prioritizes human oversight via integrity checkpoints rather than full automation, which is architecturally distinct from most coding-agent skill packs.

## What stands out immediately

- Four major skill categories: Deep Research (13 agents, 7 modes), Academic Paper writing (12 agents), Peer Review simulation (7 agents), Pipeline orchestrator (10-stage with integrity checkpoints)
- 7+ slash commands including `/ars-plan`, `/ars-lit-review`, `/ars-full`
- CC BY-NC 4.0 license — restricts commercial use; relevant for `governance_need: hard` commercial orgs
- Python 97.4% — heavier dependency footprint than Shell-based skill packs
- Systematic review and LaTeX/PDF output support — academic-native output formats

## Why clawfit should care

This is the first clear L4b domain skill pack for academia, extending the domain-skill-pack cluster (marketingskills, obsidian-skills, agency-agents, claude-code-game-studios) into the researcher persona. The `research` task type in clawfit currently serves both academic researchers and industry PMs — this tool is strongly specialized toward the former. The CC BY-NC license is a hard blocker for commercial org recommendations; org_fit metadata should reflect this constraint. At 16k★, this is a registry candidate.

## Preliminary interpretation

Current best reading:
- **Level 4b — Domain Skill Pack** (academic research vertical, researcher-primary persona)
- No significant secondary classification

## Status

- 16,121★, CC BY-NC 4.0, Python — exceeds star threshold; license restricts commercial deployment
- Registry candidate with metadata note: `network: online`, `setup_complexity: low` (plugin install), `roles: [researcher]`, `tasks: [research, summarization]`, CC BY-NC restricts commercial recommending
- Watch: whether license is upgraded to permissive (MIT/Apache) and whether a second academic-research skill pack confirms this as a stable domain cluster
