deps:
	poetry install --with dev --no-root --no-interaction
	npm install -g pnpm@10
	pnpm install

lint:
	$(DOCKER_EXEC) ruff check && ruff format

lint-check:
	$(DOCKER_EXEC) ruff check && ruff format --check

test:
	poetry run pytest --disable-warnings

# Docker

build:
	docker compose build

up:
	docker compose up -d

up-build:
	docker compose up --build -d

down:
	docker compose down
