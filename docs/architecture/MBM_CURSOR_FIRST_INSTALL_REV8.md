# MBM Cursor First Install

**Revision 8 (Locked Baseline)**

## Purpose

This document is the initial integration package for the MBM Cursor workspace. It establishes the production architecture, governance boundaries, and implementation order before feature development begins.

## Technology Stack

- Cursor (primary engineering environment)
- Git
- CI Pipeline
- Docker
- FastAPI
- PostgreSQL
- Background Workers
- React/Next.js Dashboard

## Architecture Principles

1. Provider-neutral interfaces only.
2. Immutable evidence and settlement records.
3. Typed contracts between every subsystem.
4. Versioned outputs for every projection layer.
5. Fail-closed on missing critical evidence.
6. Continuous settlement and calibration.

## Integration Order

1. Core architecture
2. Dependency injection
3. Dashboard services
4. Provider adapters
5. Projection engine
6. Settlement engine
7. Learning/calibration
8. Monitoring
9. CS2 Projection Subsystem

## CS2 Projection Subsystem

The Final Projection Engine consumes six typed layer outputs:

- Map Opportunity Profile
- Role Opportunity Profile
- Behavioral State
- Environment
- Reliability
- Market Layer

Each layer embeds its own version identifier. The Final Projection Engine assembles a Component Provenance Ledger from those embedded version tags, allowing every projection to be reproduced and audited.

## Directory Layout

```
MBM/
├── docs/
│   ├── architecture/
│   ├── governance/
│   └── projections/
├── mbm/
│   ├── behavioral/
│   ├── providers/
│   ├── projections/
│   ├── settlement/
│   ├── learning/
│   ├── dashboard/
│   └── api/
├── tests/
└── docker/
```

## Acceptance Criteria

- Provider-neutral boundaries preserved.
- Immutable evidence ledger operational.
- Dashboard resolves through dependency injection.
- Projection outputs include provenance.
- Settlement feeds calibration automatically.
- No provider-specific models cross universal boundaries.
