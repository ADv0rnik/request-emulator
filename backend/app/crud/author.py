import logging
from typing import List

from sqlalchemy.orm import Session
from app.models.author import Author


logger = logging.getLogger('bookshelf')


def create_init_author(db: Session, author: Author) -> Author:
    db_author = Author(
        first_name=author.first_name,
        last_name=author.last_name
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    logger.info(f'Created author {db_author}')
    return db_author


def get_author_by_id(db: Session, id_: int) -> Author:
    return db.query(Author).filter(Author.id == id_).first()


def get_author_list(db: Session) -> List[Author]:
    return db.query(Author).all()
