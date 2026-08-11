# Research Watch: diagram-design — Editorial Diagram Skill with Brand Onboarding for Claude Code

- Repo: https://github.com/cathrynlavery/diagram-design (⭐6,285)
- Source: GitHub Trending #1 all languages, 2026-08-11 (+1,612 stars today)
- Author: Cathryn Lavery (BestSelf.co founder, littlemight.com)
- License: MIT
- Created: 2026-04-16 (4 months old; ≤6-month recency threshold met)

## Why this is worth watching

diagram-design is a Claude Code skill delivering 29 editorial diagram types as self-contained HTML+SVG files, paired with an automated brand-extraction workflow that reads a target website, maps its palette and typography to semantic design tokens, and applies those tokens across all 29 diagram types. At 6,285 stars with 417 forks — reaching #1 on GitHub Trending all-language on its fourth month of existence — it is one of the fastest-rising Claude Code skills by star velocity in this scan series.

The project is not notable for quantity (29 types is not unusual in a diagram library) but for opinionated design constraints: no Mermaid output, no rounded-box defaults, no shadows, one accent color, a 4/10 target density rule, and a 4px grid system applied without exception. These constraints address a concrete problem: AI-generated diagrams look visually inconsistent with published content. diagram-design's WCAG AA validation at brand-extraction time, and its progressive-disclosure architecture (34 reference files loaded on demand, not all at once), reflect design thinking applied at the skill architecture level — not just the output level.

## What stands out immediately

- **Brand onboarding as a first-class workflow.** A single instruction — `"onboard diagram-design to https://yoursite.com"` — fetches the homepage, extracts dominant palette + font stack, maps colors to semantic roles (paper, ink, muted, accent, link), validates WCAG AA contrast at 9–12px, and writes the result to `references/style-guide.md`. All 29 types then use those tokens. Not a prompt trick — the token-to-type mapping is encoded in the skill's reference architecture.
- **Self-contained HTML+SVG with zero runtime dependencies.** Each diagram is a single `.html` file. No build step, no JavaScript framework, no Node.js, no external CDN. This is architecturally distinct from Mermaid-based diagram generation (requires a JavaScript renderer) and from MCP chart servers like flint-chart (requires an MCP server process). The file is the artifact.
- **Progressive disclosure architecture.** The top-level `SKILL.md` is a lean index; each of the 34 type-specific reference files loads only when that type is requested. Context stays minimal per generation — a practical constraint design that acknowledges LLM context cost, similar to book-to-skill's per-chapter loading approach (tracked 2026-07-01).
- **Three variants per diagram type.** Every type ships as minimal light, minimal dark, and full-editorial — three different visual densities from the same source. Three variants × 29 types = 87 distinct renderable outputs, with a live gallery at `assets/index.html`.
- **Opinionated design system, explicitly enforced.** Three font families only (Instrument Serif, Geist, Geist Mono assigned to specific semantic roles), 1px hairline borders, no shadows, border-radius max 10px, all coordinates/gaps divisible by 4. The README calls the 4px grid rule "non-negotiable." Opinionated constraints embedded in skill instructions rather than enforced by a linter — an architectural choice worth noting.
- **Playwright PNG export at 2× resolution via slash command.** `/diagram-design:export path/diagram.html --scale=3` rasterizes the diagram via Playwright. SVG export injects Google Fonts for standalone rendering. Export is slash-command driven, not manual — the skill handles the tooling setup path.
- **55-icon set from permissive sources.** Monochrome IT/cloud icons (Docker, Kubernetes, AWS, Azure, GitHub, Postgres, etc.) via Tabler Icons (MIT) + Simple Icons (CC0), all using `currentColor` for token-driven theming. Not a dependency — embedded in the skill's asset directory.

## Why clawfit should care

The L4b skill cluster in reference-levels.md currently includes procedural/behavioral skill packs (phuryn/pm-skills, addyosmani/agent-skills), knowledge-base skill packs (book-to-skill), and code-graph skills (graphify). diagram-design represents a distinct sub-type: **visual output template skills** — skills whose primary artifact is a human-readable visual output (diagram, chart, infographic) rather than code, documentation, or structured data.

