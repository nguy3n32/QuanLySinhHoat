from app.models.mentors import MentorsCreate, Mentors, MentorsUpdate
from app.api.response import not_found_response, Not_Found_Exception

from sqlalchemy.orm import Session
from sqlalchemy import select


def get_mentors(db: Session, skip: int = 0, limit: int = 100):
    statement = select(Mentors).offset(skip).limit(limit)
    result = db.scalars(statement).all()
    if not result:
        raise Not_Found_Exception
    return result


def add_mentor(db: Session, mentor: MentorsCreate):
    new_mentor = Mentors(**mentor.model_dump())
    db.add(new_mentor)
    db.commit()
    db.refresh(new_mentor)
    return new_mentor


def get_mentor_by_id(db: Session, mentor_id: int):
    mentor = db.get(Mentors, mentor_id)
    if not mentor:
        raise Not_Found_Exception
    return mentor


def update_mentor(db: Session, mentor_in: MentorsUpdate, mentor_id: int):
    mentor = get_mentor_by_id(db, mentor_id)
    mentor_data = mentor_in.model_dump(exclude_unset=True)
    for key, value in mentor_data.items():
        setattr(mentor, key, value)
    db.add(mentor)
    db.commit()
    db.refresh(mentor)
    return mentor
