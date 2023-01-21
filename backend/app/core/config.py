import os
from pathlib import Path
from pydantic import BaseSettings
from pydantic.networks import AnyHttpUrl

BASE_DIR = (Path(__file__) / ".." / ".." / ".." / "..").resolve()
ENV_PATH = (os.path.join(BASE_DIR, ".env"))
BASE_URL_PATH = '/api'


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_HOST: str
    PROJECT_PORT: int

    ALLOWED_ORIGIN: list[AnyHttpUrl] = [
        'http://localhost',
        'http://127.0.0.1'
    ]

    API_URL: str = "/emulator/v1"

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(levelname)-7s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'emulator.log'),
            'formatter': 'standard',
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 100,
            'encoding': 'UTF-8'
        }
    },
    'loggers': {
        'emulator': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        }
    }
}
