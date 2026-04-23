# 1. Frontend
FROM node:25-alpine AS frontend_builder
WORKDIR /app

RUN npm install -g pnpm@10
COPY package.json pnpm-lock.yaml vite.config.js ./
RUN pnpm install

COPY ./frontend ./frontend
RUN pnpm build

# 2. Backend
FROM python:3.14-slim
WORKDIR /app

ARG APP_VERSION
ENV APP_VERSION=${APP_VERSION}

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential curl gettext make \
	&& rm -rf /var/lib/apt/lists/*

ENV UV_COMPILE_BYTECODE=1 \
	UV_LINK_MODE=copy \
	UV_PROJECT_ENVIRONMENT=/usr/local

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY . ./
COPY --from=frontend_builder /app/static/ /app/static/

RUN uv sync --frozen --no-dev

CMD ["gunicorn", "settings.wsgi:application", "--config", "gunicorn.conf.py"]
