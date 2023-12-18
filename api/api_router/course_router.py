from typing import List
from fastapi import APIRouter

from ..depends import SessionDep
from app.crud import courses_crud
from app.models.courses import CoursesRead, CoursesCreate

course_router = APIRouter()


@course_router.get("/", response_model=List[CoursesRead])
async def get_all_courses(session: SessionDep):
    return courses_crud.get_courses(db=session)


@course_router.post("/add-course", response_model=CoursesRead)
async def add_course(session: SessionDep, course: CoursesCreate):
    return courses_crud.add_course(db=session, course=course)
