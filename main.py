# This is the main.py file
# This file controls the main program, menu, user input,
# file handling, validation, and connects all the classes together.

import json

import os

from datetime import date

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



save_payments(payments)

# This creates a fee account for each registered student.

fee_accounts =[]

for student in students:

    account = FeeAccount(student)

    fee_accounts.append(account)

# This adds each saved payment to the correct student's fee account. 
for payment in payments:
        # Find the fee account that belongs to this payment's student.
        for account in fee_accounts:
            if account.student.student_id == payment.student_id:
                account.add_payment(payment)

#Save payment information to the JSON file
save_payments(payments)

#this function displays the main menu and lets the user choose an option.
def main_menu():

    while True:

        print("\n--- STUDENT FEE MANAGEMENT SYSTEM---")


        print("1. Register Student")

        print("2. Display Students")

        print("3. Search Student")

        print("4. Record Payment")

        print("5. View Payment History")

        print("6. Exit")
    

        choice = input(" Enter your choice: ")

        if choice == "1":

          #This registers a new student and returns the student if successful.
            new_student = register_student(students)

         # This saves the student and creates their fee account only if registration was successful.
            if new_student is not None:
                save_students(students)
                fee_accounts.append(FeeAccount(new_student))
        


        elif choice == "2":
            display_students(students)
        # This adds spacing after the student list.
            print()

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            
             # This asks for the student ID for the payment.
            student_id = input("Enter Student ID: ").strip()

            student = next((s for s in students if s.student_id == student_id), None)
            if student is None:

                print("Student not found.")

                continue

            # This asks the user to enter the payment amount.
            try:
                amount = float(input("Enter Payment Amount: "))

            except ValueError:
                print("Error: Payment amount must be a number.")

                continue
             
            payment_id = input("Enter Payment ID: ").strip()

            

            # This finds the fee account for the selected student.
            account = next((a for a in fee_accounts if a.student.student_id == student_id), None) 
            if account is None:
                print("Fee account not found.")
                continue
             # This gets the student's current outstanding balance.

            outstanding_balance = account.calculate_outstanding_balance()

            # This creates and validates the payment.
            try:
                payment = record_payment(
                payment_id,
                amount,
                date.today().isoformat(),
                student_id,
                outstanding_balance
            )
            except ValueError as error:
                print("Error:", error)
                continue

             # This adds the payment to the student's fee account.
            account.add_payment(payment)

            # This saves the payment in the payment list.
            payments.append(payment)

            # This saves the updated payment list to the JSON file.
            save_payments(payments)
              # This confirms that the payment was recorded successfully.
            print("Payment recorded successfully.")

            

        elif  choice == "5":

        # This asks for the student ID to view their payment history.
            student_id = input("Enter Student ID: ").strip()

        # This finds the fee account for the selected student.
            account = next((a for a in fee_accounts if a.student.student_id == student_id), None)

        # This checks if the fee account exists.
            if account is None:
                print("Fee account not found.")
                continue

        # This displays the payment history for the selected student.
            account.display_payment_history()


        elif choice == "6":
            print("Thank you  very much for using the system.")
            break 

        else:
            print("Invalid choice. Please try again.")


main_menu()





