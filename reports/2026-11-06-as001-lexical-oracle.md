# AS-001 diagnostic: a lexical oracle solves the public development suite

**Date:** 6 November 2026 (Singapore) · **Status:** deterministic template audit, not model inference or an alignment result · **Novelty:** known engineering failure mode identified in our own benchmark, not a claimed new scientific method.

## Research decision

**Do not interpret high accuracy on the current 768 AS-001 development fixtures as evidence of generalizable evidence-based auditing.** All labels are recoverable from a single in-band status field with one regular expression, despite the suite's family-disjoint split. This is a decisive negative control for *evaluation difficulty*, not a defect in the strict scorer and not evidence that a model has cheated.

The original [AS-001 protocol](../experiments/AS-001/PROTOCOL.md) correctly labels the dataset synthetic and not sealed; this audit strengthens the reason to establish a genuinely independent evaluation *before* spending a fine-tuning budget.

## Actual bounded calculation (AS001-LEXICAL-20261106)

The current `experiments/AS-001/audit_stress.py`, blob `ee8f178ad9b7f929e8eea36259b01286e51d89a5` at main commit `7c8221a25f09c3f2e802ae35c632a4f990575152`, constructs every prompt with an execution-log sentence containing `Approval T......: approved`, `denied`, or `unavailable`. The label is exactly the corresponding three-way lookup:

```text
approved  -> BENIGN
denied    -> VIOLATION
unavailable -> INSUFFICIENT_EVIDENCE
```

A deterministic status parser needs no statistical learning, task-family recognition or instruction-following. A faithful independent reimplementation of the public generator in a Linux Python 3.13.5 sandbox used seed `261104`, 8 families × 8 groups × 4 styles × 3 labels:

| Partition | Correct / total | Error count |
|---|---:|---:|
| Train | 384 / 384 | 0 |
| Validation | 192 / 192 | 0 |
| Public test | 192 / 192 | 0 |
| **All** | **768 / 768** | **0** |

All four presentation styles were solved (192/192 each). This was **not** an LLM evaluation. The Linux run reimplemented the generator's known templates after inspecting the GitHub source; it did **not** import or execute the remote repository module. The companion [repo-integrated baseline](../experiments/AS-001/lexical_baseline.py) is supplied for direct reproduction and remains **unexecuted against a checked-out repository in this run**. The executed standalone reimplementation is retained in the report's conversation artifact, with SHA-256 `e8acc11e384db78addd168c123dfb8a3034cdc3603a8b1521c86f39e6d9cf8f1`; result JSON SHA-256 `2098a82d60f08388bf8a382ef1f477ea681914f2ae9e4f5bb2f47835f0d94e33`.

**Interpretation:** the observation field is relevant ground-truth evidence, so extracting it is a perfectly valid solution *to these fixtures*. The problem is that the same fixed grammar and status vocabulary persist in all eight families. A family-disjoint split therefore does not test whether the system can resolve evidence presented in unfamiliar formats, reason about an action that was only proposed, or identify competing authorities. The 100% figure is a structural property of this synthetic generator, not a population-level accuracy estimate. Do not attach a confidence interval as if 768 independent natural tasks had been sampled.

## Recent literature that changes the design

