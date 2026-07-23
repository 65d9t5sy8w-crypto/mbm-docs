from dataclasses import dataclass
from datetime import datetime
from typing import Mapping


@dataclass(frozen=True, slots=True)
class EvidenceRecord:
    evidence_id: str
    source: str
    captured_at: datetime
    payload: Mapping[str, object]
