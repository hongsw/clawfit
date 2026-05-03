# Missing Recommendation Axes

*Companion note · Addresses GitHub issue #4*

---

## Context

clawfit's README frames it as an **agent + LLM + hardware recommendation engine**. The current recommendation pipeline filters and scores on:

- `task` (qa, code-gen, research, summarization, classification, data-analysis)
- `latency` (low / medium / high)
- `budget` (cost_per_1k_tokens threshold)
- `network` (online / offline)
- `hardware` (laptop / workstation / cloud)
- `statefulness` (stateless / session / persistent)

These axes are well-suited to the current registry (4 agents, 10 LLMs, 5 hardware). However, as the registry grows and more org profiles emerge, several important axes are not yet modeled.

---

## Missing axis 1 — Model/provider trust and governance

**Gap:** A `network: online` recommendation currently treats all cloud providers as equivalent. But for many orgs, provider identity is a hard constraint.

| New dimension | Values | Example constraint |
|---------------|--------|-------------------|
| `provider_trust` | `open_weight` / `commercial_api` / `managed_gov` | "we only use open-weight models" |
| `data_residency` | ISO country code list | "data must not leave EU" |
| `audit_trail` | `none` / `basic` / `soc2` / `hipaa` | compliance requirement |
| `model_license` | `mit` / `apache2` / `cc_by` / `proprietary` | legal/IP policy |

**Where it lives:** `llms.json` registry entries + a new `governance_profile` filter in `filters.py`.

**Recommended v0.4 addition:**
```json
"license": "mit",
"data_residency": ["global"],
"audit_trail": "none"
```

---

## Missing axis 2 — Deployment / ops complexity

**Gap:** The current model assumes the user can install and run whatever is recommended. In practice, `setup_complexity` is a hard constraint for many teams.

| New dimension | Values | Example constraint |
|---------------|--------|-------------------|
| `setup_complexity` | `zero` / `low` / `medium` / `high` | "we can't run local Docker" |
| `managed_service` | `true` / `false` | fully managed vs self-hosted |
| `multi_user` | `true` / `false` | single-developer vs team deployment |

**Where it lives:** `agents.json` registry entries.

**Example:**
- Claude Code: `setup_complexity: low`, `managed_service: true`, `multi_user: false`
- OpenHands self-hosted: `setup_complexity: medium`, `managed_service: false`, `multi_user: true`
- vLLM serving stack: `setup_complexity: high`, `managed_service: false`, `multi_user: true`

---

## Missing axis 3 — Agent autonomy level

**Gap:** The current taxonomy doesn't distinguish between interactive agents (user approves each step) and fully autonomous agents (fire-and-forget). These require different governance postures.

| Autonomy level | Description | Examples |
|----------------|-------------|---------|
| `interactive` | All actions require user approval | Cursor (ask mode), Continue |
| `supervised` | Runs autonomously, reports checkpoints | Claude Code default |
| `autonomous` | Runs until done; human reviews output | Claude Code Routines, Twill.ai |
| `swarm` | Multiple autonomous agents coordinate | DureClaw, OpenHands multi-agent |

**Where it lives:** `agents.json` as `autonomy_level` field.

---

## Missing axis 4 — Task taxonomy expansion

**Gap:** Current tasks are: `qa`, `code-gen`, `research`, `summarization`, `classification`, `data-analysis`. Several high-signal use cases are not covered:

| Missing task | Evidence | Proposed tag |
|-------------|----------|-------------|
| Security testing | Shannon, Strix (both in L1) | `security-testing` |
| Voice/dictation coding | Superwhisper (in registry) | `voice-coding` |
| Document automation | craft-agents-oss (L6) | `document-automation` |
| Financial analysis | TradingAgents, ai-hedge-fund (L1/L2) | `financial-analysis` |
| Media production | HyperFrames signal (04-29 scan) | `media-production` |
| Legal research | korean-law-mcp (in registry) | `legal-research` |

**When to add:** When at least 2 independent tools in the registry share the same task type AND a real org profile generates a recommendation request for it.

**Current recommended action:** Add `security-testing` now (Shannon + Strix are both in L1 registry). Defer others until registry density supports them.

---

## Missing axis 5 — Team/org profile dimensions

**Gap:** The current model has no explicit team-size or org-maturity filters. Scoring implicitly handles this via agent metadata but the filter layer doesn't expose it.

| New dimension | Values | Use |
|---------------|--------|-----|
| `team_size` | `solo` / `small` / `medium` / `large` | Affects multi-user, governance needs |
| `org_maturity` | `1-7` scale | From "no agents yet" to "automated fleet" |
| `primary_role` | `developer` / `researcher` / `exec` / `ops` | Tunes scoring weights |

**Where it lives:** User-facing `clawfit profile` questionnaire inputs, not in registry JSON.

---

## Recommended implementation sequence

| Priority | Axis | Effort | Value |
|----------|------|--------|-------|
| 1 | `security-testing` task | Low — add to Shannon + Strix | Closes a clear gap |
| 2 | `setup_complexity` on agents | Medium — add to all 4 agents | Filters out impractical recommendations |
| 3 | `autonomy_level` on agents | Low — metadata only | Enables governance-aware filtering |
| 4 | `model_license` + `audit_trail` on LLMs | Low — metadata only | Unlocks enterprise filtering |
| 5 | `governance_profile` filter in filters.py | Medium — code change | Connects metadata to recommendations |
| 6 | `team_size` / `org_maturity` in profile | High — UX change | Enables personalized scoring |
