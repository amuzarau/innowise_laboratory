"""
Database configuration module with type annotations.
"""

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL: str = "sqlite:///./books.db"

# SQLAlchemy engine used to communicate with SQLite database.
engine: Engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Session factory used to create database sessions.
SessionLocal: sessionmaker[Session] = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base class for ORM models.
Base = declarative_base()
