from typing import Optional

from .base import Base

from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from pydantic import BaseModel


class Courses(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    course_name: Mapped[str] = mapped_column(String(20), index=True)
    room_number: Mapped[int]
    num_of_sessions: Mapped[int] = mapped_column(Integer)
    course_fee: Mapped[int] = mapped_column(Integer)
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[date] = mapped_column(Date)
    max_students: Mapped[int] = mapped_column(Integer)


class CoursesBase(BaseModel):
    course_name: str
    num_of_sessions: int
    course_fee: int
    start_date: date
    end_date: date
    max_students: int

    class Config:
        from_attributes = True


class CoursesCreate(CoursesBase):
    room_number: int


class CoursesRead(CoursesBase):
    id: int
    room_number: int


class CoursesUpdate(BaseModel):
    course_name: Optional[str]
    num_of_sessions: Optional[int]
    course_fee: Optional[int]
    start_date: Optional[date]
    end_date: Optional[date]
    max_students: Optional[int]
    room_number: Optional[int]

