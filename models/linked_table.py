from sqlalchemy import Table, Column, ForeignKey
from .base import Base


mentors_courses_link = Table(
    "mentors_courses_link",
    Base.metadata,
    Column("mentor_id", ForeignKey("mentors.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True)
)
