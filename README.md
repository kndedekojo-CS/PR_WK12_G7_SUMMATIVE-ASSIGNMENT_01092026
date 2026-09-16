<<<<<<< HEAD
# School Fee Payment Tracking System

## Team Members
- Rebekah Mensah
- Angelica Bukari
- Korkor Ndede Kojo
- Aishat Adidere

## Project Description
A Python-based School Fee Payment Tracking System designed to help schools manage student information, record fee payments, track payment history, and calculate outstanding balances.

## Main Features
- Register a student
- Display registered students
- Search for a student using an ID
- Record a fee payment
- Display a student's payment history
- Calculate the total amount paid
- Calculate the outstanding balance
- Prevent invalid payment amounts
- Prevent a payment greater than the outstanding balance
- Save student and payment information to files
- Load saved information automatically when the application starts

## Classes Used
- **Student Class** – This stores a student's details (ID, name, grade, total fee). Handles registering, displaying, and searching for students.
- **Payment Class** – This stores a single fee payment record (payment ID, student ID, amount, date). Handles recording payments and validating payment amounts.
- **FeeAccount Class** – This Links a student to their payments. Calculates total amount paid and outstanding balance, and displays payment history.

## Files Used
- `students.json` – Stores registered student records so they persist between application runs.
- `payments.json` – Stores fee payment records so they persist between application runs.

## How to Run the Application
```
python main.py
```

## Team Contributions
- **Korkor Ndede Kojo** – Repository setup, Student class (registration, display, search, validation), main menu structure
- **Angelica Bukari** – Payment class, payment validation
- **Aishat Adidere** – FeeAccount class, payment history and balance calculations
- **Rebekah Mensah** – File handling (save/load), application integration, testing
=======
## PR_WK12_G7_SUMMATIVE-ASSIGNMENT_01092026

## School Fee Payment Tracking System

A Python-based system for managing student fee payments, tracking payment history, and calculating outstanding balances.

## Team Members

- Team Member 1 – Student Class
- Team Member 2 – Payment Class
- Team Member 3 – FeeAccount Class
- Team Member 4 – Main Program, File Handling, Integration and Testing

## Project Description

The School Fee Payment Tracking System is a Python application designed to help a school manage student fee information and payment records.

The system allows users to register students, view and search for student information, record fee payments, and view payment history. It also calculates the total amount paid and the outstanding balance for each student.

Student and payment information is stored in JSON files so that the data can be saved and loaded when the program is used again.


## Main Features

- Register new students with their student ID, name, grade, and total fee.

- Display registered student information.

- Search for students using their Student ID.

- Record fee payments for students.

- Prevent invalid payment amounts and overpayments.

- Prevent duplicate Student IDs and Payment IDs.

- View payment history for each student.

- Calculate the total amount paid by a student
.
- Calculate the outstanding fee balance.

- Save student and payment information using JSON files.

- Load saved information when the program starts.

- Handle invalid user input with meaningful error messages.


## Classes

### Student
The `Student` class stores student information such as Student ID, name, grade, and total fee. It also provides methods for displaying student details.

### Payment
The `Payment` class represents a fee payment made by a student. It stores the payment ID, amount, date, and Student ID. It also validates payment amounts and prevents payments from exceeding the outstanding balance.

### FeeAccount
The `FeeAccount` class manages a student's fee account. It stores payment records, calculates the total amount paid, calculates the outstanding balance, and displays payment history.

## Files

- `main.py` – Controls the main menu, user input, file handling, validation, and connects the different classes.

- `student.py` – Contains the `Student` class and functions for registering, displaying, validating, and searching students.

- `payment.py` – Contains the `Payment` class and functions for validating and recording payments.

- `feeaccount.py` – Contains the `FeeAccount` class for managing payment history and calculating balances.

- `students.json` – Stores student information.

- `payments.json` – Stores payment information.

- `README.md` – Provides information about the project, features, files, and how to run the system.

- `Class Design` – Contains the design and description of the classes used in the system.

- `Class Diagram` – Shows the relationship between the classes in the system.

- `Test Plan` – Contains the test cases used to check the main features of the system.

- `Test Results` – Contains the actual results of the tests, including Pass/Fail results and screenshot evidence.


## How to Run the Program

1. Download or clone the project from GitHub
.
2. Open the project folder in a Python editor or terminal.

3. Make sure Python is installed on the computer.

4. Run the following command:

```text
python main.py

5. The main menu will appear.

6. Select an option by entering the corresponding number.

7. Follow the instructions displayed by the system.



### Team Contributions

### Korkor Ndede Kojo
- Designed and implemented the `Student` class.

- Added student registration and student validation features.


### Angelica Bukari
- Designed and implemented the `Payment` class.

- Added payment validation and payment recording functionality.



### Aishat Adedire 

- Designed and implemented the `FeeAccount` class.

- Added payment history and balance calculation functionality.


### Rebekah Adjoah Mensah

- Developed and integrated the `main.py` program.

- Implemented JSON file handling for students and payments.

- Connected the different classes and features.

- Added input validation and exception handling.

- Performed system testing and coordinated the Test Results.

- Managed GitHub integration and prepared the README.



## GitHub Repository

[View the project on GitHub]( https://github.com/kndedekojo-CS/PR_WK12_G7_SUMMATIVE-ASSIGNMENT_01092026.git)


###Thank You.


>>>>>>> e999c2fadda27b07b33f426477bf2053c922a684
