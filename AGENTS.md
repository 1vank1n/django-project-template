# AGENTS.md

## Cursor Cloud specific instructions

### Project overview

Django Project Template — a server-rendered Django app with a Gulp-based frontend asset pipeline (Sass/Stylus, Babel, BrowserSync). Uses SQLite by default.

### Environment details

- **Python 3.12** managed via Poetry (virtualenv in `~/.cache/pypoetry/virtualenvs/`)
- **Node.js 25** via nvm, **pnpm 10** for JS deps
- The `.env` file must be placed at the **repository root** (`/workspace/.env`), not under `settings/`. The `split_settings` `exec()` context makes `BASE_DIR` resolve to `/workspace` (not `/workspace/settings`).

### Key commands

See `README.md` for full details. Quick reference:

| Task | Command |
|---|---|
| Install all deps | `make deps` |
| Python lint | `poetry run ruff check && poetry run ruff format --check` |
| JS lint | `ESLINT_USE_FLAT_CONFIG=false npx eslint frontend/` |
| Tests | `poetry run pytest --disable-warnings` |
| Build frontend | `NODE_ENV=production BUILD=True npx gulp` |
| Dev server (backend) | `poetry run python manage.py runserver 0.0.0.0:8000` |
| Dev server (frontend) | `pnpm start` (Gulp + BrowserSync live-reload) |
| Migrations | `poetry run python manage.py migrate` |

### Non-obvious caveats

- **ESLint 9 with legacy config**: The project uses `.eslintrc.js` (legacy format) with ESLint v9. You must set `ESLINT_USE_FLAT_CONFIG=false` when running ESLint.
- **pnpm build scripts warning**: pnpm 10 may warn about ignored build scripts for `@parcel/watcher`, `core-js`, `es5-ext`. The project works without running those build scripts.
- **django-spurl deprecation warnings**: `spurl` has invalid escape sequences that produce `SyntaxWarning` on Python 3.12. These are harmless.
- **Superuser creation**: Use `poetry run python manage.py createsuperuser --noinput --username admin --email admin@example.com` then set password via `manage.py changepassword admin`.
