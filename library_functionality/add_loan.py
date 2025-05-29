from my_database_related.database import SessionLocal
from models.loan import Loan
from models.book import Book
from models.user import User
from datetime import datetime

def add_loan(book_id, user_id):
    session = SessionLocal()

    book = session.query(Book).filter_by(id=book_id).first()
    user = session.query(User).filter_by(id=user_id).first()

    if not book or not user:
        print("Invalid book or user ID.")
        session.close()
        return

    new_loan = Loan(
        book_id=book.id,
        user_id=user.id,
        book_title=book.title,    # New
        username=user.username,  # New
        borrowed_at=datetime.utcnow(),
        returned_at=None
    )

    session.add(new_loan)
    session.commit()

    print(f"Book '{book.title}' borrowed by {user.username} on {new_loan.borrowed_at}")

    session.close()

if __name__ == "__main__":
    add_loan(1, 1)
 
