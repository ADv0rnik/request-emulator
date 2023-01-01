from mixins import Timestamp

from sqlalchemy import Column, Integer, String
from ..db.db_setup import Base


class Contact(Timestamp, Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    phone_number = Column(String, index=True, unique=True)
