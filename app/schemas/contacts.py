from pydantic import BaseModel

from datetime import datetime


class BaseContacts(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str


class Contacts(BaseContacts):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
