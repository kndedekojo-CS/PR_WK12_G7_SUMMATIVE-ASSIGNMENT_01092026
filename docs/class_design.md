# Class Design Document

Project 5 – School Fee Payment Tracking System

## Team Members
- Korkor Ndede Kojo – Student class
- Angelica Bukari – Payment class
- Aishat Adedire – FeeAccount class
- Rebekah Mensah – File handling and integration

## Selected Project
Project 5 – School Fee Payment Tracking System


## Class 1: Student
**Purpose:** This represents one student and stores their basic details and fee amount. Also includes supporting functions to validate, register, display, and search students.

## Attributes

| Attribute | Data Type | Description |
|---|---|---|
| student_id | string | This is a Unique ID for the student |
| name | string |This is a Student's full name |
| grade | string |This is a Student's grade/class (e.g. "Grade 10") |
| total_fee | float | This is the Total fee amount owed |

## Methods

| Method | Parameters | Purpose |
|---|---|---|
| __init__ | student_id, name, grade, total_fee |This creates a new Student object and stores its details |
| display_details | none |This prints the student's ID, name, grade, and total fee |

## Supporting Functions (This worked with a list of Student objects)

| Function | Parameters | Purpose |
|---|---|---|
| validate_student_id | student_id, students_list |This Checks the ID isn't empty and isn't already used by another student |
| register_student | students_list |This Asks the user for student details, validates them, and adds a new Student to the list |
| display_students | students_list |This Prints the details of every student in the list |
| search_student | students_list |This Asks for a student ID, returns the matching Student object if found, otherwise returns None |

---

## Class 3: FeeAccount
**Purpose:** This acts as a financial ledger representing a fee account for a student, It tracks their payment history, calculates the total amount paid as well as the outstanding balance and links students with their payment records. 

## Attributes

| Attribute | Data Type | Description |
|---|---|---|
| student | `Student` object| Stores the student linked to the fee account
| payments | list | Stores all payment records belonging to the student

## Methods
| Method | Purpose |
|---|---|
| __init__ | This creates a new FeeAccount object linked to a student and initializes an empty payments list
| calculate_total_paid | This loops through the payments list and calculates the total sum of all payment amounts
| calculate_outstanding_balance | This subtracts the total amount paid from the student's total fee to determine the remaining balance
| add_payment | This verifies that the payment belongs to the correct student and adds it to the payments list
| display_payment_history | This prints a formatted table of all payments, the total course fee, total amount paid, and the outstanding balance

## Loops Used
| Location | Loop Type | Purpose |
|---|---|---|
| calculate_total_paid | for loop | Goes through the payments list one by one and adds each payment's amount to the running total
| display_payment_history | for loop | Goes through the payments list to extract the date, payment_id, and amount, printing each as a formatted row in the payment history table.

---
*(Payment and FeeAccount class sections to be added by Member 2)* 