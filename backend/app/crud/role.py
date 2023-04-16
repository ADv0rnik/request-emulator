import logging
from sqlalchemy.orm import Session
from app.models.role import Role


logger = logging.getLogger('bookshelf')


def create_role(db: Session, role: Role):
    db_role = Role(
        name=role.name
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)

    return db_role
