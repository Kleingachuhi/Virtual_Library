# library_functionality/add_book.py

from my_database_related.database import SessionLocal
from models.book import Book
from models.author import Author

def add_book(title, author_id):
    session = SessionLocal()

    author = session.query(Author).filter_by(id=author_id).first()

    if not author:
        print(f"No author found with ID {author_id}. Let's add a new author.")
        first_name = input("Enter author's first name: ")
        last_name = input("Enter author's last name: ")
        birth_year = input("Enter author's birth year: ")

        author = Author(first_name=first_name, last_name=last_name, birth_year=birth_year)
        session.add(author)
        session.commit() 

        print(f"New author added with ID {author.id}.")

    book = Book(title=title, author_id=author.id)
    session.add(book)
    session.commit()
    print(f"Book '{title}' added with ID {book.id} and Author ID {author.id}.")
    session.close()
