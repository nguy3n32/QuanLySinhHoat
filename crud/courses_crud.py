from app.models.courses import CoursesCreate, Courses, CoursesUpdate
from app.services.course_services import add_mentors_to_course
from app.api.response import Not_Found_Exception

from sqlalchemy.orm import Session
from sqlalchemy import select


def add_course(db: Session, course: CoursesCreate):
    new_course = Courses(
        course_name=course.course_name,
        room_number=course.room_number,
        num_of_sessions=course.num_of_sessions,
        course_fee=course.course_fee,
        start_date=course.start_date,
        end_date=course.end_date,
        max_students=course.max_students,
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


def get_courses(db: Session, offset: int = 0, limit: int = 100):
    statement = select(Courses).offset(offset).limit(limit)
    result = db.scalars(statement).all()
    if not result:
        raise Not_Found_Exception
    return result


def get_course_by_id(db: Session, course_id: int):
    course = db.get(Courses, course_id)
    if not course:
        raise Not_Found_Exception
    return course


def update_course(db: Session, course_in: CoursesUpdate, course_id: int):
    course = get_course_by_id(db, course_id)
    course_data = course_in.model_dump(exclude_unset=True)
    if "mentors_id" in course_data:
        add_mentors_to_course(db, course, course_data["mentors_id"])
        course_data.pop("mentors_id")
    for key, value in course_data.items():
        setattr(course, key, value)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course
