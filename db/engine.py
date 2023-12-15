from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models import Base


engine = create_engine(settings.DATABASE_URI, echo=True)


def create_all():
    Base.metadata.create_all(engine)


def create_table_id(code: str):
    with engine.connect() as conn:
        next_val_query = text("SELECT nextval('user_id_seq'::regclass)")
        result = conn.execute(next_val_query)

        next_val_value = result.scalar()

        return code + "{0:04d}".format(next_val_value)


def get_session():
    with Session(engine) as session:
        yield session
