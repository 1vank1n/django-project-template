# 1. Frontend
FROM node:25-alpine AS frontend_builder
WORKDIR /app

RUN npm install -g pnpm@10.15
COPY package.json pnpm-lock.yaml gulpfile.babel.js .babelrc ./
RUN pnpm install

COPY ./tasks ./tasks
COPY ./frontend ./frontend
RUN pnpm build

# 2. Backend
FROM python:3.12-slim
WORKDIR /app

ARG APP_VERSION
ENV APP_VERSION=${APP_VERSION}

RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential curl gettext make \
	&& rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.8.3
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
	&& poetry install --no-root --no-interaction

COPY . ./
COPY --from=frontend_builder /app/static/ /app/static/

COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD /entrypoint.sh
