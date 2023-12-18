from sqlalchemy.orm import DeclarativeBase
from enum import Enum


class Base(DeclarativeBase):
    pass


class Gender(Enum):
    MALE = 0
    FEMALE = 1
    OTHER = 2
