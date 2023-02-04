from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    description: str
    rating: int
    author_id: int


class BookCreate(BookBase):
    ...


class BookUpdate(BookBase):
    title: Optional[str] = None
    description: Optional[str] = None
    rating: Optional[int] = None
    author_id: Optional[str] = None


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
