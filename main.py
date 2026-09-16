# This is the main.py file
# This file controls the main program, menu, user input,
# file handling, validation, and connects all the classes together.

import json

import os

from student import Student, register_student, display_students, search_student

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

        students.append(student)

    return students

def save_students(students):
    """ Saves students to the JSON file."""

    data = []

    for student in students:
        student_data = {
            "student_id": student.student_id,
            "name": student.name,
            "grade": student.grade,
            "total_fee": student.total_fee
        }

        data.append(student_data)
    with open(STUDENTS_FILE, "w") as file:
        json.dump(data, file, indent=4)


# This function loads saved payment information from the JSON file.
def load_payments():
    with open(PAYMENTS_FILE, "r") as file:
        data = json.load(file)

    payments = []

    for payment_data in data:
        payment = Payment(
            payment_data["payment_id"],
            payment_data["amount"],
            payment_data["date"],
            payment_data["student_id"]
        )

        payments.append(payment)

    return payments

 


#This function saves payment information to the JSON file.
def save_payments(payments):
    data = []

    for payment in payments:
#store the payment information in a dictionary.
       payment_data = {
        "payment_id": payment.payment_id,
        "amount": payment.amount,
        "date": payment.date,
        "student_id": payment.student_id,
       }
       data.append(payment_data)
    with open(PAYMENTS_FILE, "w") as file:
        json . dump(data , file, indent=4)


create_data_files()
students = load_students()
payments =load_payments()
# Save payment information to the JSON file.
save_payments(payments)


