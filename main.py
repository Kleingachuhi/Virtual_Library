from library_functionality.add_author import add_author
from library_functionality.add_book import add_book
from library_functionality.add_user import add_user
from library_functionality.add_loan import add_loan
from library_functionality.update_table import update_author, update_book, update_user, update_loan
from library_functionality.delete_from_tables import delete_author, delete_book, delete_user, delete_loan
from library_functionality.list_authors import list_authors
from library_functionality.list_books import list_books
from library_functionality.list_users import list_users
from library_functionality.list_loans import list_loans
from library_functionality.return_loan import return_loan

def main_menu():
    print("\n--- Virtual Library CLI ---")
    print("1. Add record")
    print("2. Update record")
    print("3. Delete record")
    print("4. List records")
    print("5. Return a loan")  
    print("6. Exit")  

def select_entity():
    print("\nSelect entity:")
    print("1. Author")
    print("2. Book")
    print("3. User")
    print("4. Loan")
    return input("Enter choice: ")

def main():
    while True:
        main_menu()
        choice = input("Choose an action: ")

        if choice == '1': 
            entity = select_entity()
            if entity == '1':
                first = input("First name: ")
                last = input("Last name: ")
                birth_year = input("Birth year: ")
                add_author(first, last, birth_year)
            elif entity == '2':
                title = input("Book title: ")
                author_id = int(input("Author ID: "))
                add_book(title, author_id)
            elif entity == '3':
                username = input("Username: ")
                add_user(username)
            elif entity == '4':
                book_id = int(input("Book ID: "))
                user_id = int(input("User ID: "))
                add_loan(book_id, user_id)
            else:
                print("Invalid entity choice.")

        elif choice == '2': 
            entity = select_entity()
            if entity == '1':
                author_id = int(input("Author ID to update: "))
                first = input("New first name (press Enter to skip): ")
                last = input("New last name (press Enter to skip): ")
                birth = input("New birth year (press Enter to skip): ")
                update_author(author_id, first or None, last or None, birth or None)
            elif entity == '2':
                book_id = int(input("Book ID to update: "))
                title = input("New title (press Enter to skip): ")
                author_id = input("New author ID (press Enter to skip): ")
                update_book(book_id, title or None, int(author_id) if author_id else None)
            elif entity == '3':
                user_id = int(input("User ID to update: "))
                username = input("New username (press Enter to skip): ")
                card_number = input("New card number (press Enter to skip): ")
                update_user(user_id, username or None, card_number or None)
            elif entity == '4':
                loan_id = int(input("Loan ID to update: "))
                book_id = input("New Book ID (press Enter to skip): ")
                user_id = input("New User ID (press Enter to skip): ")
                returned = input("Returned date (YYYY-MM-DD or leave empty if not returned): ")
                update_loan(
                    loan_id,
                    int(book_id) if book_id else None,
                    int(user_id) if user_id else None,
                    returned_at=returned if returned else None
                )
            else:
                print("Invalid entity choice.")

        elif choice == '3': 
            entity = select_entity()
            if entity == '1':
                author_id = int(input("Author ID to delete: "))
                delete_author(author_id)
            elif entity == '2':
                book_id = int(input("Book ID to delete: "))
                delete_book(book_id)
            elif entity == '3':
                user_id = int(input("User ID to delete: "))
                delete_user(user_id)
            elif entity == '4':
                loan_id = int(input("Loan ID to delete: "))
                delete_loan(loan_id)
            else:
                print("Invalid entity choice.")

        elif choice == '4':
            entity = select_entity()
            if entity == '1':
                list_authors()
            elif entity == '2':
                list_books()
            elif entity == '3':
                list_users()
            elif entity == '4':
                list_loans()
            else:
                print("Invalid entity choice.")

        elif choice == '5':
            loan_id = int(input("Enter loan ID to return: "))
            return_loan(loan_id)

        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid action choice.")

if __name__ == "__main__":
    main()
