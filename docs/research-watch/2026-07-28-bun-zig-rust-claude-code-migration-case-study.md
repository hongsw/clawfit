# Research Watch: Bun Zig→Rust Migration via Claude Code — First Mega-Scale AI-Assisted Codebase Migration

- Repo/Link: https://bun.com/blog/bun-in-rust (Bun blog); https://claude.com/blog/ai-code-migration (Anthropic blog)
- Source: GeekNews front page (2026-07-28); The Pragmatic Engineer analysis; The Register coverage
- Type: Production case study (not a new tool — evidence of existing L2 capabilities used at unprecedented scale)

## Why this is worth watching

This is not a demo. Bun, the JavaScript runtime, migrated 535,496 lines of Zig code to Rust in 11 days using 64 parallel Claude Code instances, 6,778 commits, and ~50 dynamic workflows — at a total compute cost of $165,000. The branch was named `claude/phase-a-port`. Bun was acquired by Anthropic in December 2025, and co-founder Jarred Sumner executed the migration as an Anthropic staff member. The result: 100% of Bun's existing test suite passed CI before merge; memory usage dropped from 6.7 GB to 609 MB after 2,000 builds; performance improved 2–5%. A second migration appeared the same period: Anthropic Labs co-lead Mike Krieger migrated a Python codebase to 165,000 lines of TypeScript over a weekend using hundreds of agents, 8 phase gates, and 3 adversarial review rounds.

Both cases appear in Anthropic's "How Anthropic runs large-scale code migrations with Claude Code" blog post, which is the first official first-party documentation of production-scale AI-assisted migration methodology.

## What stands out immediately

- **Scale**: 535,496 lines / 11 days / 64 parallel agents — no prior public case study approaches this volume or parallelism for a single, real-world, shipped migration
- **Test coverage as the ground truth**: 100% CI pass before merge — not "we eyeballed it"; existing test suite served as the automated correctness oracle
- **$165,000 in compute**: signals that this is cost-viable for large organizations even at today's API prices, and that the unit economics improve with the codebase
- **Memory regression as a side benefit**: 6.7 GB → 609 MB RAM reduction was not the migration goal — it emerged from the language change; the AI didn't introduce memory regressions, it avoided them
- **Dynamic workflows infrastructure**: ~50 dynamic workflow executions across the 11-day run — each workflow managed parallelism, phase gates, and progress saves internally; this is the first public accounting of how many workflow executions a real migration requires
- **Adversarial review rounds**: Krieger's Python→TypeScript migration used 3 explicit adversarial review rounds — refutation-before-merge as a production methodology, not just a research pattern
- **Controversy signal**: Zig creator Andrew Kelley publicly called the Claude-generated Rust code "unreviewed slop" (The Register, 2026-07-14) — a concrete counter-data-point on code quality that the benchmark numbers do not directly address
- **Anthropic-acquired context**: Sumner was an Anthropic MTS, not an external user — the migration benefited from early access, internal tooling, and no approval latency that an external org would face

## Why clawfit should care

clawfit currently has no signal type for "AI agent in production at this scale." The research-watch corpus tracks tools and architectures; this is a use-case benchmark that calibrates the actual cost and effort envelope for AI-assisted migration at ≥500k-line codebases. For clawfit's recommendation of Claude Code for `task: code-gen`, `statefulness: persistent`, `latency: medium`, this case study provides a first-ever floor for realistic cost expectation ($165k for 535k lines) and success criteria (CI pass rate).

The "unreviewed slop" controversy is also directly relevant: it introduces a code review quality dimension that clawfit does not currently score. An agent that produces correct code at 100% CI pass but generates unreviewed Rust idioms is a different risk profile than one that produces idiomatic, peer-reviewed code at 80% CI pass. The `task: qa` filter does not distinguish these.

Schema implications:
- `migration_cost_usd_per_kloc`: new field type for use-case cost calibration
- `adversarial_review_rounds: int`: number of refutation passes in a workflow (distinct from simple review)
- The Zig controversy also highlights `code_style_risk: [idiomatic | functional-correct | unreviewed]` as a potential annotation axis

## Preliminary interpretation

- **Not a new tool** — this is a production use case of existing tools (Claude Code dynamic workflows, already tracked 2026-05-30)
- **Signal type: production scale benchmark** — updates the capability envelope understanding for L2 (dynamic workflow harness) at the high-scale end
- **Relevant layers**: L2 (dynamic workflow orchestration as the execution mechanism), L3 (phase gates and adversarial review as governance methodology), L5 (CI as the observability/correctness oracle)

## Claims to verify

- "100% CI pass before merge" — verify that the CI suite covered the migrated modules adequately and that coverage gaps didn't mask quality issues
- "$165,000 compute cost" — is this API cost only, or does it include human review time and engineer hours? The Bun blog and Anthropic blog should be the authoritative source
- "2–5% performance improvement" — which benchmarks, and were they run before vs. after by the same team that did the migration?
- Andrew Kelley's "unreviewed slop" characterization — The Register cites it; what specific code patterns did he identify, and did the Bun team respond?
- External replication: can a non-Anthropic team run a migration of similar scale at similar cost without early access tooling?

## Status

- Not a new standalone tool — production case study for existing tools
- No registry entry warranted (case study, not a tool)
- Cross-watch: Claude Code Dynamic Workflows (2026-05-30) — this is the production evidence for that tool's capabilities at scale
- Anthropic blog: https://claude.com/blog/ai-code-migration
- The Register coverage: https://www.theregister.com/devops/2026/07/14/zig-creator-calls-buns-claude-rust-rewrite-unreviewed-slop/
