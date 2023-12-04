# Django Project Template

It's very simple start point for django project.

For `Django >= 4.0` compatible with `Python >= 3.11`. `Node ~= 20.10`.

## Install

	django-admin startproject project_name --template=https://github.com/1vank1n/django-project-template/archive/master.zip
	poetry install
	npm i

## Usage

### Server (one terminal tab)
	python manage.py runserver

### Frontend (other terminal tab)
	npm start


## Structure

Recommend installation virtualenv in `.env` folder in project folder.

```
/.env	- virtualenv
/.git
/applications - folder for django applications
---/main      - start app point that I offer for you
/frontend     - folder for source "frontend" files
---/images    - gulp tasks look at this folder, files get->optimize->put to `/static/images/`
---/scripts   - gulp tasks look at this folder, files get->minify->put to `/static/scripts/`
---/styles    - gulp tasks look at this folder, get _common.styl->optimize->put to `/static/styles/base.css`
/settings     - django settings
/tasks        - gulp tasks
```

Any question? Create issue or type me to email = lukyanets.ivan@gmail.com
