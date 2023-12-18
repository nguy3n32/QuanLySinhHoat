from typing import List, Annotated
from fastapi import APIRouter, Query

from ..depends import SessionDep
from app.crud import mentors_crud
from app.models.mentors import MentorsCreate, MentorsRead, MentorsUpdate
from app.models.linked_schemas import MentorsWithCourses
from ..response import response

mentors_router = APIRouter()


@mentors_router.get("/", response_model=List[MentorsWithCourses],
                    responses=response[404])
async def get_mentors(session: SessionDep):
    return mentors_crud.get_mentors(db=session)


@mentors_router.post("/add_mentor", response_model=MentorsRead)
async def add_mentor(session: SessionDep, mentor: MentorsCreate):
    return mentors_crud.add_mentor(db=session, mentor=mentor)


@mentors_router.patch("/update_mentor", response_model=MentorsRead,
                      responses={**response[404], **response[500]})
async def update_mentor(session: SessionDep, mentor: MentorsUpdate, mentor_id: Annotated[int, Query()]):
    return mentors_crud.update_mentor(db=session, mentor_in=mentor, mentor_id=mentor_id)
