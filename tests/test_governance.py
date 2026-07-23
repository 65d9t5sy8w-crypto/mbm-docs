from mbm.governance.gates import evaluate_evidence_gate


def test_missing_critical_evidence_fails_closed() -> None:
    result = evaluate_evidence_gate(critical_inputs_present=False)
    assert result.eligible is False
    assert result.reason == "critical_evidence_missing"
