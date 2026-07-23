from fastapi import APIRouter

from mbm.database.health import database_health

router = APIRouter(tags=["system"])


@router.get("/status")
def status() -> dict[str, object]:
    return {
        "service": "mbm-api",
        "status": "ok",
        "architecture_revision": 8,
        "database": database_health(),
        "capabilities": {
            "projection": False,
            "settlement": False,
            "calibration": False,
            "dashboard": False,
            "cs2_adapter": False,
        },
    }
