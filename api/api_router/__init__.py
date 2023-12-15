from fastapi import APIRouter
from .parents_router import parents_router


api_router = APIRouter()
api_router.include_router(parents_router, prefix="/parents", tags=["parents"])
