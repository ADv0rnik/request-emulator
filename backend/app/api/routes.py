import logging
from typing import List

from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.db.session import get_db
from fastapi import Depends, HTTPException
from app.schemas.authors import Author, AuthorCreate
from app.schemas.books import Book, BookCreate
from app.crud.author import create_author, get_author_by_last_name, get_author_by_id
from app.crud.book import create_book, get_book_by_title, get_books, get_book_by_id


router = APIRouter()
logger = logging.getLogger('emulator')


@router.post("/author", response_model=Author)
def create_new_author(author: AuthorCreate, db: Session = Depends(get_db)):
    if db_author := get_author_by_last_name(db, author.last_name):
        logger.warning(f"Author with this last name '{db_author.last_name}' is already exist")
        raise HTTPException(status_code=400, detail="Author is already exist")
    return create_author(db, author)

#TODO: Get all authors


@router.get("/author/{author_id}", response_model=Author)
def get_author(author_id: int, db: Session = Depends(get_db)):
    if db_author := get_author_by_id(db, author_id):
        return db_author
    logger.error(f"Author with id {author_id} does not exist")
    raise HTTPException(status_code=400, detail=f"Author with id {author_id} does not exist")


@router.post("/book", response_model=Book)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    if db_book := get_book_by_title(db=db, title=book.title):
        logger.warning(f"Book with this title {db_book.title} is already exist")
        raise HTTPException(status_code=400, detail="Book is already exist")
    db_author = get_author_by_id(db, book.author_id)
    if not db_author:
        logger.error(f'Author with such id={book.author_id} doesn\'t exist')
        raise HTTPException(status_code=400,
                            detail=f'Can\'t create book object because author with id={book.author_id} doesn\'t exist')
    return create_book(db, book)


@router.get("/book", response_model=List[Book])
def get_books_list(db: Session = Depends(get_db)):
    return get_books(db=db)


@router.get("/book/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    if db_book := get_book_by_id(db, book_id):
        return db_book
    logger.error(f"Book with id {book_id} does not exist")
    raise HTTPException(status_code=400, detail=f"Book with id {book_id} does not exist")


@router.delete('/book/{book_id}')
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = get_book_by_id(db, book_id)
    if not db_book:
        logger.error(f'Book with id={book_id} does not exist')
        raise HTTPException(status_code=400, detail=f'Book with id={book_id} does not exist')
    db.delete(db_book)
    db.commit()
    logger.info(f'Status: 200; Book with id={book_id} has been deleted')
    return {'status': 'ok', 'detail': 'Book with id={} has been deleted'.format(book_id)}
