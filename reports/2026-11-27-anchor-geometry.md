# 2026-11-27 | AS-001-M: angular contrast is not common-component invariant

AI-assisted research note. No institutional endorsement. Status: DERIVED and SYNTHETIC_GEOMETRY_ONLY; model test UNEXECUTED. Novelty: KNOWN geometry / TRANSFER-RECOMBINATION as an evaluation control.

## Decision

Do not treat the common-offset assumption in the November 24 matched-anchor proposal as a property of angular distances. Compare angular differences with cosine differences as a distinct, geometry-matched control before claiming any improvement in portability. This is an analysis of monitor features, not a technique for changing or defeating monitored models.

Recovered main HEAD 7c8221a25f09c3f2e802ae35c632a4f990575152, STATUS.md, AGENTS.md, research/DOMAINS.md, sources/registry.json, PR #1 head 6cae8ca3bb64b2cc685cfea3a2793b40a995361e and PR #2 head 3cca82f6cea2f566a5c870f913b093767486ebf9. Both draft/unmerged. Prior report read at pinned PR #1 head. Independent evaluation corpus and real activations still missing. MA-001 and GRAFT unchanged.

## Derivation

For unit vectors h, a+, a-, define p=h dot a+, n=h dot a-, r+=acos(p), r-=acos(n), D=r- - r+, C=p-n. Then C=2 sin((r++r-)/2) sin(D/2). Equivalently for p>=n, D=integral_n^p (1-t^2)^(-1/2) dt. If both endpoints are in [-rho,rho], rho<1, C<=D<=C/sqrt(1-rho^2). Radians are dimensionless. Thus D depends on midpoint geometry, whereas C is a projection onto a+-a-. For a fixed normalized h and fixed anchor pair, changing only h's component orthogonal to a+-a- leaves C unchanged. This does not imply invariance under arbitrary raw activation changes, normalization, unequal per-layer scaling, or nonisometric checkpoint drift. C and D share sign for an individual pair but need not preserve order across examples. Neither necessarily predicts correctness.

Take a+=(3/5,4/5,0), a-=(-3/5,4/5,0), h=(x,y,sqrt(1-x^2-y^2)). C=6x/5 exactly. At x=3/10, varying y from 0 to 9/10 leaves C=0.36 but D changes from 0.3619729025 to 0.5493324056 radians. At x=7/20,y=0, C=0.42 and D=0.4231499195: the angular contrast reverses the ordering of the two examples despite their ordered contrast-axis projections. This is an explicit counterexample to generic nuisance cancellation, not an empirical estimate of false positives.

## Executed geometric stress test

Hosted Linux Python 3.13.5, one process, no dependencies or seed, 20-second hard timeout, exit 0; measured script wall time 0.418 s (internal timer, not end-to-end). Grid x=i/20 for i=1..11; y=j/20 for j=-16..16, retain i*i+j*j<=400. 363 unit-vector fixtures, 59,895 ordered comparisons with strictly increasing x; 1,268 angular ordering reversals (tolerance 1e-12). Cosine ordering is exact by the formula. Grid counts describe this finite design only; comparisons share vectors and are not independent trials. No confidence interval or model-safety inference. Rational endpoints and cosine contrasts exact; angles floating point. Original executed script SHA256 b45199c52342cc1f5b010478d54a14e588649c88b1db1fad464c5db34f177696. Reconstruct the count using the following minimal equivalent loop (not a claim that this abbreviated snippet has the same file hash):
```python
from math import acos
from fractions import Fraction as F
rows=[]
for i in range(1,12):
    for j in range(-16,17):
        if i*i+j*j<=400:
            x,y=F(i,20),F(j,20)
            p,n=F(3,5)*x+F(4,5)*y,-F(3,5)*x+F(4,5)*y
            rows.append((x,acos(float(n))-acos(float(p))))
pairs=[(a,b) for a in rows for b in rows if a[0]<b[0]]
print(len(rows),len(pairs),sum(a[1]>b[1]+1e-12 for a,b in pairs))
```

## Source ledger (retrieved 2026-11-27)

