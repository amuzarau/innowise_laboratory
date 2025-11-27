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

A[Start Program] --> B[Initialize students list]
B --> C[print_menu()]
C --> D[get_menu_choice()]

D -->|1| E[add_student()]
D -->|2| F[add_grades_for_student()]
D -->|3| G[show_report()]
D -->|4| H[find_top_performer()]
D -->|5| Z[Exit Program]
D -->|Other| C1[Invalid option -> Return to menu]

C1 --> C

E --> E1[Ask for student name]
E1 --> E2{Name empty?}
E2 -->|Yes| E3[Print error] --> C
E2 -->|No| E4[Check duplicate]
E4 -->|Exists| E5[Print exists] --> C
E4 -->|New| E6[Create student]
E6 --> E7[Append to list]
E7 --> C

F --> F1[Ask for student name]
F1 --> F2[Find student]
F2 -->|Not found| F3[Print error] --> C
F2 -->|Found| F4[Grade input loop]

F4 --> F5{Input == 'done'?}
F5 -->|Yes| C
F5 -->|No| F6{Is numeric?}
F6 -->|No| F7[Invalid] --> F4
F6 -->|Yes| F8{0-100?}
F8 -->|No| F9[Out of range] --> F4
F8 -->|Yes| F10[Append grade] --> F4

G --> G1{students empty?}
G1 -->|Yes| G2[Print 'No students'] --> C
G1 -->|No| G3[Loop students]
G3 --> G4{Grades empty?}
G4 -->|Yes| G5[N/A] --> G3
G4 -->|No| G6[Compute average] --> G3
G6 --> G7[Collect averages]
G7 --> G8[Print statistics]
G8 --> C

H --> H1{empty?}
H1 -->|Yes| H2[Print 'No students'] --> C
H1 -->|No| H3[Compute averages list]
H3 --> H4{Any?}
H4 -->|No| H5[Print no data] --> C
H4 -->|Yes| H6[Find top performer]
H6 --> H7[Print result]
H7 --> C

Z --> Z1[End Program]

