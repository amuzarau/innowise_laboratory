"""
Pydantic schemas with full type hints and v2-compatible validators.
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional


class BookBase(BaseModel):
    """
    Shared schema for book creation and update operations.
    """

    title: str = Field(..., min_length=2, max_length=100)
    author: str = Field(..., min_length=2, max_length=100)
    year: Optional[int] = Field(
        None,
        ge=0,
        le=2026,
        description="Publication year must be between 0 and 2026.",
    )

    # Validation: Trim strings and ensure non-empty
    @field_validator("title", "author")
    def trim_strings(cls, value: str) -> str:
        """Remove whitespace and ensure the field is not empty."""
        value = value.strip()
        if not value:
            raise ValueError("Field cannot be empty or only whitespace.")
        return value

    # Validation: Check for year with error text
    @field_validator("year")
    def validate_year(cls, value: Optional[int]) -> Optional[int]:
        """Ensure year is within allowed range."""
        if value is None:
            return None
        if not (0 <= value <= 2026):
            raise ValueError("Publication year must be between 0 and 2026.")
        return value


class BookCreate(BookBase):
    """Schema for creating a new book."""

    pass


class BookUpdate(BookBase):
    """Schema for updating a book."""

    pass


class BookOut(BookBase):
    """Schema for returning book data to client."""

    id: int

    model_config = {"from_attributes": True}