This is architecturally relevant to clawfit because visual diagram generation is a task type that does not currently appear in the task taxonomy (`qa`, `code-gen`, `research`, `writing`, `data` are the current values). A `task: diagram` or `task: visual-output` axis would capture workflows where the final deliverable is a rendered diagram, not code or prose. Star count (6,285), fork count (417), and one-day velocity (1,612) together indicate this sub-type addresses real demand.

**Two-signal cross-check:** microsoft/flint-chart (2026-07-11, L4c, MCP visualization language — "first signal for agent output formatting MCP server") and diagram-design (2026-08-11, L4b, Claude Code skill) are cross-layer signals for the "agent-native diagram generation" pattern. They share the goal (agent produces a diagram as a deliverable) but operate at different layers (L4c MCP vs. L4b slash-command skill) and use different mechanisms (semantic spec compilation vs. embedded design system templates). Cross-layer confirmation is noted but does not meet the same-layer two-signal rule for canonical taxonomy change.

**Schema gap:** `task: visual-output` or `task: diagram`; `skill_artifact_type: [code | prose | data | diagram | media]`; `brand_aware: bool`.

## Preliminary interpretation

Current best reading:

- **Level 4b — Skills / Installable Capabilities** (primary): a Claude Code slash-command skill installable via plugin marketplace or symlink, following the same delivery pattern as graphify (L4b, code-graph visualization), book-to-skill (L4b, PDF-to-skill conversion), and addyosmani/agent-skills (L4b, production coding skills). The skill format (SKILL.md + demand-loaded reference files) is the canonical L4b form factor in this corpus.
- **Level 6 — Human Interface** (secondary): the primary artifact is a rendered HTML+SVG diagram for direct human viewing — not an intermediate data structure, not code to run, not a log. The diagram is the deliverable. This positions diagram-design at the L4b/L6 boundary: capability layer (skill install, invocation) with a human-interface output (visual diagram).

Cross-reference: graphify (2026-07-03, L4b — code-to-knowledge-graph Claude Code skill, 76.9k★); book-to-skill (2026-07-01, L4b — PDF-to-skill conversion, 7.4k★); flint-chart (2026-07-11, L4c — MCP visualization language, 1.3k★, Microsoft Research). diagram-design is the first L4b "editorial diagram template skill" signal — distinct from graphify (knowledge graphs) and flint-chart (chart compilation via MCP).

## Claims to verify

- **WCAG AA validation accuracy.** The brand-extraction workflow claims automatic contrast validation. Verify whether the contrast check covers the full range of token pairs (ink-on-paper, accent-on-paper, muted-on-paper) or only the most common pair. WCAG AA at 9–12px is particularly strict for small text.
- **29 vs. 27 diagram type count.** The GitHub repository description says 29; the README body says 27; the file count yields 34 reference files. Clarify whether the discrepancy reflects draft/experimental types not yet in the gallery, or documentation inconsistency.
- **Playwright dependency friction.** PNG export requires `pip install playwright && playwright install chromium` — a significant optional dependency for a "zero-dependencies" skill. Verify whether this step is clearly gated (opt-in on export) or if first-time users encounter unexpected install prompts.
- **Brand font rendering in self-contained SVG.** SVG export injects Google Fonts for standalone rendering. Verify whether the injected fonts render correctly in offline/air-gapped environments or print-to-PDF workflows where Google Fonts may be blocked.

## Status

- 6,285★, MIT license, 4 months old — above 5k registry threshold in star count but no registry schema applies (not an agent, LLM, or hardware entry; would require a new `skills.json` registry category)
- Active development: last push 2026-08-11 same-day as trending peak
- **Registry eligibility: no.** Does not map to agents.json, llms.json, or hardware.json; no deterministic cost/latency data (it is a free Claude Code skill, not an inference provider)
- First signal for "editorial diagram template skill" sub-type in L4b
- No canonical section change: single signal; cross-layer confirmation with flint-chart (L4c) exists but does not satisfy same-layer two-signal rule
- Schema watch: `task: visual-output`; `skill_artifact_type: diagram`; `brand_aware: bool`; `context_loading: progressive-disclosure`
- Promotion criterion: a second L4b Claude Code skill that is primarily an editorial/visual-output template system (not code, prose, or knowledge-graph focused) would confirm this sub-type for reference-levels.md annotation
