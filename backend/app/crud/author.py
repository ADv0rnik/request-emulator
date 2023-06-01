import logging
from typing import List

from sqlalchemy.orm import Session
from app.models.author import Author


logger = logging.getLogger('bookshelf')


def create_init_author(db: Session, author: Author) -> Author:
    db_author = Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    logger.info(f'Created author {db_author.first_name} {db_author.last_name} with id={db_author.id}')
    return db_author


def get_author_by_id(db: Session, id_: int) -> Author:
    return db.query(Author).filter(Author.id == id_).first()


def get_author_list(db: Session) -> List[Author]:
    return db.query(Author).all()


def get_author_by_last_name(last_name: str, db: Session) -> Author:
    return db.query(Author).filter(Author.last_name == last_name).one_or_none()

