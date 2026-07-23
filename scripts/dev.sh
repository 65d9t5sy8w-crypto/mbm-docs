#!/usr/bin/env sh
set -eu
uvicorn mbm.api.main:app --reload --host 0.0.0.0 --port 8000
