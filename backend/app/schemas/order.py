from typing import List, Optional
from .book import BookModel, BookOutModel

from pydantic import BaseModel, Field
import enum


class Status(str, enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"


class OrderBaseModel(BaseModel):
    description: Optional[str] = Field(default="New order")
    user_id: int


class OrderCreateModel(OrderBaseModel):
    ...


class OrderUpdateModel(OrderBaseModel):
    description: Optional[str] = Field(default="recent order")
    cost: Optional[float] = Field(..., exclude=True)


class OrderModel(OrderBaseModel):
    id: int
    status: Status
    cost: float
    books: List[BookOutModel]

    class Config:
        orm_mode = True
