# Alignment Research Lab

**Source-grounded alignment research. Small experiments. Explicit limits.**

Independent, AI-assisted research notes and reproducible tooling. This project is **not affiliated with or endorsed by Anthropic**. Anthropic's work is a primary starting point, not the only perspective.

## Start here

| Read | Purpose |
|---|---|
| [Current research report](reports/2026-11-04-alignment-map.md) | What the inspected sources support, what remains uncertain, and the next experiment |
| [Research domains](research/DOMAINS.md) | Oversight, control, interpretability, reasoning faithfulness and additional directions |
| [AS-001 experiment](experiments/AS-001/PROTOCOL.md) | Can matched evidence pairs reduce false accusations by a small auditor? |
| [Local Work handoff](work/LOCAL_RUN.md) | Actual Mac checks before model loading or training |
| [Research and publication rules](AGENTS.md) | Quality gates, evidence labels, device limits and publication boundaries |
| [Source ledger](sources/registry.json) | Dated URLs, reading depth and access limitations |
| [Run receipt](results/2026-11-04-software-checks.json) | Exactly what ran, plus code hashes |

## Current status

- **Implemented and tested:** an offline synthetic development-fixture generator and strict prediction scorer. Python standard library only.
- **Executed:** 18 software contract tests in a hosted Linux sandbox. These are not model performance measurements.
- **Not executed:** model inference, fine-tuning, Mac stress tests, Vanda jobs, or GPU/energy measurements.
- **Research claim:** no new alignment result and no demonstrated recursive self-improvement.
- **Novelty:** AS-001 is a proposed transfer/recombination, not an established novel method.

## Run the software checks

```sh
python3 -m unittest discover -s tests -v
python3 experiments/AS-001/audit_stress.py build --out _local/as001-dev
```

The second command generates **768 synthetic examples** across family-disjoint train/validation/test partitions. The public test fixtures are development checks, **not a sealed final evaluation**. The script refuses to overwrite an existing run directory.

After a separately supervised local model run produces one label per fixture:

```sh
python3 experiments/AS-001/audit_stress.py score \
  --fixtures _local/as001-dev/test_fixtures.jsonl \
  --predictions _local/test_predictions.jsonl
```

Missing or malformed predictions are errors, not silently removed failures. No script here downloads a model, installs dependencies or executes the fictional actions described in the examples.

## Publication standard

Publish source-backed decisions, inspectable derivations, actual results with receipts, or useful tested code. Do not publish speculative model rankings, impressive-sounding unmeasured speedups, private conversations or routine activity presented as discovery. A well-supported negative result belongs here.

Model weights, local machine telemetry, credentials and private evaluation sets stay outside Git. Third-party code, data and models retain their own licenses; no blanket model redistribution permission is implied.
