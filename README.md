[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)

### Bookstore emulator

Small web application with API for practicing requests

```
request-emulator
├─ backend
│  ├─ alembic
│  │  ├─ env.py
│  │  ├─ README
│  │  ├─ script.py.mako
│  │  └─ versions
│  │     └─ 84d868244fae_new_migration.py
│  ├─ alembic.ini
│  ├─ app
│  │  ├─ api
│  │  │  ├─ routes.py
│  │  │  └─ __init__.py
│  │  ├─ core
│  │  │  ├─ config.py
│  │  │  └─ __init__.py
│  │  ├─ crud
│  │  │  ├─ author.py
│  │  │  ├─ book.py
│  │  │  └─ __init__.py
│  │  ├─ db
│  │  │  ├─ db_setup.py
│  │  │  ├─ init_db.py
│  │  │  ├─ session.py
│  │  │  └─ __init__.py
│  │  ├─ models
│  │  │  ├─ mixin.py
│  │  │  ├─ models.py
│  │  │  └─ __init__.py
│  │  ├─ schemas
│  │  │  ├─ authors.py
│  │  │  ├─ books.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  ├─ initial_db.py
│  ├─ main.py
│  └─ __init__.py
├─ docker-compose.yml
├─ Dockerfile
├─ poetry.lock
├─ pyproject.toml
├─ README.md
├─ requirements.txt
└─ scripts
   └─ start_app.sh

```
