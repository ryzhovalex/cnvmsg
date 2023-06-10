export PYTEST_SHOW=all

test:
	poetry run coverage run -m pytest -x -p no:warnings --show-capture=$(PYTEST_SHOW) --failed-first cvm

lint:
	poetry run ruff .

check: lint test

coverage:
	poetry run coverage report -m

coverage.html:
	poetry run coverage html --show-contexts && poetry run python -m http.server -d htmlcov 8000

changelog:
# Conventional Commits is used since we use exclamation marks to sign breaking
# commits.
	poetry run git-changelog -c conventional -o CHANGELOG.md .
