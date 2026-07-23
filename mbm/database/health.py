from sqlalchemy import text

from mbm.database.session import engine


def database_health() -> dict[str, object]:
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as exc:
        return {"status": "unavailable", "detail": exc.__class__.__name__}
