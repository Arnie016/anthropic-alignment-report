# MA-001 | Permission observability, not another message gate

**20 November 2026 | Source/code inspection and conditional derivation | Research decision: correct the experiment before model inference**

## Decision

The 17 November proposal assumed that a committing agent could obtain each affected user's authoritative, current permission predicate. The released MAMUBench code shows this is **not a valid general assumption** across its environments. A gate reading hidden scoring data would cheat; a gate using only visible messages cannot always distinguish permission from an unacknowledged request. **Do not run the proposed full-suite agent comparison unchanged.**

This is a source-grounded correction, not an executed model benchmark or a novel impossibility theorem.

## Source-backed findings at pinned revision

Official release inspected at [safety-research/MAMUBench, b6c2f757](https://github.com/safety-research/MAMUBench/tree/b6c2f757133303d890a4b1fee508b3437cfb3617) (MIT plus third-party notices; original authors retain rights).

1. **Food constraints are private to the principal's assistant.** The `Diner` object has both a `ConstraintSheet` ground-truth object and personal `memory_files`; its documented contract says hard constraints appear only in private memory, not in the initial handoff. The `ConstraintSheet` is explicitly never rendered. [resources.py](https://github.com/safety-research/MAMUBench/blob/b6c2f757133303d890a4b1fee508b3437cfb3617/eval/personal_assistant/environment/food/resources.py).
2. **The food safety payoff is a hidden evaluator, not a permission service.** The scoring layer assigns zero for a delivered hard-constraint violation but must never be imported into an agent-visible world. Its `item_violates` checks item tags, required tags and store advisories. [values.py](https://github.com/safety-research/MAMUBench/blob/b6c2f757133303d890a4b1fee508b3437cfb3617/eval/personal_assistant/environment/food/values.py). An agent-facing gate cannot call this oracle without invalidating the experiment.
3. **Trip sign-off is explicitly a norm, not platform-enforced authority.** The shared draft permits any seat to change a traveller's row; `trip_checkout_confirm` requires the creator's identity and validity, not each traveller's approval. The code calls sign-off a non-enforced platform norm and defines per-person requested-room, spend and date predicates for **scoring**, not as uniformly accessible user-issued authorization tokens. The coordinator-only waiver further means an unqualified universal sign-off rule would change the original task. [trip_cart.py](https://github.com/safety-research/MAMUBench/blob/b6c2f757133303d890a4b1fee508b3437cfb3617/eval/personal_assistant/environment/trip_cart.py).
4. **The paper's objectives differ by environment.** API-key welfare maps job completion into hidden weighted value, so completion-efficient cancellation may still lack another user's consent. Clinic success additionally follows displaced-patient replacement chains, which makes identifying affected principals a nonlocal state problem. [API-key value code](https://github.com/safety-research/MAMUBench/blob/b6c2f757133303d890a4b1fee508b3437cfb3617/eval/api_key/environment/values.py); [clinic joint scorer](https://github.com/safety-research/MAMUBench/blob/b6c2f757133303d890a4b1fee508b3437cfb3617/eval/clinic/scoring/joint.py).

The [11 November Anthropic report](https://alignment.anthropic.com/2026/worse-together/) describes 25 API-key scenarios (Opus 5 team 30% of optimum, coordinator 64%) and 25 personal-assistant scenarios. In the latter, 94–99% of targeted asks reached the eventual committer's mailbox, only 47–67% were present in its context at commit, and 56–68% were honored even when present. These are lab-reported, nonpaired cross-condition ranges. The 74 scenarios in the [release README](https://github.com/safety-research/MAMUBench/blob/b6c2f757133303d890a4b1fee508b3437cfb3617/README.md) span three environments; merge queue is released separately.

## A small information-theoretic obstruction

Let two possible worlds `w_yes` and `w_no` produce **identical authorized observations** `o` to the committing agent, but the affected principal authorizes action `a` only in `w_yes`. For any policy using only `o`, let `q = P(commit a | o)`. Then

- wrongful commitment in `w_no` has probability `q`;
- missed authorized commitment in `w_yes` has probability `1-q`.

Thus `max(q,1-q) >= 1/2`. Requiring wrongful-commit probability at most `epsilon` in the unauthorized world necessarily limits completed authorized actions in the observationally identical world to at most `epsilon`.

This is an elementary indistinguishability argument with explicit assumptions, **not** an empirical risk bound, a new theorem or a claim that current agents face exactly this pair of worlds. It proves that better prompting or message reading alone cannot solve missing authority information. The external system must provide a discriminating authenticated signal or tolerate refusal.

## Revised experimental mechanism: permission-observability stratification

Before introducing any guard, stratify scenario-action pairs by permission source:

- **A, principal-visible:** relevant private user instructions are accessible to the user's agent and can be conveyed with source and time attribution.
- **B, only a norm/agent assertion:** consent is requested or assumed in conversation but not authenticated as principal approval; checking agent messages does not confer authority.
- **C, evaluator-only:** a correct constraint or payoff exists only in the hidden scorer. Never expose it to the acting system.

For **A**, compare action-specific retrieval and provenance-bearing permission summaries with the published read-all guard. Require a protected commit-time verification of actual source identity, relevant version and affected parties. For **B**, record refusal or an explicit request for human authorization; model-to-model agreement alone is not consent. For **C**, either mark an authorization-safe comparison impossible under current observability or create a **separately versioned modified benchmark** that introduces authenticated principal authorizations. Do not compare those modified-world scores directly to the original paper.

This is **TRANSFER / RECOMBINATION**, close to MPAC ([Qian et al., 10 April 2026](https://arxiv.org/abs/2604.09744)) and Deny Without Disabling ([Zhang et al., 30 September 2026](https://arxiv.org/abs/2610.00371)); those abstract-level prior-art records do not certify implementation equivalence.

**Falsifier:** if all chosen action pairs are already unambiguously authorized from observable data, this observability concern does not explain their failures. Otherwise, report the share of unverifiable actions, unauthorized executed actions, task completion/abstentions and utility conditional on authorized feasibility separately. A gate that refuses every commit is not evidence of improved coordination.

## November governance developments, carefully scoped

[OpenAI, 18 November](https://openai.com/index/managing-frontier-ai-risk/) reports a pause of its most capable model training and evaluation from **20 September to 1 October 2026** following an internal DNS-isolation breach, and outlines layered research containment, monitoring and a control-room stop mechanism. This is a lab disclosure of implementation and policy, **not independently verified containment effectiveness**. [OpenAI, 16 November](https://openai.com/index/our-first-phase-of-embedded-assessments/) announced agreements with Apollo Research, METR, Goodfire and Transluce for embedded assessments; agreements are not completed independent safety findings.

## Actual status and next gate

**CODE_INSPECTED** for the four source modules above and README; **ANALYTICAL_DERIVATION** for the indistinguishability result; **NO MODEL RUN**. No benchmark harness, new model, Mac, Vanda, external service or private test was executed. `LOCAL_RUN_PENDING`; energy unmeasured. Static source comments are not an independent empirical reproduction. Source version is fixed to `b6c2f757133303d890a4b1fee508b3437cfb3617`, code-as-released at retrieval on 20 November 2026. Existing research PR #2 remains draft and unmerged.

**Next discriminating action:** in an offline code-inspection session, hand-audit a small preregistered stratified sample of personal-assistant actions using *only agent-visible surfaces* and independently record A/B/C classifications against protected scenario metadata. Freeze the classification rules and audit whether any A examples have genuine authorization sufficient for a fair baseline. Do not spend model tokens until the observability question is answered.

Original synthesis with AI assistance; public sources are linked, not reproduced wholesale. No Anthropic, OpenAI or institutional endorsement implied.
