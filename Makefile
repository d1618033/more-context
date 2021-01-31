CODE=src
FOLDERS=src tests

check:
	poetry run pylint ${CODE}
	poetry run black --check ${FOLDERS}
	poetry run pytest --cov-report html:cov_html --cov=${CODE}

format:
	poetry run black ${FOLDERS}
