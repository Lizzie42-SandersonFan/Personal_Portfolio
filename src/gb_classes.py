# Class for MAKING A STUDENT
from all_helpers import *
import csv
import ast

# (Add grade, calculate average, Display info, get letter for average (A=90+, B=80-89, C=70-79, D=60-69, F=<60))
class MakeStudent:
    def __init__(self, name, id, grades=None):
        self.name = name
        self.id = id
        # Parse grades if it's a string (from CSV), otherwise use list or empty list
        if grades is None:
            self.grades = []
        elif isinstance(grades, str):
            # Convert string representation of list to actual list
            try:
                self.grades = ast.literal_eval(grades)
                # Ensure it's a list
                if not isinstance(self.grades, list):
                    self.grades = []
            except Exception as e:
                print(f"Could not parse grades '{grades}': {e}")
                self.grades = []
        else:
            self.grades = grades if isinstance(grades, list) else []

    def student_overview(self):
        if not self.grades:
            # The list is empy and I want to display that fact
            grade_display = "None"
        else:
            # There are grades to display
            grade_display = self.grades # Set to the list so the list is printed

        return f"Name: {self.name}, ID: {self.id}, Grades: {grade_display}"

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            avg = 0
        else:
            avg = 0
            for item in self.grades:
                avg += item
            avg = avg / len(self.grades)
            avg = round(avg, 2)
        return avg
    
    def get_letter(self, average = None):
        if average is None:
            average = self.average_grade()
        if average >= 90:
            letter = "A"
        elif average >= 80 and average < 90:
            letter = "B"
        elif average >= 70 and average < 80:
            letter = "C"
        elif average >= 60 and average < 70:
            letter = "D"
        else:
            letter = "F"
        
        return letter


# Class for MANAGING LOTS OF STUDENTS. Add student, find student, see class overview, see all students for selection
class GradeBook:
    def __init__(self, students=None):
        if students is None:
            students = []
        self.students = students
        # Open a written CSV and save each student in the students list. At the end of program, this list will be WRITTEN to be saved
        try:
            with open('P:\DeLong, Lizzie\Personal_Portfolio\docs\grade_book.csv', 'r') as file:
                content = csv.reader(file)
                headers = next(content)
                for line in content:
                    a_student = MakeStudent(line[0], line[1], line[2])
                    self.students.append(a_student)
                    continue
        except Exception as e:
            print(f"Could not open file in ALL_CLASSES GRADEBOOK __INIT__ method: {e}")

    def display_students(self):
        for child in self.students:
            print(f"Name: {child.name} (ID: {child.id})")

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, name, id):
        for student in self.students:
            if student.name == name or student.id == id:
                return student
            else:
                continue

    def view_all_kids(self):
        for student in self.students:
            print(f"Name: {student.name}, ID: {student.id}, Average: {student.average_grade()}, Letter Grade: {student.get_letter()}")

    def class_overview(self):
        for kid in self.students:
            # Print the name and the LETTER grade
            print(f"Name: {kid.name}, Grade: {kid.get_letter()}")

    def save_students(self):
        # take the students list, write the headers, and write each list item
        try:
            with open("P:\DeLong, Lizzie\Personal_Portfolio\docs\grade_book.csv", "w") as file:
                fieldnames = ['name','id','all_grades']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for item in self.students:
                    writer.writerow({'name': item.name, 'id': item.id, 'all_grades': item.grades})
                    continue
        except:
            print("Could not open file in ALL_CLASSES GRADEBOOK SAVE_STUDENTS method")