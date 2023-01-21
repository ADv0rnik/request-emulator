import logging
from typing import List

from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.db.session import get_db
from fastapi import Depends, HTTPException
from app.schemas.authors import Author, AuthorCreate
from app.schemas.books import Book, BookCreate
from app.crud.author import create_author, get_author_by_last_name
from app.crud.book import create_book, get_book_by_title, get_books, get_book_by_id


router = APIRouter()
logger = logging.getLogger('emulator')


@router.post("/author", response_model=Author)
def create_new_author(author: AuthorCreate, db: Session = Depends(get_db)):
    if db_author := get_author_by_last_name(db, author.last_name):
        logger.error(f"Author with this last name '{author.last_name}' is already exist")
        raise HTTPException(status_code=400, detail="Author is already exist")
    return create_author(db, author)


@router.post("/book", response_model=Book)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    if db_book := get_book_by_title(db=db, title=book.title):
        logger.error(f"Book with this title {book.title} is already exist")
        raise HTTPException(status_code=400, detail="Book is already exist")
    return create_book(db, book)


@router.get("/book", response_model=List[Book])
def read_books(db: Session = Depends(get_db)):
    return get_books(db=db)


@router.get("/book/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    if db_book := get_book_by_id(db, book_id):
        return db_book
    logger.error(f"Book with id {book_id} does not exist")
    raise HTTPException(status_code=400, detail=f"Book with id {book_id} does not exist")
