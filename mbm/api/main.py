from fastapi import FastAPI

from mbm.api.routes.status import router as status_router
from mbm.config import get_settings

settings = get_settings()

app = FastAPI(
    title="MBM API",
    version="0.1.0",
    description="Universal MBM projection, settlement, and calibration platform.",
)

app.include_router(status_router, prefix="/api")


@app.get("/", tags=["root"])
def root() -> dict[str, str]:
    return {
        "service": "mbm-api",
        "status": "running",
        "environment": settings.environment,
    }
