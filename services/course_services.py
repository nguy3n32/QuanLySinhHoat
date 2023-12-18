from typing import List

from sqlalchemy.orm import Session

from app.crud import mentors_crud
from app.models import courses
from app.models.courses import Courses


def add_mentors_to_course(db: Session, course: Courses, mentors: List[int]):
    list_of_mentors = []
    for mentor_id in mentors:
        mentor_data = mentors_crud.get_mentor_by_id(db, mentor_id)
        list_of_mentors.append(mentor_data)
    course.mentors = list_of_mentors
    return course
