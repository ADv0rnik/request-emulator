import pytest

from typing import Generator, Any

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from fastapi import FastAPI


from app.db.base import Base
from app.db.session import get_db
from app.core.config import settings
from app.api.api import api_router
from backend.app.db.init_db import create_book, create_author



TEST_SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://{settings.TEST_DB_USER}:{settings.TEST_DB_PASS}@' \
                          f'{settings.TEST_DB_HOST}:{settings.TEST_DB_PORT}/{settings.TEST_DB_NAME}'

engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)
SessionTesting = sessionmaker(bind=engine)


def start_application():
    app = FastAPI()
    app.include_router(api_router)
    return app


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    Base.metadata.create_all(bind=engine)
    _app = start_application()
    yield _app
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    create_author(session)
    create_book(session)

    yield session 
    session.close()
    transaction.rollback()
    connection.close()



@pytest.fixture(scope="function")
def client(
    app: FastAPI, db_session: SessionTesting
) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client
