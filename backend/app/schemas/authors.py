from pydantic import BaseModel


class AuthorBase(BaseModel):
    first_name: str
    last_name: str


class AuthorCreate(AuthorBase):
    ...


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True
