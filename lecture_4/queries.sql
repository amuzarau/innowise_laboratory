-- SCHEMA FOR school.db
-- ========================================== 
-- Create table 1: students
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL UNIQUE, 
    birth_year INTEGER CHECK(birth_year BETWEEN 1990 AND 2020)
    );

-- Create table 2: grades
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    student_id INTEGER, 
    subject TEXT, 
    grade INTEGER CHECK(grade BETWEEN 1 AND 100), 
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Create indexes to optimize queries on student names and grades.

-- Index for fast lookup by name
CREATE INDEX idx_students_name ON students(full_name);

-- Index to speed up filtering and joins on student_id
CREATE INDEX idx_grades_student ON grades(student_id);

-- Index to accelerate subject-based aggregations
CREATE INDEX idx_grades_subject ON grades(subject);

-- ========================================== 


-- 2.Insert data 
-- Insert sample data into students table, with error-proof inserts
INSERT OR IGNORE INTO students (full_name, birth_year) VALUES 
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

-- Insert sample data into grades table
INSERT INTO grades (student_id, subject, grade) VALUES 
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);

--3. Find all grades for a specific student (Alice Johnson)
SELECT subjects.subject, subjects.grade
FROM grades AS subjects
JOIN students ON subjects.student_id  = students.id
WHERE students.full_name = 'Alice Johnson';

/*
--4. Calculate the average grade per student
SELECT students.full_name, 
ROUND(AVG(grades.grade), 2) AS average_grade
FROM students
JOIN grades on students.id = grades.student_id
GROUP BY students.id;
*/
-- 4. Calculate the average grade per student (with CTE) 
WITH grade_avg AS (
    SELECT student_id, AVG(grade) AS avg_grade
    FROM grades
    GROUP BY student_id
)
SELECT s.full_name, ROUND(a.avg_grade, 2) AS average_grade
FROM students s
JOIN grade_avg a ON s.id = a.student_id;

--5. List all students born after 2004.
SELECT * FROM students
WHERE birth_year > 2004;

--6. Create a query that lists all subjects and their average grades.
SELECT subject, 
    AVG(grade) AS avg_grade
FROM grades
GROUP BY subject;

--7. Find the top 3 students with the highest average grades, with window function.
SELECT full_name, avg_grade
FROM (
    SELECT
        s.full_name,
        AVG(g.grade) AS avg_grade,
        RANK() OVER (ORDER BY AVG(g.grade) DESC) AS rank_position
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
)
WHERE rank_position <= 3;


/*
-- Simple solution for 7. Find the top 3 students with the highest average grades.
SELECT students.full_name,
    AVG(grades.grade) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id
ORDER BY avg_grade DESC
LIMIT 3;
*/


--8. Show all students who scored below 80 in any subject.
SELECT DISTINCT students.full_name
FROM students
JOIN grades ON students.id = grades.student_id
WHERE grades.grade < 80;

