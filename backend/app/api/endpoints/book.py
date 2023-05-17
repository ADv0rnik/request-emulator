import logging
from typing import List
from unittest import mock

mock.patch("fastapi_cache.decorator.cache", lambda *args, **kwargs: lambda f: f).start()

from fastapi import APIRouter, Depends, HTTPException
from app.db.session import get_db
from fastapi_cache.decorator import cache
from sqlalchemy.orm import Session

from app.schemas.book import BookModel
from app.crud.book import get_book_list, get_book_by_id


book_router = APIRouter()
logger = logging.getLogger('bookshelf')


@book_router.get('/{book_id}', response_model=BookModel)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    if book := get_book_by_id(db, book_id):
        return book
    else:
        logger.error(f"Book wasn't found, {book_id}")
        raise HTTPException(status_code=404, detail=f"Book wasn't found, {book_id}")


@book_router.get('/', response_model=List[BookModel])
@cache(expire=3600)
async def get_books(db: Session = Depends(get_db)):
    return get_book_list(db)


