from mbm.dashboard.models import BoardSnapshot


class BoardService:
    def get_snapshot(self) -> BoardSnapshot:
        return BoardSnapshot(status="empty", total_projections=0)
