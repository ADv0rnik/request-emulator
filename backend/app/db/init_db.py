import logging

from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.core.config import Settings
from app.schemas.author import AuthorCreateModel
from app.schemas.book import BookCreateModel
from app.schemas.user import UserCreateModel

from app.crud.user import create_init_user
from app.crud.book import create_init_book
from app.crud.author import create_init_author


settings = Settings()
logger = logging.getLogger('bookshelf')


def init_db(db: Session):
    create_user(db)
    create_author(db)
    create_book(db)


def create_user(db: Session):
    user = settings.INIT_USER
    try:
        db_user = UserCreateModel(
            username=user['username'],
            email=user['email'],
            password=user['password'],
            is_active=user['is_active'],
            role_id=user['role_id']
        )
    except ValidationError as e:
        logger.error(f"An error occur while creating model {e}")
    else:
        create_init_user(db, db_user)


def create_author(db: Session):
    for author in settings.INIT_AUTHOR:
        db_author = AuthorCreateModel(
            first_name=author['first_name'],
            last_name=author['last_name']
        )
        create_init_author(db, db_author)


def create_book(db: Session):
    for book in settings.INIT_BOOK:
        db_book = BookCreateModel(
            title=book['title'],
            description=book['description'],
            amount=book['amount'],
            price=book['price'],
            author_id=book['author_id']
        )
        create_init_book(db, db_book)
