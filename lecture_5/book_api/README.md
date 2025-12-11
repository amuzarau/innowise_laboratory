📘 Simple Book Collection API — FastAPI Project

This project implements a minimal but fully functional RESTful API using:

FastAPI

SQLAlchemy ORM

Pydantic v2

SQLite

Ruff (linting / formatting)

The API allows a user to create, view, update, delete, and search books in a local database.

🚀 Features

Add a new book

Get a paginated list of books

Update book information

Delete a book

Search by title, author, or year

Automatic input validation with Pydantic v2

SQLAlchemy ORM integration

Easy API testing via Swagger UI

Clean, typed, well-documented code

📂 Project Structure
book_api/
│── main.py             # FastAPI application & endpoints
│── database.py         # DB engine & session management
│── models.py           # SQLAlchemy ORM model
│── schemas.py          # Pydantic request/response schemas
│── requirements.txt    # Project dependencies
│── ruff.toml           # Ruff linter configuration
│── __init__.py         # Makes folder a Python package


🔥 Note:
Files such as venv/, __pycache__/, .vscode/, and books.db are intentionally excluded.

🛠 Installation
1️⃣ Clone the repository
git clone https://github.com/<your-username>/innowise_lab.git
cd innowise_lab/lecture_5/book_api

2️⃣ Create a virtual environment
python -m venv venv


Activate it:

Windows (PowerShell)
venv\Scripts\Activate

Linux/Mac
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run the Application

Start the FastAPI server:

uvicorn main:app --reload


Your API will be available at:

👉 http://127.0.0.1:8000

Swagger UI (interactive API docs):

👉 http://127.0.0.1:8000/docs

Redoc documentation:

👉 http://127.0.0.1:8000/redoc

📘 API Endpoints
➕ Create a book
POST /books/


Request body:

{
  "title": "Think and Grow Rich",
  "author": "Napoleon Hill",
  "year": 1937
}

📚 Get list of books (with pagination)
GET /books/?skip=0&limit=10


skip → how many records to skip

limit → how many records to return

🔍 Search books
GET /books/search/?title=king&author=martin&year=1990


All fields are optional.

✏️ Update a book
PUT /books/{book_id}

❌ Delete a book
DELETE /books/{book_id}


Returns 204 No Content on success.

🧪 Testing the API

Swagger UI allows full testing of:

POST

GET

PUT

DELETE

Search

Pagination

Automatic validation errors

No external tools (Postman, curl) are required.

🧹 Code Quality — Ruff Linter

Ruff config (ruff.toml) ensures:

clean imports

standard PEP8 styling

modern Python syntax

safe bug-prevention rules

consistent formatting

To run linting manually:

ruff check .


Auto-fix:

ruff check . --fix

💾 Database

SQLite database file books.db is created automatically when the app runs.

It is not included in the repo.

New clean DB is generated on every fresh run.
