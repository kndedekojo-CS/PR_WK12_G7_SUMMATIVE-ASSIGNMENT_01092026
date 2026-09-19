# PR_WK12_G7_SUMMATIVE-ASSIGNMENT_01092026

# School Fee Payment Tracking System

A Python-based system for managing student fee payments, tracking payment history, and calculating outstanding balances.

## Team Members

Korkor Ndede Kojo – Student class
Angelica Bukari – Payment class
Aishat Adidere – FeeAccount class
Rebekah Adjoah Mensah – File handling and integration

## Project Description

The School Fee Payment Tracking System is a Python application designed to help a school manage student fee information and payment records.

The system allows users to register students, view and search for student information, record fee payments, and view payment history. It also calculates the total amount paid and the outstanding balance for each student.

Student and payment information is stored in JSON files so that the data can be saved and loaded when the program is used again.

## Main Features

 Register new students with their Student ID, name, grade, and total fee.
 Display registered student information.
 Search for students using their Student ID.
 Record fee payments for students.
 Prevent invalid payment amounts and overpayments.
 Prevent duplicate Student IDs and Payment IDs.
 View payment history for each student.
 Calculate the total amount paid by a student.
 Calculate the outstanding fee balance.
 Save student and payment information using JSON files.
 Load saved information when the program starts.
 Handle invalid user input with meaningful error messages.
 Automatically start the application using the `Start School Fee System.bat` launcher.

## Classes

### Student

The `Student` class stores student information such as Student ID, name, grade, and total fee. It also provides functions for registering, validating, displaying, and searching for students.

### Payment

The `Payment` class represents a fee payment made by a student. It stores the payment ID, amount, date, and Student ID. It also validates payment amounts and prevents payments from exceeding the outstanding balance.

### FeeAccount

The `FeeAccount` class manages a student's fee account. It stores payment records, calculates the total amount paid, calculates the outstanding balance, and displays payment history.

## Files

`main.py` – Controls the main menu, user input, file handling, validation, and connects the different classes.

 `student.py` – Contains the `Student` class and functions for registering, displaying, validating, and searching students. `payment.py` – Contains the `Payment` class and functions for validating and recording payments.

 `feeaccount.py` – Contains the `FeeAccount` class for managing payment history and calculating balances.

 `students.json` – Stores student information.

 `payments.json` – Stores payment information.

  `Start School Fee System.bat` – Launches the Python application automatically.

  `README.md` – Provides information about the project and how to use the system.

   `docs/Class Design.pdf` – Contains the class design information.

  `docs/Class Diagram.pdf` – Shows the relationship between the classes.

   `docs/Test Plan.pdf` – Contains the test cases used to check the system.

   `docs/Test Results.pdf` – Contains the actual test results.

   `Test Screenshots/` – Contains screenshots taken during system testing.

## How to Run the Program

### Option 1: Using the Application Launcher

1. Download or clone the project from GitHub.

2. Make sure Python is installed on the computer.

3. Open the project folder.

4. Double-click `Start School Fee System.bat`.

5. The School Fee Management System will start automatically.

6. Select an option from the main menu and follow the instructions.

### Option 2: Using the Python Command

1. Open the project folder in a terminal.

2. Make sure Python is installed.

3. Run:

```text
python main.py

4.The main menu will appear.

5. Select an option by entering the corresponding number.

6. Follow the instructions displayed by the system.

###Team Contributions

Korkor Ndede Kojo

Designed and implemented the Student class.
Added student registration and student validation features.
Added student display and search functionality.


Angelica Bukari

Designed and implemented the Payment class.
Added payment validation.
Added payment recording functionality.


Aishat Adidere
Designed and implemented the FeeAccount class.
Added payment history functionality.
Added total paid and outstanding balance calculations.

Rebekah Adjoah Mensah

Developed and integrated the main.py program.
Implemented JSON file handling for students and payments.
Connected the different classes and features.
Added input validation and exception handling.
Performed system testing and coordinated the Test Results.
Managed GitHub integration.
Added the application launcher.
Prepared and updated the README

GitHub Repository
https://github.com/kndedekojo-CS/PR_WK12_G7_SUMMATIVE-ASSIGNMENT_01092026.git

