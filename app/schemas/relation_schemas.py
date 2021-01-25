from typing import Optional, List
from pydantic import BaseModel, EmailStr
from datetime import datetime


class RelationUser(BaseModel):
    id: Optional[int] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    department_id: Optional[int] = None

    class Config:
        orm_mode = True


class RelationProject(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    create_date: Optional[datetime] = None

    class Config:
        orm_mode = True
