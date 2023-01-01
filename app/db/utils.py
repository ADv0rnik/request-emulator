from sqlalchemy.orm import Session
from db_setup import SessionLocal


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

