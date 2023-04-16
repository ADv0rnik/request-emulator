from typing import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient


from app.db.base import Base
from app.db.session import get_db
from app.core.config import settings
from backend.app.db.init_db import create_user, create_author
from backend.app.db.init_role import init_role
from backend.main import app


TEST_SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://{settings.TEST_DB_USER}:{settings.TEST_DB_PASS}@' \
                          f'{settings.TEST_DB_HOST}:{settings.TEST_DB_PORT}/{settings.TEST_DB_NAME}'

engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)
Session = sessionmaker(bind=engine)


@pytest.fixture(scope="session", autouse=True)
def override_get_db() -> Generator:
    Base.metadata.drop_all(bind=engine)  # pylint: disable=E1101
    Base.metadata.create_all(bind=engine)  # pylint: disable=E1101

    db_session = Session()
    init_role(db_session)
    create_user(db_session)
    create_author(db_session)
    try:
        yield db_session
    finally:
        db_session.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)