import os
import secrets

from pydantic import BaseSettings
from pydantic.types import Optional


class Settings(BaseSettings):
    PROJECT_NAME: str = f"SQLModel API - {os.getenv('ENV', 'development').capitalize()}"
    DESCRIPTION: str = "A FastAPI + SQLModel production-ready API"
    ENV: str = os.getenv('ENV', 'development')
    VERSION: str = "1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # DATABASE_URI: Optional[PostgresDsn] = None
    DATABASE_URI: str = "postgresql://postgres:postgres@db:5432/blog"  # sqlite tmp db just for test


settings = Settings()