# Project FandomHub

<p align="center">
  <a href="https://github.com/tyronejosee/project_new_store#gh-light-mode-only" target="_blank">
    <img src="./static/img/logo_light.svg" alt="logo-light" width="80">
  </a>
  <a href="https://github.com/tyronejosee/project_new_store#gh-dark-mode-only" target="_blank">
    <img src="./static/img/logo_dark.svg" alt="logo-dark" width="80">
  </a>
</p>
<p align="center">
An API for querying information about anime and manga, based on MyAnimeList, providing details such as titles, genres, ratings, and user reviews.
<p>
<p align="center">
  <a href="#"><strong>Documentation</strong></a>
</p>
<p align="center">
  <a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/python-3.11.8-blue" alt="python-version">
  </a>
  <a href="https://www.djangoproject.com/">
  <img src="https://img.shields.io/badge/django-5.0.1-green" alt="django-version">
  </a>
  <a href="https://www.django-rest-framework.org/">
  <img src="https://img.shields.io/badge/drf-3.14.0-red" alt="django-version">
  </a>
</p>

## Installation

Clone the repository.

```bash
git clone git@github.com:tyronejosee/project_fandomhub_api.git
```

Create a virtual environment (Optional).

```bash
python -m venv env
```

Activate the virtual environment (Optional).

```bash
env\Scripts\activate
```

Install all dependencies.

```bash
pip install -r requirements/local.txt
```

Create an environment variable file .env.

```bash
SECRET_KEY=""
EMAIL_BACKEND=""
EMAIL_HOST=""
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
EMAIL_PORT=""
EMAIL_USE_TLS=""
```

Docker run.

```bash
(env) docker compose up
(env) docker compose up --build
(env) docker compose stop
(env) docker compose logs -f
(env) docker compose start
(env) docker compose restart <service>
```

Perform database migrations.

```bash
(env) docker compose exec web bash
(env) docker compose exec web python manage.py makemigrations*
(env) docker compose exec web python manage.py migrate
```

> Note: Create the migrations in case Django skips any.

## Usage

Create a superuser to access the entire site without restrictions.

```bash
(env) docker compose exec web python manage.py createsuperuser
```

Log in to `admin`:

```bash
http://127.0.0.1:8000/admin/
```

Access to Swagger o Redoc.

```bash
http://127.0.0.1:8000/api/schema/swagger/
http://127.0.0.1:8000/api/schema/redoc/
```

## Internationalization

Generate translation files for the languages.

```bash
(env) docker compose exec web django-admin makemessages -l ja --ignore=env/*
(env) docker compose exec web django-admin makemessages -l es --ignore=env/*
```

> Use --ignore to exclude specific directories from translation.

Compile translation files after making changes to translations.

```bash
(env) docker compose exec web django-admin compilemessages
```

## Important Notes

Check the creation of migrations before creating them.

```bash
(env) docker compose exec web bash
(env) docker compose exec web python manage.py makemigrations users
(env) docker compose exec web python manage.py makemigrations
(env) docker compose exec web python manage.py migrate
```

> Note: Checking migrations before their creation is necessary to avoid inconsistencies in user models.

## PostgreSQL

```bash
(env) docker compose exec db psql -U postgres -d fandomhub_db
(fandomhub_db=#) \dt
```

## Redis

```bash
(env) docker compose exec redis redis-cli
(127.0.0.1:6379) keys *
```

## License

This project is under the [Apache-2.0 license](https://github.com/tyronejosee/project_fandomhub_api/blob/main/LICENSE).
