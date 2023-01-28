from sqlalchemy.orm import Session
from app.core.config import settings

from app.schemas.authors import AuthorCreate
from app.schemas.books import BookCreate

from app.crud.author import create_author
from app.crud.book import create_book


def init_db(db: Session):
    create_init_author(db)
    create_init_book(db)


def create_init_author(db: Session):
    for author in settings.INIT_AUTHOR:
        db_author = AuthorCreate(
            first_name=author["fname"],
            last_name=author["lname"]
        )
        create_author(db, db_author)


def create_init_book(db: Session):
    for book in settings.INIT_BOOK:
        db_book = BookCreate(
            title=book["title"],
            description=book["description"],
            rating=book["rating"],
            author_id=book["author_id"]
        )
        create_book(db, db_book)
