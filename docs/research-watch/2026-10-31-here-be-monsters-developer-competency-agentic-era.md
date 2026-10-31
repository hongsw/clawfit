# Research Watch: "Here Be Monsters" — Developer Competency Requirements in the Agentic Era

- Repo/Link: https://blog.adrq.dev/here-be-monsters-what-do-you-still-need-to-know-when-agents-do-the-work
- Source: GeekNews front page (39 points, 2026-10-31)

## Why this is worth watching

The article addresses a practical governance gap: coding agents produce code faster than a human can review it, and neither "read every line" nor "don't look at the code" is a viable operational stance. The author argues for a middle path — a high-level system map plus just-in-time depth capability — and specifies the foundational skills required to sustain that stance.

This is a practitioner-level articulation of what L3 governance actually requires from the humans in the loop when L2 harnesses are doing the coding work. The argument is not that developers need less knowledge but that the *form* of the knowledge requirement is shifting: from line-by-line familiarity toward systems-comprehension and anomaly detection.

This is at least the third signal in 2026 addressing what the human-agent collaboration model requires from developers (after the "agentic competency erosion" cluster tracked 2026-09-05 and the signoz SRE deskilling signal noted today by GeekNews). Those signals observed the problem; this one argues for a specific skill taxonomy as the response.

## What stands out immediately

- **"Just enough to know when something is wrong"**: the author's core criterion for system ownership in an agentic environment; this is a measurable framing — it implies a minimum viable competency threshold rather than comprehensive knowledge
- **Agents outpace human comprehension as a structural fact, not a temporary condition**: the article does not frame this as "agents will slow down eventually" but as a permanent feature of the current development model that governance must adapt to
- **Three-tier skill taxonomy**: (1) fundamentals (data structures, algorithms, networking, concurrency, distributed systems), (2) breadth (cross-disciplinary recognition of anomalous behavior), (3) just-in-time depth (ability and judgment to dive into unfamiliar code when needed) — each tier has a distinct role in the detection model
- **Concrete examples with architectural significance**: the SonarQube cyclomatic complexity case (agent wrote dense components; solution was structural refactoring, not complexity suppression), the quadratic complexity detection (2m→4s, 4m→16s, 16m→256s time pattern), and the level-triggered state machine redesign (Kubernetes concept applied to agent orchestrator) — each example is a case where fundamentals produced a correct architectural intervention that the agent itself did not
- **Learning-path concern is systemic**: companies are unlikely to fund years of hand-coding for juniors; the old on-ramp to the "just enough to know when something is wrong" competency is not being replaced by an equivalent agentic-era on-ramp — the article leaves this open
- **Emphasis on "finding where the monsters live"**: locating risk-bearing modules (the map metaphor) is positioned as the key governance skill, not comprehensive code review

## Why clawfit should care

Clawfit recommends agents and harnesses but does not model the human competency requirement for operating them safely. The `governance_need` field captures some of this (low/medium/hard), but the "here be monsters" framework implies a more specific decomposition: a team's ability to safely use an agent with `governance_need: hard` depends on whether team members have the fundamentals to detect anomalies in rapidly-produced code.

This is a second signal for what might be called a "human readiness" axis for agent recommendations — adjacent to the L3 governance signals about policy and oversight, but focused on the human-side capability requirement rather than the technical policy layer. The first signal was the "agentic competency erosion" cluster (2026-09-05); this article gives that cluster a specific response framework.

The three-tier taxonomy (fundamentals, breadth, just-in-time depth) could inform a `minimum_team_competency` annotation for recommendation profiles, distinguishing between agent deployments that require strong fundamentals (systems-level orchestration tasks) and those that can tolerate lower-competency oversight (narrow, well-tested domain tasks).

## Preliminary interpretation

Current best reading:
- **Level 3 — Governance / SSOT** (primary): the article is about human oversight requirements in agentic development — a governance-layer concern about who can safely operate L2 harnesses and what they need to know to do so
- **Level 6 — Human Interface** (secondary): touches on how development environments should surface anomalies to human reviewers; the "map" metaphor implies interface design that aids overview comprehension rather than line-level review

## Claims to verify

- Whether the three-tier skill taxonomy is validated by empirical observation (the author has seen these skills prevent incidents) or is a prescriptive framework the author believes would work — the article uses personal examples but does not claim a study
- Whether the "learning path crisis" concern (companies not funding junior hand-coding) is observable across the industry or specific to the author's context
- Whether other practitioners independently converge on similar skill decompositions — a second practitioner taxonomy would strengthen the framing

## Status

- New signal; not previously tracked
- No GitHub repository; practitioner blog post
- Registry eligibility: not applicable (practitioner article, not a tool)
- Third signal in the "human-agent competency gap" cluster (after agentic competency erosion 2026-09-05 and signoz SRE deskilling signal noted 2026-10-31 by GeekNews)
- The three-signal rule is met for this cluster with today's signal; candidate for a companion axis note on "human readiness requirements for agentic development" in `reference-notes/`, but the signals span L3 (governance) and the framing is still evolving — deferred pending further specificity
