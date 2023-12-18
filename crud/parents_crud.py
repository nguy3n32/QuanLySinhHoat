from app.models.parents import ParentsCreate, Parents
from sqlalchemy.orm import Session
from sqlalchemy import select


def add_parent(parent: ParentsCreate, db: Session):
    new_parent = Parents(
        full_name=parent.full_name,
        address=parent.address,
        email=parent.email
    )
    db.add(new_parent)
    db.commit()
    db.refresh(new_parent)
    return new_parent


def get_all_parents(db: Session, skip: int = 0, limit: int = 100):
    statement = select(Parents).offset(skip).limit(limit)
    result = db.scalars(statement).all()
    return result
