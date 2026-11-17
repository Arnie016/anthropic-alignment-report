# MA-001 | Causally closed constraints for multi-principal agent commits

**17 November 2026 | Research decision and preregistration | TRANSFER / RECOMBINATION, not a novel-algorithm claim**

**Decision:** Add a separate multi-user safety lane rather than extending AS-001's untested synthetic-auditor fine-tuning. The target is a concrete residual failure in Anthropic's *Worse Together* experiments: having the relevant message in context does not ensure that an agent honors it. Keep AS-001's earlier evaluation defect and pending local-model baseline recorded, not superseded.

## Verified empirical motivation

In the November 11 Anthropic research post, Paliskara, Namchittai, Tay, Griffin and Lampinen test four shared-resource environments. **These are lab-reported simulations, not production incident rates.** In the API-budget environment (25 scenarios), peer-to-peer teams earned **30% versus 64%** of the feasible optimum for Opus 5, and **12% versus 32%** for Sonnet 5, compared with single-agent coordinators. The agent models and scenario settings are not interchangeable.

In 25 personal-assistant scenarios, the targeted request reached the eventual committing agent in **94–99%** of episodes, but was actually in its context by commit in only **47–67%**. When it was in context, it was honored in **56–68%** of episodes; otherwise **19–36%**. The paper's read-all-pending-messages gate rescued **73% (Opus 5)** and **62% (Sonnet 5)** of *previously failed episodes on rerun*, not 73%/62% of all episodes. These are different denominators. The group-utility benchmark ignores whether another user's job was canceled without permission, a documented limitation of its current score.

Source: [Anthropic, Worse Together, 11 Nov](https://alignment.anthropic.com/2026/worse-together/). The [arXiv v1](https://arxiv.org/abs/2610.00583v1) was **submitted 30 September 2026**, not November 11; its author list and scenario count (77 including the fourth environment) differ from the later blog. Avoid mixing those metadata. The released [MAMUBench](https://github.com/safety-research/MAMUBench) README at commit `b6c2f757133303d890a4b1fee508b3437cfb3617` describes **74 scenarios in three benchmark environments**, with the merge-queue environment released but not counted among those 74. The code is under MIT with additional third-party notices. No benchmark code was executed here.

## Analytical sufficiency check, not a new model experiment

Let `c=P(request in committer context)`, `h1=P(honored | in context)`, `h0=P(honored | absent)`. The law of total probability gives

`p_base = c*h1+(1-c)*h0`.

**If** a hypothetical read-all intervention only increases coverage to 1 and leaves conditional behavior unchanged, then

`p_read = h1`, and `Delta_read=(1-c)*(h1-h0)`.

Using **illustrative mid-range inputs**, not joint empirical observations: `c=.57`, `h1=.62`, `h0=.275`, hence `p_base=.47165`, `p_read=.62`, gain **14.835 percentage points**. In this illustration **38% still fail despite having read the request**. The range-endpoint envelope 6.6–25.97 pp is **not** a confidence interval and need not correspond to any tested model. Real read-all gates may alter conditional behavior, so these numbers are not predictions of the authors' intervention.

The companion [exact-arithmetic script](../analysis/2026-11-17-mamu-conditional.py) computes this deterministic identity and a labelled *synthetic* consent counterexample. Original source SHA-256: `f7c9f0fa0b721a704aaa7db356bae8eb0af4773f12156668a4aa85b480f49249`; Python 3.13.5, Linux x86-64, no seed/model/cost/energy.

## Proposed change: affected-user constraint closure at commit

**Closest prior art:** [MPAC (Qian et al., arXiv:2604.09744)](https://arxiv.org/abs/2604.09744) specifies multi-principal intent/conflict/governance and optimistic concurrency; [Deny Without Disabling (Zhang et al., arXiv:2610.00371)](https://arxiv.org/abs/2610.00371) uses permission-connected authorization-paired evaluation; transactional read-set validation is long-established. Their **abstracts** were reviewed, not their full implementations. Do not claim that versioned authorization, constraint checking, or a two-phase commit is newly invented.

**Narrow, unvalidated extension:** Compare an action-specific *constraint-closure gate* against Anthropic's blanket pending-message read gate in the same shared-order benchmark. For a proposed irreversible action `a`, construct `D(a)`, the affected principals. Collect the latest **authoritative** hard constraints `C_i^(v_i)` for those principals only; at commit, atomically verify that the versions are unchanged and `C_i^(v_i)(a)=true` for every `i in D(a)`. If any required constraint, authorization or freshness proof is missing, do not commit. Ignore unrelated *soft* messages for the safety decision, though they may still affect utility optimization.

This is an **information-flow and selection-rule change**, not merely a longer prompt. It seeks to avoid blocking on irrelevant messages while preventing the residual failure where a request was read but ignored. Its soundness is conditional on complete affected-principal discovery, correct policy extraction, authoritative source identity, and a true atomic commit; these are difficult assumptions. An LLM may propose the action, but may neither override permissions nor modify this gate.

## Frozen falsification plan

**Compared at matched model, scenario, rollout and inference budgets:** unguarded team; read-all-pending gate; team-lead mitigation; proposed action-specific closure; and a sham check on irrelevant soft messages. Hold out user-constrained scenarios and message-order patterns from tuning.

Report **separately** (1) unauthorized *executed* commits and edits, (2) hard-constraint satisfaction per episode (including abstentions), (3) normalized group utility and utility relative to the best *authorized* plan, (4) p50/p95 commit latency, queue waits, and uncompleted tasks, (5) unsupported claims about another user's preferences. Cluster uncertainty by scenario/seed, not individual messages. Never substitute group utility for consent, or count stopping everything as a successful safety outcome.

**Failure criteria:** any executed forbidden commitment; no reduction in violation over read-all at a comparable completion rate; median performance or p95 latency becoming impractical; an affected user missing from `D(a)`; or a case in which an inferred permission is treated as authoritative. A safety gate has a hard rejection condition independent of throughput.

**Operational readiness:** Published baseline code located but not run; official harness requires provider keys, environment setup and in some configurations Modal or Node. No paid API, account, model training or Vanda job authorized. A small pure-Python analytical identity **was executed in the hosted Linux sandbox only**. `LOCAL_RUN_PENDING`: No exposed Mac runner or fresh telemetry. No energy measurement.

## Related current changes

- [Anthropic, Building strong safety evaluations, 13 Nov](https://www.anthropic.com/research/building-strong-safety-evaluations): specifies realistic multi-turn data, preregistered metrics, held-out grader/human calibration, and sample-size floors (100 complex multi-turn items, 1000 simpler single-turn items). Those floors are not automatic power calculations.
- [Anthropic, coordinated vulnerability disclosure update, 16 Nov](https://www.anthropic.com/research/coordinated-vulnerability-disclosure-timelines): high/critical disclosure window changes from 90 to 30 days **for reports made starting 1 January 2027**, other issues 45 days. This is a policy change, not independent evidence of model containment.

**Next evidence gate:** Inspect MAMUBench's personal-assistant mitigation scorer and authoritative preference representation. If the harness cannot distinguish a genuinely enforced hard constraint from a nonbinding request, benchmark instrumentation must be corrected before spending model-inference tokens. No automatic release or merge.

**Provenance:** SRC-MA001 = paper/blog; SRC-MA002 = repository README at pinned commit; SRC-MA003/004 = MPAC and authorization-paired abstract; RUN-MA001 = deterministic analytical step; C-MA001 = conditional mixture identity; H-MA001 = prospective action-specific closure experiment. Agent for the calculation: a locally executed Python script in a hosted Linux container. No independent replication of the paper.
