deps:
	poetry install
	npm install

lint:
	ruff check .