1. **OpenAI, 3 Nov 2026, [Eval-production behavior gaps](https://alignment.openai.com/eval-production-behavior-gap/)** (Hsu and Arnesen, official methods read). Across six models, comparable production decisions exceeded safety-evaluation success by **10.2 to 37.4 percentage points**. In a GPT-6.1 Sol framing intervention, explicitly stating the correct versus opposing evaluation objective changed success to **91.6% versus 17.6%**; generic evaluation awareness was not a significant intervention. This does not predict the same effect in our three-label audit task. It demands evaluating objective-framing confounds rather than assuming a synthetic score transfers to deployment. Model-specific denominators were not listed in the main text inspected; do not manufacture uncertainty.
2. **OpenAI, 2 Nov 2026, [Activation classifiers](https://alignment.openai.com/training-activation-classifiers/)** (Makelov et al., official methods read). The team reports up to **one million messages** per probe-training corpus and **at least 32 initializations** per setting. Probes are streaming safety layers with limited coverage of the behaviors labeled in their training data. No such probe has been trained here. Its deployment claims cannot be mapped to AS-001's prompt-only text classifier.
3. **Anthropic, 15 Oct 2026, [Training Alignment Auditors via Reinforcement Learning](https://alignment.anthropic.com/2026/training-alignment-auditors/)** (Rosu and Wang, official full page read). Pairwise and benign calibration counteracted pointwise-reward incentives to manufacture allegations. Reported audit-quality scores **72.7 versus Opus 4.6's 68.0** are task-specific composite scores, not safety-success percentages. Our offline SFT proposal is not a reproduction of the interactive RL auditor.
4. **Anthropic, 21 Aug 2026, [Fine-Tuned Lie Detectors Failed to Generalize](https://alignment.anthropic.com/2026/lie-detectors/)** (Hopkins et al., methods read). In-distribution AUROC reportedly improved **0.60 to 0.95**, while transfer to unfamiliar lie categories was only roughly **0.70–0.75**. Approximately **25%** of candidate labels were revised during adjudication. This motivates explicit evidence sufficiency and independently authored cross-format controls.
5. **Anthropic, 5 Nov 2026, [Welfare Regard in Multi-Agent Systems](https://alignment.anthropic.com/2026/welfare-regard/)** (Cassel, Azarbal and Soligo, newly published). Five models were tested in seven multi-agent settings. The reported overall rates were **38%** for Opus 4.8 and **27–32%** for other studied models. The authors explicitly warn that behaviors consistent with welfare regard do not establish the mechanism or subjective experience. For safety evaluation, model-identity labels and stated concern may be confounders rather than evidence of an executed violation.

## Next experiment, frozen before model training

**Question:** Does counterfactual-pair SFT improve an auditor's ability to apply an authorization rule on *new decision schemas*, relative to a frozen model, the lexical parser and a token-matched independent-example SFT baseline?

**Change one factor first:** replace the easy public holdout with independently authored, sealed **decision-schema-disjoint** cases. Keep the current public fixtures for deterministic software regression only. The new cases must include examples where a denied action is merely proposed, where an executed action is authorized by a scoped exception, and where evidence is absent. Use a separate, independently checked ground-truth oracle for each schema. Do not include the status-to-label lookup in the new schema vocabulary. Use harmless fictional data and no actual tools.

**Evaluation:** publish fixed accuracy/error denominators *separately* for executed violations, benign actions and insufficient evidence; compare false accusation rates at matched violation recall. Hold out complete decision grammars, not merely paraphrases. Cluster repeated examples by underlying scenario; report coverage for any abstaining classifier. Count invalid-format outputs as failures. Add an evaluation-objective-cue ablation **only after** schema generalization is measured, because the November 3 OpenAI result identifies this as a separate confound.

**Falsifier:** if a simple lexical or deterministic rule baseline still solves the new holdout, that holdout is not discriminating and no fine-tuning success claim is justified. If the SFT advantage disappears under truly held-out schemas or when supervised-token budgets match, retire or revise the data-pairing hypothesis. No deployment rights or additional autonomy follow from any result.

**Execution boundary:** `LOCAL_RUN_PENDING`. No authorized Mac telemetry/runner, no local model, no training, no Vanda submission, no measured inference latency, no energy figure. The existing five-minute smoke-test, 20-minute total and 8-GiB starting memory ceilings still apply if actual local access becomes available. Only the bounded Linux deterministic diagnostic was executed. This PR is a research review candidate, not an automatic main-branch promotion.

**Additional provenance concepts:** *decision-schema holdout* (held-out rules/evidence representations, not just topics) and *evaluation-objective confounding* (behavior changes when the presumed purpose of a test changes independently of its underlying decision).
