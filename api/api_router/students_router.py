from typing import List

from fastapi import APIRouter
from app.models.students import StudentCreate, StudentRead
from app.models.linked_schemas import StudentWithParent
from app.api.depends import SessionDep
from app.crud import students_crud as std

students_router = APIRouter()


@students_router.get("/", response_model=StudentWithParent)
async def get_students(session: SessionDep):
    students = std.get_students(db=session)
    print(type(students))
    return students


@students_router.post("/add-student", response_model=StudentRead)
async def add_new_student(new_student: StudentCreate, session: SessionDep):
    return std.add_student(session, new_student)
