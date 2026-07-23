.PHONY: install test lint typecheck run

install:
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

typecheck:
	mypy mbm

run:
	uvicorn mbm.api.main:app --reload
