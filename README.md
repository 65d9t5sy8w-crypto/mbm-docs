# MBM Cursor Drop 01 — Executable Foundation

This repository is the first executable baseline for MBM.

## Included
- FastAPI service
- PostgreSQL-ready configuration
- SQLAlchemy session layer
- Provider-neutral contracts
- Projection, settlement, learning, dashboard, and governance package boundaries
- Docker and Docker Compose
- CI workflow
- Smoke tests
- Architecture documentation
- Durable agent instructions

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

Open:

- API root: http://localhost:8000
- Status: http://localhost:8000/api/status
- OpenAPI: http://localhost:8000/docs

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
uvicorn mbm.api.main:app --reload
```

## Current scope

Drop 01 establishes the universal runtime foundation. It does not yet implement the full Revision 9 CS2 projection subsystem.
