import os

from pydantic import BaseSettings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_HOST: str
    PROJECT_PORT: int

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"


settings = Settings()
