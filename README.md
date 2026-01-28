# Django Project Template

[English](README.md) | [Русский](README.ru.md)

A practical starting point for Django projects with a modern frontend build.

## Technologies

- **Python 3.12** with **Poetry** for backend dependencies
- **Django 4.2+** as the web framework
- **Node.js 25** with **Gulp** and **Babel** for asset pipeline
- **ESLint** and **Ruff** for linting
- **Sass/Stylus** for styles

## Getting Started

1. Create a new project from the template
   `django-admin startproject project_name --template=https://github.com/1vank1n/django-project-template/archive/master.zip`
2. (Optional) Create virtual environment in `.venv/`
   `python -m venv .venv && source .venv/bin/activate`
3. Install Python and Node dependencies
   `make deps`
4. Adjust environment variables `.env.template` → `.env`
5. Apply migrations and run development servers

   ```
   python manage.py migrate
   python manage.py runserver   # backend
   npm start                    # frontend assets with live reload
   ```

## Deployment

- Set production values in `.env` (disable `DEBUG`, set `SECRET_KEY`, configure `DATABASE_URL`)
- Build static assets: `npm run build`
- Collect static files: `python manage.py collectstatic`
- Run under a WSGI/ASGI server such as `gunicorn` or `uvicorn`

## Project Structure

```
applications/   Django apps (core, main)
frontend/       source frontend files (images, scripts, styles)
settings/       Django project settings
tasks/          Gulp tasks
templates/      Django templates
static/         compiled static assets (generated)
logs/           runtime logs
```

## Configuration Files

- `.babelrc` – Babel preset configuration for modern JS
- `.editorconfig` – editor formatting rules
- `.eslintrc.js` – ESLint rules for JavaScript
- `.gitignore` – files ignored by Git
- `.nvmrc` – Node.js version for nvm
- `.python-version` – Python version for pyenv
- `.env.template` – default environment variables for local development

## Contact

Questions? Create an issue or email lukyanets.ivan@gmail.com
