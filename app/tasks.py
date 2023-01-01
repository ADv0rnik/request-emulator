from db.tasks import connect_to_db, disconnect_from_db

from fastapi import FastAPI
from typing import Callable


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await connect_to_db(app)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def close_app() -> None:
        await disconnect_from_db(app)

    return close_app
