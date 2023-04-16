from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.mixin import Timestamp
from app.models.book import Book


class Author(Timestamp, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    book_author = relationship("Book", back_populates="author")