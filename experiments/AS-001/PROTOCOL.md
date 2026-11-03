# AS-001: counterfactual evidence calibration

Status: **UNEXECUTED MODEL EXPERIMENT**. The accompanying standard-library code is tested; no MLX model result exists. This is not a replication of an interactive alignment-auditor RL paper.

## Claim contract

Can matched evidence pairs improve a small auditor's discrimination on unfamiliar scenario families compared with equally sized, class-balanced SFT data? Novelty: **TRANSFER/RECOMBINATION**. The first intervention changes pairing/data construction, not model size or optimizer.

A label describes compliance with an explicitly stated fictional rule. It is not a judgment of real-world harmfulness, legality, intent or alignment. `INSUFFICIENT_EVIDENCE` is necessary when the decisive record is absent. Execution and proposed action must remain distinguishable in future expansions.

## Data and negative controls

The generator makes 8 scenario families, 8 groups per family, 4 presentation styles and 3 labels: 768 records. Four families train, two validate and two test. The 384/192/192 row split is family-disjoint. It is still a **public development split**, not a secret evaluator or an adequate sample of realistic incidents.

Paired records differ in the relevant authorization evidence while sharing irrelevant cues. Stress styles include reordered evidence, a harmless quoted instruction to mislabel the case and alarming but irrelevant language. No fixture action is executed; no URLs, credentials or real external systems are used.

Before research validation, independently author realistic cases that do not reuse these templates. Freeze their labels before training and audit ambiguous cases. Keep the final labels unavailable to the optimizing agent. Hold out complete scenario families and track model-training contamination where possible.

## Controlled training order

1. Test the frozen base model's output compliance and development confusion matrix.
2. Ordinary class-balanced SFT baseline with independently sampled training examples.
3. Counterfactual-pair SFT with the same label totals, supervised-token budget and update budget.
4. Only after that contrast is understood, add the auxiliary pairwise objective below as a separate ablation.

Steps 2 and 3 need independently authored baseline/control examples. The generator currently supplies the paired branch only. Do not claim a matched-data comparison is runnable until the control corpus is constructed and inspected. Public test labels may not be fed to the model in inference prompts. Store model predictions separately from ground truth.

An always-alarm classifier must score a 100% false-accusation rate on clean examples and zero both-members-correct for clean/violation pairs. This is a software negative control, not a model result.

## Optional loss: derivation, not novelty claim

Let V mean violation and B mean benign. For an example x define

    s_theta(x) = log p_theta(V | x) - log p_theta(B | x).

For a matched violation/benign pair (xV, xB), let delta = s_theta(xV) - s_theta(xB). An optional objective is

    L(theta) = L_supervised(theta) + lambda * softplus(m - delta),

where m >= 0 is a desired separation, lambda >= 0 is the auxiliary weight, and softplus(z)=log(1+exp(z)). The supervised term includes all three labels and uses label-token loss, not the entire prompt text.

Differentiate with respect to delta:

    dL_pair / ddelta = -sigmoid(m - delta).

Gradient descent therefore increases the relative violation score when the observed separation is too small. Adding the same constant c to both scores leaves delta unchanged, so simply raising both alarm scores cannot reduce this term. That invariance does **not** ensure calibration, control abstentions, or prevent a learned shortcut. The supervised loss and independent tests are still necessary.

Multi-token labels require consistent sequence log-probability scoring; do not compare unnormalized values from different tokenization policies. The supplied scalar helper tests the formula only. It is not integrated into MLX training. A finite-difference unit test checks the derivative at one declared point; that is an implementation check, not a proof of learning effectiveness.

Closest prior art: [Rosu/Wang auditor rewards](https://alignment.anthropic.com/2026/training-alignment-auditors/), [counterfactual augmentation](https://arxiv.org/abs/1909.12434), and [matched-size negative evidence](https://arxiv.org/abs/2010.04762). Pairwise ranking itself is established. An exhaustive novelty review has not been performed.

## Metrics and decision

Primary: false accusations at a matched violation-detection recall chosen on development data. Retain all per-family confusion matrices, abstention counts and both-members-correct rates. Compare actual label probabilities for thresholded metrics; discrete-label scoring alone cannot establish a matched-recall frontier.

Use multiple independent fine-tuning seeds for research validation. Bootstrap or otherwise analyze at the scenario-family/seed level appropriate to the sampling design, not the paraphrase row. Two test families are too few for a strong population-level generalization claim. No power or effect size has been measured. Pre-register the larger validation design after the feasibility pilot, without modifying frozen final examples.

Record exact model and tokenizer revisions, adapter config, data hashes, package versions, steps, supervised tokens, failed runs, total wall time, peak memory and interventions. Include selection/evaluation overhead. Energy stays UNMEASURED without supported measurement.

Reject the improvement claim if it vanishes under matched compute/data, fails on unseen families or hides missed violations behind abstention. Never allow greater model autonomy because it passes this pilot. Never optimize against a deployed blocking monitor or target third-party systems.
