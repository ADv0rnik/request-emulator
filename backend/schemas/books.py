from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    description: str
    rating: int
    author_id: int


class BookCreate(BookBase):
    ...


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
