from typing import Optional, List

from pydantic import BaseModel
from .relation_schemas import RelationUser

# Shared properties
class DepartmentBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class DepartmentCreate(DepartmentBase):
    name: str


# Properties to receive on item update
class DepartmentUpdate(DepartmentBase):
    pass


# Properties shared by models stored in DB
class DepartmentInDBBase(DepartmentBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Department(DepartmentInDBBase):
    users: Optional[List[RelationUser]] = None


# Properties properties stored in DB
class DepartmentInDB(DepartmentInDBBase):
    pass
