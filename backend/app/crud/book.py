from sqlalchemy.orm import Session

from app.models.models import Book
from app.schemas.books import BookCreate


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
