# Research Watch: react-doctor — AI-Aware React Codebase Health Scanner

- Repo: https://github.com/millionco/react-doctor
- Also see: https://betterstack.com/community/guides/scaling-nodejs/react-doctor/ (architecture deep-dive, 2026-02-22); https://blog.openreplay.com/scan-react-code-anti-patterns-react-doctor/ (usage walkthrough); https://skillstore.io/skills/millionco-react-doctor (L4b skill distribution via Skillstore); https://lobehub.com/skills/ngxtm-devkit-react-doctor (Lobe Hub skill listing); https://github.com/millionco (parent org — also maintains million.js, the React compiler optimization library)

## Why this is worth watching

react-doctor is the first React-specific static analysis tool in this taxonomy to ship a dual distribution form: a standalone CLI/Node.js library *and* an installable agent skill for 50+ AI coding assistants (Claude Code, Cursor, GitHub Copilot, and others). The `npx react-doctor install` path writes React diagnostic rules directly into the host agent's context, making the scanner itself a skill-delivery mechanism — a form factor not previously observed in the L4b static-analysis sub-type. At 7.5k GitHub stars (above the 5k registry threshold), MIT license, and backed by the millionco org (creators of million.js, the widely-adopted React compiler optimization library), the tool has organizational credibility and distribution momentum that peer React linters typically lack.

## What stands out immediately

- **Star count and origin.** 7.5k stars, MIT, TypeScript 100%. Maintained by millionco, the same org behind million.js (React compiler optimization, 17k+★). Provenance from a known React performance tooling org is a distinguishing credential vs. standalone scanner projects.

- **Dual form factor: CLI scanner + agent skill installer.** Two distinct deployment paths: (1) `npx react-doctor@latest .` runs a one-shot codebase scan; (2) `npx react-doctor@latest install` writes the diagnostic rule set as a skill into the host agent. The second path means the tool functions as an L4b skill pack for agent runtimes — not merely a developer-facing linter. Skill distribution via Skillstore and Lobe Hub confirms this path is in production.

- **Rules engine: Oxlint (Rust-based AST) + dead-code detection pass, running in parallel.** Two analysis passes run concurrently: a lint pass using Oxlint (a Rust linter claiming 50–100x faster execution than ESLint) and a dead-code detection pass. 60+ pre-configured rules cover six diagnostic categories: state/effects, performance, architecture, security, accessibility, and dead code. The security detection layer uses regex over variable names (`SECRET_VARIABLE_PATTERN`, detecting `api_key`, `secret`, `token`, `password`) — a shallow pattern match, not semantic analysis.

- **Health score: 0–100 with three grade bands.** `Great` (75+), `Needs Work` (50–74), `Critical` (<50). Leaderboard published with named real codebases: executor (96), nodejs.org (86), tldraw, excalidraw. Named-codebase scoring is more inspectable than aggregate marketing figures, though scoring methodology is vendor-defined.

- **Framework-aware rules.** Rule sets toggle based on detected framework (Next.js, Vite, React Native) and React version. React Native-specific rules (e.g., raw text without `<Text>`) are documented as framework-gated. The automation of rule selection is more sophisticated than flat-config linters but framework detection accuracy is not independently verified.

- **GitHub Actions CI integration.** Composite action posts findings as PR comments when a `github-token` is provided. This is a governance integration point: the scanner can become part of a team's quality gate without manual CI configuration beyond a token.

- **CLI output modes: `--json`, `--verbose`, `--diff`, `--explain`.** The `--explain` flag suggests LLM-augmented output (rule rationale, not just rule name). Not confirmed whether `--explain` calls an external LLM or is static prose — claim to inspect.

- **Suppression and override support.** `react-doctor.config.json` with global rule ignores, file-pattern ignores, and per-file overrides. Respects `.gitignore` and existing ESLint/Oxlint configs. This is a pragmatic governance feature for brownfield adoption.

- **Activity indicators.** 275+ commits, 8 open PRs, 1 open issue. The near-zero open issue count may indicate active maintenance, aggressive triage, or incomplete community engagement — cannot distinguish from external observation. No explicit versioning scheme noted.

