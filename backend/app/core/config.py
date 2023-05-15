import os
from pathlib import Path
from pydantic import BaseSettings, AnyHttpUrl

BASE_DIR = (Path(__file__) / ".." / ".." / ".." / "..").resolve()
ENV_PATH = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    API_V1_STR: str = "/bs/v1"
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_HOST: str
    PROJECT_PORT: int

    DB_USER: str
    DB_NAME: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int

    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str
    TEST_DB_HOST: str
    TEST_DB_PORT: int
      
    REDIS_HOST: str

    ALLOWED_ORIGIN: list[AnyHttpUrl] = [
        'http://localhost',
        'http://127.0.0.1',
        'http://0.0.0.0'
    ]

    INIT_AUTHOR: list = [
        {"first_name": "John", "last_name": "Tolkien"},
        {"first_name": "Aizek", "last_name": "Azimov"}
    ]

    INIT_BOOK: list = [
        {"title": "Hobbit", "description": "Bilbo's adventures", "amount": 10, "price": 10.50, "author_id": 1},
        {"title": "Robot dreams", "description": "about robots", "amount": 8, "price": 12.50, "author_id": 2}
    ]

    INIT_ROLE: list = [
        {"name": "admin"},
        {"name": "user"}
    ]

    INIT_USER: dict = {
        "username": "User1",
        "email": "user@test.com",
        "password": "U12e-!aQ",
        "is_active": "true",
        "role_id": 1
    }

    INIT_ORDER: dict = {
        "status": "pending",
        "description": "test",
        "cost": 1.00,
        "user_id": 1,
        "book_id": 1
    }

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(levelname)-7s %(asctime)s %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, 'logs', 'api.log'),
            "formatter": "standard",
            "encoding": "UTF-8",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 1000
        }
    },
    "loggers": {
        "bookshelf": {
            "handlers": ["console", "file"],
            "level": "DEBUG"
        }
    }
}
