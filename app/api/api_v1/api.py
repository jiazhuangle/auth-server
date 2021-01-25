from fastapi import APIRouter

from app.api.api_v1.endpoints import  login, users,departments,projects

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(departments.router, prefix="/departments", tags=["departments"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])

