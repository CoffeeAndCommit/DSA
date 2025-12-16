# Represents a borrowing transaction.

import datetime
from datetime import datetime


class Loan:
    def __init__(self, loan_id, member_id, book_id, due_date: datetime ,return_date: datetime):
        self.loan_id = loan_id
        self.member_id = member_id
        self.book_id = book_id
        self.due_date = due_date
        self.return_date = return_date
    
    # Determine if overdue

    def is_overdue(self):
        return self.due_date < self.return_date or self.return_date is None 
    
    # Calculate fine

    def calculate_fine(self):
        if self.is_overdue():
            days_overdue = (datetime.now() - self.due_date).days
            return days_overdue * 0.5
        else:
            return 0
            
            
    # Close the loan on return

    def close_loan(self):
        self.return_date = datetime.now()
        
    

