import logging
from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.db.session import get_db
from app.schemas.user import Token
from app.api.dependencies import authenticate_user
from app.core.security import create_access_token
from app.core.config import settings


token_router = APIRouter()
logger = logging.getLogger('bookshelf')


@token_router.post('', response_model=Token)
async def login_for_access_token(
        from_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
) -> Any:
    if not (user := authenticate_user(
            email=from_data.username,
            password=from_data.password,
            db=db
    )):
        logger.error(msg="Incorrect username or password")
        return HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    logger.info(msg='Success returning token')
    return {"access_token": access_token, "token_type": "bearer", "email": user.email}
