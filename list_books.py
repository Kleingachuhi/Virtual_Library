from database import SessionLocal
from models.book import Book


def list_books():
    session = SessionLocal()
    books = session.query(Book).all()


    for book in books:
        author = book.author
        print(f"Book ID: {book.id} | Title: '{book.title}' | Author: {author.first_name} {author.last_name} (ID: {author.id})")

    session.close()

if __name__ == "__main__":
    list_books()