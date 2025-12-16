# Add/remove/update books

import datetime
from data.storage import books, members, loans
from domain.books import Book
from domain.member import Member
from domain.loan import Loan
import uuid

def add_book(title, author, category):
    unique_id = uuid.uuid4()

    book = Book(
        book_id=unique_id,
        title=title,
        author=author,
        category=category,
        is_available=True
    )
    books.append(book)

def remove_book(book_id):
    for book in books:
        if book.book_id == book_id:
            books.remove(book)
            break   

 

def update_book(book_id, new_title, new_author, new_category):
    for book in books:
        if book.book_id == book_id:
            book.title = new_title
            book.author = new_author
            book.category = new_category
            break



# Register members

def register_member(name, email):
    unique_id = uuid.uuid4()

    member = Member(
        member_id=unique_id,
        name=name,
        email=email
    )
    members.append(member)

# Remove members

def remove_member(member_id):
    for member in members:
        if member.member_id == member_id:
            members.remove(member)
            break

# Issue books

def issue_book(member_id, book_id):
    for member in members:
        if member.member_id == member_id:
            for book in books:
                if book.book_id == book_id and book.is_available:
                    loan = Loan( 
                        loan_id=uuid.uuid4(),
                        member_id=member_id,
                        book_id=book_id,
                        due_date=datetime.now() + datetime.timedelta(days=14),
                        return_date=None
                    )
                    loans.append(loan)
                    book.toggle_availability()
                    member.borrow_book(book_id,
                    )

# Accept returns

def accept_return(loan_id):
    for loan in loans:
        if loan.loan_id == loan_id:
            loan.close_loan()
            for book in books:
                if book.book_id == loan.book_id:
                    book.toggle_availability()
            break
# Perform searches

def search_books(query):    
    results = []
    for book in books:
        if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query.lower() in book.category.lower():
            results.append(book)
    return results


# Generate reports

def generate_report():
    pass

