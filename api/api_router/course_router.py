from typing import List
from fastapi import APIRouter

from ..depends import SessionDep
from app.crud import courses_crud
from app.models.courses import CoursesRead, CoursesCreate, CoursesUpdate
from app.models.linked_schemas import CoursesWithMentors
from app.api.response import response

course_router = APIRouter()


@course_router.get("/", response_model=List[CoursesWithMentors])
async def get_all_courses(session: SessionDep):
    return courses_crud.get_courses(db=session)


@course_router.post("/add-course", response_model=CoursesRead)
async def add_course(session: SessionDep, course: CoursesCreate):
    return courses_crud.add_course(db=session, course=course)


@course_router.patch("/update-course", response_model=CoursesWithMentors,
                     responses=response[404])
async def update_course(session: SessionDep, course_in: CoursesUpdate, course_id: int):
    return courses_crud.update_course(db=session, course_in=course_in, course_id=course_id)
