from mbm.governance.gates import EvidenceGateResult, evaluate_evidence_gate


def run_preprojection_gate(*, critical_inputs_present: bool) -> EvidenceGateResult:
    return evaluate_evidence_gate(critical_inputs_present=critical_inputs_present)
