import logging

from sqlalchemy.orm import Session

from app.schemas.role import RoleCreateModel
from app.crud.role import create_role
from app.core.config import Settings
from app.core.exceptions import RoleException


logger = logging.getLogger('bookshelf')
settings = Settings()


def init_role(db: Session):
    roles = settings.INIT_ROLE
    for role in roles:
        try:
            db_role = RoleCreateModel(
                name=role['name']
            )
            if new_role := create_role(db, db_role):
                logger.info(f"Created new role")
                return new_role
        except RoleException as err:
            logger.error(f"Error during created role {err}")
            return {"status": 500, "detail": "Can't create new role"}
