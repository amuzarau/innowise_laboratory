# 📘 Student Grade Analyzer

A console-based Python application for managing student academic records.  
The program supports adding students, entering grades, generating reports, and identifying top performers — all through a clean, type-safe, menu-driven interface.

This project demonstrates:
- Type hints and `TypedDict`
- Input validation
- Error handling (`try/except`)
- Pattern matching (`match/case`)
- Functional program structure
- Professional Python coding practices

---

## 📋 Menu Options

| Option | Action | Description |
|--------|---------|-------------|
| **1. Add a new student** | Creates a new student record | Prevents duplicates, ensures valid names |
| **2. Add grades for a student** | Adds one or more grades | Validates input, prevents invalid grades |
| **3. Show report (all students)** | Displays averages + statistics | Includes `try/except ZeroDivisionError` handling |
| **4. Find top performer** | Finds the student with the highest average | Uses `max(..., key=lambda)` |
| **5. Exit program** | Closes application | Ends main loop gracefully |

---

## 🧠 Program Architecture (Mermaid Diagram)

```mermaid
flowchart TD

%% MAIN PROGRAM LOOP
A[Start Program] --> B[Initialize students: List[Student] = []]
B --> C[print_menu()]
C --> D[get_menu_choice()]

%% MENU DECISIONS
D -->|1| E[add_student()]
D -->|2| F[add_grades_for_student()]
D -->|3| G[show_report()]
D -->|4| H[find_top_performer()]
D -->|5| Z[Exit Program]
D -->|Other| C1[Invalid Option]

C1 --> C

%% ADD STUDENT
E --> E1[Input student name]
E1 --> E2{Name empty?}
E2 -->|Yes| E3[Print 'Name cannot be empty'] --> C
E2 -->|No| E4[Check duplicate via find_student()]
E4 -->|Exists| E5[Print 'Student already exists'] --> C
E4 -->|New| E6[Create Student dict]
E6 --> E7[Append to students list]
E7 --> C

%% ADD GRADES
F --> F1[Input student name]
F1 --> F2[student = find_student()]
F2 -->|Not found| F3[Print 'Student not found'] --> C
F2 -->|Found| F4[Input grades loop]

F4 --> F5{Input == 'done'?}
F5 -->|Yes| C
F5 -->|No| F6{Is numeric?}

F6 -->|No| F7[Print 'Invalid number'] --> F4
F6 -->|Yes| F8{0 <= grade <= 100?}

F8 -->|No| F9[Print 'Grade must be between 0 and 100'] --> F4
F8 -->|Yes| F10[Append grade] --> F4

%% SHOW REPORT
G --> G1{students empty?}
G1 -->|Yes| G2[Print 'No students added'] --> C
G1 -->|No| G3[Loop over students]

G3 --> G4{Grades empty?}
G4 -->|Yes| G5[Print 'N/A' (ZeroDivisionError handled)] --> G3
G4 -->|No| G6[Compute avg = sum/len] --> G3

G6 --> G7[Collect averages]
G7 --> G8[Print Max, Min, Overall Avg]
G8 --> C

%% FIND TOP PERFORMER
H --> H1{students empty?}
H1 -->|Yes| H2[Print 'No students added'] --> C
H1 -->|No| H3[Build (student, avg) list]
H3 --> H4{Any averages?}
H4 -->|No| H5[Print 'No top performer yet'] --> C
H4 -->|Yes| H6[Find max(..., key=lambda)]
H6 --> H7[Print top performer]
H7 --> C

%% EXIT
Z --> Z1[End Program]
