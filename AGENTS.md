# MBM Agent Instructions

## Non-negotiable architecture rules
1. Provider-specific payloads never cross provider adapter boundaries.
2. Universal layers communicate through typed contracts.
3. Every projection result carries provenance and component version tags.
4. Missing critical evidence fails closed.
5. Settlement records are immutable after creation.
6. Calibration consumes settled observations only.
7. Composition wiring belongs in the composition root.
8. No dashboard layer computes projections or settlement results.

## Current milestone
Deliver an executable universal baseline that can start, expose health/status endpoints, connect to PostgreSQL, and support later CS2 integration without architectural rewrites.

## Cursor Cloud specific instructions

Services and standard commands are documented in `README.md`, `Makefile`, and `pyproject.toml`. Notes below are the non-obvious bits for this environment.

- Python: use `python3.12` (the app requires `>=3.12`). The startup update script provisions a `.venv`; activate it with `source .venv/bin/activate` before running any command. Reinstall deps with `pip install -e ".[dev]"` (also `make install`).
- Checks: `ruff check .`, `mypy mbm`, `pytest` (or `make lint` / `make typecheck` / `make test`). CI (`.github/workflows/ci.yml`) runs all three, so lint must be clean before pushing.
- Run the API: `uvicorn mbm.api.main:app --host 0.0.0.0 --port 8000` (or `make run` for `--reload`). Endpoints: `/`, `/api/status`, `/docs`.
- Database is optional for the API to be healthy. `GET /api/status` returns 200 even when the DB is down — `database.status` reports `unavailable` (fail-open on the health probe by design). Tests do not require a running database.
- Docker is NOT installed in this VM, so `docker compose up` (the README quick start) does not work here. To exercise the real DB session layer, run a native Postgres instead: start the cluster (`sudo pg_ctlcluster 16 main start`) and create a role/db matching `MBM_DATABASE_URL` (role `mbm`/password `mbm`, database `mbm` on `localhost:5432`). With that running, `GET /api/status` shows `database.status: ok`.
- Config is read from env vars prefixed `MBM_` (see `.env.example`); `mbm/config.py` also loads a local `.env`. The SQLAlchemy engine is created at import time in `mbm/database/session.py`, but each health probe opens a fresh connection, so starting Postgres after the app is already running still flips the status to `ok` without a restart.
