from pydantic import BaseModel


class RoleBaseModel(BaseModel):
    name: str


class RoleCreateModel(RoleBaseModel):
    pass


class RoleUpdateModel(RoleBaseModel):
    pass


class RoleModel(RoleBaseModel):
    id: int

    class Config:
        orm_mode = True
