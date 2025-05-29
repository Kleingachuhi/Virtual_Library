from database import SessionLocal
from models.user import User
import random

def generate_card_number():
    return str(random.randint(100000, 999999))

def add_user(user_name):
    session = SessionLocal()

    new_user = User(username = user_name, card_number = generate_card_number())
    session.add(new_user)
    session.commit()

    session.close()

if __name__ == "__main__":
    add_user("Martin Garrix")