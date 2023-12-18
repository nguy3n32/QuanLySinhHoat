from typing import Optional, List, Set

from .linked_table import mentors_courses_link
from .base import Base

from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from pydantic import BaseModel, Field


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

    mentors: Mapped[List["Mentors"]] = relationship(secondary=mentors_courses_link, back_populates="courses")


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
    mentors_id: Optional[Set[int]] = Field(default=None)


class CoursesRead(CoursesBase):
    id: int
    room_number: int


class CoursesUpdate(BaseModel):
    course_name: Optional[str] = Field(default=None)
    num_of_sessions: Optional[int] = Field(default=None)
    course_fee: Optional[int] = Field(default=None)
    start_date: Optional[date] = Field(default=None)
    end_date: Optional[date] = Field(default=None)
    max_students: Optional[int] = Field(default=None)
    room_number: Optional[int] = Field(default=None)
    mentors_id: Optional[List[int]] = Field(default=None)
