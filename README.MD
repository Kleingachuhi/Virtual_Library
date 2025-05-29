# Virtual Library CLI - README  

A simple command-line interface (CLI) for managing a virtual library, built with Python and SQLAlchemy.  

## 📚 Features  

- **Manage Authors**: Add, update, delete, and list authors  
- **Manage Books**: Add, update, delete, and list books (linked to authors)  
- **Manage Users**: Add and list users with unique card numbers  
- **Track Loans**: Borrow books, return them, and view loan history  

## ⚙️ Setup  

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

## 🖥️ Usage  

### Main Menu  
```
--- Virtual Library CLI ---  
1. Add record  
2. Update record  
3. Delete record  
4. List records  
5. Exit  
```  

### Example Workflow  

1. **Add an author**:  
   - Select `1` (Add) → `1` (Author)  
   - Enter first name, last name, and birth year  

2. **Add a book**:  
   - Select `1` (Add) → `2` (Book)  
   - Enter title and author ID  

3. **List all books**:  
   - Select `4` (List) → `2` (Books)  

4. **Exit**:  
   - Select `5`  

## 🗃️ Database Structure  

- **Authors**: `id`, `first_name`, `last_name`, `birth_year`  
- **Books**: `id`, `title`, `author_id` (linked to Authors)  
- **Users**: `id`, `username`, `card_number`  
- **Loans**: `book_id`, `user_id`, `borrowed_at`, `returned_at`  

## 📝 Notes  

- All data is saved in an SQLite database (`library.db`)  
- Card numbers are auto-generated (6 digits)  
- Loan dates are recorded automatically  

---

Made with Python 🐍 + SQLAlchemy 🔥  
Simple, clean, and functional!  

---