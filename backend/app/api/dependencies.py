import logging
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, HTTPBasic
from jose import JWTError, jwt
from sqlalchemy.orm import Session


from app.core.config import settings
from app.core.security import verify_password
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import CurrentUserModel
from app.crud.user import get_user_by_email


security = HTTPBasic()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f'{settings.API_V1_STR}/token')
logger = logging.getLogger('bookshelf')


def authenticate_user(email: str, password: str, db: Session = Depends(get_db)) -> User | bool:
    user = get_user_by_email(db, email)
    if not (user and verify_password(password, user.password)):
        logger.error(msg="Password verification error")
        return False
    return user


async def get_current_user(
        db: Session = Depends(get_db),
        token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=400,
        detail="Wrong login or password"
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
    except JWTError as err:
        raise credentials_exception from err
    else:
        email = payload.get('sub')
        if (user := get_user_by_email(db, email)) is None:
            raise credentials_exception
        return CurrentUserModel(
            id=user.id,
            email=user.email,
            role_id=user.role_id
        )


async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
