class FeeAccount:
    """This class acts as a financial ledger representing a fee account for a student, tracking their payments and outstanding balance."""

    def __init__(self, student):
        self.student = student
        self.payments = []

    def calculate_total_paid(self):
        """Calculates the total amount paid by the student."""
        total = 0
        for payment in self.payments:  
            total += payment.amount     #Adds each payment amount to the total paid.
        return total

    def calculate_outstanding_balance(self):
        """Calculates the outstanding balance for the student."""
        return self.student.total_fees - self.calculate_total_paid()  #this subtracts the total amount paid from the total fees owed by the student.