from sqlalchemy import Integer, String, Date, ForeignKey
from datetime import date
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pydantic import BaseModel


class Students(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(50), index=True)
    birth_date: Mapped[date] = mapped_column(Date)

    parent_id: Mapped[int] = mapped_column(ForeignKey("parents.id"))

    parent: Mapped["Parents"] = relationship(back_populates="children")


class StudentBase(BaseModel):
    full_name: str
    birth_date: date
    parent_id: int

    class Config:
        from_attributes = True


class StudentCreate(StudentBase):
    pass


class StudentRead(StudentBase):
    id: int


class StudentUpdate(StudentBase):
    pass
