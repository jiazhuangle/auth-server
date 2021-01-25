from typing import Any, List,Union

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/", response_model= List[schemas.Project], response_model_exclude=["user_list"])
def read_projects(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve projects.
    """
    if current_user.is_superuser:
        projects = crud.project.get_multi(db, skip=skip, limit=limit)
        return projects
    else:
        raise HTTPException(
            status_code=400,
            detail="The user doesn't have enough privileges.",
        )


@router.post('/', response_model=schemas.Project)
def create_department(
        *,
        db: Session = Depends(deps.get_db),
        project_in: schemas.ProjectCreate,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    '''
    CREATE a project.
    '''
    if current_user.is_superuser:
        return crud.project.create(db, obj_in=project_in)
    else:
        raise HTTPException(
            status_code=400,
            detail="The user doesn't have enough privileges.",
        )


@router.put("/{project_id}", response_model=schemas.Project)
def update_project(
    project_id: int,
    project_in: schemas.ProjectUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    project = crud.project.get(db, id=project_id)

    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    project = crud.project.update(db,db_obj=project,obj_in=project_in)
    return project
