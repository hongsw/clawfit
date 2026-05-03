# Evidence Schema for Registry Entries

*Companion note · Addresses GitHub issue #2*

---

## Problem

The taxonomy currently depends on curated markdown with hand-maintained star counts and descriptive claims. There is no structured way to:
- know when a claim was last verified
- trace a claim back to its source
- assess confidence level for a data point
- distinguish "we verified this ourselves" from "we read it in a tweet"

This matters as clawfit moves from "good essay" to "real comparison engine."

---

## Minimum evidence fields

These fields should be added to all registry entries (`agents.json`, `llms.json`, `hardware.json`):

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `verified_at` | ISO date string | Yes | Date the entry's key fields were last validated against primary sources |
| `evidence_source` | URL string | Yes | Primary source URL for the most important claim (pricing / benchmark / feature) |
| `confidence` | `"confirmed"` / `"reported"` / `"estimated"` | Yes | How firmly established the data is |
| `ecosystem_level` | `"L1"` … `"L7"` | Yes | Primary taxonomy layer from reference-levels.md |

### Confidence values defined

- **`confirmed`** — we personally checked the primary source (official docs, API pricing page, official benchmark report)
- **`reported`** — sourced from a credible third-party report (HN discussion, reputable blog, research paper) but not independently verified
- **`estimated`** — derived from analogy or inference (e.g., "similar to GPT-4o pricing") or community consensus without a clear primary source

---

## Optional evidence fields

| Field | Type | Description |
|-------|------|-------------|
| `secondary_levels` | array of level strings | Multi-layer classification e.g. `["L1", "L4c"]` |
| `benchmark_source` | URL | Specific benchmark citation (SWE-bench, HumanEval, etc.) |
| `benchmark_value` | number | Score at the cited benchmark |
| `benchmark_name` | string | e.g. `"SWE-bench Verified"` |
| `stars_at_verified` | integer | GitHub star count at `verified_at` date |
| `license` | SPDX identifier | e.g. `"MIT"`, `"Apache-2.0"`, `"proprietary"` |

---

## Applied example — DeepSeek V4-Pro (current entry)

**Current `llms.json` entry:**
```json
{
  "id": "deepseek-v4-pro",
  "name": "DeepSeek V4-Pro",
  "provider": "deepseek",
  "tasks": ["code-gen", "research", "qa", "summarization"],
  "latency": "medium",
  "cost_per_1k_tokens": 0.000435,
  "context_window": 1000000,
  "network": "online"
}
```

**With evidence fields added:**
```json
{
  "id": "deepseek-v4-pro",
  "name": "DeepSeek V4-Pro",
  "provider": "deepseek",
  "tasks": ["code-gen", "research", "qa", "summarization"],
  "latency": "medium",
  "cost_per_1k_tokens": 0.000435,
  "context_window": 1000000,
  "network": "online",
  "verified_at": "2026-05-03",
  "evidence_source": "https://api-docs.deepseek.com/",
  "confidence": "confirmed",
  "ecosystem_level": "LLM",
  "benchmark_name": "SWE-bench Verified",
  "benchmark_value": 80.6,
  "benchmark_source": "https://huggingface.co/deepseek-ai/DeepSeek-V4",
  "license": "MIT",
  "stars_at_verified": null
}
```

---

## Applied example — Claude Code (agent entry)

```json
{
  "id": "claude-code",
  "name": "Claude Code",
  "provider": "anthropic",
  "verified_at": "2026-05-03",
  "evidence_source": "https://docs.anthropic.com/claude-code",
  "confidence": "confirmed",
  "ecosystem_level": "L1",
  "secondary_levels": ["L2"],
  "license": "proprietary"
}
```

---

## Migration plan

**Phase 1 (now):** Add `verified_at`, `evidence_source`, `confidence`, `ecosystem_level` to all 17 current registry entries.

**Phase 2 (v0.4):** Add optional benchmark fields to LLM entries that have confirmed benchmark data.

**Phase 3 (v0.5):** Add `test_registry_schema.py` test that validates required evidence fields are present on every entry.

**Phase 4 (v1.0):** Add a `scripts/verify_entry.py` script that spot-checks evidence URLs are still live and benchmark values haven't been superseded.

---

## Schema update for current registry

Minimum backward-compatible change — add evidence fields without breaking existing filters:

The filters in `filters.py` and the scoring in `scoring.py` only read the fields they know about. New fields are ignored by existing code, so adding them to JSON is safe and non-breaking.

Run `python -m pytest tests/ -v` before and after adding fields to confirm no regressions.
