from app.models.mentors import MentorsCreate, Mentors
from sqlalchemy.orm import Session
from sqlalchemy import select


def get_mentors(db: Session, skip: int = 0, limit: int = 100):
    statement = select(Mentors).offset(skip).limit(limit)
    result = db.scalars(statement).all()
    return result


def add_mentor(db: Session, mentor: MentorsCreate):
    new_mentor = Mentors(**mentor.model_dump())
    db.add(new_mentor)
    db.commit()
    db.refresh(new_mentor)
    return new_mentor
