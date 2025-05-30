from my_database_related.database import SessionLocal
from models.author import Author

def list_authors():
    session = SessionLocal()
    authors = session.query(Author).all()
    for author in authors:
        print(f"ID: {author.id}, Name: {author.first_name} {author.last_name}, Born: {author.birth_year}, Books Written: {len(author.books)}")
    session.close()
