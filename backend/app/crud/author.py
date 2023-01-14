from sqlalchemy.orm import Session

from app.models.models import Author
from app.schemas.authors import AuthorCreate


def create_author(db: Session, author: AuthorCreate):
    db_author = Author(
        first_name=author.first_name,
        last_name=author.last_name
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author



