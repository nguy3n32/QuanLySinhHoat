from typing import Optional

from sqlalchemy import Column, String
from sqlalchemy.orm import mapped_column, Mapped
from pydantic import BaseModel, EmailStr

from .base import Base


class Parents(Base):
    __tablename__ = "parents"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100), index=True)
    address: Mapped[Optional[str]]
    email: Mapped[str] = mapped_column(String(100))


class ParentsBase(BaseModel):
    full_name: str
    address: Optional[str]
    email: EmailStr


class ParentsCreate(ParentsBase):
    pass


class ParentRead(ParentsBase):
    address: str
