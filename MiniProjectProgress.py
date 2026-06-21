students=[]

def main():                                            #DECLARED MAIN FUNCTION FIRST FOR CHECKING THE STRUCTURE OF PROGRAM.
    while True:
        print("\n--- Grade Calculator ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Class Report")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":                              
           # addStudent()                             #COMMENTED FOR LATER USE.     
           print("1")
        elif choice == "2":
           # viewStudents()                           #COMMENTED FOR LATER USE. 
           print("2")
        elif choice == "3":
           # classReport()                            #COMMENTED FOR LATER USE.
            print("3")
        elif choice == "4":
            print("Program Ended")
            break
        else:
            print("Invalid choice")

main()


# def addStudent():
#     name=input("Enter the name of student: ")
#     scores=[]
#     while True:
#         score=input("Enter score (or 'done'): ")
#         if score.lower()=="done":
#             break
#         score=float(score)
#         if 0<=score<=100:
#             scores.append(score)
#         else:
#             print("Score must be between 0 and 100")

#     average = calcAverage(scores)
#     grade = getGrade(average)

#     student = {
#         "name": name,
#         "scores": scores,
#         "average": average,
#         "grade": grade
#     }

#     students.append(student)

#     print(f"\nAdded {name}")
#     print(f"Average: {average:.2f}")
#     print(f"Grade: {grade}")

# def calcAverage(scores):
#     if len(scores) == 0:
#         return 0
#     return sum(scores) / len(scores)

# def get_letter_grade(avg):
#     if avg >=90:
#         return "A"
#     elif avg >=80:
#         return "B"
#     elif avg >=70:
#         return "C"
#     elif avg >=60:
#         return "D"
#     else:
#         return "F"                                

                                #WILL SORT AND ORDER THE FUNCTIONS LATER.