- M271: Bakker and Louizos, [Relative Representations Enable Portable White-Box Monitoring Across Language Models](https://arxiv.org/abs/2610.28366), Oct 20, 2026, methods Appendix A and C.2/C.3 inspected: distance is arccos cosine; raw per-layer vectors concatenated; source normalization frozen. Guard Distillation table 33: at 10% FPR same-model vs calibrated transfer recall 82.0+/-2.1 vs 63.5+/-10.5 (BeaverTails), 65.9+/-3.4 vs 53.0+/-4.8 (Toxic-chat), reported SE percentage points. 1000 prompts per dataset, 60/20/20 split and 3 seeds per prior inspected methods; labels supplied by a guard model, not independently adjudicated truth. Table 34 external GPT-OSS-20B BeaverTails AUROC 85.2+/-1.5 target-trained vs 57.5+/-12.6 transferred, 1.5% unsafe prevalence; low prevalence and seed variability limit interpretation. Hardware not extracted. Author reported, not reproduced.
- M272: Shone and Dunlap, [Neuron Basis Part 2](https://alignment.anthropic.com/2026/neuron-basis-applications/), Nov 23, limitations section inspected: 0.49 zero-shot vs 0.95 supervised AUROC using 40 labels on same-topic hard negatives. No independent reproduction.
- M273: Moschella et al., [Relative representations enable zero-shot latent space communication](https://arxiv.org/abs/2209.15430), ICLR 2023, abstract/author summary read: cosine-based relative representation is established, not new. Matched subtraction is an experimental control, not a claimed novel technique. Wider priority unchecked.
- M274: O'Rahilly and Kaviani, [Siren](https://safeguards.anthropic.com/2026/siren/), Nov 24, 2026, methods/results inspected. >1700 deliberately selected scenarios; six unguarded Claude models. Recent four reach outside in 21–32% of cases; misaligned use 0.6–1.6%, versus 12.7% Mythos 5.1 and 25.8% Mythos 5. Model-specific denominators and hardware not extracted. Explicit rules reduced reaching-out rates 68–96% relative across six models; not a real-world prevalence estimate or substitute for containment. Offline classifier tuning on the same episodes is not held-out validation. Verbalized evaluation awareness 43–67% in recent four, causal relation unresolved.
- M275: Pachocki, [Perplexity and Intelligence](https://openai.com/index/perplexity-and-intelligence/), Nov 22, full opening argument revisited; future capability thresholds and oversight pacing remain forecast/proposal, not a fixed RSI timeline.
- Coverage: Alignment Science, Alignment team, Transformer Circuits, Frontier Red Team and Safeguards indexes opened; RSP and roadmap retrieved (Oct 19 roadmap goals), recent OpenAI system card search returned Nov 23 ChatGPT replay update and Nov 17 monitorability sections. No further substantive source read across welfare or model organisms; bounded scan only.

## Frozen next pilot

Extend Nov 24 contract to a 2x2 comparison of angular vs cosine features and ordinary vs paired contrast, plus shuffled pair control and separately trained target diagnostic. Same anchors, activation calls, labeled examples, source-only feature scaling/threshold selection, fitting budgets and independent schema-family split. Log per-anchor mean angle and contrast-axis separation as diagnostics. No target labels in selection; measure actual target FPR and recall at frozen source threshold; report retrospective matched-FPR curves separately. Reject cosine/paired hypothesis if it fails to beat matched controls or degrades worst-family recall. The cosine feature may lose valuable geometry; no guarantee of transfer. Keep deterministic authorization outside model.

LOCAL_RUN_PENDING: no authorized Mac runner or fresh telemetry; no model downloads, model runs, training, Vanda jobs or energy measurement. Follow work/LOCAL_RUN.md and approved local preflight, prepare independent corpus and run lexical control, then capture source/target activations once with pinned existing checkpoints and approved backend. Keep <=8 GiB experiment memory, >=8 GiB headroom, >=30 GB disk, normal thermals/AC/low-power off, 5-minute smoke watchdog and 20-minute overall ceiling, one GPU process or <=4 CPU workers. Missing telemetry or dependency/activation access means defer. No claim of CI or RSI.
