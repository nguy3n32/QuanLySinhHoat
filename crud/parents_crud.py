from app.models.parents import ParentsCreate, Parents
from app.api.response import InternalError, Not_Found_Exception

from sqlalchemy.orm import Session
from sqlalchemy import select, exc


def add_parent(parent: ParentsCreate, db: Session):
    new_parent = Parents(
        full_name=parent.full_name,
        address=parent.address,
        email=parent.email
    )
    try:
        db.add(new_parent)
        db.commit()
        db.refresh(new_parent)
        return new_parent
    except exc.SQLAlchemyError:
        raise InternalError


def get_all_parents(db: Session, skip: int = 0, limit: int = 100):
    try:
        statement = select(Parents).offset(skip).limit(limit)
        result = db.scalars(statement).all()
        return result
    except exc.SQLAlchemyError:
        raise InternalError


def get_parent_by_id(db: Session, parent_id: int):
    parent = db.get(Parents, parent_id)
    if not parent:
        raise Not_Found_Exception
    return parent
