# Шаблон проекта Django

[English](README.md) | [Русский](README.ru.md)

Практичный шаблон для проектов на Django с современным фронтенд-стеком.

## Технологии

- **Python 3.11** и **Poetry** для управления зависимостями
- **Django 4.2+** как веб-фреймворк
- **Node.js 20**, **Gulp** и **Babel** для сборки фронтенда
- **ESLint** и **Ruff** для статического анализа
- **Sass/Stylus** для оформления

## Быстрый старт

1. Создайте проект из шаблона  
   `django-admin startproject project_name --template=https://github.com/1vank1n/django-project-template/archive/master.zip`
2. (Опционально) создайте виртуальное окружение в `.env/`  
   `python -m venv .env && source .env/bin/activate`
3. Установите зависимости Python и Node  
   `make deps`
4. Настройте переменные окружения в `config/.env.local`
5. Примените миграции и запустите сервера разработки

   ```
   python manage.py migrate
   python manage.py runserver   # backend
   npm start                    # сборка фронтенда и livereload
   ```

## Развертывание

- Укажите боевые значения в `config/.env.local` (`DEBUG=off`, `SECRET_KEY`, `DATABASE_URL`)
- Соберите статические ресурсы: `npm run build`
- Выполните `python manage.py collectstatic`
- Запускайте под WSGI/ASGI-сервером (`gunicorn`, `uvicorn` и т.п.)

## Структура проекта

```
applications/   приложения Django (core, main)
config/         конфигурация окружения (.env.local)
frontend/       исходники фронтенда (images, scripts, styles)
settings/       настройки проекта Django
tasks/          задачи Gulp
templates/      шаблоны Django
static/         собранные статические файлы (генерируются)
logs/           журналы работы
```

## Конфигурационные файлы

- `.babelrc` — настройки Babel для современного JS
- `.editorconfig` — правила форматирования редакторов
- `.eslintrc.js` — правила ESLint для JavaScript
- `.gitignore` — игнорируемые Git файлы
- `.nvmrc` — версия Node.js для nvm
- `.python-version` — версия Python для pyenv
- `config/.env.local` — переменные окружения по умолчанию для разработки

## Контакты

Вопросы? Создайте issue или напишите на lukyanets.ivan@gmail.com
