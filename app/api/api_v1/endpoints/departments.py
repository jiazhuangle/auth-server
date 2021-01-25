from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/", response_model=List[schemas.Department])
def read_departments(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve DEPARTMENTS.
    """
    if current_user.is_superuser:
        departments = crud.department.get_multi(db, skip=skip, limit=limit)
        return departments
    else:
        raise HTTPException(
            status_code=400,
            detail="The user doesn't have enough privileges.",
        )


@router.post('/', response_model=schemas.Department)
def create_department(
        *,
        db: Session = Depends(deps.get_db),
        department_in: schemas.DepartmentCreate,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    '''
    CREATE a department.
    '''
    if current_user.is_superuser:
        return crud.department.create(db, obj_in=department_in)
    else:
        raise HTTPException(
            status_code=400,
            detail="The user doesn't have enough privileges.",
        )


@router.get("/{department_id}", response_model=schemas.Department)
def read_department_by_id(
    department_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific department by id.
    """
    department = crud.department.get(db, id=department_id)
    return department


@router.put("/{department_id}", response_model=schemas.Department)
def update_department(
    *,
    db: Session = Depends(deps.get_db),
    department_id: int,
    department_in: schemas.DepartmentUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a user.
    """
    department = crud.department.get(db, id=department_id)
    if not department:
        raise HTTPException(
            status_code=404,
            detail="The department does not exist in the system",
        )
    user = crud.department.update(db, db_obj=department, obj_in=department_in)
    return user
