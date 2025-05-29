from database import SessionLocal
from models.author import Author
from models.book import Book
from models.user import User
from models.loan import Loan
from datetime import datetime

def update_author(author_id, first_name=None, last_name=None, birth_year=None):
    session = SessionLocal()
    author = session.query(Author).filter_by(id=author_id).first()
    if not author:
        print(f"Author with ID {author_id} not found.")
        session.close()
        return
    
    if first_name:
        author.first_name = first_name
    if last_name:
        author.last_name = last_name
    if birth_year:
        author.birth_year = birth_year
    
    session.commit()
    print(f"Author ID {author_id} updated.")
    session.close()


def update_book(book_id, title=None, author_id=None):
    session = SessionLocal()
    book = session.query(Book).filter_by(id=book_id).first()
    if not book:
        print(f"Book with ID {book_id} not found.")
        session.close()
        return
    
    if title:
        book.title = title
    if author_id:
        book.author_id = author_id
    
    session.commit()
    print(f"Book ID {book_id} updated.")
    session.close()


def update_user(user_id, username=None, card_number=None):
    session = SessionLocal()
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print(f"User with ID {user_id} not found.")
        session.close()
        return
    
    if username:
        user.username = username
    if card_number:
        user.card_number = card_number
    
    session.commit()
    print(f"User ID {user_id} updated.")
    session.close()


def update_loan(loan_id, book_id=None, user_id=None, borrowed_at=None, returned_at=None):
    session = SessionLocal()
    loan = session.query(Loan).filter_by(id=loan_id).first()
    if not loan:
        print(f"Loan with ID {loan_id} not found.")
        session.close()
        return
    
    if book_id:
        loan.book_id = book_id
    if user_id:
        loan.user_id = user_id
    if borrowed_at:
        loan.borrowed_at = borrowed_at
    if returned_at is not None:
        loan.returned_at = returned_at
    
    session.commit()
    print(f"Loan ID {loan_id} updated.")
    session.close()
