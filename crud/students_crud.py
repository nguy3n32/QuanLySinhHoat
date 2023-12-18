from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.students import StudentCreate, Students


def add_student(db: Session, new_student: StudentCreate):
    new_student = Students(**new_student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.scalars(select(Students).offset(skip).limit(limit)).first()
