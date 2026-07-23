from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class BoardSnapshot:
    status: str
    total_projections: int
