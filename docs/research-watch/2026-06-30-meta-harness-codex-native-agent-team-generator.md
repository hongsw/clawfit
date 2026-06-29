# Research Watch: SaehwanPark/meta-harness — Codex-native port of the Team-Architecture Meta-Skill

- Repo: <https://github.com/SaehwanPark/meta-harness>
- Also see: <https://github.com/revfactory/harness> (upstream Claude Code analog), <https://github.com/hongsw/harness> (Korean-localized Claude Code fork, research-watch 2026-04-30), <https://github.com/coleam00/Archon> (L3 neighbor, research-watch 2026-04-11)

## Why this is worth watching

meta-harness is explicitly positioned as the Codex runtime equivalent of `revfactory/harness` — the same six-phase Team-Architecture Factory pattern, ported away from Claude Code's `.claude/` conventions to Codex's `.agents/` layout with `AGENTS.md` as the SSOT anchor. The repo confirms that the "meta-skill that generates a team of agents and the skills they use" pattern is not a Claude Code artifact but a runtime-transferable design primitive. At 113 stars and user-nominated, it sits below the automated trending threshold but above the point where it can be dismissed as noise.

## What stands out immediately

Based on the repo README, tree, and fetch of actual content:

- Self-description: "Codex-native meta-skill that designs domain-specific & specialized agents and generates the skills they use." The "Codex-native" qualifier is explicit and intentional — this is a declared port, not an independent reinvention.
- Six-phase workflow is structurally identical to `revfactory/harness`: Domain Analysis → Team Architecture Design → Role/Artifact Definition → Skill Generation → Integration/Orchestration → Validation/Testing. No new phases; same sequencing.
- Six architecture patterns match the upstream: Pipeline, Fan-out/Fan-in, Expert Pool, Producer-Reviewer, Supervisor, Hierarchical Delegation.
- Output paths differ from the Claude Code version: generates `.agents/skills/<domain>/SKILL.md` and `docs/harness/` artifacts rather than `.claude/agents/*.md` + `.claude/skills/*/SKILL.md`. This is the primary runtime-specific adaptation.
- AGENTS.md used as the root governance contract (WHAT/WHY/HOW progressive disclosure format), replacing CLAUDE.md in the same structural role.
- Bootstrap installer (`scripts/install_harness.py`) supports multiple layout targets: `--scope project` or `--scope user`, with named presets for ForgeCode, Droid, OpenHands, Aider, and Codex runtimes. This multi-target design is a claim to inspect — compatibility breadth is stated, not independently verified.
- Validation layer (`scripts/validate_codex_port.py`, smoke tests) is present and suggests the author is tracking fidelity to the upstream spec, not just copying structure.
- Apache 2.0 license. Python only (100%). Version 0.3; 40 commits on main; last push 2026-04-11.
- 113 stars, 5 forks. No published releases.

## Why clawfit should care

The harness:harness / meta-skill pattern was identified in clawfit's taxonomy as an L2/L3 border zone: meta-skills that generate `.claude/agents/` + `.claude/skills/` artifacts sit at L2 (meta wrapper / harness) as generators, with L3 character (governance SSOT) once the artifacts are installed. meta-harness performs the same operation against a Codex runtime target. If clawfit's recommendation engine needs to handle cases where a team has standardized on Codex rather than Claude Code as its base runtime, meta-harness is the structural analog of hongsw/harness and revfactory/harness for that deployment surface.

Additionally, the "generates skills" component of meta-harness maps to L4b output: the meta-skill's terminal product is SKILL.md files, which are L4b artifacts. This means meta-harness simultaneously operates at L3 (team SSOT generation) and produces L4b (skill pack) artifacts — the same L3/L4b co-production pattern documented for `hongsw/harness` and `revfactory/harness` in earlier research-watch entries.

## Preliminary interpretation

Current best reading:

- **Level 3 — Team harness / executable SSOT / governance layer** (primary classification). The meta-skill's output is an AGENTS.md-anchored team operating spec — precisely the L3 "executable SSOT" definition. It generates the governance artifacts, not just the executable skills.
- **Level 2 secondary** — the meta-skill itself is a harness-as-generator, same shape as Archon (harness-builder sub-type). The distinction from Archon: Archon claims to build arbitrary harness configurations; meta-harness applies one specific pattern (six-phase team-architecture) to one execution artifact family (`.agents/skills/`).
- **Level 4b secondary** — SKILL.md files are the terminal artifacts of the generation process. The meta-skill is an L3 generator that produces L4b outputs, parallel to how `claude-plugins-official` packages L4b skills inside an L3-adjacent distribution container.

Relationship to neighbors:
- **vs. harness:harness (hongsw/harness + revfactory/harness):** Same six-phase workflow, same six patterns, same co-generation of team + skills. The sole structural difference is runtime target: `.claude/` path hierarchy → `.agents/` path hierarchy; CLAUDE.md anchor → AGENTS.md anchor. This is an ecosystem portability signal, not a capability extension.
- **vs. Archon:** Archon is a "harness builder" claiming determinism and repeatability at the configuration layer. meta-harness is a "team-architecture factory" claiming to generate not just a configuration but a full agent team with skills. Different scope; Archon is more general, meta-harness is more opinionated about the output structure.
- **vs. L3 canonical entries (superpowers, gsd, CLAUDE.md specs):** meta-harness is generative (produces L3 artifacts for a target project) rather than consumable (is itself the L3 artifact). It belongs in the "meta-skill / generator" sub-type alongside revfactory/harness rather than in the behavioral-spec or methodology-guide sub-types.

## Distinguishing claims from validated facts

- Validated by repo inspection: six-phase workflow, six patterns, `.agents/` output path, AGENTS.md governance anchor, multi-target installer, Apache 2.0 license, Python-only, 40 commits, 113 stars, last push 2026-04-11, v0.3 label.
- Claim to inspect: the multi-platform compatibility list (ForgeCode, Droid, OpenHands, Aider, Codex layout presets). "Compatible" may mean only path layout differences are handled; deep runtime behavior of generated skills across all listed runtimes is not independently verified.
- Not validated: any effectiveness claim. Unlike the upstream `revfactory/harness` (which carries a contested "+60% quality" n=15 self-measured benchmark), meta-harness makes no effectiveness claims in the inspected content — a notable restraint worth recording.

## Status

- Below registry threshold (113 stars vs. 5,000 minimum). No registry entry created.
- No mutation to `docs/reference-levels.md`. The Team-Architecture Factory sub-type at L3 is already documented through the harness:harness lineage (revfactory + hongsw forks). meta-harness is a corroborating signal confirming the pattern is runtime-portable, which strengthens the existing L3 sub-type case but does not require a new sub-type entry today.
- Signal quality note: user nomination with explicit taxonomy cross-reference provides stronger signal than star count alone. The author is actively tracking the upstream (via structural mirroring and validation scripts), not just copying it.
- Watch condition: if meta-harness reaches 1,000 stars OR a second independent Codex-native team-generator appears applying the same six-phase pattern to `.agents/` artifacts, flag for L3 sub-type note on "Codex-runtime port of Team-Architecture Factory."
- Cross-link: record as a third datapoint (after revfactory + hongsw) for the L3 Team-Architecture Factory meta-skill sub-type. The sub-type is confirmed cross-runtime.
