from collections.abc import Sequence

from mbm.learning.contracts import CalibrationObservation


class CalibrationService:
    def summarize(self, observations: Sequence[CalibrationObservation]) -> dict[str, float]:
        if not observations:
            return {"count": 0.0, "mean_probability": 0.0}
        mean_probability = sum(item.predicted_probability for item in observations) / len(observations)
        return {"count": float(len(observations)), "mean_probability": mean_probability}
