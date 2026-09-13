# This is the main.py file
# This file controls the main program, menu, user input,
# file handling, validation, and connects all the classes together.

import json

import os

from student import Student

from payment import Payment, record_payment

from feeaccount import FeeAccount

# JSON(JavaScript Object Notation) files are used to store student and payment information.
# This allows the data to be saved even after the program is closed.
# students.json stores registered students, while payments.json stores payment records.


STUDENTS_FILE = "students.json"

PAYMENTS_FILE = "payments.json"


def create_data_files():

    """Create the data files if they do not exist."""

    #check if the student file exists.

    try:
        open(STUDENTS_FILE, "r"). close()

    except FileNotFoundError:

        with open(STUDENTS_FILE, "w") as file:

            json.dump([], file)   


    #check if the payment file exists.

    try:
        open(PAYMENTS_FILE, "r").close()

    except FileNotFoundError:

        with open(PAYMENTS_FILE, "w") as file:

            json.dump([], file )    


def load_students():

    """Loads students from the JSON file."""

    with open(STUDENTS_FILE, "r") as file:

        data = json.load(file)

    students = []

    for student_data in data:

        student = Student(
            student_data["student_id"],

            student_data["name"],

            student_data["grade"],

            student_data["total_fee"]
        )

        students. append(student)

    return students

create_data_files()


