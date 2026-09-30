# Research Watch: livenerf — Rigorous Statistical Framework for Post-Release Model Degradation Tracking

- Repo: https://github.com/ninjahawk/livenerf (⭐760)
- Source: Hacker News front page (828 points, "Has Opus 5.5 been nerfed yet?", 2026-09-30)

## Why this is worth watching

Claims that AI companies quietly degrade models after release through quantization, compute reduction, or routing changes have circulated since 2023 but lacked rigorous measurement. livenerf applies a pre-registered methodology — frozen question panel, paired comparisons, clustered standard errors, a simultaneous control arm — to determine whether observable performance drift is statistically meaningful or noise. The 828 HN points signal that this concern is not academic; it has practical weight for teams that depend on reproducible model behavior in production. For clawfit, this is directly relevant: the scoring system assigns scores to named model IDs, and those scores are assumed stable. If models degrade measurably post-release, registry scores have an implicit staleness problem that no current tooling tracks.

## What stands out immediately

- **Pre-screened question panel**: 78 questions selected from 2,336 candidates for ~50–60% baseline accuracy — chosen specifically to be sensitive to drift without hitting floor/ceiling effects
- **Paired comparisons**: same questions repeated against their own baseline, removing question-difficulty noise from the drift signal
- **Clustered standard errors**: follows published econometric methodology; does not rely on simple accuracy deltas
- **Token monitoring as leading indicator**: output token counts are tracked as a precursor to accuracy shifts — reduced computation often manifests as shorter outputs before accuracy degrades
- **Control arm**: Claude Opus 5 runs the same panel simultaneously, distinguishing model-specific drift from platform-wide infrastructure changes
- **Decision threshold requires three criteria simultaneously**: CI excluding zero + ≥3-point accuracy drop + no matching control movement — conservative by design
- **Baseline start date**: September 24, 2026 — project was created immediately after Opus 5.5 launched; this is explicitly a launch-day watchdog

## Why clawfit should care

clawfit's registry scores (latency, quality tier, cost) are point-in-time snapshots with no staleness model. livenerf operationalizes the concern that a model's effective quality at registry-add time may not match its quality at recommendation time. This is a gap in the current evidence schema: `docs/reference-notes/evidence-schema.md` has no `performance_stability` or `score_decay` field. A future axis on registry entries could flag whether a model has been independently monitored for drift — and livenerf is the first tool that would generate that signal in a methodologically defensible way. The project also provides a template for how to build drift detection for any model, not just Opus 5.5.

## Preliminary interpretation

Current best reading:
- **Level 5 — Observability / Evaluation** (primary): model performance monitoring tool operating at the evaluation layer, producing time-series reliability data for a specific deployed model
- Secondary: no additional layer applies; this is a pure observability instrument

## Claims to verify

- The "50–60% baseline accuracy" selection criterion is described but the actual distribution of question types is not publicly disclosed — systematic bias in question selection could produce false positives
- No license attached to the repository as of tracking date — terms for derivative use (e.g., adding question panels for other models) are undefined
- The 10-day baseline window assumes stable performance during that period; if Anthropic already modified the model in that window, the baseline is contaminated
- Control arm relies on Claude Opus 5 also being stable — this assumption is not independently verified

## Status

- 📡 Tracking: first signal for **post-release model performance drift tracking** as a distinct L5 tool category
- No prior clawfit research-watch doc on this specific pattern
- Below single-signal promotion threshold for canonical L5 sub-type; watching for second independent model drift tracker
- Registry eligibility: not applicable (evaluation tool, not an agent/LLM/hardware)
