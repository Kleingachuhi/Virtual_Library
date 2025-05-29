from database import SessionLocal
from models.author import Author

def add_author(first_name, last_name, birth_year=None):
    session = SessionLocal()
    new_author = Author(first_name=first_name, last_name=last_name, birth_year=birth_year)

    session.add(new_author)
    session.commit()
    print(f"New Author: {new_author.first_name} {new_author.last_name} born in the year {new_author.birth_year}")
    session.close()

if __name__ == "__main__":
    add_author("Jane", "Austen", 1775)
    add_author('Klein', 'Gachuhi',2007)


