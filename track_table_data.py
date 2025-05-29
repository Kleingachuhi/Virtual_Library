from update_table import update_author, update_book, update_user, update_loan
from delete_from_tables import delete_author, delete_book, delete_user, delete_loan
from datetime import datetime

def main():
    print("Welcome to Virtual Library CLI")
    while True:
        action = input("\nChoose an action: [update/delete/exit]: ").strip().lower()
        if action == 'exit':
            print("Goodbye!")
            break
        if action not in ['update', 'delete']:
            print("Invalid action, try again.")
            continue
        
        table = input("Choose a table: [author/book/user/loan]: ").strip().lower()
        if table not in ['author', 'book', 'user', 'loan']:
            print("Invalid table, try again.")
            continue

        if action == 'update':
            handle_update(table)
        elif action == 'delete':
            handle_delete(table)

def handle_update(table):
    if table == 'author':
        author_id = int(input("Enter Author ID to update: "))
        first_name = input("New First Name (or blank to skip): ") or None
        last_name = input("New Last Name (or blank to skip): ") or None
        birth_year = input("New Birth Year (or blank to skip): ") or None
        update_author(author_id, first_name, last_name, birth_year)
    
    elif table == 'book':
        book_id = int(input("Enter Book ID to update: "))
        title = input("New Title (or blank to skip): ") or None
        author_id = input("New Author ID (or blank to skip): ")
        author_id = int(author_id) if author_id else None
        update_book(book_id, title, author_id)
    
    elif table == 'user':
        user_id = int(input("Enter User ID to update: "))
        username = input("New Username (or blank to skip): ") or None
        card_number = input("New Card Number (6 digits) (or blank to skip): ") or None
        update_user(user_id, username, card_number)
    
    elif table == 'loan':
        loan_id = int(input("Enter Loan ID to update: "))
        book_id = input("New Book ID (or blank to skip): ")
        book_id = int(book_id) if book_id else None
        user_id = input("New User ID (or blank to skip): ")
        user_id = int(user_id) if user_id else None
        borrowed_at = input("New Borrowed At (YYYY-MM-DD HH:MM:SS) (or blank to skip): ") or None
        if borrowed_at:
            borrowed_at = datetime.strptime(borrowed_at, "%Y-%m-%d %H:%M:%S")
        returned_at = input("New Returned At (YYYY-MM-DD HH:MM:SS) (or blank for NULL): ")
        if returned_at == "":
            returned_at = None
        elif returned_at:
            returned_at = datetime.strptime(returned_at, "%Y-%m-%d %H:%M:%S")
        else:
            returned_at = None

        update_loan(loan_id, book_id, user_id, borrowed_at, returned_at)

def handle_delete(table):
    if table == 'author':
        author_id = int(input("Enter Author ID to delete: "))
        delete_author(author_id)
    elif table == 'book':
        book_id = int(input("Enter Book ID to delete: "))
        delete_book(book_id)
    elif table == 'user':
        user_id = int(input("Enter User ID to delete: "))
        delete_user(user_id)
    elif table == 'loan':
        loan_id = int(input("Enter Loan ID to delete: "))
        delete_loan(loan_id)


if __name__ == "__main__":
    main()
