"""
Main FastAPI application with type hints.
"""

from typing import Generator, List
from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
from models import Book
from schemas import BookCreate, BookUpdate, BookOut

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Book Collection API")


# -----------------------------
# Database session dependency
# -----------------------------
def get_db() -> Generator[Session, None, None]:
    """
    Provides a database session for dependency injection.
    Ensures the session is closed after request.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# POST /books/  (Create)
# -----------------------------
@app.post("/books/", response_model=BookOut)
def create_book(book: BookCreate, db: Session = Depends(get_db)) -> BookOut:
    """
    Create a new book in the database.
    """
    db_book: Book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# -----------------------------
# GET /books/ (List + Pagination)
# -----------------------------
@app.get("/books/", response_model=list[BookOut])
def read_books(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
) -> List[BookOut]:
    """
    Retrieve a paginated list of books.
    """
    books: List[Book] = db.query(Book).offset(skip).limit(limit).all()
    return books


# -----------------------------
# DELETE /books/{book_id}
# -----------------------------
@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)) -> Response:
    """
    Delete a book by ID.
    """

    book: Book | None = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return Response(status_code=204)


# -----------------------------
# PUT /books/{book_id} (Update)
# -----------------------------
@app.put("/books/{book_id}", response_model=BookOut)
def update_book(
    book_id: int, payload: BookUpdate, db: Session = Depends(get_db)
) -> BookOut:
    """
    Update an existing book's details.
    """
    book: Book | None = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    for key, value in payload.model_dump().items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book


# -----------------------------
# GET /books/search/
# -----------------------------
@app.get("/books/search/", response_model=list[BookOut])
def search_books(
    title: str | None = None,
    author: str | None = None,
    year: int | None = None,
    db: Session = Depends(get_db),
) -> List[BookOut]:
    """
    Search books by optional filters: title, author, year.
    """
    query = db.query(Book)

    if title is not None:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author is not None:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    if year is not None:
        query = query.filter(Book.year == year)

    results: List[Book] = query.all()
    return results
