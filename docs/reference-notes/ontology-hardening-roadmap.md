# Ontology Hardening Roadmap

*Companion note · Addresses GitHub issue #6*

---

## Goal

Turn `reference-levels.md` from a strong market map into a stable comparison model that a recommendation engine can consume reliably. The map is already accurate; this roadmap makes it **machine-legible and self-consistent**.

---

## Phase 0 — Purpose and scope declaration ✅ (in progress)

**Done:** The document header now explicitly states it is a set of ecosystem layers/lenses, not a maturity ladder.

**Remaining:**
- Finalize the separation between canonical taxonomy (stable) and discovery logs (dated, movable) — see issue #7 and `docs/scans/README.md`
- Confirm the explicit in/out-of-scope boundary: clawfit tracks agent-adjacent tooling; standalone LLM model catalogs, cloud infrastructure, and general-purpose developer tools are out unless structurally important

---

## Phase 1 — Classification-axis decision

**Status:** Deferred to v0.5

**Decision to make:** Keep the current 7-level system as the primary axis, or shift to a multi-dimensional model?

**Current position:**
- The 7 levels are architectural layers (L1 base → L7 interface), not a quality ranking
- Several projects already carry primary + secondary layer tags (e.g., deepagents = L1+L2; cc-connect = L7+L4c)
- A multi-dimensional model (primary role + secondary tags for scope, modality, deployment, governance) would improve precision but increase maintenance cost

**Proposed resolution:**
- Keep the 7-level architecture stack as the primary axis (it is working well)
- Add a lightweight secondary tag vocabulary without changing the primary structure
- Example tags: `multi-layer`, `offline-capable`, `enterprise-ready`, `memory-native`, `audit-trail`

**Acceptance criterion:** At least 10 entries in the registry carry secondary tags before declaring this phase complete.

---

## Phase 2 — Discriminating criteria

**Status:** Not started

**Problem:** Two raters looking at a new tool may assign it to different levels because there are no written exclusion/inclusion rules.

**Proposed criteria format for each level:**

```
## Level N — [Name]

Inclusion: tool must [X]
Exclusion: tool is excluded if [Y]
Boundary with Level N+1: [Z is the distinguishing feature]
```

**Example (Level 2 vs Level 3):**
- Level 2 (harness): wraps one or more L1 agents; handles session/context lifecycle; may add memory or tool routing
- Level 3 (SSOT/governance): defines executable workflow rules that agents must follow; version-controlled; human-auditable; the *policy* that governs the harness
- Distinguishing feature: does the artifact define *what agents should do* (L3) or *how the session runs* (L2)?

**Milestone:** Discriminating criteria written for all 7 levels.

---

## Phase 3 — Schema linkage

**Status:** Partial (agents.json, llms.json, hardware.json exist)

**Problem:** The prose taxonomy in reference-levels.md is not directly consumed by the recommendation engine. The engine reads the three JSON registries, which have different field sets.

**Proposed linkage fields to add to registry entries:**

| Field | Type | Purpose |
|-------|------|---------|
| `ecosystem_level` | `"L1"` … `"L7"` | Primary taxonomy layer |
| `secondary_levels` | `["L4c", "L2"]` | Multi-layer entries |
| `evidence_verified_at` | ISO date | When specs were last validated |
| `evidence_source` | URL | Source for star count / pricing / benchmark |

**See also:** `docs/reference-notes/evidence-schema.md` for the full evidence-field spec.

**Milestone:** All 17 current registry entries carry `ecosystem_level` and `evidence_verified_at`.

---

## Phase 4 — Hardware and infrastructure alignment

**Status:** Companion note written (`docs/reference-notes/hardware-deployment-axis.md`)

**Problem:** clawfit's README promises an agent + LLM + **hardware** recommendation engine, but the taxonomy is weak on hardware and deployment distinctions.

**Resolution:** The hardware companion note (issue #8) defines the axis. The next step is wiring those categories into the scoring model.

---

## Phase 5 — Discovery log separation

**Status:** Companion note written (`docs/scans/README.md`)

**Problem:** Date-stamped "New signals as of YYYY-MM-DD" sections are embedded inside `reference-levels.md`, making the canonical taxonomy definition hard to distinguish from the research log.

**Resolution approach:** Going forward, dated scan content goes to `docs/research-watch/` (already the convention) and eventually to `docs/scans/` once a migration script is written. `reference-levels.md` keeps only the stable taxonomy plus a pointer to scans.

**Migration is deferred** (high blast radius; existing content is already cross-linked). New daily scans follow the new convention immediately.

---

## Phase 6 — Ontology validation loop

**Status:** Partially running (daily scan + pytest)

**Current loop:**
1. Daily scan produces research-watch docs
2. ecosystem-mapper agent decides whether to update reference-levels.md
3. scoring-analyst audits three reference profiles
4. test-guardian runs pytest after registry changes

**Gaps:**
- No automated check that every new registry entry has an `ecosystem_level` field
- No automated drift check between README tool count and actual registry count (star counts drift)
- No periodic review of whether Level definitions still fit new entries

**Proposed additions:**
- `tests/test_registry_schema.py` — validate that every entry has required fields including `ecosystem_level`
- Monthly star-count refresh via `scripts/refresh_stars.py`
- Quarterly level-definition review in `CLAUDE.md` (next scheduled: 2026-07)

---

## Issue relationships

| This issue | Depends on / blocks |
|------------|---------------------|
| #6 (ontology hardening) | parent of #1, #2, #3, #4, #7, #8 |
| #1 (critique backlog) | addressed by Phases 0–1 |
| #2 (evidence fields) | Phase 3 |
| #3 (primary/secondary tags) | Phase 1 |
| #4 (missing axes) | Phase 4 |
| #7 (scan separation) | Phase 5 |
| #8 (hardware dimension) | Phase 4 |
| #9 (inference substrate) | Phase 4 (done) |
