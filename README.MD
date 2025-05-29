# Virtual Library CLI - README  

A simple command-line interface (CLI) for managing a virtual library, built with Python and SQLAlchemy.  

##  Features  

- **Manage Authors**: Add, update, delete, and list authors  
- **Manage Books**: Add, update, delete, and list books (linked to authors)  
- **Manage Users**: Add and list users with unique card numbers  
- **Track Loans basically lent books**: Borrow books, return them, and view loan history 

##  Setup  

### Prerequisites  
- Python 3.10+  
- Pipenv (recommended)  

### Installation  
1. Clone this repository  
2. Navigate to the project folder  
3. Set up the virtual environment:  

```bash
pipenv install
pipenv shell
```

4. Run the application:  

```bash
python main.py
```  

## Complete Usage Guide

### Main Menu  
When you run the program, you'll see:
```
--- Virtual Library CLI ---  
1. Add record  
2. Update record  
3. Delete record  
4. List records  
5. Exit  
```

### Adding Records
1. **Add an Author**:
   - Select `1` (Add) → `1` (Author)
   - Enter when prompted:
     ```
     First name: J.K.
     Last name: Rowling
     Birth year: 1965
     ```

2. **Add a Book**:
   - Select `1` (Add) → `2` (Book)
   - Enter:
     ```
     Book title: Harry Potter
     Author ID: 1
     ```
   - *Tip: List authors first to find correct IDs*

3. **Add a User**:
   - Select `1` (Add) → `3` (User)
   - Just enter a username (card number generates automatically)

4. **Create a Loan**:
   - Select `1` (Add) → `4` (Loan)
   - Enter:
     ```
     Book ID: 1
     User ID: 1
     ```

###  Updating Records
1. Select `2` (Update) from main menu
2. Choose what to update (Author=1, Book=2, etc.)
3. Example - Update a Book:
   ```
   Enter Book ID to update: 1
   New Title (or blank to skip): Harry Potter and the Sorcerer's Stone
   New Author ID (or blank to skip): [press Enter to skip]
   ```

### Deleting Records
1. Select `3` (Delete) from main menu
2. Choose what to delete
3. Example - Delete User:
   ```
   Enter User ID to delete: 1
   ```

###  Listing Records
1. Select `4` (List) from main menu
2. Choose what to list:
   - Authors (`1`): Shows all authors
   - Books (`2`): Shows titles with author names
   - Users (`3`): Shows usernames and card numbers
   - Loans (`4`): Shows borrowing history

###  Returning Books
1. Go to Update → Loan (`2` → `4`)
2. Enter Loan ID
3. For `Returned At`, enter today's date:
   ```
   New Returned At (YYYY-MM-DD HH:MM:SS): 2023-11-15 14:30:00
   ```
   or leave blank to mark as still borrowed

## Database Structure  

- **Authors**: `id`, `first_name`, `last_name`, `birth_year`  
- **Books**: `id`, `title`, `author_id` (linked to Authors)  
- **Users**: `id`, `username`, `card_number`  
- **Loans**: `book_id`, `user_id`, `borrowed_at`, `returned_at`  

##  Pro Tips and guidance --
- Use `List` before updating/deleting to check IDs
- Loans automatically record borrow dates
- Card numbers are 6-digit auto-generated IDs
- All data saves to `library.db` (SQLite)

## Note
- No data is lost if you exit accidentally
---

Made with Python 🐍 + SQLAlchemy 🔥  
Simple, clean, and functional!  

--- 

