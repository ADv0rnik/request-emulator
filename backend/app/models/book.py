from sqlalchemy import Column, Integer, Float, ForeignKey, Text, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.mixin import Timestamp


class Book(Timestamp, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    amount = Column(Integer, nullable=False)
    price = Column(Float, nullable=False, default=1.00)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)

    order = relationship("OrderBook", back_populates="book")
    author = relationship("Author", back_populates="book_author")