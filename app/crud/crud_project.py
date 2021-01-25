from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.crud import user
from app.models import Project
from app.schemas.project_schemas import ProjectCreate, ProjectUpdate


class CRUDProject(CRUDBase[Project, ProjectCreate, ProjectUpdate]):
    def get_by_id(self, db: Session, *, id: int) -> Optional[Project]:
        return db.query(Project).filter_by(id=id).first()

    def create(self, db: Session, *, obj_in: ProjectCreate) -> Project:
        db_obj = Project()
        db_obj.name = obj_in.name
        db_obj.description = obj_in.description
        db_obj.status = obj_in.status
        db.add(db_obj)

        user_list = obj_in.user_list
        users = user.get_all_users(db, list_id=user_list)
        print(users)
        if users:
            db_obj.users = users
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self,
            db: Session,
            *,
            db_obj: Project,
            obj_in: Union[ProjectUpdate, Dict[str, Any]]
    ) -> Project:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data['user_list']:
            del update_data['user_list']
        return super().update(db, db_obj=db_obj, obj_in=update_data)


project = CRUDProject(Project)
