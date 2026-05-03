# Discovery Scans

*Addresses GitHub issue #7 — separation of scans from canonical taxonomy*

---

## Purpose

This directory is the home for **date-stamped discovery content**: daily scan summaries, trending-signal logs, and research-watch cross-references indexed by date.

It is explicitly **separate** from `docs/reference-levels.md`, which is the canonical ecosystem taxonomy. The taxonomy should be stable and human-curated; discovery logs are high-velocity and machine-assisted.

---

## Directory structure

```
docs/scans/
├── README.md              ← this file (index + policy)
├── YYYY-MM-DD-summary.md  ← optional scan-day summary (high-signal days only)
└── index.md               ← rolling index of scan dates + signal counts (optional)

docs/research-watch/
└── YYYY-MM-DD-<tool>.md   ← individual tool/signal analysis documents
                              (primary home for per-signal deep dives)
```

---

## Relationship between this directory and research-watch/

| Content | Location | Owner |
|---------|----------|-------|
| Individual tool analysis (deep dive) | `docs/research-watch/YYYY-MM-DD-<tool>.md` | research-watcher agent |
| Scan-day summary (multi-signal) | `docs/scans/YYYY-MM-DD-summary.md` | daily-ecosystem-scan skill |
| Canonical taxonomy layer definitions | `docs/reference-levels.md` §Level 1–7 | ecosystem-mapper agent (curated) |
| Dated scan log sections | **DEPRECATED in reference-levels.md** — see policy below | — |

---

## Policy: "New signals as of YYYY-MM-DD" sections

**Going forward:** All new dated scan content goes to `docs/research-watch/` (individual tool docs) and optionally to `docs/scans/YYYY-MM-DD-summary.md`.

**Legacy content:** The existing "New signals as of YYYY-MM-DD" sections currently embedded in `reference-levels.md` are preserved as-is (migration is deferred due to the volume and cross-linking cost). They are annotated in the reference-levels.md header as a discovery log, not part of the canonical taxonomy definition.

**When a scan signal should promote to the canonical taxonomy:**
- The signal must be validated by a second independent source
- The ecosystem-mapper agent or a human curator decides it merits a stable taxonomy entry
- The promotion goes into the relevant Level section (e.g., Level 2, Level 4a) — not as a dated bullet but as a named taxonomy entry with star count
- The dated source bullet stays in research-watch/ as supporting evidence

---

## Scan day format (docs/scans/YYYY-MM-DD-summary.md)

```markdown
# Scan YYYY-MM-DD

## Signals collected

| Tool | Source | Stars | Suggested layer |
|------|--------|-------|----------------|
| [name](repo-url) | HN/GeekNews/GitHub Trending | ★NNN | L2 |

## Map mutations applied

- [x] <tool> added to Level N in reference-levels.md
- [ ] <tool> deferred — single signal, needs confirmation

## Registry changes

- `llms.json`: added <name> (evidence: <url>)

## Scoring audit

[healthy / N fixes applied]
```

---

## Why this separation matters

`reference-levels.md` is the document that ecosystem-mapper agents read to calibrate new entries. If it is full of dated scan notes, it is harder to tell what is stable taxonomy vs. in-progress research. Separating them:

1. Makes the canonical taxonomy more readable and stable
2. Lets daily scans move fast without risking taxonomy corruption
3. Allows the taxonomy to be versioned independently of the scan log
4. Makes it possible to run the recommendation engine against a clean, unambiguous level-taxonomy map
