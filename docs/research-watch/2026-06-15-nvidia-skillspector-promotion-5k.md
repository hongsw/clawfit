# Research Watch: NVIDIA SkillSpector — Promotion Threshold Reached (5,260★)

- Repo: https://github.com/NVIDIA/SkillSpector
- Source: GitHub Trending (today, 964 new stars)
- Prior entry: `docs/research-watch/2026-06-09-nvidia-skillspector-agent-skill-security.md`

## Status update

First tracked 2026-06-09 at 1,517★ with watch criterion: "5k★ OR GitHub Actions marketplace entry." Star count today: **5,260★** — promotion threshold met. Velocity of 964 stars in a single day is the highest observed for a security-focused agent-layer tool in this taxonomy.

## What changed since first signal

- Star count increased from 1.5k → 5.2k (+246%) in 6 days; confirmed organic trending (not artificially boosted)
- No independent replication of the 26.1% vulnerability rate published, but the NVIDIA org affiliation reduces fabrication risk
- SARIF output integration (GitHub Advanced Security, VS Code) unchanged; CI/CD posture confirmed
- No GitHub Actions marketplace entry detected at time of this entry; star threshold alone triggers promotion

## Why this matters for clawfit

SkillSpector is now the highest-starred dedicated security tool for the agent skill/plugin layer in this taxonomy. At 5k+ stars under the NVIDIA org with SARIF output, it is a credible CI/CD artifact for teams enforcing governance at the L4 skill intake boundary. The two-stage pipeline (static Stage 1 + optional LLM Stage 2) allows governance-heavy orgs to audit skills without LLM API calls — directly relevant to `data_sensitivity: confidential` and `governance_need: hard` profiles.

## Taxonomy update

- **Level 4 — Capability / skill layer** (primary): pre-admission static security scanner for agent plugins
- **L4/L5 cross-cutting**: MCP protocol threat category spans both layers
- **Map mutation:** L4 entry warranted — threshold met; adding to reference-levels.md
- **Registry entry:** adding to `tools_registry.json` under `tasks: [security-testing, qa]`, `roles: [developer, devops]`

## Status

- Promoted: threshold met 2026-06-15 at 5,260★
- Registry candidate confirmed; metadata: `network: online`, `setup_complexity: medium`, `governance_need: hard`
- Next watch: independent vulnerability-rate replication OR GitHub Actions Marketplace listing
