from fastapi import APIRouter
from .parents_router import parents_router
from .students_router import students_router


api_router = APIRouter()
api_router.include_router(parents_router, prefix="/parents", tags=["parents"])
api_router.include_router(students_router, prefix="/students", tags=["students"])
