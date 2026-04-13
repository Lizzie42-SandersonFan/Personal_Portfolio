from gb_classes import *
from all_helpers import *
# Add student: Get student name and id. Create empty list for future grade holding
def add_new_student(the_gradebook):
    name = input("Enter student FULL name:\n").strip()
    stu_id = input("Enter student ID:\n").strip()
    student = MakeStudent(name, stu_id)
    
    the_gradebook.add_student(student)
    print("Student added!")
    print(student.student_overview())
    return
    

# Add grade: Show students with ID. Have user enter ID for student that needs a grade added. Enter a number between 0-100 (will need to be checked. Check if it is even a number first). Find the student by ID and append that grade into the list created
def add_stu_grade(the_gradebook):
    the_gradebook.display_students()
    while True:
        name = input("Enter student name:\n").strip()
        id = input("Enter student ID:\n").strip()
        a_student = the_gradebook.find_student(name, id)
        if not a_student:
            print("Seems that student couldn't be found. Try again.")
            continue
        else:
            break
    while True:
        grade = input(f"Enter the grade for {a_student.name} (0-100):\n")
        valid, int_grade = is_number(grade)
        if valid == True:
            if int_grade < 0 or int_grade > 100:
                print("Grade out of valid range. Try again.")
                continue
            else:
                a_student.add_grade(int_grade)
                print(f"Grade {int_grade} added to {a_student}!")
                break
        else:
            print("Seems you entered an invalid grade. Try again.")
            continue
    return

# View Student record: Show all students and select student by ID. Print that student as : Name, ID, ALL Grades, Average % Grade, Letter grade
def view_student(the_gradebook):
    def format_grade_list(stu_grades):
        if not stu_grades:
            return "None"
        else:
            return ", ".join(str(grade) for grade in stu_grades)

    the_gradebook.display_students()
    while True:
        name = input("Enter student name:\n").strip()
        id = input("Enter student ID:\n").strip()
        a_student = the_gradebook.find_student(name, id)
        if not a_student:
            print("Seems that student couldn't be found. Try again.")
            continue
        else:
            grades_str = format_grade_list(a_student.grades)
            print(f"Name: {a_student.name}\nID: {a_student.id}\nGrades: {grades_str}\nAverage: {a_student.average_grade()}\nLetter: {a_student.get_letter()}")
            break
    return

# View ALL Students: Show Name, ID, Average, Letter Grade for EACH student in CSV
def view_all(the_gradebook):
    the_gradebook.view_all_kids()
    return

# Class Summary: Names with corresponding Letter Grade
def class_sum(the_gradebook):
    the_gradebook.class_overview()
    return