# grade_calculator.py
# Week 2 Project: Student Grade Calculator

def get_grade(marks: int) -> str:
    """Return grade letter based on marks."""
    if 90 <= marks <= 100:
        return "A"
    elif 80 <= marks <= 89:
        return "B"
    elif 70 <= marks <= 79:
        return "C"
    elif 60 <= marks <= 69:
        return "D"
    else:
        return "F"


def get_message(grade: str) -> str:
    """Return encouraging message for each grade."""
    messages = {
        "A": "Excellent! You're a star! 🌟",
        "B": "Very Good! Keep it up! 👍",
        "C": "Good effort! You can do even better! 💪",
        "D": "Don't give up! Practice more and improve! 📚",
        "F": "It's okay! Try again — you will improve! 🌈"
    }
    return messages.get(grade, "Keep learning!")


def get_valid_marks() -> int:
    """Use a while loop to keep asking until marks are valid (0-100)."""
    while True:
        raw = input("Enter marks (0-100): ").strip()

        # Basic error handling for non-integers
        try:
            marks = int(raw)
        except ValueError:
            print("❌ Invalid input! Please enter a number (example: 85).")
            continue

        # Range validation
        if 0 <= marks <= 100:
            return marks
        else:
            print("❌ Marks must be between 0 and 100. Try again.")


def main():
    print("📘 STUDENT GRADE CALCULATOR")

    name = input("Enter student name: ").strip()
    if not name:
        name = "STUDENT"

    marks = get_valid_marks()
    grade = get_grade(marks)
    message = get_message(grade)

    print("\n📊 RESULT FOR " + name.upper() + ":")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


if __name__ == "__main__":
    main()
