from pydantic import BaseModel, Field
from .author import AuthorModel


class BookBaseModel(BaseModel):
    title: str
    description: str
    amount: int
    price: float
    author_id: int


class BookCreateModel(BookBaseModel):
    pass


class BookUpdateModel(BookBaseModel):
    pass


class BookOutModel(BookBaseModel):
    id: int
    title: str = Field(alias='book_title')
    description: str = Field(alias='book_description', title='Book description')
    price: float = Field(..., exclude=True, alias='book_price')
    author_id: int = Field(..., exclude=True, alias='book_author_id')
    amount: int = Field(..., exclude=True)
    author: AuthorModel = Field(alias='book_author')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class BookModel(BookBaseModel):
    id: int
    author_id: int = Field(..., exclude=True)
    author: AuthorModel

    class Config:
        orm_mode = True

