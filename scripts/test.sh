#!/usr/bin/env sh
set -eu
ruff check .
mypy mbm
pytest
