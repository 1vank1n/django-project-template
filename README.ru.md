# Шаблон проекта Django

[English](README.md) | [Русский](README.ru.md)

Практичный шаблон для проектов на Django с современным фронтенд-стеком.

## Технологии

- **Python 3.13** и **uv** для управления зависимостями
- **Django 5.2 LTS** как веб-фреймворк
- **Node.js 25** и **Vite** для сборки фронтенда (через **django-vite**)
- **ESLint** и **Ruff** для статического анализа
- **Sass** для стилей
- **Gunicorn** для продакшн-сервинга WSGI
- **django-axes** для защиты от брутфорса

## Быстрый старт

1. Создайте проект из шаблона
   `django-admin startproject project_name --template=https://github.com/1vank1n/django-project-template/archive/master.zip`
2. Установите зависимости Python и Node
   `make deps`
3. Настройте переменные окружения `.env.template` → `.env`
4. Примените миграции и запустите сервера разработки

   ```
   uv run python manage.py migrate
   uv run python manage.py runserver   # backend
   pnpm dev                            # Vite dev server с HMR
   ```

## Развертывание

- Укажите боевые значения в `.env` (`DEBUG=off`, `SECRET_KEY`, `DATABASE_URL`, `GUNICORN_*`)
- Запустите `make deploy` — соберёт образ, поднимет контейнер, применит миграции, соберёт статику

## Структура проекта

```
applications/     приложения Django (core, main)
frontend/         исходники фронтенда (images, scripts, styles)
settings/         настройки проекта (компоненты split-settings)
templates/        шаблоны Django
static/           собранная статика (генерируется Vite)
logs/             журналы работы
gunicorn.conf.py  конфигурация Gunicorn (читает GUNICORN_* из env)
vite.config.js    конфигурация Vite
```

## Конфигурационные файлы

- `.editorconfig` — правила форматирования редакторов
- `eslint.config.js` — правила ESLint (flat config)
- `.gitignore` — игнорируемые Git файлы
- `.dockerignore` — файлы, исключаемые из контекста Docker-сборки
- `.nvmrc` — версия Node.js для nvm
- `.python-version` — версия Python для pyenv
- `.env.template` — переменные окружения по умолчанию для разработки

## Контакты

Вопросы? Создайте issue или напишите на lukyanets.ivan@gmail.com
