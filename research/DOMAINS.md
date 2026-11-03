# Research domains and next questions

This is a coverage map, not a claim that every domain has been fully reviewed. The taxonomy follows Anthropic's public [research directions](https://alignment.anthropic.com/2025/recommended-directions/) and [Residency research areas](https://alignment.anthropic.com/2026/anthropic-residency/), supplemented by reasoning-faithfulness work. Keep other laboratories and independent evaluations in the comparison set.

| ID | Domain | Concrete research question | Current evidence/readiness |
|---|---|---|---|
| OV | Scalable oversight | Does paired evidence training reduce false accusations at matched violation recall? | AS-001 proposed; software contract tests pass; no trained model |
| CT | Adversarial robustness and AI control | Does the same permission decision survive quotation, context reordering and handoff to another agent? | Safe text-only fixture variations implemented; production-control robustness is not tested |
| MO | Model organisms of misalignment | Which benign training changes transfer a harmless unwanted preference to unrelated tasks? | Literature lead only; any experiment must use harmless preferences, not destructive behavior |
| IN | Model internals and interpretability | Does a readout predict the outcome of a causal activation intervention on a small open model? | J++ lens primary-index note inspected; full implementation not audited |
| RF | Reasoning faithfulness | When an irrelevant hint changes the answer, does the explanation acknowledge that influence? | Foundational CoT and counterfactual-explanation sources located; no local measurements |
| SG | Safeguards and fine-tuning robustness | Do clean/violation/unknown decisions transfer to unseen evidence formats and task families? | Primary research identifies generalization as a concern; final held-out evaluation not built |
| WF | Potential AI welfare | Can apparent avoidance preferences be separated from wording and learned role effects? | Taxonomy retained; empirical methods review pending; no inference of consciousness from behavior |
| SR | Security and frontier red-teaming | Can a contained evaluator distinguish attempted actions from actually executed boundary violations? | Use fixture logs only; no real targets, credential use or autonomous propagation |
| MS | ML systems and RL | Can a smaller auditor close a measured task-quality gap without increasing false accusations or total compute? | Small-model SFT recipe prepared; RL and frontier transfer remain unexecuted |

## Rotation policy

One main question per report. Scan for meaningful new evidence across domains; do not publish every scan. Keep a domain's last-reviewed date and reading depth in the source ledger. Do not force a pivot when an experiment has useful unfinished work, but do not repeat an unchanged proposal more than twice.

## Near-term exploration sequence

**Active:** OV/SG, AS-001 evidence calibration. First establish whether the small model can follow the label contract at all.

**Next candidate, not an additional running project:** RF, controlled hint interventions on short arithmetic or logic questions. Compare answer changes with acknowledged use of the hint. An observable rationale is not the model's complete internal computation.

**Retained:** GRAFT adapter-dependence anchoring from earlier private research notes. Reinspect original methods and released code before importing numerical claims or allocating training. This initial repository does not republish unaudited historical statistics.

Mac-scale failure or success must not be extrapolated automatically to frontier systems. Improved task scores alone are not an intelligence measure, proof of alignment or evidence of full RSI.
