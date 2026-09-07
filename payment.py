class Payment:
    """Represents a fee payment made by a student."""

    def __init__(self, payment_id, amount, date, student_id):
# validate payment amount.
        if amount <= 0:
            raise ValueError("Payment amount must be greater than 0.")
# check payment against outstanding balance.
        if amount > outstanding_balance:
            raise ValueError("Payment cannot be grater than the outstanding balance.")

        self.payment_id = payment_id
        self.amount = amount
        self.date = date
        self.student_id = student_id

payment1 = Payment("P001" , 5000, "2026-09-07" , "ST001")

print(payment1.payment_id)
print(payment1.amount)
print(payment1.date)
print(payment1.student_id)