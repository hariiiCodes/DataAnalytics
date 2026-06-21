students = []

def add_student():
    name = input("Enter the name of student: ")
    scores = []
    while True:
        score = input("Enter score (or 'done'): ")
        if score.lower() == "done":
            break
        score = float(score)
        if 0 <= score <= 100:
            scores.append(score)
        else:
            print("Score must be between 0 and 100")

    average = calculate_average(scores)
    grade = get_letter_grade(average)

    student = {
        "name": name,
        "scores": scores,
        "average": average,
        "grade": grade
    }

    students.append(student)

    print(f"\nAdded {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
