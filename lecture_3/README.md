# 📘 Student Grade Analyzer

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

## 🚀 Features

### ✔ Add Students  
Create a new student record while preventing duplicates.

### ✔ Add Grades  
Enter multiple grades (0–100), with validation and safe handling of incorrect input.

### ✔ View Report  
Displays each student’s average grade and overall class statistics:  
- Highest average  
- Lowest average  
- Overall class average  

Includes a **required `try/except ZeroDivisionError`** block for handling missing grades.

### ✔ Find Top Performer  
Automatically determines which student has the highest average grade using:
```python
max(..., key=lambda item: item[1])
