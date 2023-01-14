from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.db.session import get_db
from fastapi import Depends
from app.schemas.authors import Author, AuthorCreate
from app.schemas.books import Book, BookCreate
from app.crud.author import create_author
from app.crud.book import create_book


router = APIRouter()


@router.post("/author/", response_model=Author)
def create_new_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return create_author(db, author)


@router.post("/book/", response_model=Book)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)
