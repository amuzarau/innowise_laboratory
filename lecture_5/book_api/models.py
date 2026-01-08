"""
SQLAlchemy ORM models with type annotations.
"""

from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):
    """
    ORM model representing a Book record in the database.
    """

    __tablename__: str = "books"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, nullable=False)
    author: str = Column(String, nullable=False)
    year: int = Column(Integer, nullable=True)
