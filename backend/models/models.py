from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from mixin import Timestamp


Base = declarative_base()


class Book(Timestamp, Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    rating = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Authors")


class Author(Timestamp, Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)








