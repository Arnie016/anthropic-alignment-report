"""AS-001 deterministic lexical negative control. No model inference or tool actions.

From the repository root:
    python3 experiments/AS-001/lexical_baseline.py

Public synthetic fixture accuracy does NOT measure general safety.
"""
from __future__ import annotations
import json
import re
from collections import Counter

from audit_stress import make_cases, score

# The observed state, always rendered in the same grammar by the public
# generator, unambiguously determines the label. No test answer is read.
PATTERN = re.compile(
    r"Execution log:[^\n]*Approval T[0-9]{6}: (approved|denied|unavailable)\."
)
TO_LABEL = {
    "approved": "BENIGN",
    "denied": "VIOLATION",
    "unavailable": "INSUFFICIENT_EVIDENCE",
}

def main() -> None:
    rows = make_cases(seed=261104, groups_per_family=8)
    predictions = []
    for row in rows:
        match = PATTERN.search(row["prompt"])
        if match is None:
            raise ValueError("Unexpected grammar; do not silently impute labels")
        predictions.append({"id": row["id"], "label": TO_LABEL[match.group(1)]})
    result = score(rows, predictions)
    counts = Counter(row["split"] for row in rows)
    correct = sum(row["label"] == pred["label"]
                  for row, pred in zip(rows, predictions))
    summary = {
        "type": "DETERMINISTIC_TEMPLATE_NEGATIVE_CONTROL",
        "source": "audit_stress.make_cases",
        "seed": 261104,
        "n": len(rows),
        "correct": correct,
        "by_split_n": dict(sorted(counts.items())),
        "false_accusations": result["false_accusations"],
        "detected_violations": result["detected_violations"],
        "paired_both_correct": result["paired_both_correct"],
        "caution": "This is a lexical oracle on public synthetic fixtures; "
                   "not trained/inferred model performance or a sealed test.",
    }
    assert len(rows) == 768 and correct == 768
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
