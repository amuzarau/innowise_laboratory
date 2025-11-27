# Student Grade Analyzer

A clean and fully type-annotated Python console application for managing student academic records.  
The program allows users to:

- Add new students  
- Record grades for existing students  
- Display an organized performance report  
- Identify the top-performing student  
- Exit through a menu-driven interface  

This project demonstrates best practices in Python such as:
- Type hinting (`TypedDict`, `List`, `Optional`)
- User input validation
- Error handling (`try/except`)
- Functional decomposition
- Pattern matching (`match/case`)
- Clean, modular design

---

##  Menu 

### ✔ Option 1: Add a new student  
Create a new student record while preventing duplicates.

### ✔ Option 2: Add a grade for a student  
Enter multiple grades (0–100), with validation and safe handling of incorrect input.

Includes a **required `try/except ValueError`** block for rejecting non-numeric input gracefully.

### ✔ Option 3: Show report (all students)  
Displays each student’s average grade and overall class statistics:  
- Highest average  
- Lowest average  
- Overall class average  

Includes a **required `try/except ZeroDivisionError`** block for handling missing grades.

### ✔ Option 4: Find top performerOption 5: Exit
Automatically determines which student has the highest average grade using:
```python
max(..., key=lambda item: item[1])

### ✔ Option 5: Exit
Breaks the infinite loop to end the program.

