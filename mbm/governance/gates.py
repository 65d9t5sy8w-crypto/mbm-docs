from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EvidenceGateResult:
    eligible: bool
    reason: str | None = None


def evaluate_evidence_gate(*, critical_inputs_present: bool) -> EvidenceGateResult:
    if not critical_inputs_present:
        return EvidenceGateResult(eligible=False, reason="critical_evidence_missing")
    return EvidenceGateResult(eligible=True)
