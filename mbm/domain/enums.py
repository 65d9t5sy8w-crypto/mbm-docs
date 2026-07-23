from enum import StrEnum


class ProjectionDecision(StrEnum):
    MORE = "MORE"
    UNDER = "UNDER"
    PASS = "PASS"


class LifecycleState(StrEnum):
    PROVISIONAL = "PROVISIONAL"
    SCORED = "SCORED"
    PUBLISHED = "PUBLISHED"
    MONITORING = "MONITORING"
    SETTLED = "SETTLED"
    POST_MORTEM = "POST_MORTEM"
