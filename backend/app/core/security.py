import logging
from datetime import timedelta, datetime
from jose import jwt, JWTError

from passlib.context import CryptContext
from .config import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
logger = logging.getLogger('bookshelf')


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hash_: str) -> bool:
    return pwd_context.verify(password, hash_)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    logger.info(msg='Token has been created')
    return encoded_jwt
