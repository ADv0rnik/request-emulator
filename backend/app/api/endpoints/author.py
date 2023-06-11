import logging

from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.schemas.author import AuthorModel, AuthorCreateModel
from app.models.author import Author
from app.crud.author import get_author_by_id, get_author_list, get_author_by_last_name, create_init_author
from app.api.dependencies import get_current_user


author_router = APIRouter()
logger = logging.getLogger('bookshelf')


@author_router.get('/{author_id}', response_model=AuthorModel)
def get_author(author_id: int, db: Session = Depends(get_db)) -> Author:
    if db_author := get_author_by_id(db, author_id):
        logger.info(msg=f"Get author {db_author.first_name}, {db_author.last_name}")
        return db_author
    else:
        logger.error(f'Author does\'t with id={author_id} exist')
        raise HTTPException(status_code=404, detail=f'Author with id={author_id} doesn\'t exist')


@author_router.post('/author', response_model=AuthorModel)
async def create_author(
        author: AuthorCreateModel,
        db: Session = Depends(get_db),
        _=Security(get_current_user)
):
    if db_author := get_author_by_last_name(author.last_name, db):
        logger.error(msg=f'Author with {db_author.last_name} already exist')
        return HTTPException(status_code=200, detail=f'Author with {db_author.last_name} already exist')
    else:
        db_author = create_init_author(db, author)
        return db_author
        raise HTTPException(status_code=404, detail=f'Author does\'t with id={author_id} exist')
