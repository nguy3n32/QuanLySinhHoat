from typing import List
from fastapi import APIRouter

from ..depends import SessionDep
from app.crud import mentors_crud
from app.models.mentors import MentorsCreate, MentorsRead

mentors_router = APIRouter()


@mentors_router.get("/", response_model=List[MentorsRead])
async def get_mentors(session: SessionDep):
    return mentors_crud.get_mentors(db=session)


@mentors_router.post("/add_mentor", response_model=MentorsRead)
async def add_mentor(session: SessionDep, mentor: MentorsCreate):
    return mentors_crud.add_mentor(db=session, mentor=mentor)
