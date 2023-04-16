from pydantic import BaseModel


class AuthorBaseModel(BaseModel):
    first_name: str
    last_name: str


class AuthorCreateModel(AuthorBaseModel):
    pass


class AuthorUpdateModel(AuthorBaseModel):
    pass


class AuthorModel(AuthorBaseModel):
    id: int

    class Config:
        orm_mode = True

