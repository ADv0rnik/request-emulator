from pydantic import BaseModel, Field


class UserBaseModel(BaseModel):
    username: str
    email: str
    is_active: bool
    role_id: int


class UserCreateModel(UserBaseModel):
    password: str = Field(
        min_length=8,
        max_length=20,
        regex=r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])"
    )


class UserUpdateModel(UserBaseModel):
    password: str


class UserModel(UserBaseModel):
    id: int

    class Config:
        orm_mode = True
