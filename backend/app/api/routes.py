import logging

from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.db.session import get_db
from fastapi import Depends, HTTPException
from app.schemas.authors import Author, AuthorCreate
from app.schemas.books import Book, BookCreate
from app.crud.author import create_author, get_author_by_last_name
from app.crud.book import create_book


router = APIRouter()
logger = logging.getLogger('emulator')


@router.post("/author/", response_model=Author)
def create_new_author(author: AuthorCreate, db: Session = Depends(get_db)):
    if db_author := get_author_by_last_name(db, author.last_name):
        logger.warning(f"Author with this last name {author.last_name} is already exist")
        raise HTTPException(status_code=400, detail="Author is already exist")
    return create_author(db, author)


@router.post("/book/", response_model=Book)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)
