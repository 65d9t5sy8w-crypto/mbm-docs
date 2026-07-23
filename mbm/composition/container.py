from dataclasses import dataclass

from mbm.dashboard.service import BoardService


@dataclass(frozen=True, slots=True)
class Container:
    board_service: BoardService


def build_container() -> Container:
    return Container(board_service=BoardService())
