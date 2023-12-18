from typing import Optional, List

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from pydantic import BaseModel, EmailStr

from .base import Base


class Parents(Base):
    __tablename__ = "parents"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100), index=True)
    address: Mapped[Optional[str]]
    email: Mapped[str] = mapped_column(String(100))

    children: Mapped[List["Students"]] = relationship(back_populates="parent")


class ParentsBase(BaseModel):
    full_name: str
    address: Optional[str]
    email: EmailStr

    class Config:
        from_attributes = True


class ParentsCreate(ParentsBase):
    pass


class ParentRead(ParentsBase):
    id: int
    address: str

    class Config:
        from_attributes = True
