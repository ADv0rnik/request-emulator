from pydantic import BaseModel


class OrderBookBaseModel(BaseModel):
    amount: int
    order_id: int
    book_id: int


class OrderBookCreateModel(OrderBookBaseModel):
    pass


class OrderBookUpdateModel(OrderBookBaseModel):
    pass


class OrderBookModel(OrderBookBaseModel):
    id: int

    class Config:
        orm_mode = True
