from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel
from .relation_schemas import RelationUser


# Shared properties
class ProjectBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    user_list:Optional[List[int]]=None


# Properties to receive via API on creation
class ProjectCreate(ProjectBase):
    name: str


# Properties to receive via API on update
class ProjectUpdate(ProjectBase):
    pass


class ProjectInDBBase(ProjectBase):
    id: Optional[int] = None
    create_date: Optional[datetime] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Project(ProjectInDBBase):
    users: Optional[List[RelationUser]] = None


# Additional properties stored in DB
class ProjectInDB(ProjectInDBBase):
    pass

