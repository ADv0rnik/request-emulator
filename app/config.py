import os
from typing import Any

from pydantic import BaseSettings
from pydantic import PostgresDsn
from pydantic import validator


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_HOST: str
    PROJECT_PORT: int

    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    POSTGRES_DATABASE: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    DATABASE_URL: PostgresDsn | None

    @validator("DATABASE_URL", pre=True)
    def assemble_db_connection(cls, value: str, values: dict) -> Any:
        if isinstance(value, str):
            return value
        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            user=values.get("POSTGRES_USERNAME"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOST"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DATABASE') or ''}"
        )

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"


settings = Settings()
