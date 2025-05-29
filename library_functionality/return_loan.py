from my_database_related.database import SessionLocal
from models.loan import Loan
from datetime import datetime

def return_loan(loan_id):
    session = SessionLocal()
    loan = session.query(Loan).filter_by(id=loan_id).first()

    if not loan:
        print(f"No loan found with ID {loan_id}.")
        session.close()
        return

    if loan.returned_at:
        print(f"Loan {loan_id} already returned on {loan.returned_at}.")
        session.close()
        return

    loan.returned_at = datetime.utcnow()
    session.commit()
    print(f"Loan {loan_id} marked as returned.")
    session.close()

if __name__ == "__main__":
    loan_id = int(input("Enter loan ID to return: "))
    return_loan(loan_id)
