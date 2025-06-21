"""Configuration management for HRM."""

import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Base settings for the application."""

    database_url: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/hrm")


settings = Settings()
