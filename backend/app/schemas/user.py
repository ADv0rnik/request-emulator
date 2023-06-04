from typing import List, Optional

from pydantic import BaseModel, Field


USER_PASSWORD_REGEX = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])"


class UserBaseModel(BaseModel):
    username: str
    email: str
    role_id: int


class UserCreateModel(UserBaseModel):
    password: str = Field(
        min_length=8,
        max_length=20,
        regex=USER_PASSWORD_REGEX
    )


class UserUpdateModel(UserBaseModel):
    password: str


class UserModel(UserBaseModel):
    id: int

    class Config:
        orm_mode = True


class CurrentUserModel(BaseModel):
    id: int
    email: str
    role_id: int


class UserOutModel(UserBaseModel):
    id: int
    role: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
    email: str


class TokenData(BaseModel):
    email: str | None = None
