from pydantic import BaseModel, Field


USER_PASSWORD_REGEX = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])"


class UserBaseModel(BaseModel):
    username: str
    email: str
    is_active: bool
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


class Token(BaseModel):
    access_token: str
    token_type: str
    username: str