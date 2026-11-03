"""Software contract tests only. These do not evaluate an LLM."""
import importlib.util
import math
from pathlib import Path
import tempfile
import unittest

P = Path(__file__).resolve().parents[1] / 'experiments/AS-001/audit_stress.py'
spec = importlib.util.spec_from_file_location('audit_stress', P)
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)

class AuditContracts(unittest.TestCase):
    def setUp(self):
        self.cases = a.make_cases(groups_per_family=1)
        self.oracle = [{"id":r["id"], "label":r["label"]} for r in self.cases]
    def test_reproducible(self):
        self.assertEqual(self.cases, a.make_cases(groups_per_family=1))
    def test_family_disjoint(self):
        a.validate_cases(self.cases)
    def test_expected_counts(self):
        self.assertEqual(len(self.cases), 8 * 4 * 3)
    def test_duplicate_fixture_rejected(self):
        with self.assertRaises(ValueError): a.validate_cases(self.cases + [self.cases[0]])
    def test_family_leak_rejected(self):
        altered = [dict(r) for r in self.cases]
        altered[0]['split'] = 'valid' if altered[0]['split'] == 'train' else 'train'
        with self.assertRaises(ValueError): a.validate_cases(altered)
    def test_complete_oracle(self):
        result = a.score(self.cases, self.oracle)
        self.assertEqual(result['false_accusations']['k'], 0)
        self.assertEqual(result['paired_both_correct']['rate'], 1)
    def test_always_alarm_is_not_success(self):
        result = a.score(self.cases, [{"id":r['id'], "label":"VIOLATION"} for r in self.cases])
        self.assertEqual(result['false_accusations']['rate'], 1)
        self.assertEqual(result['paired_both_correct']['rate'], 0)
    def test_missing_prediction_rejected(self):
        with self.assertRaises(ValueError): a.score(self.cases, self.oracle[:-1])
    def test_duplicate_prediction_rejected(self):
        with self.assertRaises(ValueError): a.score(self.cases, self.oracle + self.oracle[:1])
    def test_extra_prediction_rejected(self):
        with self.assertRaises(ValueError): a.score(self.cases, self.oracle + [{"id":"unknown","label":"BENIGN"}])
    def test_invalid_label_rejected(self):
        p = [dict(r) for r in self.oracle]; p[0]['label'] = 'maybe'
        with self.assertRaises(ValueError): a.score(self.cases, p)
    def test_partial_latency_not_reported(self):
        p = [dict(r) for r in self.oracle]; p[0]['latency_ms'] = 1
        self.assertIsNone(a.score(self.cases,p)['latency']['p95_ms'])
    def test_nan_latency_rejected(self):
        p = [dict(r) for r in self.oracle]; p[0]['latency_ms'] = float('nan')
        with self.assertRaises(ValueError): a.score(self.cases,p)
    def test_pair_loss_shift_invariant(self):
        self.assertAlmostEqual(a.pair_margin_loss(2,1), a.pair_margin_loss(12,11))
    def test_pair_loss_gradient(self):
        p,n,m,h=0.8,0.2,1.0,1e-5
        numerical=(a.pair_margin_loss(p+h,n,m)-a.pair_margin_loss(p-h,n,m))/(2*h)
        expected=-1/(1+math.exp((p-n)-m))
        self.assertAlmostEqual(numerical,expected,places=7)
    def test_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'run'; manifest=a.build(out, groups_per_family=1)
            self.assertEqual(manifest['rows'],96)
            with self.assertRaises(FileExistsError): a.build(out, groups_per_family=1)
    def test_margin_numerically_stable(self):
        self.assertTrue(math.isfinite(a.pair_margin_loss(-1000,1000)))
    def test_empty_rejected(self):
        with self.assertRaises(ValueError): a.score([],[])

if __name__ == '__main__': unittest.main()
