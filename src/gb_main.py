# LD 1st Simple Grade Book Personal Project
from gb_actions import *
from all_helpers import *
import time

# Main menu: Add student, Add grade to student, View Student (name, ID, ALL grades, average, letter), View ALL students (Name, ID, Average, letter for EACH), Class summary (name and letter grade for all), Exit
def gb_main():
    gradebook = GradeBook()
    while True:
        clear_screen()
        type_print("-- Main Menu --\n1) Add New Student\n2) Add Grade to Student\n3) View a Student\n4) View All Students\n5) Class Summary\n6) Leave\n")
        action = input("Enter number corresponding to action:\n").strip().lower()
        if action == "1":
            # Add Student
            add_new_student(gradebook)
            time.sleep(2)
        elif action == "2":
            # Add grade
            add_stu_grade(gradebook)
            time.sleep(2)
        elif action == "3":
            # View child
            view_student(gradebook)
            time.sleep(4)
        elif action == "4":
            # View all
            view_all(gradebook)
            time.sleep(4)
        elif action == "5":
            # Class summary
            class_sum(gradebook)
            time.sleep(3)
        elif action == "6":
            # leave
            type_print("Saving changes . . .")
            gradebook.save_students()
            time.sleep(1)
            type_print("Changes saved!")
            break
        else:
            print("Invalid input. Try again")
            continue
    print("Goodbye!")
    return

# See Actions file for more code