from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CalibrationObservation:
    projection_id: str
    predicted_probability: float
    outcome: int
