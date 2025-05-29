from database import SessionLocal
from models.loan import Loan

def list_loans():
    session = SessionLocal()
    loans = session.query(Loan).all()

    if not loans:
        print("No loans found.")
        session.close()
        return

    for loan in loans:
        print(f"Loan ID: {loan.id}")
        print(f"Book: {loan.book_title}")
        print(f"User: {loan.username}")
        print(f"Borrowed At: {loan.borrowed_at}")
        print(f"Returned At: {loan.returned_at if loan.returned_at else 'Not returned'}")
        print("-" * 40)

    session.close()

if __name__ == "__main__":
    list_loans()
