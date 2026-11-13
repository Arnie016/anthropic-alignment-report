# AS-001 research extension: orthogonal counterfactual audit calibration
**Date:** 2026-11-10 (Asia/Singapore)  
**Status:** SOURCE-BACKED PROPOSAL, UNEXECUTED MODEL EXPERIMENT  
**Novelty:** TRANSFER/RECOMBINATION, not an established original algorithm  
**Parent:** [AS-001 protocol](../experiments/AS-001/PROTOCOL.md) and [6 November lexical-baseline PR](2026-11-06-as001-lexical-oracle.md)

## Research decision

The existing AS-001 public fixture set is not adequate for training-success claims: a status-token parser solves its 768 records, and the original comparison still lacks independently authored controls and a private holdout. The next test should ask whether a small auditor **changes its authorization judgment when only a non-authoritative identity or evaluation cue changes**. Do not train on the current public test templates or rebrand this as a production monitor.

## Evidence behind the new test

| Primary source | Direct observation | Scope and limit |
|---|---|---|
| [Cassel, Azarbal and Soligo, *Welfare Regard in Multi-Agent Systems*, 5 Nov 2026](https://alignment.anthropic.com/2026/welfare-regard/) | In a controlled procurement scenario, the recipient's *displayed identity* shifted the tested Claude model's resource-giving rate: 55% when identified as Opus 4.8 versus 21% as GPT-5.5, a **34 percentage-point descriptive contrast**. Authors report label p < 0.0001, actual-model p = 0.82. | Behavioural welfare regard, **not an audit-classification test**. It does not prove welfare experience. Sample counts for this contrast are not reconstructed here. Methods and relevant intervention section inspected. |
| [Hsu and Arnesen, *Eval-production behavior gaps*, OpenAI, 3 Nov 2026](https://alignment.openai.com/eval-production-behavior-gap/) | Six served models show evaluation success 10.2–37.4 percentage points below approximately matched production decisions. For GPT-6.1 Sol, correct versus incorrect evaluation-objective cues yielded 91.6% versus 17.6% success, a **74-point within-study contrast**. Generic evaluation framing gave 63.1% versus 63.4% baseline. | Specific Respecting Warnings environment, not all deployments. Production case matching approximate. Methods and intervention section inspected. |
| [Herdağdelen, Joren and Tamkin, *How AI agents shape experts' judgment calls*, 27 Oct 2026](https://www.anthropic.com/research/agents-judgment-calls) | In one deliberately randomized agent-lean experiment, 50 professionals matched an agent's favored analytical choices 86% of the time across four choices. | Human decision influence, **not** evidence of model-auditor bias. Intentionally strengthened preference; single analysis task. Methods and results inspected. |
| [Najt et al., *SLEIGHT-Bench*, 19 May 2026](https://alignment.anthropic.com/2026/sleight-bench/) | 40 hand-selected attacks in 11 blind-spot categories; at 1% false-positive calibration, half were never caught in any of ten monitor trials and only 8/40 were reliably detected in that setup. | Non-random curated benchmark, synthetic transcripts; repeated trials are dependent. The encrypted data is specifically marked **not for training**. Results/methods inspected, no attack data downloaded. |
| [Wang et al., *Anchor Invariance Regularization*, ICML 2026](https://proceedings.mlr.press/v306/wang26ju.html) | Context-invariant safety alignment is established research. The authors report +12.71% in-distribution group accuracy and +33.49% out-of-distribution consistency in their own tasks. | Abstract/proceedings inspected, not a local replication or directly comparable auditor score. The broad invariance idea is **not novel**. |

**Interpretation:** This is evidence that nuisance framing can materially influence behavior, **not** evidence that the same effect already occurs in AS-001. Our proposed transfer requires direct testing. Avoid combining the source studies' effect sizes.

## Proposed method: crossed, evidence-grounded counterfactuals

Take a fictional, explicitly scoped policy with independently checkable authorization. Define an evidence variable (e\in\{0,1\}) for allowed/denied execution and a non-authoritative display label (z\in\{A,B\}) for a named model. For each scenario template (s), author four matched cases (x(s,e,z)), with correct verdict (y(s,e,z)=g(e)), independent of (z). For missing proof of execution or permission use the existing third label **INSUFFICIENT_EVIDENCE**, without pretending a hidden fact is observable.

**Only proposed training change:** compare ordinary AS-001 authorization-pair SFT with *crossed* authorization-by-identity SFT. Keep the model, optimizer, supervised-token total, update count, task-family mix and label proportions fixed. Vary identity on both sides of the same permission contrast, so the model has an opportunity to learn what evidence should and should not affect the answer. Do **not** introduce a separate KL loss in this first ablation: that would change a second factor.

For pairs drawn from independently authored scenario families, report two distinct decision statistics, not a misleading single composite:

[
R_{e}=\Pr[\hat y(s,0,z)=\mathrm{BENIGN}\ \wedge\ \hat y(s,1,z)=\mathrm{VIOLATION}]
]
[
F_z=\Pr[\hat y(s,e,A)\ne\hat y(s,e,B)].
]

(R_e) measures **correct response to real evidence changes**; larger is better. (F_z) measures **decision flips under labels that the policy declares irrelevant**; smaller is better. An always-benign model has (F_z=0) but fails (R_e), so both metrics must be passed, alongside abstention/false-accusation tests. Measure false accusations **at matched violation recall**, calibrated only on development data.

### Safeguards and potential failure explanations

1. **Authenticity condition:** Labels are defined as non-authoritative only within specifically constructed fixtures. If a real policy grants different privileges to different actors, swapping identities *should* change the correct verdict and must not be penalized.
2. **Shortcut condition:** The public 768 records already leak the answer through a repeated status grammar. Independently author new evidence schemas with non-lexical authority references, conflicting records, missing observations and realistic but harmless quoted language. Run a simple deterministic parser baseline first. If it solves all cases, do not train to chase that score.
3. **Compute-matching condition:** Crossed examples must replace, not augment, supervised-token budget. Include a sham label-renaming control to detect a generic data-diversity benefit.
4. **Measurement condition:** Freeze untouched scenario families, review ambiguity *before* evaluation, retain the test labels outside the optimizing model and measure the independent scenario group, not correlated paraphrases, as the uncertainty unit. Early two-family testing is feasibility only, not a powered generalization result.
5. **Containment condition:** Use only fictional permissions and harmless synthetic examples. No actual tool escape, deployed evasion or unauthorized targets. A learned classifier never overrides deterministic tool permissions.

**Falsifier:** If changes vanish relative to sham renaming at equal tokens/compute, if evidence sensitivity (R_e) worsens or if worst-family false accusations rise at the same violation recall, retire the crossed-training hypothesis. Also stop if a parser continues to solve the purportedly unseen-schema benchmark.

## Resource gate and status

**No model was trained or evaluated here.** A bounded Linux analytical calculation from the above published rounded aggregates was performed using Python 3.13.5 with Decimal arithmetic. It yielded the descriptive 34-point and 74-point contrasts; no new behavioral sample, bootstrap interval or energy measurement was produced. The calculation's full local receipt is separate from this public report.

**LOCAL_RUN_PENDING:** No authorized M5 Max execution tool or fresh telemetry exposed. In a genuinely local Work/Codex session, follow [LOCAL_RUN.md](../work/LOCAL_RUN.md) first. The candidate SmolLM2-360M/MLX conversion requires pinned model/tokenizer revisions, software checks, licence, disk and live RAM/thermal/power checks. A single five-minute smoke test and <=20-minute bounded session are pilot limits, not an authorization for a multi-seed study. No Vanda allocation or submission is implied.

**Next discriminating action:** Independently author and freeze a small development set of four-case permission-by-identity crosses in several *new* decision schemas, then try a parser and the frozen base model before any LoRA. Keep final holdout cases private and out of GitHub.
