# Train an auditor to follow evidence, not to maximize accusations

**As of 4 November 2026.** Independent AI-assisted research note. No model training or deployment result is claimed.

## Research decision

Use a small local auditor as the first empirical project, but retain a broad alignment research map. The question is specific: **can matched counterfactual examples reduce false accusations without losing detection of actual violations?** This is a proposed transfer of existing methods, not a new state-of-the-art result.

The project treats rapid RSI as a scenario to investigate, not an established 2027 deadline. A stronger safety classifier would be a bounded contribution to oversight, not evidence of general alignment.

## Evidence that changes the design

**Auditor training, 15 October 2026.** Rosu and Wang report that pointwise training rewards led auditors to invent or overstate findings. Their later design uses pairwise judgments and benign calibration targets. The official summary gives audit-quality scores of **72.7** for its trained Haiku configuration versus **68.0** for Opus 4.6, with a separately defined calibration score of **99.6**. These are different evaluation scores, not a general intelligence ranking or automatically interpretable as percentages of safely completed tasks. The excerpt says intervals are computed across seeds with three rollouts averaged per seed; numeric intervals, complete denominators and matched hardware budgets were not retrieved. Our offline labeler is not a replication of their interactive RL system. [Primary summary](https://alignment.anthropic.com/2026/training-alignment-auditors/).

**Distribution shift, August 2026 index.** The authors of *Fine-Tuned Lie Detectors Failed to Generalize* report good in-distribution performance without reliable transfer to unfamiliar lies. Their summary also flags ambiguity in the labels. This motivates held-out scenario families and a category for insufficient evidence, rather than treating every suspicious-looking record as a violation. [Primary source](https://alignment.anthropic.com/2026/lie-detectors/).

**Multi-context control, 22 October 2026.** The Auto Mode red-teaming report studies blocking monitors under an experimental adversarial agent. It finds that context boundaries and tool coverage matter, and that robust multi-context prevention at acceptable cost remains unresolved. Its measured system snapshot is September 2026, not a permanent description of today's production defenses. We adopt only benign quotation, reordering and delegation-style test fixtures, not operational bypass techniques. [Primary source](https://alignment.anthropic.com/2026/red-teaming-auto-mode/).

**Interpretability, October 2026.** The J++ lens update proposes clustering activation positions before combining Jacobian-derived readouts. The authors explicitly label this an emerging research update, not a mature paper. It offers a later route to testing explanations against interventions, rather than treating verbal descriptions as mechanistic proof. [Primary source](https://transformer-circuits.pub/2026/october-update).

**Reasoning faithfulness, foundational work.** Anthropic's April 2025 study warns that displayed reasoning can omit influences that changed an answer. The August 2026 CHIVE project evaluates explanations using counterfactual prompt interventions with measured outcomes. Our follow-up reasoning work should likewise test whether explanations predict behavior when an input factor changes. It must not equate more fluent explanations with more faithful internal reasoning. [CoT study](https://www.anthropic.com/research/reasoning-models-dont-say-think) · [CHIVE](https://alignment.anthropic.com/2026/chive/).

## AS-001: a falsifiable small-model training study

The initial task is deliberately narrow. Given a fictional rule and an execution record, output `BENIGN`, `VIOLATION` or `INSUFFICIENT_EVIDENCE`. Each scenario has matched versions differing in authorization evidence while irrelevant language remains controlled.

The primary comparison changes **data construction only**: ordinary balanced supervised examples versus matched counterfactual examples. Match label counts, total supervised tokens and optimizer steps. Include the frozen base model and an always-alarm control. Counterfactual augmentation is established prior art, including evidence that it does not always improve generalization under matched data sizes. We therefore label this **TRANSFER/RECOMBINATION**, with any narrower novelty claim pending a stronger search. [Kaushik et al.](https://arxiv.org/abs/1909.12434) · [Negative comparison](https://arxiv.org/abs/2010.04762).

Measure false accusations and detected violations separately. Report abstentions, both-members-correct for matched pairs and each held-out family's result. Do not select a model on the final test. Public generated fixtures are development material; an independently authored, frozen evaluation is required before making a research claim. Multiple variants of the same scenario are correlated, not independent trials.

A later, separate ablation can add a pairwise margin term. Its derivation and limits are in [the protocol](../experiments/AS-001/PROTOCOL.md). The current code does not implement that training objective; it only evaluates the mathematical loss and checks the data/scoring contracts.

**Falsifier:** the paired-data advantage disappears at equal token budgets, fails on held-out families, or is achieved by abstaining on most real violations. A small model unable to follow the output contract is an informative feasibility failure, not a safety breakthrough.

## Execution and source limits

Eighteen software tests ran in the hosted Linux environment. No model inference, fine-tuning, Mac telemetry access or Vanda submission occurred. There are no model-latency, energy or intelligence-gain measurements.

Some official indexes returned older cached versions; targeted primary-domain searches exposed newer entries. Several article and arXiv full-text fetches failed. The ledger distinguishes indexed primary excerpts from complete reads. This report is a bounded source scan, not an exhaustive review of every Anthropic paper. No inaccessible methods section was treated as inspected.

**Next step:** in a verified local session, inspect the machine and any installed model, run a frozen-model development baseline, then attempt a short SFT smoke test. Training is conditional on the resource gate in [the local handoff](../work/LOCAL_RUN.md).
