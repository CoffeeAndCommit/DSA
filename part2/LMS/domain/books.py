#  Domain model1 represents a physical book

class Book:
    def __init__(self,book_id,title,author, category,is_available:bool):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.is_available = is_available
    
    # Know whether it is available
    def is_available(self):
        return self.is_available
    
    # Toggle availability
    
    def toggle_availability(self):
        self.is_available = not self.is_available



    def __str__(self):
        return  f'{self.book_id} {self.title} {self.author} {self.category} '