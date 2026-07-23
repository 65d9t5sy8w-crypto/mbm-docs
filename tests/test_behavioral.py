import pytest

from mbm.behavioral.contracts import BehavioralState


def test_behavioral_state_rejects_out_of_range_values() -> None:
    with pytest.raises(ValueError):
        BehavioralState(aggression=1.1, discipline=0.5, volatility=0.5)
