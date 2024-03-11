install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

gendiff:
	poetry run gendiff jsons/file1.json jsons/file2.json

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -s

.PHONY: gendiff
