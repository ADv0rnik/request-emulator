import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.schemas.author import AuthorModel
from app.models.author import Author
from app.crud.author import get_author_by_id, get_author_list


author_router = APIRouter()
logger = logging.getLogger('bookshelf')


@author_router.get('/author/{author_id}', response_model=AuthorModel)
def get_author(author_id: int, db: Session = Depends(get_db)) -> Author:
    if db_author := get_author_by_id(db, author_id):
        logger.info(msg=f"Get author {db_author.first_name}, {db_author.last_name}")
        return db_author
    else:
        logger.error(f'Author does\'t with id={author_id} exist')
        raise HTTPException(status_code=404, detail=f'Author does\'t with id={author_id} exist')
