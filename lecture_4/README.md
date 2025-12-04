📘 Student Grades Manager — SQL Project

A lightweight relational database project built with SQLite, designed to store student information and their grades.
The goal is to demonstrate:

Table design

Data insertion

Relational joins

Aggregations

Filtering & sorting

Simple SQL analysis

This project contains:

school.db — SQLite database file

queries.sql — full SQL script (schema + inserts + queries)

create_db.py — minimal Python file used only to initialize an empty SQLite database file

🛠️ 1. Database Initialization

The database file school.db was created using a minimal Python script:

import sqlite3

conn = sqlite3.connect("school.db")
conn.close()


This script simply creates an empty SQLite file.
All the real work (schema definitions, inserts, queries) happens inside queries.sql.

✔ No ORMs
✔ No frameworks
✔ Pure SQL used for database structure and data manipulation

📂 2. Database Schema

The database contains two tables:

students
Column	Type	Description
id	INTEGER PK	Unique ID of student
full_name	TEXT	Student full name
birth_year	INTEGER	Year of birth
grades
Column	Type	Description
id	INTEGER PK	Unique grade record
student_id	INTEGER FK	References students.id
subject	TEXT	Subject name
grade	INTEGER	Grade (1–100)

🗂️ 3. Mermaid ER Diagram

erDiagram
    STUDENTS {
        INTEGER id PK "Primary key"
        TEXT full_name "Full name"
        INTEGER birth_year "Year of birth"
    }

    GRADES {
        INTEGER id PK "Primary key"
        INTEGER student_id FK "References students.id"
        TEXT subject "Subject name"
        INTEGER grade "1–100"
    }

    STUDENTS ||--o{ GRADES : "has many"


🧩 4. Sample Data

queries.sql inserts:

9 students

27 grade entries (3 per student)

This allows all analytical queries to return meaningful results.

Example (from queries.sql):

INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
...

INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
...

🔍 5. Analytical Queries (from queries.sql)
✔ Find all grades for Alice Johnson
SELECT g.subject, g.grade
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.full_name = 'Alice Johnson';

✔ Average grade per student
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id;

✔ Students born after 2004
SELECT * FROM students WHERE birth_year > 2004;

✔ Average grade per subject
SELECT subject, ROUND(AVG(grade), 2) AS avg_grade
FROM grades
GROUP BY subject;

✔ Top 3 students by average grade
SELECT s.full_name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 3;

✔ Students who scored below 80
SELECT DISTINCT s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80;

⚡ 6. Optional Indexes

Added in queries.sql to improve performance:

CREATE INDEX idx_students_name ON students(full_name);
CREATE INDEX idx_grades_student ON grades(student_id);
CREATE INDEX idx_grades_subject ON grades(subject);
