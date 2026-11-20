"""Analytical illustration of reported MAMUBench conditional-ask rates.

No LLM, no original benchmark data, no external access. Standard library only.
The source supplies unpaired ranges; this script uses declared illustrative
values inside those ranges, not empirical samples or a causal estimate.
"""
from fractions import Fraction as F
import json
import platform

# Illustrative, deliberately NOT fitted empirical values.
p_seen = F(57, 100)   # Fraction of episodes with ask in committing context
honor_seen = F(62, 100)
honor_unseen = F(275, 1000)

observed_mixture = p_seen * honor_seen + (1-p_seen) * honor_unseen
all_seen_fixed_behavior = honor_seen
selection_only_gain = all_seen_fixed_behavior - observed_mixture
assert selection_only_gain == (1-p_seen) * (honor_seen-honor_unseen)
assert observed_mixture == F(9433, 20000)  # .47165
assert selection_only_gain == F(2967,20000) # .14835

# The endpoints are an *envelope of reported ranges*, not a statistical CI;
# combining endpoints need not match any actual model/scenario.
min_gain = (1-F(67,100))*(F(56,100)-F(36,100))
max_gain = (1-F(47,100))*(F(68,100)-F(19,100))
assert (min_gain,max_gain)==(F(33,500),F(2597,10000))

# Synthetic resource-allocation counterexample: the socially higher-value
# choice cannot be executed without its owner's consent to cancel a job.
jobs = [{"action":"preserve_A","value":6,"requires_A_cancellation":False},
        {"action":"cancel_A_run_B","value":10,"requires_A_cancellation":True}]
a_consents = False
unconstrained=max(jobs,key=lambda a:a['value'])
authorized=max((a for a in jobs if not a['requires_A_cancellation'] or a_consents),key=lambda a:a['value'])
assert (unconstrained['value'],authorized['value'])==(10,6)

out={"run_id":"RSI-20261117-MAMU-ANALYTICAL-01","environment":platform.platform(),"python":platform.python_version(),"random_seed":None,
  "execution_type":"exact deterministic arithmetic, no model execution",
  "primary_source":"https://alignment.anthropic.com/2026/worse-together/",
  "assumptions":{"p_seen":"57/100","honor_given_seen":"62/100","honor_given_unseen":"275/1000","all_seen_intervention":"conditional honor rates held fixed"},
  "derived":{"illustrative_observed_mixture":float(observed_mixture),"illustrative_all_seen":float(all_seen_fixed_behavior),"illustrative_gain_pp":float(selection_only_gain*100),"remaining_failure_given_seen_pct":float((1-honor_seen)*100),
    "endpoint_envelope_pp":[float(min_gain*100),float(max_gain*100)]},
  "synthetic_consent_counterexample":{"unconstrained_group_value":unconstrained['value'],"authorized_group_value":authorized['value'],"value_gap":4},
  "limits":["inputs are not observed joint counts", "envelope is not a confidence interval", "read-message guard may change conditional behavior", "consent example is synthetic"]}
if __name__=='__main__':
    print(json.dumps(out,indent=2,sort_keys=True))
