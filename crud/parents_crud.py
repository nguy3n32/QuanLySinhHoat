from app.models.parents import ParentsCreate, Parents
from sqlalchemy.orm import Session


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
