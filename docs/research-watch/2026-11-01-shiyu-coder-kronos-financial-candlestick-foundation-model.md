# Research Watch: Kronos — Open-Source Foundation Model for Financial Candlestick Data

- Repo: https://github.com/shiyu-coder/Kronos (⭐45,180)
- Source: GitHub Trending (all languages + Python, daily, 2026-11-01)

## Why this is worth watching

Kronos is a decoder-only foundation model family pre-trained on candlestick (K-line) sequences from 45+ global exchanges. It is described as "the first open-source foundation model for financial candlesticks," and the paper was accepted at AAAI 2026. The star count (45k) is high relative to a specialized domain research model, which suggests either strong community validation or significant amplification from financial ML communities.

The technical claim is straightforward: instead of adapting a general-purpose time-series foundation model to financial data, Kronos trains a domain-specific tokenizer that encodes multi-dimensional OHLCV data into hierarchical discrete tokens before pre-training an autoregressive Transformer on them. Whether this domain-specific tokenization outperforms existing general-purpose TSFMs in out-of-distribution financial regimes is not established by the AAAI paper alone — the benchmark is the paper's own backtesting pipeline.

## What stands out immediately

- **Candlestick-specific tokenizer**: converts OHLCV data into hierarchical discrete tokens; this is architecturally distinct from projecting scalar time-series into a shared embedding space, as general-purpose TSFMs typically do
- **Model zoo**: four sizes — Kronos-mini (4.1M), Kronos-small (24.7M), Kronos-base (102.3M), Kronos-large (499.2M); the largest is not open-source
- **Probabilistic forecasting**: supports temperature, top-p, and sample_count; outputs are distribution samples over future K-line sequences, not point forecasts
- **45+ exchanges**: claims coverage across global markets including A-share; this is broader geographic scope than existing public TSFMs (TimesFM is largely US/Euro industrial; Timestral focuses on telemetry and industrial data)
- **Simple API surface**: `KronosPredictor.predict()` handles preprocessing, normalization, prediction, and inverse normalization in one call — low integration friction for quantitative researchers
- **AAAI 2026 peer review**: provides credibility baseline; the paper was not a workshop submission
- **MIT license**: permissive; commercial use permitted
- **Fine-tuning pipeline included**: Qlib-based data prep, tokenizer fine-tuning, and backtesting are documented; users can adapt to exchange-specific data or additional features

## Why clawfit should care

Kronos is the third time-series / domain-specific foundation model signal in the tracker, after TimesFM (Google, 2026-08-16, general-purpose industrial time-series with agent integration) and Mistral Timestral (2026-10-19, industrial telemetry). Kronos extends the pattern to a different domain — financial market prediction — and to a different technical stance: domain-specific tokenizer rather than a general-purpose temporal embedding.

The three-signal cluster now spans:
- Industrial time-series inference (TimesFM, Timestral)
- Financial market forecasting (Kronos)

This is not yet the same sub-type. TimesFM and Timestral share the industrial telemetry domain; Kronos is financial. Two signals for "financial domain foundation model" would require a second (TimesFM announced a financial fine-tune or a competitor in the same OHLCV space). At present, Kronos is a first signal for this specific combination of architecture choice (candlestick tokenizer) and domain (financial markets).

For clawfit registry: Kronos is an LLM-class entry (it is a domain-specific model), not an agent entry. The registry currently models LLMs by cost and latency, not by domain specialization. A `domain: financial` or `domain_specialization` field in `llms.json` would be needed to model this class of entry meaningfully.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base Model** (primary): a domain-specific pre-trained model that provides the inference foundation for financial quantitative workflows
- **Level 5 — Evaluation / Research** (secondary): the AAAI paper and backtesting pipeline are structured as an evaluation contribution

## Claims to verify

- Whether the "first open-source foundation model for financial candlesticks" claim holds — there are prior financial time-series models (N-BEATS, PatchTST, Moirai) but none are specifically tokenized for K-line data; worth a literature check
- Whether the backtesting results are on train/test-split historical data or true out-of-sample; the AAAI publication provides credibility but in-sample overfitting is a known risk in financial ML
- Whether Kronos-large (499.2M) is available via API, or withheld entirely; the README says not open-source but does not say whether it is commercially accessible
- Star count trajectory: 45k is high for a research model; whether the star count reflects genuine quant community adoption or a short-term HN/social spike would change the urgency of tracking

## Status

- New signal; not previously tracked
- Registry eligibility: LLM-class model; would need `domain: financial` schema field to add meaningfully — no registry addition at this time
- Watch for: a second financial foundation model signal, or TimesFM financial fine-tune announcement — would confirm "domain-specific financial TSFMs" as a registry sub-type
- 📡 note: third time-series foundation model signal (after TimesFM and Timestral); domain cluster is forming but not yet homogeneous enough for a canonical taxonomy entry
