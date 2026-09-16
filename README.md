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