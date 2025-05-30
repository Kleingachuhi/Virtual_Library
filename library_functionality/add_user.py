from my_database_related.database import SessionLocal
from models.user import User
import random

def add_user(username):
    session = SessionLocal()
    
    while True:
        card_number = str(random.randint(100000, 999999))
        existing = session.query(User).filter_by(card_number=card_number).first()
        if not existing:
            break

    new_user = User(username=username, card_number=card_number)
    session.add(new_user)
    session.commit()
    print(f"User '{username}' added with card number: {card_number}")
    session.close()
