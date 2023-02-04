import logging
from typing import List

from sqlalchemy.orm import Session

from app.models.models import Book
from app.schemas.books import BookCreate

logger = logging.getLogger('emulator')


def create_book(db: Session, book: BookCreate):
    db_book = Book(
        title=book.title,
        description=book.description,
        rating=book.rating,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_book_by_title(db: Session, title: str) -> Book:
    return db.query(Book).filter(Book.title == title).first()


def get_books(db: Session) -> List[Book]:
    return db.query(Book).all()


def get_book_by_id(db: Session, book_id: int) -> Book:
    return db.query(Book).filter(Book.id == book_id).first()
