from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.config.config import get_settings


engine = create_engine(get_settings().DATABASE_URI, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autoflush=True, autocommit=False)

Base = declarative_base()


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
