# MBM Cursor First Install
**Revision 8 — Locked Baseline**

## Purpose
Establish the executable universal MBM foundation in Cursor.

## Locked stack
- Cursor
- Git
- CI
- Docker
- FastAPI
- PostgreSQL
- Background workers
- React/Next.js dashboard

## Architecture rules
1. Provider-neutral interfaces only.
2. Immutable evidence and settlement records.
3. Typed contracts between every subsystem.
4. Versioned outputs for every projection layer.
5. Fail closed on missing critical evidence.
6. Continuous settlement and calibration.
7. Provider models remain inside adapter boundaries.
8. Final projections assemble a Component Provenance Ledger.

## Initial integration order
1. Universal package boundaries
2. Runtime configuration
3. FastAPI composition root
4. PostgreSQL session layer
5. Evidence ledger
6. Projection contracts
7. Settlement contracts
8. Learning/calibration contracts
9. Dashboard read service
10. CS2 Revision 9 subsystem

## Drop 01 acceptance criteria
- Installs from `pyproject.toml`.
- API starts.
- `/api/status` returns HTTP 200.
- PostgreSQL is provisioned through Docker Compose.
- Smoke tests pass.
- CI configuration exists.
- Universal package boundaries exist.
