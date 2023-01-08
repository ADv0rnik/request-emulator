import os
from pathlib import Path
from pydantic import BaseSettings

BASE_DIR = (Path(__file__) / ".." / ".." / "..").resolve()
ENV_PATH = (os.path.join(BASE_DIR, ".env"))


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_HOST: str
    PROJECT_PORT: int

    API_URL: str = "/emulator/v1/"

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
