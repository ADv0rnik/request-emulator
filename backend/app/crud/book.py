import logging
from typing import List

from sqlalchemy.orm import Session
from app.models.book import Book


logger = logging.getLogger('bookshelf')


def create_init_book(db: Session, book: Book) -> Book:
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    logger.info(f'Created book {db_book.title} with id={db_book.id}')
    return db_book


def get_book_by_id(db: Session, book_id: int) -> Book:
    return db.query(Book).filter(Book.id == book_id).first()


def get_book_list(db: Session) -> List[Book]:
    return db.query(Book).all()

