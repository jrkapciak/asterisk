.DEFAULT_GOAL := all

black:
	poetry run black . $(diff)

bandit:
	poetry run bandit -c pyproject.toml -r .

flake8:
	poetry run flake8 .

isort:
	poetry run isort . $(diff)

pylint:
	poetry run pylint */*.py

test:
	poetry run pytest --durations=1

lint: black bandit flake8 isort pylint
all: lint test