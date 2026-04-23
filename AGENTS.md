# AGENTS.md

## Cursor Cloud specific instructions

### Project overview

Django Project Template — a server-rendered Django app with a Vite-based frontend asset pipeline (Sass, ES modules) integrated via django-vite. Uses SQLite by default, optionally S3-compatible storage for static/media.

### Environment details

- **Python 3.13** managed via **uv** (project venv in `.venv/`)
- **Node.js 25** via nvm, **pnpm 10** for JS deps
- The `.env` file must be placed at the **repository root** (`/workspace/.env`), not under `settings/`. The `split_settings` `exec()` context makes `BASE_DIR` resolve to `/workspace` (not `/workspace/settings`).

### Key commands

See `README.md` for full details. Quick reference:

| Task | Command |
|---|---|
| Install all deps | `make deps` |
| Python lint | `uv run ruff check && uv run ruff format --check` |
| JS lint | `pnpm lint` |
| Tests | `uv run pytest --disable-warnings` |
| Build frontend | `pnpm build` |
| Dev server (backend) | `uv run python manage.py runserver 0.0.0.0:8000` |
| Dev server (frontend) | `pnpm dev` (Vite dev server with HMR on :5173) |
| Migrations | `uv run python manage.py migrate` |
| Django shell | `make shell` (`shell_plus --ipython`) |
| Deploy | `make deploy` (build image, migrate, collectstatic) |

### Non-obvious caveats

- **Settings are split**: all Django settings live under `settings/components/*.py` and are combined via `django-split-settings` in `settings/settings.py`. Add new sections as separate files and include them there.
- **Vite dev vs prod**: `DJANGO_VITE['default']['dev_mode']` is bound to `DEBUG`. In dev, `{% vite_asset %}` tags point to `http://localhost:5173`; in prod, they read `static/vite/manifest.json`. Make sure `pnpm build` ran before `collectstatic` in prod.
- **S3 is opt-in**: storage switches to S3 automatically when `AWS_STORAGE_BUCKET_NAME` is set in `.env`. Empty — local filesystem. See `settings/components/storages.py`.
- **django-axes**: login failures beyond `AXES_FAILURE_LIMIT` lock out the IP+username pair for `AXES_COOLOFF_TIME` hours. Migrations required (`axes_*` tables).
- **pnpm build scripts warning**: pnpm 10 may warn about ignored build scripts for `@parcel/watcher`, `esbuild`. The project works without them.
- **Superuser creation**: `uv run python manage.py createsuperuser --noinput --username admin --email admin@example.com` then `uv run python manage.py changepassword admin`.
