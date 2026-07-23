from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class SettlementRecord:
    settlement_id: str
    projection_id: str
    result: str
    settled_at: datetime
