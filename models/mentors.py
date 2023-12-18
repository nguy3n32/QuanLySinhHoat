from datetime import date
from typing import Optional, List
from sqlalchemy import String, Date
from sqlalchemy.orm import mapped_column, Mapped, relationship
from pydantic import BaseModel, Field

from .base import Base
from .linked_table import mentors_courses_link


class Mentors(Base):
    __tablename__ = "mentors"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    gender: Mapped[str] = mapped_column(String(1))
    birthday: Mapped[date] = mapped_column(Date, nullable=False)
    address: Mapped[Optional[str]] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(10))

    courses: Mapped[List["Courses"]] = relationship(secondary=mentors_courses_link, back_populates="mentors")


class MentorsBase(BaseModel):
    full_name: str = Field(max_length=100)
    gender: str = Field(max_length=1)
    birthday: date
    address: Optional[str] = Field(default="Da nang")
    phone: str

    class Config:
        from_attributes = True


class MentorsCreate(MentorsBase):
    pass


class MentorsRead(MentorsBase):
    id: int
    address: str


class MentorsUpdate(BaseModel):
    full_name: Optional[str] = Field(default=None)
    gender: Optional[str] = Field(default=None)
    birthday: Optional[date] = Field(default=None)
    address: Optional[str] = Field(default=None)
    phone: Optional[str] = Field(default=None)
