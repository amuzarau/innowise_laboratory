from typing import List, Optional, TypedDict


class Student(TypedDict):
    """Typed dictionary defining the structure of a student record."""

    name: str
    grades: List[int]


def print_menu() -> None:
    """Render the main command menu."""
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Show report (all students)")
    print("4. Find top performer")
    print("5. Exit")


def get_menu_choice() -> int:
    """
    Read and validate the user's menu selection.
    Ensures input is an integer in the range [1, 5].
    """
    while True:
        try:
            choice_str = input("Enter your choice (1-5): ").strip()
            choice = int(choice_str)
            if 1 <= choice <= 5:
                return choice
            print("Please enter a number between 1 and 5")
        except ValueError:
            # Reject non-numeric input gracefully
            print("Invalid input. Please enter a number between 1 and 5.")


def normalize_name(name: str) -> str:
    """Trim extra whitespace from user-provided names."""
    return name.strip()


def find_student(students: List[Student], name: str) -> Optional[Student]:
    """
    Locate a student by name, using case-insensitive comparison.
    Returns the matching record or None if the student is not found.
    """
    name = normalize_name(name)
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None


def add_student(students: List[Student]) -> None:
    """Option 1: Create and register a new student entry."""
    name = normalize_name(input("Enter student name: "))

    if not name:
        print("Name cannot be empty.")
        return

    # Prevent duplicate student records
    if find_student(students, name) is not None:
        print(f"Student '{name}' already exists.")
        return

    # Initialize student dictionary through TypedDict structure
    new_student: Student = {"name": name, "grades": []}
    students.append(new_student)
    print(f"Student '{name} added successfully.")


def add_grades_for_student(students: List[Student]) -> None:
    """Option 2: validated grade values to an existing student's record."""
    if not students:
        print("No students yet. Please add a student first.")
        return

    name = input("Enter student name: ")
    student = find_student(students, name)

    if student is None:
        print(f"Student '{name}' was not found.")
        return

    print("Enter grades for the student (0–100).")
    print("Type 'done' when you finish.")

    while True:
        raw = input("Enter a grade (or 'done' to finish): ").strip()
        if raw.lower() == "done":
            break

        try:
            grade = int(raw)
            # Validate grade boundaries
            if 0 <= grade <= 100:
                student["grades"].append(grade)
            else:
                print("Grade must be between 0 and 100")
        except ValueError:
            # Reject non-numeric input gracefully
            print("Invalid input! Please enter a number.")


def calculate_average(grades: List[int]) -> Optional[float]:
    """
    Calculate the average of a list of grades.
    Returns None for empty grade lists.
    """
    if not grades:
        return None
    return sum(grades) / len(grades)


def show_report(students: List[Student]) -> None:
    """Option 3: Show per-student averages + aggregated class statistics."""
    if not students:
        print("No students have been added yet.")
        return

    print("\n--- Student Report ---")
    averages: List[float] = []

    for student in students:
        try:
            # Attempt to compute average; may raise ZeroDivisionError
            avg = sum(student["grades"]) / len(student["grades"])
        except ZeroDivisionError:
            # Student has no grades
            print(f"{student['name']}'s average grade is N/A.")
            continue

        # Average computed successfully
        print(f"{student['name']}'s average grade is {avg:.1f}.")
        averages.append(avg)

    print("-" * 27)

    if not averages:
        print("No grades have been added for any student yet.")
        return

    max_avg = max(averages)
    min_avg = min(averages)
    overall_avg = sum(averages) / len(averages)

    print(f"Max Average: {max_avg:.1f}")
    print(f"Min Average: {min_avg:.1f}")
    print(f"Overall Average: {overall_avg:.1f}")


def find_top_performer(students: List[Student]) -> None:
    """Option 4: Find and display the student with the highest average."""
    if not students:
        print("No students have been added yet.")
        return

    # Build list of (student, average_value) pairs for students who have at least one grade
    students_with_avgs = [
        (student, calculate_average(student["grades"]))
        for student in students
        if calculate_average(student["grades"]) is not None
    ]

    if not students_with_avgs:
        print("No grades have been added, so there is no top performer yet.")
        return

    # Select the tuple with the highest average; item[1] = average grade
    top_student, top_avg = max(students_with_avgs, key=lambda item: item[1])

    print(
        f"The student with the highest average is "
        f"{top_student['name']} with a grade of {top_avg:.1f}"
    )


def main() -> None:
    """Main entry point of the program: handles menu navigation and user actions."""
    students: List[Student] = []

    while True:
        print_menu()
        choice = get_menu_choice()

        # Handle user selection
        match choice:
            case 1:
                add_student(students)
            case 2:
                add_grades_for_student(students)
            case 3:
                show_report(students)
            case 4:
                find_top_performer(students)
            case 5:
                print("Exiting program.")
                break
            case _:
                print("Unknown option.Please try again.")


if __name__ == "__main__":
    main()
