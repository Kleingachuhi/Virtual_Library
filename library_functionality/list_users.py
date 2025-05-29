from my_database_related.database import SessionLocal
from models.user import User

def list_users():
    session = SessionLocal()
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Card Number: {user.card_number}")
    session.close()

if __name__ == "__main__":
    list_users()
