from pydantic_settings import BaseSettings
from typing import List
import secrets
import os
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"

    # TEST: str = Field(validation_alias="my_test", default="nguyen")

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PW: str = os.getenv("POSTGRES_PW")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")

    DATABASE_URI: str = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_HOST}:{POSTGRES_PORT}/"
        f"{POSTGRES_DB}")

    ORIGINS: List[str] = [
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost",
        "http://localhost:8080",
    ]


settings = Settings()
