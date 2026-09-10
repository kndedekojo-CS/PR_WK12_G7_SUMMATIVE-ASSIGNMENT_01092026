#This is the  student.py file
#This file defines the Student class and the functions used to register, display, and search for students.


class Student:
    # This creates a student and stores their information.

    def __init__(self, student_id, name, grade, total_fee):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.total_fee = total_fee

    # This displays the student's information.
    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Grade:", self.grade)
        print("Total Fee: ${:,.2f}".format(self.total_fee))


# This function checks if the student ID is valid.
def validate_student_id(student_id, students_list):

    # This function checks if the student ID is empty.
    if student_id.strip() == "":
        print("Error: Student ID cannot be empty.")
        return False

    #This function checks if the student ID is already being used by another student.
    for student in students_list:
        if student.student_id == student_id:
            print("Error: The Student ID is already being used.")
            return False

    #This function checks if the student ID is valid.
    return True


# This function registers a new student.
def register_student(students_list):
    print("\n~~~~~~Register New Student ~~~~~~")

    # This asks the user to enter the student's ID.
    student_id = input("Enter Student ID: ").strip()

    # This checks if the student ID is valid.
    if not validate_student_id(student_id, students_list):
        return

    # This asks the user to enter the student's name.
    name = input("Enter Student Name: ").strip()

    # This checks if the name is empty.
    if name == "":
        print("Error: Name cannot be empty.")
        return

    # This asks the user to enter the student's grade.
    grade = input("Enter Grade/Class (e.g. Grade 10): ").strip()

    # This asks the user to enter the total fee.
    try:
        total_fee = float(input("Enter Total Fee Amount: "))
    except ValueError:
        print("Error: Fee must be a number.")
        return

    # This checks if the fee is negative.
    if total_fee < 0:
        print("Error: Fee cannot be negative.")
        return

    # This creates a new student.
    new_student = Student(student_id, name, grade, total_fee)

    # This adds the student to the list.
    students_list.append(new_student)

    print(f"Student {name} registered successfully.")
