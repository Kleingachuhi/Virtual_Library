from my_database_related.database import SessionLocal
from models.book import Book
from models.author import Author

def add_book(title, author_id):
    session = SessionLocal()

    author = session.query(Author).filter_by(id=author_id).first()
    if not author:
        print(f"Author with ID {author_id} does not exist.")
        session.close()
        return

    new_book = Book(title=title, author_id=author_id)
    session.add(new_book)
    session.commit()
    print(f"New Book: '{new_book.title}' added for Author ID {author_id}")

    session.close()

if __name__ == "__main__":
    add_book("The Hobbit", 1)
    add_book("Chilling adventures of Klein", 2)
