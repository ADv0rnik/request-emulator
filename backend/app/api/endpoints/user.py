import logging

from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserOutModel, UserCreateModel, UserModel
from app.crud.user import create_init_user, get_user_by_email, get_user
from app.api.dependencies import get_current_user


user_router = APIRouter()
logger = logging.getLogger('bookshelf')


@user_router.post('/', response_model=UserModel)
async def create_user(user: UserCreateModel, db: Session = Depends(get_db)):
    if db_user := get_user_by_email(db, user.email):
        logger.error(msg=f"User with {db_user.email} already exist")
        return HTTPException(status_code=400, detail=f"User with {db_user.email} already exist")
    else:
        return create_init_user(db, user)


@user_router.get('/{user_id}', response_model=UserOutModel)
async def return_user(user_id: int, db: Session = Depends(get_db), _=Security(get_current_user)):
    if user := get_user(db, user_id):
        logger.info(f'Return user {user.id}')
        return UserOutModel(
            id=user.id,
            username=user.username,
            email=user.email,
            role_id=user.role_id,
            role=user.role.name
        )
    logger.error(msg=f'User with {user_id} not found')
    return HTTPException(status_code=404, detail=f'User with {user_id} not found')

