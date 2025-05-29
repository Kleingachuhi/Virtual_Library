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

def main_menu():
    print("\n--- Virtual Library CLI ---")
    print("1. Add record")
    print("2. Update record")
    print("3. Delete record")
    print("4. List records")
    print("5. Exit")

def select_entity():
    print("\nSelect entity:")
    print("1. Author")
    print("2. Book")
    print("3. User")
    print("4. Loan")
    choice = input("Enter choice: ")
    return choice

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
            print("Update functionality coming soon!")

        elif choice == '3':  
            entity = select_entity()
            print("Delete functionality coming soon!")

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
            print("Goodbye!")
            break
        else:
            print("Invalid action choice.")

if __name__ == "__main__":
    main()
