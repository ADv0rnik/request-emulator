from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .role import Role
from .mixin import Timestamp


class User(Timestamp, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean, nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False, default=2)

    role = relationship("Role", back_populates="user")
    order = relationship("Order", back_populates="user_order")