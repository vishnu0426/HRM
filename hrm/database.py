"""Database utilities using SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

engine = create_engine(settings.database_url, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    """Yield a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
