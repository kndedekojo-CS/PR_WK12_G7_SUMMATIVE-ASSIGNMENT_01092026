# Class Design Document

Project 5 – School Fee Payment Tracking System

## Team Members
- Korkor Ndede Kojo – Student class
- Angelica Bukari – Payment class
- Aishat Adidere – FeeAccount class
- Rebekah Mensah – File handling and integration


## Class 1: Student

**Purpose:** This represents one student and stores their basic details and fee amount. Also includes supporting functions to validate, register, display, and search students.

### Attributes

| Attribute | Data Type | Description |
|---|---|---|
| student_id | string | This is a unique ID for the student |
| name | string | This is a student's full name |
| grade | string | This is a student's grade/class (e.g. "Grade 10") |
| total_fee | float | This is the total fee amount owed |

### Methods

| Method | Type | Parameters | Purpose |
|---|---|---|---|
| __init__ | Constructor | student_id, name, grade, total_fee | This creates a new Student object and stores its details |
| display_details | Instance | none | This prints the student's ID, name, grade, and total fee |

### Supporting Functions (this worked with a list of Student objects)

| Function | Type | Parameters | Purpose |
|---|---|---|---|
| validate_student_id | Function | student_id, students_list | This checks the ID isn't empty and isn't already used by another student |
| register_student | Function | students_list | This asks the user for student details, validates them, and adds a new Student to the list |
| display_students | Function | students_list | This prints the details of every student in the list |
| search_student | Function | students_list | This asks for a student ID, returns the matching Student object if found, otherwise returns None |

### Loops Used

| Location | Loop Type | Purpose |
|---|---|---|
| display_students | for loop | This goes through the students list one by one and displays each student's details |
| search_student | for loop | This goes through the students list one by one, comparing each student's ID to the one being searched for |



## Class 2: Payment

**Purpose:** This represents a single fee payment made by a student. It stores the payment's ID, amount, date, and the ID of the student it belongs to, and includes validation to make sure the payment amount is valid and does not exceed the student's outstanding balance before the payment is recorded.

### Attributes

| Attribute | Data Type | Description |
|---|---|---|
| payment_id | string | This is a unique ID for the payment |
| amount | float | This is the amount paid |
| date | string | This is the date the payment was made |
| student_id | string | This is the ID of the student the payment belongs to |

### Methods

| Method | Type | Parameters | Purpose |
|---|---|---|---|
| __init__ | Constructor | payment_id, amount, date, student_id | This creates a new Payment object and stores its details |
| validate_amount | Instance | none | This checks that the payment amount is greater than zero; raises a ValueError if not |
| check_outstanding_balance | Instance | outstanding_balance | This checks that the payment doesn't exceed the outstanding balance; raises a ValueError if it does |

### Supporting Functions

| Function | Type | Parameters | Purpose |
|---|---|---|---|
| record_payment | Function | payment_id, amount, date, student_id, outstanding_balance | This creates a Payment object and runs both validation checks on it before returning it |

### Loops Used

This class does not use any loops. Each method works with a single Payment object and validates it using `if` statements, rather than looping through a collection.



## Class 3: FeeAccount

**Purpose:** This acts as a financial ledger representing a fee account for a student. It tracks their payment history, calculates the total amount paid as well as the outstanding balance, and links students with their payment records.

### Attributes

| Attribute | Data Type | Description |
|---|---|---|
| student | Student object | This stores the student linked to the fee account |
| payments | list | This stores all payment records belonging to the student |

### Methods

| Method | Type | Parameters | Purpose |
|---|---|---|---|
| __init__ | Constructor | student | This creates a new FeeAccount object linked to a student and initializes an empty payments list |
| calculate_total_paid | Instance | none | This loops through the payments list and calculates the total sum of all payment amounts |
| calculate_outstanding_balance | Instance | none | This subtracts the total amount paid from the student's total fee to determine the remaining balance |
| add_payment | Instance | payment | This verifies that the payment belongs to the correct student and adds it to the payments list |
| display_payment_history | Instance | none | This prints a formatted table of all payments, the total fee, total amount paid, and the outstanding balance |

### Loops Used

| Location | Loop Type | Purpose |
|---|---|---|
| calculate_total_paid | for loop | This goes through the payments list one by one and adds each payment's amount to the running total |
| display_payment_history | for loop | This goes through the payments list to extract the date, payment ID, and amount, printing each as a formatted row in the payment history table |