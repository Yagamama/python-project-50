install:
	pipx install poetry

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

gendiff:
	poetry run gendiff test_files/file1.json test_files/file2.json

gd_plain:
	poetry run gendiff -f plain test_files/file1.json test_files/file2.json

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -s

test-coverage:
	poetry run pytest --cov

.PHONY: gendiff
