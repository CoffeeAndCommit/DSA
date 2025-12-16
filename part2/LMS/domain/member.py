


# member represents a library user

class Member:
    def __init__(self,member_id,name,email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = [] # list of book_ids
    
    def borrow_book(self,book_id):
        self.borrowed_books.append(book_id)
    # Return books
    def return_book(self,book_id):
        self.borrowed_books.remove(book_id)
    # Track books borrowed
    def get_borrowed_books(self):
        return self.borrowed_books
    
    # Check borrowing limits
    def has_borrowed_limit(self):
        return len(self.borrowed_books) >= 3
    
    def __str__(self):
        return f'{self.member_id} {self.name} {self.email}'