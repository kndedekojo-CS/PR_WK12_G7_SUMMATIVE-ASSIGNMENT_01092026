# Class Design Document

Project 5 – School Fee Payment Tracking System

## Team Members
- Korkor Ndede Kojo – Student class
- Angelica Bukari – Payment class
- Aishat Adidere – FeeAccount class
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

*(Payment and FeeAccount class sections to be added by Member 2 and Member 3)*