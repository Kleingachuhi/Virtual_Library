from my_database_related.database import SessionLocal
from models.author import Author
from models.book import Book
from models.user import User
from models.loan import Loan

def delete_author(author_id):
    session = SessionLocal()
    author = session.query(Author).filter_by(id=author_id).first()
    if not author:
        print(f"Author with ID {author_id} not found.")
        session.close()
        return
    
    session.delete(author)
    session.commit()
    print(f"Author ID {author_id} deleted.")
    session.close()


def delete_book(book_id):
    session = SessionLocal()
    book = session.query(Book).filter_by(id=book_id).first()
    if not book:
        print(f"Book with ID {book_id} not found.")
        session.close()
        return
    
    session.delete(book)
    session.commit()
    print(f"Book ID {book_id} deleted.")
    session.close()


def delete_user(user_id):
    session = SessionLocal()
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print(f"User with ID {user_id} not found.")
        session.close()
        return
    
    session.delete(user)
    session.commit()
    print(f"User ID {user_id} deleted.")
    session.close()


def delete_loan(loan_id):
    session = SessionLocal()
    loan = session.query(Loan).filter_by(id=loan_id).first()
    if not loan:
        print(f"Loan with ID {loan_id} not found.")
        session.close()
        return
    
    session.delete(loan)
    session.commit()
    print(f"Loan ID {loan_id} deleted.")
    session.close()
