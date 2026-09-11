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

    def add_payment(self, payment):
        """Adds a Payment object to the account history."""
        if payment.student_id != self.student.student_id:       #checks that the payment belongs to the same student as the account
            print("Error: Payment student ID does not match the account's student ID.")
            return False

        self.payments.append(payment)  #Adds the payment to the payments list.
        return True

    def display_payment_history(self):
        """Displays all payments and the current balance."""
        print(f"Payment History for {self.student.name} (ID: {self.student.student_id}):")

        if not self.payments:    #checks if the student has made any payments
            print("No payments have been made yet.")
        else:
            print("Payments:")
            #displays the payment history in a tabular format with headers for date, payment ID, and amount paid.
            print(f"{'Date':<15} |{'Payment ID':<15} | {'Amount Paid'}")
            print("-" * 50)
            for payment in self.payments:      #loops through each payment in the payments list and prints the date, payment ID, and amount paid in a formatted manner.
                print(f"{payment.date:<15} | {payment.payment_id:<15} | ${payment.amount:,.2f}")

        print("-" * 50)    #prints a line of dashes to separate the payment history from the summary of fees, total paid, and outstanding balance.
        
        print(f"Total Fees: ${self.student.total_fees:,.2f}")
        print(f"Total Paid: ${self.calculate_total_paid():,.2f}")
        print(f"Outstanding Balance: ${self.calculate_outstanding_balance():,.2f}")
