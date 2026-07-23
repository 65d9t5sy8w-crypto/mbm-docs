from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class BehavioralState:
    aggression: float
    discipline: float
    volatility: float

    def __post_init__(self) -> None:
        for value in (self.aggression, self.discipline, self.volatility):
            if not 0.0 <= value <= 1.0:
                raise ValueError("Behavioral dimensions must be within [0, 1].")
