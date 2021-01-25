from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models import Department
from app.schemas.department_schemas import DepartmentCreate, DepartmentUpdate


class CRUDDepartment(CRUDBase[Department,DepartmentCreate,DepartmentUpdate]):
    def get_by_id(self,db:Session,*,id:int)->Optional[Department]:
        return db.query(Department).filter_by(id=id).first()

    def create(self, db: Session, *, obj_in: DepartmentCreate) -> Department:
        return super().create(db,obj_in=obj_in)

    def update(
        self,
        db: Session,
        *,
        db_obj: Department,
        obj_in: Union[DepartmentUpdate, Dict[str, Any]]
    ) -> Department:
        if isinstance(obj_in,dict):
            update_data=obj_in
        else:
            update_data=obj_in.dict(exclude_unset=True)
        return super().update(db,db_obj=db_obj,obj_in=update_data)


department=CRUDDepartment(Department)
