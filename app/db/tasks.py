from databases import Database
from fastapi import FastAPI

from ..config import settings


async def connect_to_db(app: FastAPI) -> None:
    db = Database(settings.DATABASE_URL)

    try:
        await db.connect()
        app.state._db = db
    except Exception as error:
        print(error)


async def disconnect_from_db(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as error:
        print(error)


