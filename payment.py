class Payment:
    """Represents a fee payment made by a student."""

    def __init__(self, payment_id, amount, date, student_id):
        self.payment_id = payment_id
        self.amount = amount
        self.date = date
        self.student_id = student_id
    def validate_amount(self):
        """check whether the payment amount is valid."""
        if self.amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        return True
    def check_outstanding_balance(self, outstanding_balance):
        """Prevent a payment from exceeding the outstanding balance."""
        if self.amount > outstanding_balance:
            raise ValueError("Payment amount cannot be greater than the outstanding balance.")
        return True

    
def record_payment(payment_id, amount,date, student_id, outstanding_balance):
        """Create and validate a new payment."""
        payment = Payment(payment_id, amount, date, student_id)
        payment.validate_amount()
        payment.check_outstanding_balance(outstanding_balance)
        return payment

payment1 =Payment("P001", 5000, "2026-09-09", "ST001")
payment1 = record_payment("P001", 5000, "2026-09-09", "ST001",10000)

print("Payment recorded successfully!")
print("Payment ID:", payment1.payment_id)
print("Amount:", payment1.amount)
print("Date:", payment1.date)
print("Student ID:", payment1.student_id)

try:
    payment1 = record_payment(
        "P002",
        -500,
        "2026-09-10",
        "ST001",
        10000
    )

    print("Payment recorded successfully!")

except ValueError as error:
    print("Invalid payment:", error)

