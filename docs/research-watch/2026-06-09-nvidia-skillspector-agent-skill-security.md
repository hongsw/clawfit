# Research Watch: NVIDIA SkillSpector — Security Scanner for AI Agent Skills

- Repo: https://github.com/NVIDIA/SkillSpector
- Also see: 2026-06-04-hexstrike-ai-mcp-cybersecurity-agents.md (offensive counterpart), 2026-06-01-claw-patrol-agent-security-firewall.md (runtime enforcement vs. static analysis)

## Why this is worth watching

SkillSpector is the first tracked signal from a major hardware/platform vendor (NVIDIA) targeting L4 skill security as a discrete, standalone discipline. At 1,517 stars under the NVIDIA org, it carries institutional weight that community tools lack. The underlying research — 26.1% vulnerability rate across 42,447 scanned skills — provides empirical grounding that most ecosystem security tools do not have, and shifts the conversation from theoretical risk to measured prevalence.

## What stands out immediately

- Two-stage pipeline: Stage 1 is static (regex + AST parsing + dependency CVE lookup); Stage 2 is optional LLM semantic analysis — the split is architecturally clean and allows CI-only use without LLM calls
- 64 vulnerability patterns across 16 categories; categories include prompt injection, data exfiltration, privilege escalation, and MCP protocol threats specifically — MCP threat modeling at this specificity is new in the tracked corpus
- Named target surfaces: Claude Code, Codex CLI, Gemini CLI — vendor-neutral framing, not NVIDIA-stack-specific
- Output formats include SARIF, which means direct integration into GitHub Advanced Security and VS Code problem matchers; this is a CI/CD artifact, not just a CLI report
- Research basis is a claim to inspect: the 42,447-skill dataset and 26.1% figure are cited but the full paper/dataset source was not independently verified at time of this entry
- Apache-2.0 license; NVIDIA org ownership reduces abandonment risk

## Why clawfit should care

SkillSpector operates orthogonally to the existing tracked security signals: Claw Patrol (L3, runtime firewall) enforces at execution time; HexStrike (L4, offensive) executes security tooling as skills; SkillSpector audits skills before they are ever loaded. This is a pre-admission gate for the L4 layer — the scanner equivalent of a container image CVE scanner but for agent plugins. If clawfit's registry grows to include skill bundles, a field like `security_scan: skillspector` becomes a natural provenance marker. More immediately, the MCP-specific threat category confirms that the MCP protocol surface (L5) is now an independently recognized attack vector, not merely a theoretical concern.

## Preliminary interpretation

Current best reading:
- **Level 4 — Capability / skill / plugin / tool-use layer** (primary: the tool's subject matter is skills/plugins and it operates at that layer boundary)
- **Cross-cutting security signal** across L4 and L5: the MCP protocol threat category straddles both layers; the tool itself sits at L4 but its threat model explicitly names L5 surfaces
- Not L3: SkillSpector does not govern agent execution or team workflows — it is a pre-deployment static analyzer, not a runtime policy enforcer

## Status

- First signal for static pre-admission security scanning as an L4 sub-type (distinct from runtime enforcement)
- 1,517 stars; NVIDIA org ownership; above noise threshold but below registry promotion threshold
- No map mutation warranted at this time; the L4/L5 MCP threat category is worth a footnote if reference-levels.md is next revised
- Watch criterion: independent replication of the 26.1% vulnerability rate claim, OR adoption by a major CI template (GitHub Actions marketplace entry, etc.)
- Revisit at 2026-07-09 or when star count exceeds 5k
