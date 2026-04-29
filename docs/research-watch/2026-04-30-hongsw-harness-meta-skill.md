# Research Watch: hongsw/harness — Korean-localized fork of the Team-Architecture meta-skill

- Repo: <https://github.com/hongsw/harness>
- Upstream: <https://github.com/revfactory/harness>
- Companion benchmark: <https://github.com/revfactory/claude-code-harness> (n=15 effectiveness claim)
- Related (already in map): `DureClaw/dureclaw` (hongsw cross-machine orchestrator), `revfactory/harness-100` (200 production harnesses)
- Related (already in research-watch): `2026-03-29-harness-meta-skill-plugin.md` (upstream `revfactory/harness`)

## Why this is worth watching
This is a hongsw-authored fork of the same `revfactory/harness` meta-skill that was already flagged on 2026-03-29 — but with a non-trivial localization layer attached. The fork is also the actual code source for the `harness:harness` skill registered in this environment's system prompt, so it is not just a discovery artifact but the runtime substrate the user is actively iterating on. Combined with `DureClaw/dureclaw`, this is the second hongsw-authored entry that directly informs how clawfit should categorize meta-level harness tooling, regardless of star count (currently 6★).

## What stands out immediately
From the repo and README:
- Forked from `revfactory/harness`; main branch fast-forwarded to `feat/korean-persona-injection`.
- Same six-phase team-architecture workflow as upstream (Domain Analysis → Team Architecture → Agent Definitions → Skill Generation → Integration → Validation).
- Same six architecture patterns (Pipeline, Fan-out/Fan-in, Expert Pool, Producer-Reviewer, Supervisor, Hierarchical Delegation).
- Same output shape: writes `.claude/agents/*.md` and `.claude/skills/*/SKILL.md` into the consumer project.
- Adds three localization skills not in upstream: `korean-persona-search`, `korean-voice-adapter`, `korean-persona-harness`.
- Korean injection sources personas from NVIDIA `Nemotron-Personas-Korea` (1M rows, CC BY 4.0) at runtime — modifies agent voice/manner, does not restructure the generated team.
- Distributed both as a Claude Code plugin marketplace entry (`/plugin marketplace add hongsw/harness` → `/plugin install harness@harness`) and as a global skill copy target (`cp -r skills/harness ~/.claude/skills/harness`).
- README positions itself at "L3 Meta-Factory / Team-Architecture Factory," neighboring `coleam00/Archon` (Runtime-Configuration Factory). This is the upstream's own terminology, not clawfit's level system — see interpretation below.
- Carries forward the upstream effectiveness claim (49.5 → 79.3 quality, 15/15 win rate, n=15, author-measured). Inherited claim, not independently re-validated by the fork.

## Why clawfit should care
Three reasons specific to this fork (vs. the upstream already on file):

1. **Author identity matters for the registry baseline.** This repo is the hongsw-customized version of the meta-skill that hongsw is actually running. Like `DureClaw`, it functions as a "design origin" datapoint for what clawfit's harness/skill categories should be able to express — even at 6★. The pattern hongsw is converging on (cross-machine crew via DureClaw + team-architecture meta-skill via this fork) is a coherent two-layer stack, not two unrelated tools.
2. **Localization-as-overlay is a distinct sub-pattern.** The fork does not change the team-architecture engine; it injects culturally-specific persona/voice data on top of unchanged team structure. That is a different shape from the L4b "domain skill packs" already tracked (marketingskills, obsidian-skills, Game Studios) — those replace the *content* of skills; this one parameterizes the *voice* of generated agents. Worth watching as a possible third L4b axis: locale/voice overlay separate from domain/skill content.
3. **Confirms the meta-skill sub-type.** Two independent repos (revfactory upstream + hongsw fork with localization additions) now both implement the "meta-skill that generates .claude/agents/ + .claude/skills/" pattern. With `DureClaw` as an adjacent cross-machine orchestrator from the same author, the meta-harness sub-type has multiple datapoints rather than a single signal.

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta wrappers / harnesses / orchestration layers** — primary classification. Specifically the same "meta-skill / team architect generator" sub-type already proposed for the upstream on 2026-03-29.
- **Level 4b — Skill packs** — secondary, via the three Korean-localization skills bundled in the fork. These are conventional skill packs that happen to ship inside a meta-harness repo.
- Cross-cutting note: the fork sits at the L2/L4b intersection — the meta-skill engine (L2) ships a default skill set (L4b) used by the personas it generates. This is structurally interesting because it shows a meta-harness can also be its own first-party skill distributor.

Not a Level 3 entry: this generates `.claude/agents/` and `.claude/skills/` artifacts but does not itself encode an executable team SSOT or governance contract. Level 3 overlap exists at the upstream level but is weaker for the fork specifically.

## Distinguishing claims vs. validated facts
- Claim to inspect: the inherited "+60% quality, 15/15 win rate, −32% variance" effectiveness numbers. Same caveat as the 2026-03-29 entry — author-measured, n=15, no third-party replication. Fork does not strengthen or weaken this.
- Validated by repo inspection: fork relationship, branch state (`feat/korean-persona-injection`), three added Korean-localization skills, NVIDIA Nemotron-Personas-Korea as the persona source, plugin + global-skill installation paths.
- Not validated: claimed runtime effect of persona injection ("5 distinguishable speakers vs 5 indistinct") — internal blind test, not externally reproduced.

## Status
- New research-watch entry. No registry inclusion (6★, well below threshold; would also duplicate the upstream's slot).
- No mutation to `docs/reference-levels.md`. The 2026-03-29 entry on the upstream already opened the meta-skill sub-type discussion; this fork adds a localization-overlay datapoint but does not by itself justify a new sub-category.
- Flag for the 2026-05 calibration cycle: if a second locale overlay (non-Korean) appears on top of `revfactory/harness` or a similar meta-skill, promote "locale/voice overlay" to a named L4b sub-axis. Currently a single datapoint.
- Cross-link with the existing `DureClaw` reference-map entry as the second hongsw-authored design-origin signal — useful when reasoning about which categories clawfit's schema must support natively.
