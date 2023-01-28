import logging

from sqlalchemy.orm import Session

from app.models.models import Author
from app.schemas.authors import AuthorCreate


logger = logging.getLogger('emulator')


def create_author(db: Session, author: AuthorCreate):
    db_author = Author(
        first_name=author.first_name,
        last_name=author.last_name
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    logger.info(f"Created author {author.first_name}{author.last_name}")
    return db_author


def get_author_by_last_name(db: Session, last_name: str) -> Author:
    return db.query(Author).filter(Author.last_name == last_name).first()


def create_init_author(db: Session, author: dict):
    db_author = Author(
        first_name=author["first_name"],
        last_name=author["last_name"]
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    logger.info(f"initial state for author table has been created")
    return db_author



