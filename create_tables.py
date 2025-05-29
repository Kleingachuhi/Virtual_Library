from database import engine, Base
from models.author import Author
from models.book import Book
from models.user import User
from models.loan import Loan

def creating_tables():
    print("Creating your tables in the database...")
    Base.metadata.create_all(engine)
    print('Your tables are successfully created')

if __name__ == "__main__":
    creating_tables()