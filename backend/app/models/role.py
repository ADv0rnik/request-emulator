from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .mixin import Timestamp


class Role(Timestamp, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False, default='user')

    user = relationship("User", back_populates='role', uselist=False)