## Why clawfit should care

**The dual CLI + agent skill form factor introduces a new pattern in the L4 layer.** Most tools in the current L4b sub-type (skill packs) are pure agent skills — they exist to augment agent behavior and have no standalone use. react-doctor is the opposite entry point: it begins as a standalone developer tool and gains an agent-installation path as a secondary distribution. This inverts the typical flow (skill-first → developer adoption vs. developer-first → skill injection). If this inversion pattern spreads, clawfit's L4b classification may need to distinguish between *skill-native* (designed for agents, developer use secondary) and *dev-tool-to-skill* (designed for developers, agent skill as distribution layer).

**The agent skill path directly affects clawfit's `task: code-gen` recommendation surface.** A coding agent running with react-doctor installed gains React-specific diagnostic capability at the point of code generation, not only post-hoc. For a `task: code-gen` + `frontend: react` profile, this is a capability layer improvement — the agent produces diagnostically-guided output rather than unconstrained output validated externally. The current clawfit registry has no way to surface "agent uses this diagnostic rule set during generation" as a scored dimension.

**millionco org provenance is signal-relevant.** million.js addressed a real, measurable React performance problem (virtual DOM overhead) and was absorbed into the React ecosystem as a widely-used optimization primitive. react-doctor repeating the pattern — identify a real React anti-pattern category, build a fast toolchain for it, then wrap it as an agent skill — is consistent with that prior trajectory. Org track record is not a guarantee of product quality but does elevate the signal above a solo-maintainer entry.

**Skill distribution via Skillstore and Lobe Hub.** The presence in two third-party skill marketplaces confirms external distribution infrastructure is being used. This is the same distribution surface as entries already tracked at L4b in the clawfit taxonomy (e.g., agency-agents, obsidian-skills). react-doctor occupies the same distribution slot but with a domain-specific (React) rather than general-purpose scope.

## Preliminary interpretation

Current best reading:

- **Level 4 — Capability / skill / plugin / tool-use layer (primary)**
  - **Sub-type: L4b (domain skill pack, dev-tool-to-skill path).** The agent-installation form factor (`npx react-doctor install`) distributes React diagnostic rules as an agent skill for 50+ runtimes. This is the operative L4b characteristic. The standalone CLI path is a developer tool, not an agent capability.
  - **Secondary sub-type consideration: L4c (static analysis MCP candidate).** react-doctor does not currently ship an MCP server interface — it is a CLI and a skill injector. However, the `--json` output mode and Node.js API (`diagnose()`, `toJsonReport()`, `summarizeDiagnostics()`) are the correct primitives for wrapping as an MCP tool. If an MCP server wrapper ships, it would land solidly in L4c alongside GitNexus and codegraph.

- **Not L3.** react-doctor does not govern agent behavior or function as a team SSOT. The `install` command injects rules into agent context but does not produce a repo-level governance artifact (no `react-doctor.md` spec file, no delta artifact chain). Contrast with OpenSpec or acai.sh, which produce persistent repo-tracked governance artifacts.

- **Not L2.** No orchestration loop, no agent runtime wrapping.

- **Not L6/L7.** No retrieval pipeline, no UI layer, no hardware dependency.

## Status

- 7.5k stars, MIT, millionco org. Above the 5k registry threshold. Candidate for L4b registry entry under a "domain diagnostic skill pack (React)" sub-type. Existing L4b entries (agency-agents, obsidian-skills, anthropics/financial-services) are general-purpose or financial-vertical; react-doctor would be the first frontend-framework-specific L4b entry, occupying the (frontend framework) × (diagnostic/quality) cell. Registry promotion deferred pending: (1) independent verification that the agent skill install correctly injects rules into Claude Code, Cursor, and at least one other named runtime; (2) confirmation of whether `--explain` uses static prose or an external LLM call (affects governance surface). The dev-tool-to-skill inversion pattern is worth tracking as a potential L4b sub-type naming candidate if a second independent tool follows the same trajectory.
