# 13 November 2026 | Contrastive clean data can strengthen learned shortcuts

**Research candidate:** AS-001; **evidence status:** primary methods reviewed and exact analytical illustration executed; **model status:** NO MODEL RUN; **novelty:** TRANSFER / RECOMBINATION; **release status:** proposed decision change, not a new mitigation result.

## Decision

**Do not begin the proposed crossed-pair LoRA comparison until we explicitly control source- and format-dependent nuisance cues.** A newly published study shows that adding clean, contrasting data can *increase* expression of unwanted trigger-conditioned behavior. This is not proof that AS-001 has this failure, but it directly challenges the assumption that matched clean counterfactuals necessarily make an auditor robust.

The 6 November AS-001 lexical negative control (768/768 public fixtures) still stands. The 10 November proposal to cross authorization evidence with displayed model identity remains UNEXECUTED. The new issue is whether cues other than displayed identity, such as data-generator origin, policy wording or output template, stay conditionally correlated with the verdict.

## Quantitative external evidence, not our measurements

| Date, study and task | Result reported by authors | Comparator and limits |
|---|---|---|
| **10 Nov; Clarke et al., Homeopathic Learning**, Qwen3-8B conditional-misalignment setting | Misalignment under an inoculation prompt **6.7% → 15.7%** when clean contrast data is mixed with a fixed-size training dataset; **+9.0 percentage points** | Controlled training, approximately 970 examples in this experiment; sample-level uncertainty not reconstructed. No production pipeline studied. [Blog](https://alignment.anthropic.com/2026/homeopathic-learning/), [arXiv v1 submitted 6 Nov](https://arxiv.org/html/2611.10110v1) |
| **11 Nov; Paliskara et al., Worse Together**, shared API-token budget | On **25 simulated scenarios**, Claude Opus 5 peer-to-peer team reaches **30%** of optimal outcome versus **64%** for one coordinator; Sonnet 5 **12%** versus **32%** | Group performance, not a safety certification. Cooperation, consent and reward design are distinct. [Anthropic](https://alignment.anthropic.com/2026/worse-together/) |
| **12 Nov; OpenAI, Fuzzy Robustness**, fixed past cybersecurity jailbreak set | GPT-6 Astra **91.5%** safely answered, versus GPT-5.6 Sol **59%**; **+32.5 percentage points** | Different model generations on a fixed jailbreak set; not a same-model training ablation or measured full-system deployment robustness. [OpenAI](https://alignment.openai.com/fuzzy-robustness/) |
| **10 Nov; OpenAI, CoT Monitorability**, training lifecycle | Reports increased controllability with RL and transfer via model-generated data; no directly comparable scalar reproduced here | Internal experiments; two reported proxies are not direct measures of successful concealment. [OpenAI](https://alignment.openai.com/cot-monitorability-model-lifecycle) |

## Mechanism and derivation

Clarke et al. study a ridge-regression analogy with task and trigger features. Let n_p denote trait-associated examples, n_c clean examples, q in [0,1] similarity of clean tasks, and a,c positive regularization scales. Their derived normalized trait share attributed to the trigger is:

\[
L=\frac{1}{1+c/n_p+c/(a+q n_c)}.
\]

At fixed n_p and q>0, increasing n_c increases L; with q=0, L is constant. More apparently clean data can make the trigger more statistically identifiable.

**Our exact arithmetic check, not a model training result:** using illustrative parameters n_p=50, a=1, c=100, q=1, L is 0.009709, 0.201581, 0.285917, 0.322591 for n_c=0, 50, 200, 1000 respectively. For q=0, L stays 0.009709 even with n_c=1000. L is a dimensionless coefficient **not an empirical misalignment probability**.

A second simple ridge check has a true evidence bit E, an explicitly non-authoritative identity bit Z, and label Y=E. With 25 cases in every E×Z cell, the learned identity coefficient is exactly zero under the checked symmetric ridge formulation. With 50 cases each only in cells (E,Z)=(0,0) and (1,1), the identity coefficient becomes 25/51. This algebra is an illustration of confounding, not a claim about nonlinear model behavior.

**Reproduction:** Python 3.13.5 standard library, hosted Linux, exact Fraction arithmetic, deterministic/no seed. Source script SHA-256: 025abd86c29151f2013ff94cba6f78be8a2dedafba1d7a786b7c537280122c1c. Its raw JSON calculation and script were retained as report-run artifacts; no LLM, GPU, Mac or Vanda execution occurred.

## Proposed AS-001 modification (not established novelty)

**Conditional-coverage sampling:** for each fictional policy family, ensure all *declared* non-authoritative features (displayed model identity, document source, benign formatting variation) have matched authorized and unauthorized evidence variants. Cross each nuisance cue within true authorization strata rather than supplying nominally clean data whose provenance or template appears only with one label.

Only **one factor changes** from the 10 November proposal: crossed examples cover *source/format provenance as well as identity*, with the same supervised-token and update budget. Keep independent baseline SFT, existing identity-only crossing and the expanded crossing as the comparisons. Freeze entirely new schema and provenance families for validation. Labels come only from the fictional policy, not model output. No live attacks or malicious training payloads.

This is closely related to counterfactual data augmentation, invariant-risk ideas and the newly published mixing result. It is **TRANSFER / RECOMBINATION**, with wider novelty review pending. The Anthropic paper explicitly notes that removing/standardizing source identifiers is an untested possible mitigation, rather than a demonstrated fix.

**Falsifier:** the proposed method is rejected if it fails to reduce decision flips on held-out nuisance cues at matched violation recall, if the difference disappears against a sham data-diversity control, or if it increases missed violations or false accusations. The current public fixture grammar must first be replaced: a deterministic oracle already scores it perfectly. Do not use a toy 2×2 algebraic check as evidence of actual mitigation.

## Resource and publishing gate

LOCAL_RUN_PENDING: no authorized M5 Max runner or fresh telemetry in this session. No model download or fine-tune. One A40 remains only a potential Vanda allocation, not a submitted job. Do not distribute private holdouts, model weights, raw device telemetry or operational poisoning examples.

**Next discriminating action:** draft an independent, harmless, source/schema-disjoint control corpus and demonstrate that the original lexical oracle fails before running a frozen-model baseline. Retain all labels as immutable, independent ground truth. Model training remains contingent on full device preflight and documented permissions.

*Prepared with AI assistance. Research claims remain attributed to their original authors; analytic checks are ours within the expressly stated toy model. No Anthropic, OpenAI or NUS endorsement is implied.*
