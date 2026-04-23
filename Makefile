deps:
	uv sync
	npm install -g pnpm@10
	pnpm install

lint:
	uv run ruff check && uv run ruff format
	pnpm lint

lint-check:
	uv run ruff check && uv run ruff format --check
	pnpm lint

test:
	uv run pytest --disable-warnings

shell:
	uv run python manage.py shell_plus --ipython

# Docker

build:
	docker compose build

up:
	docker compose up -d

up-build:
	docker compose up --build -d

down:
	docker compose down

logs:
	docker compose logs -f app

bash:
	docker compose exec app bash

# Deploy

deploy:
	docker compose up --build -d
	docker compose exec app python manage.py migrate --noinput
	docker compose exec app python manage.py collectstatic --noinput
