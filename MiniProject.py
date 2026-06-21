students=[]

def calcAvg(scores):
    if len(scores)==0:
        return 0
    return sum(scores)/len(scores)

def getGrade(avg):
    if avg>=90:
        return "A"
    elif avg>=80:
        return "B"
    elif avg>=70:
        return "C"
    elif avg>=60:
        return "D"
    else:
        return "F"                   

def addStudent():
    name=input("Enter the name of student: ")
    scores=[]
    while True:
        score=input("Enter score (or 'done'): ")
        if score.lower()=="done":
            break
        score=float(score)
        if 0<=score<=100:
            scores.append(score)
        else:
            print("Score must be between 0 and 100")

    average=calcAvg(scores)
    grade=getGrade(average)

    student = {
        "name": name,
        "scores": scores,
        "average": average,
        "grade": grade
    }

    students.append(student)

    print(f"\nAdded {name}\nAverage score: {average:.2f}\nGrade: {grade}")

def viewStudents():
    if len(students)==0:
        print("No students found.")
        return
    
    print("\n---------------------------------------\n")
    print("      STUDENTS LIST    ")

    for student in students:
        print(f"{student['name']} | Average: {student['average']:.2f} | Grade: {student['grade']}")
    print("\n---------------------------------------")

def classReport():
    if len(students)==0:
        print("No student data available.")
        return

    highest=students[0]
    lowest=students[0]

    total_average=0

    for student in students:
        total_average+=student["average"]

        if student["average"]>highest["average"]:
            highest=student

        if student["average"]<lowest["average"]:
            lowest = student

    class_avg = total_average/len(students)

    print("\n--------------------------------------\n")
    print("      CLASS REPORT    ")
    print("Total Students:", len(students))

    print(f"Highest Average: {highest['name']} ({highest['average']:.2f})")

    print(f"Lowest Average: {lowest['name']} ({lowest['average']:.2f})")
    print(f"Class Average: {class_avg:.2f}")
    print("\n---------------------------------------")

def main():                                            
    while True:
        print("\n--- Grade Calculator ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Class Report")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice==1:                              
           addStudent()    
        elif choice==2:
           viewStudents()                        
        elif choice==3:
           classReport()     
        elif choice==4:
            print("\n--------------------------------------\n")
            print("           PROGRAM ENDED               ")
            print("\n--------------------------------------\n")
            break
        else:
            print("Invalid choice")

main()
