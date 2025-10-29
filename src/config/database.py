from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.config.config import get_settings


engine = create_engine(get_settings().DATABASE_URI, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False)


class Base(DeclarativeBase):
    pass


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
