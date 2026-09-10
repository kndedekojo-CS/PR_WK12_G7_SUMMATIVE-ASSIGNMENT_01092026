#This is the  student.py file
#This file defines the Student class and the functions used to register, display, and search for students.


class Student:
    # This creates a student and stores their information.

    def __init__(self, student_id, name, grade, total_fee):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.total_fee = total_fee
