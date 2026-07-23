from typing import Protocol


class FixtureReadSource(Protocol):
    def read_fixture(self, external_id: str) -> object:
        ...
