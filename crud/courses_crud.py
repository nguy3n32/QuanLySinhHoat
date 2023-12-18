from app.models.courses import CoursesCreate, Courses
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
    return result
