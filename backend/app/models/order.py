from sqlalchemy import Column, Integer, Float, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from app.schemas.order import Status

from app.db.base_class import Base
from .mixin import Timestamp
from .book import Book
from .user import User


class Order(Timestamp, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    status = Column(Enum(Status), default="pending", nullable=False)
    description = Column(Text, nullable=True, default="")
    cost = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user_order = relationship("User", back_populates="order")
    books = relationship("OrderBook", back_populates="order")
