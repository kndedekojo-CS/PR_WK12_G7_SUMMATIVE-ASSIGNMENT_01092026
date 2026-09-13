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

