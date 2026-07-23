from dataclasses import dataclass
from datetime import datetime
from typing import Mapping

from mbm.domain.enums import ProjectionDecision


@dataclass(frozen=True, slots=True)
class ComponentVersion:
    component: str
    version: str


@dataclass(frozen=True, slots=True)
class ProjectionResult:
    projection_id: str
    decision: ProjectionDecision
    probability: float
    created_at: datetime
    provenance: Mapping[str, ComponentVersion]
