from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True, slots=True)
class LayerOutput:
    name: str
    version: str
    payload: Mapping[str, object]


@dataclass(frozen=True, slots=True)
class ComponentProvenanceLedger:
    components: Mapping[str, str]
