from pydantic import BaseModel

from datetime import datetime


class BaseContact(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str


class CreateContact(BaseContact):
    pass


class UpdateContact(BaseContact):
    updated_at: datetime


class Contact(BaseContact):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
