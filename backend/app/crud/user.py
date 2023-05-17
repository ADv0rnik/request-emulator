import logging
from sqlalchemy.orm import Session
from app.models.user import User


logger = logging.getLogger('bookshelf')


def create_init_user(db: Session, user: User) -> User:
    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
        is_active=user.is_active,
        role_id=user.role_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logger.info(f'Created user {db_user}')
    return db_user


def get_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()
